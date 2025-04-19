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

query = '''INSERT INTO promotions(id, name, promotion_type_id, start_date, period) VALUES (1, "Приведи друга и получи скидку", 1, "2024-10-01", "2025-03-01"),
    (2, "Повышенные бонусы на месяц", 2, "2024-10-01", "2024-11-01"),
    (3, "Приведи друга и получи скидку", 3, "2025-09-01", "2028-01-01");
'''
cur.execute(query)

query = '''
    CREATE TABLE subscriptions (
        id INT PRYMARY KEY,
        name VARCHAR(100),
        price DECIMAL
    );
'''
cur.execute(query)

query = '''INSERT INTO promotions(id, subscription_type, price) VALUES (1, "Недельный", 2000),
    (2, "Месячный", 4000),
    (3, "Годовой", 12000);
'''
cur.execute(query)

query = '''
    CREATE TABLE training_types (
        id INT PRYMARY KEY,
        name VARCHAR(100)
    );
'''
cur.execute(query)

query = '''INSERT INTO promotions(id, name) VALUES (1, "Кардио"),
    (1, "Силовая"),
    (1, "Жиросжигающая"),
    (1, "Аэробные"),
    (1, "Анаэробные"),
    (1, "Круговые"),
    (1, "Интервальные"),
    (1, "Сплит"),
    (1, "Йога"),
    (1, "Шейпинг"),
    (1, "Калланетика"),
    (1, "Bodyart");
'''
cur.execute(query)

query = '''
    CREATE TABLE training_types (
        id INT PRYMARY KEY,
        first_name VARCHAR(100),
        middle_name VARCHAR(100),
        last_name VARCHAR(100),
        birthday DATE,
        phone_number VARCHAR(100),
        email VARCHAR(100),
        gender_id INT,
        subscription_id INT,
    );
'''
cur.execute(query)

query = '''INSERT INTO promotions(id, name) VALUES (1, "Кардио"),
    (1, "Силовая"),
    (1, "Жиросжигающая"),
    (1, "Аэробные"),
    (1, "Анаэробные"),
    (1, "Круговые"),
    (1, "Интервальные"),
    (1, "Сплит"),
    (1, "Йога"),
    (1, "Шейпинг"),
    (1, "Калланетика"),
    (1, "Bodyart");
'''
cur.execute(query)

print(cur.fetchall())

con.commit()
con.close()