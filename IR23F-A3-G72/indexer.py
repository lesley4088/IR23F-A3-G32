import os
from bs4 import BeautifulSoup
from pathlib import Path
import json
from TextProcessor import *
from prepare_data import *
from create_database import *
from tqdm import tqdm
import warnings
import math


class Indexer:

    def __init__(self, PathObj):
        self.dict_docID = {}
        self.dict_tfidf = {}
        self.dict_wordfreq = {}
        self.DocsCount = 1
        self.textProcessor = TextProcessor()
        self.path = PathObj
        self.URLs = []
        self.importantTokens_dict = {}
        

    def create_index_data(self):
        for folder in self.path.iterdir():
            if folder.is_dir():
                for file in tqdm(folder.iterdir()):
                    with open(file, "r", encoding="ascii", errors='ignore') as fileObj:
                        content = json.load(fileObj)
                        text = BeautifulSoup(content["content"], "html.parser")
                        self.URLs.append(content["url"])
                        content_tokenList = self.textProcessor.get_tokenList_for_content(text)
                        important_tokens = self.textProcessor.get_tokenList_for_important_title_and_anchor(text)
                        content_tokenList += important_tokens
                        prepare_data(self.dict_docID, self.dict_tfidf, self.dict_wordfreq, content_tokenList, self.DocsCount, important_tokens, self.importantTokens_dict)
                        self.DocsCount += 1
                        
            

        for word in self.dict_tfidf.keys():
            IDF = math.log10(1988 / len(self.dict_docID[word]))
            tempList =[]

            for TF in self.dict_tfidf[word]:
                tempList.append(str(TF*IDF))
            
            self.dict_tfidf[word] = tempList

        create_database(self.dict_docID, self.dict_tfidf, self.dict_wordfreq, self.importantTokens_dict)

        create_URL_table(self.URLs)



if __name__ == "__main__":

    warnings.filterwarnings("ignore", category=UserWarning, module="bs4")   
    path = Path("ANALYST")
    indexer = Indexer(path)
    indexer.create_index_data()
    print("done")
