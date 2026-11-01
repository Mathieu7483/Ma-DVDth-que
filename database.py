import sqlite3

class Database:
    def __init__(self, db_name="dvds.db"):
        self.db_name = db_name
        self.init_db()

    def get_connection(self):
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row
        return conn

    def init_db(self):
        with self.get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS dvds (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    year TEXT,
                    director TEXT,
                    actors TEXT,
                    genres TEXT,
                    synopsis TEXT,
                    poster_url TEXT
                )
            """)
            # Migration douce si la colonne 'genres' n'existait pas
            cursor = conn.execute("PRAGMA table_info(dvds)")
            columns = [column[1] for column in cursor.fetchall()]
            if "genres" not in columns:
                conn.execute("ALTER TABLE dvds ADD COLUMN genres TEXT")
            conn.commit()

    def add_dvd(self, dvd_data: dict):
        with self.get_connection() as conn:
            conn.execute("""
                INSERT INTO dvds (title, year, director, actors, genres, synopsis, poster_url)
                VALUES (:title, :year, :director, :actors, :genres, :synopsis, :poster_url)
            """, dvd_data)
            conn.commit()

    def get_all_dvds(self, search_query="", genre_filter="") -> list:
        with self.get_connection() as conn:
            query = "SELECT * FROM dvds WHERE 1=1"
            params = []

            if search_query:
                query += " AND (title LIKE ? OR director LIKE ? OR actors LIKE ? OR genres LIKE ?)"
                p = f"%{search_query}%"
                params.extend([p, p, p, p])

            if genre_filter:
                query += " AND genres LIKE ?"
                params.append(f"%{genre_filter}%")

            query += " ORDER BY title ASC"
            cursor = conn.execute(query, params)
            return [dict(row) for row in cursor.fetchall()]

    def get_all_genres(self) -> list:
        """Récupère la liste de tous les genres uniques présents dans la base."""
        with self.get_connection() as conn:
            cursor = conn.execute("SELECT genres FROM dvds WHERE genres IS NOT NULL AND genres != ''")
            raw_genres = cursor.fetchall()
            genres_set = set()
            for row in raw_genres:
                for g in row["genres"].split(","):
                    genres_set.add(g.strip())
            return sorted(list(genres_set))

    def delete_dvd(self, dvd_id: int):
        with self.get_connection() as conn:
            conn.execute("DELETE FROM dvds WHERE id = ?", (dvd_id,))
            conn.commit()