import time
import re
from database import Database
from tmdb_service import search_and_get_movie_details

def seed_database(filepath="movies_list.txt"):
    db = Database()
    
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            raw_lines = f.readlines()
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{filepath}' est introuvable.")
        return

    # Nettoyage et suppression automatique des doublons de la liste
    seen_titles = set()
    cleaned_lines = []
    
    for line in raw_lines:
        cleaned = line.replace('\xa0', ' ').strip()
        if cleaned and not cleaned.startswith("#"):
            # On vérifie que la ligne n'a pas déjà été traitée
            if cleaned.lower() not in seen_titles:
                seen_titles.add(cleaned.lower())
                cleaned_lines.append(cleaned)

    print(f"Début de l'importation de {len(cleaned_lines)} films uniques...")

    success_count = 0
    for raw_line in cleaned_lines:
        # Extraction du titre et de l'année optionnelle ex: "Aladdin (1992)"
        match = re.match(r"^(.*?)\s*\((\d{4})\)$", raw_line)
        if match:
            title = match.group(1).strip()
            year = match.group(2)
        else:
            title = raw_line
            year = None

        if not title:
            continue
        
        print(f"Recherche de : '{title}' (Année: {year if year else 'Libre'})...")
        dvd_data = search_and_get_movie_details(title, year)
        
        if dvd_data:
            db.add_dvd(dvd_data)
            success_count += 1
            print(f"  -> [SUCCÈS] Ajouté : {dvd_data['title']} ({dvd_data['year']})")
        else:
            print(f"  -> [ÉCHEC] Introuvable : '{raw_line}'")
        
        time.sleep(0.2)

    print(f"\nImportation terminée ! {success_count} films uniques ajoutés avec succès.")

if __name__ == "__main__":
    seed_database()