from TextProcessor import *
import sqlite3


class QueryProcessor:

    def __init__(self) -> None:
        self.textProcessor = TextProcessor()


    def retrieveURLs(self, query):       
        queryTokens = self.textProcessor.get_tokenLlist_for_string(query)
        doc_tfidf = self.get_doc_tfidf(queryTokens)
        return self.find_top_five_url(doc_tfidf)


    def get_doc_tfidf(self, queryTokens):
        doc_tfidf = {}
        
        for word in queryTokens:
            conn = sqlite3.connect("WordsDatabase.db")
            cursor = conn.cursor()
            cursor.execute(f"""
                select doc_ID, tf_idf
                from words
                where word = '{word}'
            """)
            result = cursor.fetchall()
            tempDocID = result[0][0].split(",")
            tempTfidf = result[0][1].split(",")
            if queryTokens.index(word) == 0:
                for doc in tempDocID:
                    doc_tfidf[doc] = [tempTfidf[tempDocID.index(doc)]]
            else:
                for doc in tempDocID:
                    if doc in doc_tfidf.keys():
                        doc_tfidf[doc].append(tempTfidf[tempDocID.index(doc)])
            
            print(len(doc_tfidf))

        for doc in doc_tfidf.copy().keys():
            if len(doc_tfidf[doc]) != len(queryTokens):
                del doc_tfidf[doc]

        return doc_tfidf

    def find_top_five_url(self, dict_tfidf):
        tfidfList = []
        top_five_docID = []
        top_five_url = []
        for doc in dict_tfidf:
            summ = 0
            for tfidf in dict_tfidf[doc]:
                summ += float(tfidf)
            tfidfList.append(summ)
            dict_tfidf[doc] = summ
        
        tfidfList = sorted(tfidfList, reverse=True)

        for i in range(5):
            for id in dict_tfidf.keys():
                if dict_tfidf[id] == tfidfList[i] and id not in top_five_docID:
                    top_five_docID.append(id)
                if len(top_five_docID) >= 5:
                    break
            


        for id in top_five_docID:
            conn = sqlite3.connect("WordsDatabase.db")
            cursor = conn.cursor()
            cursor.execute(f"""
                select url
                from URLs
                where doc_ID = '{id}'
            """)
            url = cursor.fetchall()[0][0]
            print(url)
            top_five_url.append(url)

        return top_five_url






if __name__ == "__main__":
    q = QueryProcessor()
    q.retrieveURLs("master of software engineering")