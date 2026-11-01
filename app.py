from flask import Flask, render_template, request, redirect, url_for
from database import Database
from tmdb_service import search_and_get_movie_details

app = Flask(__name__)
db = Database()

@app.route("/")
def index():
    search = request.args.get("q", "").strip()
    selected_genre = request.args.get("genre", "").strip()
    
    dvds = db.get_all_dvds(search_query=search, genre_filter=selected_genre)
    all_genres = db.get_all_genres()
    
    return render_template(
        "index.html", 
        dvds=dvds, 
        search=search, 
        selected_genre=selected_genre, 
        all_genres=all_genres
    )

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

@app.route("/delete/<int:dvd_id>", methods=["POST"])
def delete_dvd(dvd_id):
    db.delete_dvd(dvd_id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)