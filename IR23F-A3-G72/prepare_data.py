import math


def prepare_data(dict_docID, dict_tfidf, dict_wordfreq, tokenList, doc_ID):

    for token in set(tokenList):
        if token not in dict_docID.keys():
            dict_docID[token] = [str(doc_ID)]
        else:
            dict_docID[token].append(str(doc_ID))
        

        frequency = get_token_frequencies(token, tokenList)
        if token not in dict_wordfreq:
            dict_wordfreq[token] = [str(frequency)]
        else:
            dict_wordfreq[token].append(str(frequency))

        TF = 1 + math.log10(frequency)
        if token not in dict_tfidf.keys():
            dict_tfidf[token] = [TF]
        else:
            dict_tfidf[token].append(TF)

def get_token_frequencies(token, tokenList):
     count = 0
     for word in tokenList:
          if word == token.lower():
               count += 1
     return count


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
