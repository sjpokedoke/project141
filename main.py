from flask import Flask, jsonify, request
import csv

articleslist = []

with open("articles.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    articleslist = data[1:]

likedarticles = []
dislikedarticles = []

app = Flask(__name__)

@app.route("/getarticle")
def getarticle():
    return jsonify({
        "data": articleslist[0],
        "status": "success"
    })

@app.route("/likedarticle")
def likedarticle():
    article = articleslist[0]
    likedarticles.append(article)
    articleslist.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/dislikedarticle")
def dislikedarticle():
    article = articleslist[0]
    dislikedarticles.append(article)
    articleslist.pop(0)
    return jsonify({
        "status": "success"
    }), 201

if __name__ = "__main__":
    app.run()