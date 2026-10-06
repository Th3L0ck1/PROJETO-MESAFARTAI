"""
MESAFARTAI - Logística e Inteligência Assistiva no Combate à Fome
Módulo: database.py

Responsável por criar o banco de dados relacional SQLite3 (mesafartai.db)
com as tabelas fundamentais do sistema e popular com dados de teste (seeds).

Tabelas:
    - usuarios : Doadores e ONGs cadastrados (com coordenadas para o KNN)
    - doacoes  : Ofertas de alimentos registradas pelos doadores
    - matches  : Resultado do matchmaking logístico (doação -> ONG)

Execução (a partir da raiz do repositório):
    python src/database.py
"""

import os
import sqlite3
import sys

# Garante que os emojis dos prints funcionem em terminais Windows (cp1252)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# O banco é criado na raiz do repositório, independente de onde o script é chamado
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "mesafartai.db")


def conectar():
    """Abre uma conexão com o banco e habilita a checagem de chaves estrangeiras."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def inicializar_banco():
    conn = conectar()
    cursor = conn.cursor()

    # 1. Tabela de Usuários (Doadores e ONGs)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            tipo TEXT CHECK(tipo IN ('DOADOR', 'ONG')) NOT NULL,
            cep TEXT NOT NULL,
            latitude REAL,
            longitude REAL,
            telefone TEXT
        )
    ''')

    # 2. Tabela de Doações de Alimentos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS doacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            doador_id INTEGER,
            descricao_alimento TEXT NOT NULL,
            quantidade_kg REAL,
            data_validade TEXT,
            status TEXT DEFAULT 'DISPONIVEL',
            FOREIGN KEY (doador_id) REFERENCES usuarios (id)
        )
    ''')

    # 3. Tabela de Matches Logísticos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS matches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            doacao_id INTEGER,
            ong_id INTEGER,
            distancia_km REAL,
            data_match TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (doacao_id) REFERENCES doacoes (id),
            FOREIGN KEY (ong_id) REFERENCES usuarios (id)
        )
    ''')

    # Inserção de Carga Inicial (Seeds de Teste)
    cursor.execute("SELECT COUNT(*) FROM usuarios")
    if cursor.fetchone()[0] == 0:
        # Cadastra ONGs de teste
        cursor.execute("INSERT INTO usuarios (nome, tipo, cep, latitude, longitude, telefone) VALUES ('ONG Prato Quente', 'ONG', '06700-000', -23.612, -46.781, '11999990001')")
        cursor.execute("INSERT INTO usuarios (nome, tipo, cep, latitude, longitude, telefone) VALUES ('Abrigo Esperanca', 'ONG', '06705-000', -23.625, -46.795, '11999990002')")

        # Cadastra Doadores de teste
        cursor.execute("INSERT INTO usuarios (nome, tipo, cep, latitude, longitude, telefone) VALUES ('Supermercado Silva', 'DOADOR', '06701-000', -23.615, -46.785, '11999990003')")
        cursor.execute("INSERT INTO usuarios (nome, tipo, cep, latitude, longitude, telefone) VALUES ('Restaurante Sabor', 'DOADOR', '06703-000', -23.618, -46.789, '11999990004')")

        # Cadastra Doações de teste (para já termos dados no futuro matchmaking KNN)
        cursor.execute("INSERT INTO doacoes (doador_id, descricao_alimento, quantidade_kg, data_validade) VALUES (3, 'Frutas e verduras', 30.0, '2026-10-07')")
        cursor.execute("INSERT INTO doacoes (doador_id, descricao_alimento, quantidade_kg, data_validade) VALUES (4, 'Marmitas prontas', 12.5, '2026-10-06')")
        print("✅ Dados iniciais de teste inseridos com sucesso!")

    conn.commit()
    conn.close()
    print(f"✅ Banco de dados 'mesafartai.db' inicializado com sucesso! ({DB_PATH})")


def listar_tabelas():
    """Função auxiliar para conferir rapidamente o conteúdo do banco."""
    conn = conectar()
    cursor = conn.cursor()
    for tabela in ("usuarios", "doacoes", "matches"):
        cursor.execute(f"SELECT COUNT(*) FROM {tabela}")
        print(f"   - {tabela}: {cursor.fetchone()[0]} registro(s)")
    conn.close()


if __name__ == "__main__":
    inicializar_banco()
    listar_tabelas()
