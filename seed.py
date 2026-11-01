import time
from database import Database
from tmdb_service import search_and_get_movie_details

def seed_database(filepath="movies_list.txt"):
    db = Database()
    
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{filepath}' est introuvable.")
        return

    print(f"Début de l'importation de {len(lines)} films...")

    success_count = 0
    for line in lines:
        title = line.strip()
        if not title:
            continue
        
        print(f"Recherche et ajout de : '{title}'...")
        dvd_data = search_and_get_movie_details(title)
        
        if dvd_data:
            db.add_dvd(dvd_data)
            success_count += 1
            print(f"  -> Succès : {dvd_data['title']} ({dvd_data['year']}) ajouté.")
        else:
            print(f"  -> Échec : Film introuvable pour '{title}'.")
        
        # Petite pause pour éviter de saturer l'API TMDb (rate limiting)
        time.sleep(0.25)

    print(f"\nImportation terminée ! {success_count} films ajoutés avec succès à votre base de données.")

if __name__ == "__main__":
    seed_database()