from get_tokens import *


def prepare_data(dict_docID, dict_tfidf, dict_wordfreq, tokenList, doc_ID):

    for token in set(tokenList):
        if token not in dict_docID.keys():
            dict_docID[token] = [str(doc_ID)]
        else:
            dict_docID[token].append(str(doc_ID))
        
        tfidf = 0
        if token not in dict_tfidf.keys():
            dict_tfidf[token] = [str(tfidf)]
        else:
            dict_tfidf[token].append(str(tfidf))

        frequency = get_token_frequencies(token, tokenList)
        if token not in dict_wordfreq:
            dict_wordfreq[token] = [str(frequency)]
        else:
            dict_wordfreq[token].append(str(frequency))


# dict_docID = {}
# dict_tfidf = {}
# dict_wordfreq = {}
# doc_id = 1
# x = "Tropical fish include fish found in tropical environments around the world, \n including both freshwater and salt water species."
# tokenList = get_tokenList(x)

# prepare_data(dict_docID, dict_tfidf, dict_wordfreq, tokenList, doc_id)
# print(dict_docID)
# print("---------------------------------")
# print(dict_tfidf)
# print("---------------------------------")
# print(dict_wordfreq)