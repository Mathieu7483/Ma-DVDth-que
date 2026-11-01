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
                    synopsis TEXT,
                    poster_url TEXT
                )
            """)
            conn.commit()

    def add_dvd(self, dvd_data: dict):
        with self.get_connection() as conn:
            conn.execute("""
                INSERT INTO dvds (title, year, director, actors, synopsis, poster_url)
                VALUES (:title, :year, :director, :actors, :synopsis, :poster_url)
            """, dvd_data)
            conn.commit()

    def get_all_dvds(self) -> list:
        with self.get_connection() as conn:
            cursor = conn.execute("SELECT * FROM dvds ORDER BY id DESC")
            return [dict(row) for row in cursor.fetchall()]