from flask import Flask,jsonify,request
import csv
all_movies=[]
with open('movies.csv',encoding="utf8") as f:
    reader=csv.reader(f)
    data=list(reader)
    all_movies=data[1:]
    
liked_movies=[]
disliked_movies=[]
not_watched_movies=[]


app=Flask(__name__)

@app.route("/get-movies")
def get_movies():
    return jsonify({
        "data":all_movies[0],
        "status":"succsess"
    })

@app.route("/liked-movies",methods=["POST"])
def liked_movies():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        "status":"succsess"
    }),201

@app.route("/disliked-movies",methods=["POST"])
def disliked_movies():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    disliked_movies.append(movie)
    return jsonify({
        "status":"succsess"
    }),201
@app.route("/not_watched_movies",methods=["POST"])
def not_watched_movies():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    not_watched_movies.append(movie)
    return jsonify({
        "status":"succsess"
    }),201

if __name__ =="__main__":
    app.run()
    