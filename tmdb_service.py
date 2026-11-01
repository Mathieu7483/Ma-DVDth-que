import requests

API_KEY = "b9e11dd2b1af80d311f2fb0f381a5ddc" 
BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"

def search_and_get_movie_details(title: str, year: str = None) -> dict | None:
    search_url = f"{BASE_URL}/search/movie"
    
    # 1. Première tentative avec l'année si elle est spécifiée
    results = []
    if year:
        params = {"api_key": API_KEY, "query": title, "year": year, "language": "fr-FR"}
        response = requests.get(search_url, params=params)
        if response.status_code == 200:
            results = response.json().get("results", [])

    # 2. Si aucun résultat ou pas d'année, on cherche sans filtrer par année
    if not results:
        params = {"api_key": API_KEY, "query": title, "language": "fr-FR"}
        response = requests.get(search_url, params=params)
        if response.status_code == 200:
            results = response.json().get("results", [])

    if not results:
        return None

    movie_basic = results[0]
    movie_id = movie_basic["id"]

    # Récupération des détails complets
    details_url = f"{BASE_URL}/movie/{movie_id}"
    details_params = {"api_key": API_KEY, "append_to_response": "credits", "language": "fr-FR"}
    details_response = requests.get(details_url, params=details_params)
    if details_response.status_code != 200:
        return None

    data = details_response.json()
    crew = data.get("credits", {}).get("crew", [])
    director = next((member["name"] for member in crew if member["job"] == "Director"), "Inconnu")
    
    cast_list = data.get("credits", {}).get("cast", [])[:5]
    actors = ", ".join([actor["name"] for actor in cast_list])

    genres_list = data.get("genres", [])
    genres = ", ".join([genre["name"] for genre in genres_list])

    poster_path = data.get("poster_path")
    poster_url = f"{IMAGE_BASE_URL}{poster_path}" if poster_path else ""

    release_date = data.get("release_date", "")
    movie_year = release_date.split("-")[0] if release_date else "Inconnue"

    return {
        "title": data.get("title"),
        "year": movie_year,
        "director": director,
        "actors": actors,
        "genres": genres,
        "synopsis": data.get("overview", "Aucun synopsis disponible."),
        "poster_url": poster_url
    }