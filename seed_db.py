
import sqlite3

def seed_db():
    conn = sqlite3.connect("ong_projetos.db")
    cursor = conn.cursor()
    
    # Inserir um edital de exemplo
    cursor.execute("""
        INSERT INTO editais (nome_edital, orgao_financiador, data_limite, arquivo_pdf_path)
        VALUES ('Edital Cultura Viva 2026', 'Ministério da Cultura', '2026-12-31', 'edital_exemplo.pdf')
    """)
    
    # Inserir um projeto de exemplo
    cursor.execute("""
        INSERT INTO projetos (titulo, autor, status, edital_id)
        VALUES ('Oficina de Artesanato Sustentável', 'Ana da Silva', 'Em Preenchimento', 1)
    """)
    
    conn.commit()
    conn.close()
    print("Banco de dados populado com sucesso!")

if __name__ == "__main__":
    seed_db()
