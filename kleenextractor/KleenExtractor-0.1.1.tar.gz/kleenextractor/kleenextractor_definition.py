from enum import Enum


class KleenExtractorDefinition(Enum):
    CREATE_TABLES_SCRIPT = """
        DROP TABLE IF EXISTS files;
        DROP TABLE IF EXISTS folders;
        CREATE TABLE files(
            source varchar(255),
            name varchar(255),
            parent varchar(255),
            executed integer(1)
        );
        CREATE TABLE folders(
            source varchar(255),
            name varchar(255),
            parent varchar(255),
            googleid varchar(255)
        );
    """
    INSERT_IN_FOLDER = """INSERT INTO folders(source, name, parent, googleid) VALUES (?, ?, ?, NULL)"""
    INSERT_IN_FILE = """INSERT INTO files(source, name, parent, executed) VALUES (?, ?, ?, 0)"""
    GET_ALL_FOLDERS = """SELECT count(*) FROM folders"""
    GET_ALL_FILES = """SELECT count(*) FROM files"""
