import os
from bs4 import BeautifulSoup
from pathlib import Path
import json
from get_tokens import *
from prepare_data import *
from create_database import *
from tqdm import tqdm
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="bs4")

path = Path("ANALYST")
dict_docID = {}
dict_tfidf = {}
dict_wordfreq = {}
doc_id = 1

for folder in path.iterdir():
    if folder.is_dir():
        for file in tqdm(folder.iterdir()):
            with open(file, "r", encoding="ascii", errors='ignore') as fileObj:
                content = json.load(fileObj)
                text = BeautifulSoup(content["content"], "html.parser")
                tokenList = get_tokenList(str(text))
                prepare_data(dict_docID, dict_tfidf, dict_wordfreq, tokenList, doc_id)
                doc_id += 1   

create_database(dict_docID, dict_tfidf, dict_wordfreq)
print("done")

