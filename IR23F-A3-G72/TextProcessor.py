import nltk
nltk.download("punkt")
nltk.download("wordnet")
nltk.download("omw-1.4")
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer

class TextProcessor:
     
     def __init__(self) -> None:
          self.lemmatizer = WordNetLemmatizer()
          self.tokenizer = RegexpTokenizer(r'[^\W_]+')


     def get_tokenList_for_content(self, fileContent):
        words = self.tokenizer.tokenize(fileContent.get_text())
        tokenList = [self.lemmatizer.lemmatize(word.lower()) for word in words]
        return tokenList
     

     def get_tokenLlist_for_string(self, string):
        words = self.tokenizer.tokenize(string)
        token_list = [self.lemmatizer.lemmatize(word.lower()) for word in words]
        return token_list
     
     
     def get_tokenList_for_important_title_and_anchor(self, fileContent):
         words = []

         title_and_anchor = fileContent.find_all(["h1", "h2", "h3", "title" "a"])
         for content in title_and_anchor:
             tokens = self.tokenizer.tokenize(content.text)
             for token in tokens:
                  words.append(token)

         tokenList = [self.lemmatizer.lemmatize(word.lower()) for word in words]
         return tokenList
# y = TextProcessor()
# x = "Post navigation ← Training Tomorrow's Software Engineers\nInclusive Streaming Workshop Builds Community to Advance Research →\n\n\nOctober 2019"
# print(y.get_tokenList(x))
