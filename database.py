
import sqlite3
import os

DB_NAME = "ong_projetos.db"

def create_connection():
    """Create a database connection to the SQLite database specified by DB_NAME."""
    conn = None
    try:
        conn = sqlite3.connect(DB_NAME)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def create_table(conn, create_table_sql):
    """Create a table from the create_table_sql statement."""
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

def main():
    database = DB_NAME

    # SQL Code to create tables
    sql_create_editais_table = """
    CREATE TABLE IF NOT EXISTS editais (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_edital TEXT NOT NULL,
        orgao_financiador TEXT,
        data_limite TEXT,
        arquivo_pdf_path TEXT
    );
    """

    sql_create_projetos_table = """
    CREATE TABLE IF NOT EXISTS projetos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT,
        status TEXT NOT NULL,
        edital_id INTEGER,
        justificativa TEXT,
        objetivos TEXT,
        publico_alvo TEXT,
        FOREIGN KEY (edital_id) REFERENCES editais (id)
    );
    """

    sql_create_orcamentos_table = """
    CREATE TABLE IF NOT EXISTS orcamentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        projeto_id INTEGER NOT NULL,
        item TEXT NOT NULL,
        valor REAL,
        categoria TEXT,
        FOREIGN KEY (projeto_id) REFERENCES projetos (id)
    );
    """

    sql_create_anexos_table = """
    CREATE TABLE IF NOT EXISTS anexos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        projeto_id INTEGER NOT NULL,
        nome_arquivo TEXT NOT NULL,
        caminho_arquivo TEXT NOT NULL,
        FOREIGN KEY (projeto_id) REFERENCES projetos (id)
    );
    """

    # Create a database connection
    conn = create_connection()

    # Create tables
    if conn is not None:
        print("Creating table 'editais'...")
        create_table(conn, sql_create_editais_table)
        
        print("Creating table 'projetos'...")
        create_table(conn, sql_create_projetos_table)
        
        print("Creating table 'orcamentos'...")
        create_table(conn, sql_create_orcamentos_table)
        
        print("Creating table 'anexos'...")
        create_table(conn, sql_create_anexos_table)
        
        print("Database setup completed successfully.")
        conn.close()
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
