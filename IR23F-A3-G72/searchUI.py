from QueryProcessor import *
from flask import Flask, render_template, request
import time

app = Flask(__name__)

@app.route('/')
def home():
    """This function creates the home page by using the format in home.html."""
    return render_template('home.html')

@app.route('/search')
def search():
    start = time.time()

    queryTokens =request.args.get('query')
    queryProcessor = QueryProcessor()
    urls = queryProcessor.retrieveURLs(queryTokens)

    processing_time = f"{time.time() - start:.2f}"
    if urls:
        return render_template(
            "searchWebsite.html", 
            urls=urls, 
            query=request.args.get('query'), 
            missing="", 
            time=processing_time)
    else:
        return render_template(
            "searchWebsite.html", 
            urls=urls, 
            query=request.args.get('query'), 
            missing="Words not in database.", 
            time=processing_time)

if __name__ == '__main__':
    app.run()
