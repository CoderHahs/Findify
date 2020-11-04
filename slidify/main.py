from flask import Flask, render_template, request
import spotify as sp
import sys

app = Flask(__name__)

@app.route("/")
def home():
    if request.method == 'GET':
        if 'submit_button' in request.args:
            if request.args['submit_button'] == 'Like':
                spotify_id = request.args['id']
                sp.configure_score(spotify_id, True)
            elif request.args['submit_button'] == 'Dislike':
                spotify_id = request.args['id']
                sp.configure_score(spotify_id, False)
    spotify_id = sp.getSpotifyId()
    return render_template("home.html", spotify_id=spotify_id)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/hire-me")
def hire_me():
    return render_template("hire_me.html")


    
if __name__ == "__main__":
    app.run(debug=True)
