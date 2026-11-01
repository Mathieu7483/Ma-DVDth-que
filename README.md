<p align="center">
<img src="https://raw.githubusercontent.com/Mathieu7483/Ma-DVDth-que/main/Ma%20dvdth%C3%A8que.jpg" width="800px" alt="Ma DVDthèque Banner">
</p>
<p align="center">
<img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Flask-2.0+-green?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
<img src="https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
</p>

# 🎬 Ma DVDthèque

> Une application web locale style *Prime Video* développée en Python et Flask pour gérer, cataloguer et explorer sa collection physique de DVD et de séries TV.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0%2B-black?style=for-the-badge&logo=flask&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?style=for-the-badge&logo=bootstrap&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-informational?style=for-the-badge&logo=sqlite&logoColor=white)
![TMDb API](https://img.shields.io/badge/API-TMDb-green?style=for-the-badge&logo=themoviedb&logoColor=white)

---

## ✨ Fonctionnalités

* **Recherche & Import Automatique (Films & Séries)** : Couplage intelligent avec l'API TMDb pour récupérer instantanément les affiches, synopsis, réalisateurs, acteurs et genres à partir d'une simple liste textuelle.
* **Gestion des Séries TV** : Prise en charge transparente des intégrales de séries (comme *Frères d'armes*) en plus des longs-métrages.
* **Ajout Manuel Sur-Mesure** : Formulaire dédié pour ajouter ou corriger des éditions spéciales, des raretés ou des objets non référencés.
* **Interface Style Streaming** : Design sombre, épuré et responsive inspiré des plateformes de streaming modernes (grâce à Bootstrap).
* **Gestion en un clic** : Suppression directe des œuvres indésirables directement depuis leur fiche.
* **Alimentation par Script (`seed.py`)** : Nettoyage rigoureux des caractères invisibles, dédoublonnage strict et import massif automatisé.

---

## 🛠️ Stack Technique

* **Back-end** : Python, Flask (Routes, Templates Jinja2)
* **Base de données** : SQLite (via un module de gestion dédié `database.py`)
* **Services externes** : API TMDb (v3) pour les métadonnées et affiches officielles
* **Front-end** : HTML5, CSS3, Bootstrap 5

---

## 🚀 Installation & Lancement local

### 1. Cloner le projet
```bash
git clone [https://github.com/Mathieu7483/Ma-DVDth-que.git](https://github.com/Mathieu7483/Ma-DVDth-que.git)
cd Ma-DVDth-que

```

### 2. Configurer l'environnement virtuel

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```

### 3. Configurer votre clé API TMDb

Ouvrez le fichier `tmdb_service.py` et insérez votre clé API personnelle :

```python
API_KEY = "VOTRE_VRAIE_CLE_API_TMDB"

```

### 4. Initialiser la base de données (Seed)

Remplissez votre liste de films dans `movies_list.txt`, puis lancez le script d'importation :

```bash
python3 seed.py

```

### 5. Lancer l'application

```bash
python3 app.py

```

Ouvrez ensuite votre navigateur à l'adresse : `http://127.0.0.1:5000`

---

## 📂 Structure du Projet

```text
Ma-DVDthèque/
│
├── static/
│   └── style.css            # Styles personnalisés additionnels
├── templates/
│   ├── index.html           # Page d'accueil / Catalogue principal
│   ├── add.html             # Interface d'ajout automatique
│   └── add_manual.html      # Formulaire de saisie manuelle
├── app.py                   # Cœur de l'application Flask et routes
├── database.py              # Gestion de la base de données SQLite
├── tmdb_service.py          # Logique d'interrogation de l'API TMDb (Films & Séries)
├── seed.py                  # Script d'importation automatisée en masse
├── movies_list.txt          # Liste brute des titres de la collection
└── README.md                # Documentation du projet

```

---

## 👤 Auteur

Projet personnel développé par **Mathieu** dans le cadre de son apprentissage de la programmation.

```

---
