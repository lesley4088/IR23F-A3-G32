from TextProcessor import *
import sqlite3
import math
import numpy as np


class QueryProcessor:

    def __init__(self) -> None:
        self.textProcessor = TextProcessor()
        self.conn = sqlite3.connect("WordsDatabase.db")
        self.cursor = self.conn.cursor()


    def retrieveURLs(self, query):       
        queryTokens = self.textProcessor.get_tokenLlist_for_string(query)
        doc_tfidf, word_df = self.get_doc_tfidf(set(queryTokens))
        if not doc_tfidf:
            return []
        query_tfidf = self.get_query_tfidf(queryTokens, word_df)
        return self.find_top_five_url(doc_tfidf, query_tfidf, queryTokens)

    
    def get_query_tfidf(self, query, df_dict):
        result = []
        for token in set(query):
            tf = 1 + math.log10(query.count(token))
            idf = math.log10(1988 / df_dict[token])
            result.append(tf*idf)

        return result
    

    def get_doc_tfidf(self, queryTokens):
        doc_tfidf = {}
        word_df = {}
        count = 1
        missing = 1
        
        for word in queryTokens:
            try:
                self.cursor.execute(f"""
                    select doc_ID, tf_idf
                    from words
                    where word = '{word}'
                """)
                result = self.cursor.fetchall()
                tempDocID = result[0][0].split(",")
                tempTfidf = result[0][1].split(",")
                word_df[word] = len(tempDocID)
                for doc in tempDocID:
                    if doc not in doc_tfidf:
                        doc_tfidf[doc] = []
                    while len(doc_tfidf[doc]) < count - 1:
                        doc_tfidf[doc].append(0)
                    doc_tfidf[doc].append(float(tempTfidf[tempDocID.index(doc)]))
            except:
                missing += 1
            count += 1

        if missing == count:
            return None, None
        
        for pair in doc_tfidf:
            while len(doc_tfidf[pair]) < len(queryTokens):
                    doc_tfidf[pair].append(0)

        return doc_tfidf, word_df
    

    def add_weight_to_title_and_anchor(self, scores, query, docs):
        for token in query:
            for doc in docs:
                self.cursor.execute(f"""
                    SELECT *
                    FROM ImportantWords
                    WHERE word = '{token}' AND doc_ID LIKE '%{doc}%'
            """)
                is_title_or_anchor = self.cursor.fetchall()
                if is_title_or_anchor != []:
                    scores[docs.index(doc)] *= 2


    def find_top_five_url(self, doc_tfidf, query_tfidf, query):
        doc_matrix = np.zeros((len(doc_tfidf.keys()), len(query_tfidf)))
        docs = []

        count = 0
        for key in doc_tfidf.keys():

            docs.append(key)

            doc_tfidf_array = np.array(doc_tfidf[key])
            length = np.sqrt(np.sum(doc_tfidf_array ** 2))
            doc_matrix[count] = doc_tfidf_array / length

            count += 1
    
        docs_array = np.array(docs)
        query_array = np.array([query_tfidf]).T
        query_array_length = np.sqrt(np.sum(query_array ** 2))
        query_unit_vector = query_array / query_array_length

        scores = doc_matrix.dot(query_unit_vector).T[0]
        self.add_weight_to_title_and_anchor(scores, query, docs)
        sortedIndex = np.argsort(scores)[::-1]
        # print(scores[sortedIndex][:15])

        top_five_docID = docs_array[sortedIndex][:5]
        top_five_url = []
        for id in top_five_docID:
            self.cursor.execute(f"""
                    select url
                    from URLs
                    where doc_ID = {id}          
            """)
            url = self.cursor.fetchall()[0][0]
            print(url)
            top_five_url.append(url)


        return top_five_url






if __name__ == "__main__":
    q = QueryProcessor()
    q.retrieveURLs("acm")