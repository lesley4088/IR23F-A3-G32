from QueryProcessor import *
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    """This function creates the home page by using the format in home.html."""
    return render_template('home.html')

@app.route('/search')
def search():
    queryTokens =request.args.get('query')
    queryProcessor = QueryProcessor()
    urls = queryProcessor.retrieveURLs(queryTokens)
    return render_template("searchWebsite.html", urls=urls, query=request.args.get('query'))

if __name__ == '__main__':
    app.run()
