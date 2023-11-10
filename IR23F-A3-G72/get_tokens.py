def get_tokenList(fileContent):
    tokenList = []
    token = ""
    for char in fileContent:
        if char.isalnum() and char.isascii():
                token += char
        else:
            if token != "":
                tokenList.append(token.lower())
                token = ""
    return tokenList

# x = "Post navigation ← Training Tomorrow’s Software Engineers\nInclusive Streaming Workshop Builds Community to Advance Research →\n\n\nOctober 2019"
# print(get_tokenList(x))

def get_token_frequencies(token, tokenList):
     count = 0
     for word in tokenList:
          if word == token.lower():
               count += 1
     return count

def get_tf_idf():
     return 0