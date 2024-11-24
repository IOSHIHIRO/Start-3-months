import sqlite3

class Database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                """
                    CREATE TABLE IF NOT EXISTS survey_results (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        phone_number INTEGER,
                        visit_date TEXT,
                        food_rating TEXT,
                        cleanliness_rating INTEGER,
                        extra_comments TEXT
                    )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS dish_categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS dishes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                price INTEGER,
                category INTEGER,
                FOREIGN KEY(category) REFERENCES dishes(category_id)
                )
                """
            )
            conn.commit()


    def execute(self, query: str, params: tuple):
        with sqlite3.connect(self.path) as conn:
            conn.execute(query, params)
            conn.commit()

    def fetch(self, query: str, params: tuple = None):
        with sqlite3.connect(self.path) as conn:
            if not params:
                params = tuple()
            result = conn.execute(query, params)
            result.row_factory = sqlite3.Row
            data = result.fetchall()
            return [dict(r) for r in data]


# comm = sqlite3.connect('database.db')
# cursor = comm.cursor()
#
# comm.execute("""
# CREATE TABLE IF NOT EXTSTS opros (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT,
#     age INTEGER,
#     gender TEXT,
#     genre TEXT
# )
# """)
#
# comm.commit()