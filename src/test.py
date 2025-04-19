import sqlite3
con = sqlite3.Connection('../data/sqlTrain.db')
cur = con.cursor()
query = '''
    CREATE TABLE genders (
        id INT PRYMARY KEY,
        name VARCHAR(100)
    );
'''
cur.execute(query)

query = '''INSERT INTO genders(id, name) VALUES (1, "М"), (2, "Ж");'''
cur.execute(query)

query = '''
    CREATE TABLE program_types (
        id INT PRYMARY KEY,
        name VARCHAR(100)
    );
'''
cur.execute(query)

query = '''INSERT INTO program_types(id, name) VALUES (1, "Индивидуальная"), (2, "Групповая");'''
cur.execute(query)

query = '''
    CREATE TABLE promotion_types (
        id INT PRYMARY KEY,
        name VARCHAR(100)
    );
'''
cur.execute(query)

query = '''INSERT INTO promotion_types(id, name) VALUES (1, "Дисконтная"), (2, "Бонусная"), (2, "Партнерская");'''
cur.execute(query)

query = '''
    CREATE TABLE promotions (
        id INT PRYMARY KEY,
        name VARCHAR(100),
        promotion_type_id INT,
        start_date DATE,
        period DATE,
        FOREIGN KEY (promotion_type_id) REFERENCES promotion_types (id)
    );
'''
cur.execute(query)

query = '''INSERT INTO promotions(id, name, promotion_type_id, start_date, period) VALUES (1, "Приведи друга и получи скидку", 1, "2024-10-01", "2025-03-01"), (2, "Бонусная"), (2, "Партнерская");'''
cur.execute(query)

print(cur.fetchall())

con.commit()
con.close()