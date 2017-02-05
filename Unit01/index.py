#coding=utf-8

from flask import Flask, render_template, redirect, request, url_for
import json
import jieba
import operator

app = Flask(__name__)

@app.route("/")
def index():
    title = '結巴圖析'
    return render_template('index.html', title=title)

@app.route("/results")
def getResults():
    return render_template('results.html')

@app.route("/submit", methods=['POST'])
def handleAnalytic():
    if request.method == 'POST':
        ret = request.form['content']
        seglist = jieba.cut(ret, cut_all=False)
        hash = {}
        with open('stopwords.txt', 'r') as file: 
            stopwords = file.readlines()
        stopwords = [stopword.strip('\n') for stopword in stopwords]
        stopwords.append('\n');
        stopwords.append('\r\n');
        stopwords.append(' ');

        for item in seglist:
            if item in stopwords:
                continue
            else:
                if item in hash:
                    hash[item] += 1
                else:
                    hash[item] = 1

        hash = sorted(hash.items(), key=operator.itemgetter(1), reverse=True)
        json.dump(hash, open('count.json', 'w'))
        return redirect(url_for('getResults'))

@app.route("/api/count.json")
def getCount():
    with open('count.json', 'r') as f:
        return f.read()

if __name__ == "__main__":
    app.run()