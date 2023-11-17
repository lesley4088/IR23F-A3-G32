import nltk
nltk.download("punkt")
nltk.download("wordnet")
nltk.download("omw-1.4")
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer

class TextProcessor:
     
     def __init__(self) -> None:
          self.lemmatizer = WordNetLemmatizer()


     def get_tokenList(self, fileContent):
        tokenizer = RegexpTokenizer(r'[^\W_]+')
        words = tokenizer.tokenize(fileContent.get_text())
        tokenList = [self.lemmatizer.lemmatize(word.lower()) for word in words]
        return tokenList
     
     def get_tokenLlist_for_string(self, string):
        tokenizer = RegexpTokenizer(r'[^\W_]+')
        words = tokenizer.tokenize(string)
        token_list = [self.lemmatizer.lemmatize(word.lower()) for word in words]
        return token_list

# y = TextProcessor()
# x = "Post navigation ← Training Tomorrow's Software Engineers\nInclusive Streaming Workshop Builds Community to Advance Research →\n\n\nOctober 2019"
# print(y.get_tokenList(x))
