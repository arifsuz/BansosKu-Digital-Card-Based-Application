import sqlite3
import os


def get_connection():
    base_dir = os.path.dirname(__file__)
    db_path = os.path.join(base_dir, "bansosku.db")
    return sqlite3.connect(db_path)
