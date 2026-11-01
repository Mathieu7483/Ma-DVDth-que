from flask import Flask, render_template, request, redirect, url_for
from database import Database
from tmdb_service import search_and_get_movie_details

app = Flask(__name__)
db = Database()

@app.route("/")
def index():
    dvds = db.get_all_dvds()
    return render_template("index.html", dvds=dvds)

@app.route("/add", methods=["GET", "POST"])
def add_dvd():
    error = None
    if request.method == "POST":
        title = request.form.get("title")
        if title:
            dvd_data = search_and_get_movie_details(title)
            if dvd_data:
                db.add_dvd(dvd_data)
                return redirect(url_for("index"))
            else:
                error = f"Aucun film trouvé pour '{title}'."
    return render_template("add.html", error=error)

if __name__ == "__main__":
    # host='0.0.0.0' rend l'application accessible sur le réseau local
    app.run(host="0.0.0.0", port=5000, debug=True)