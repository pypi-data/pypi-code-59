import sqlite3
from glob import glob

from os import path
from .kleenextractor_definition import KleenExtractorDefinition


class KleenExtractor:
    def __init__(self):
        self.conn = sqlite3.connect('extract.db')
        self.path_source = None

    def create_tables(self):
        try:
            cursor = self.conn.cursor()
            cursor.executescript(KleenExtractorDefinition.CREATE_TABLES_SCRIPT.value)
            cursor.close()
        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)

    def set_path_source(self, path_source: str):
        if path_source.endswith('\\'):
            path_source = path_source[:-1]
        self.path_source = path_source + "\\**"

    def insert_in_db(self, current_path, isdir):
        parent = current_path.split("\\")
        name = parent.pop()
        parent = "\\".join(parent)
        cursor = self.conn.cursor()
        if isdir:
            if name != "":
                cursor.execute(KleenExtractorDefinition.INSERT_IN_FOLDER.value, (current_path, name, parent))
        else:
            cursor.execute(KleenExtractorDefinition.INSERT_IN_FILE.value, (current_path, name, parent))
        cursor.close()

    def get_all(self, isdir):
        cursor = self.conn.cursor()
        if isdir:
            cursor.execute(KleenExtractorDefinition.GET_ALL_FOLDERS.value)
            print(f"Folders : {cursor.fetchone()}")
        else:
            cursor.execute(KleenExtractorDefinition.GET_ALL_FILES.value)
            print(f"Files : {cursor.fetchone()}")
        cursor.close()

    def extract_folder(self):
        self.create_tables()
        path_source = self.path_source
        extract = glob(path_source, recursive=True)
        for entry in extract:
            self.insert_in_db(entry, path.isdir(entry))
        self.conn.commit()


kleenextractor = KleenExtractor()
