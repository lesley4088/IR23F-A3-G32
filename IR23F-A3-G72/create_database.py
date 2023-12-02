import sqlite3

def create_database(dict_docID, dict_tfidf, dict_wordfreq, important_dic):
    conn = sqlite3.connect("WordsDatabase.db")
    cursor = conn.cursor()


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS words (
            word TEXT,
            doc_ID TEXT,
            tf_idf TEXT,
            frequency TEXT,
            PRIMARY KEY (word)
        )
    """)
    for word in dict_docID.keys():
        doc_ID = ",".join(dict_docID[word])
        tf_idf = ",".join(dict_tfidf[word])
        frequency = ",".join(dict_wordfreq[word])
        cursor.execute('INSERT INTO words (word, doc_ID, tf_idf, frequency) VALUES (?, ?, ?, ?)', (word, doc_ID, tf_idf, frequency))


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ImportantWords (
        word TEXT,
        doc_ID TEXT,
        PRIMARY KEY (word)
        )
    """)
    for importantWord in important_dic.keys():
        doc_ID = ",".join(important_dic[importantWord])
        cursor.execute('INSERT INTO ImportantWords (word, doc_ID) VALUES (?, ?)', (importantWord, doc_ID))

        
    conn.commit()
    conn.close()


def create_URL_table(URLs):
    conn = sqlite3.connect("WordsDatabase.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS URLs (
            doc_ID TEXT,
            url Text,
            PRIMARY KEY (doc_ID)
        )
    """)
    
    docID = 1
    for url in URLs:
        cursor.execute('INSERT INTO URLs (doc_ID, url) VALUES (?, ?)', (str(docID), url))
        docID += 1
    
        conn.commit()
    conn.close()