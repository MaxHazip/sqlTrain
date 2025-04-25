import sqlite3
con = sqlite3.Connection('../data/sqlTrain.db')
cur = con.cursor()
query = '''
    CREATE TABLE genders (
        id INT PRIMARY KEY,
        name VARCHAR(100)
    );
'''
cur.execute(query)

query = '''INSERT INTO genders(id, name) VALUES (1, "М"), (2, "Ж");'''
cur.execute(query)

query = '''
    CREATE TABLE program_types (
        id INT PRIMARY KEY,
        name VARCHAR(100)
    );
'''
cur.execute(query)

query = '''INSERT INTO program_types(id, name) VALUES (1, "Индивидуальная"), (2, "Групповая");'''
cur.execute(query)

query = '''
    CREATE TABLE promotion_types (
        id INT PRIMARY KEY,
        name VARCHAR(100)
    );
'''
cur.execute(query)

query = '''INSERT INTO promotion_types(id, name) VALUES (1, "Дисконтная"), (2, "Бонусная"), (3, "Партнерская");'''
cur.execute(query)

query = '''
    CREATE TABLE promotions (
        id INT PRIMARY KEY,
        name VARCHAR(100),
        promotion_type_id INT,
        start_date DATE,
        period DATE,
        FOREIGN KEY (promotion_type_id) REFERENCES promotion_types (id)
    );
'''
cur.execute(query)

query = '''
    INSERT INTO promotions(id, name, promotion_type_id, start_date, period) 
    VALUES (1, "Приведи друга и получи скидку", 1, "2024-10-01", "2025-03-01"),
    (2, "Повышенные бонусы на месяц", 2, "2024-10-01", "2024-11-01"),
    (3, "Приведи друга и получи скидку", 3, "2025-09-01", "2028-01-01");
'''
cur.execute(query)

query = '''
    CREATE TABLE subscriptions (
        id INT PRIMARY KEY,
        subscription_type VARCHAR(100),
        price DECIMAL
    );
'''
cur.execute(query)

query = '''
    INSERT INTO subscriptions(id, subscription_type, price) 
    VALUES (1, "Недельный", 2000),
    (2, "Месячный", 4000),
    (3, "Годовой", 12000);
'''
cur.execute(query)

query = '''
    CREATE TABLE training_types (
        id INT PRIMARY KEY,
        name VARCHAR(100)
    );
'''
cur.execute(query)

query = '''
    INSERT INTO training_types(id, name) 
    VALUES (1, "Кардио"),
    (2, "Силовая"),
    (3, "Жиросжигающая"),
    (4, "Аэробные"),
    (5, "Анаэробные"),
    (6, "Круговые"),
    (7, "Интервальные"),
    (8, "Сплит"),
    (9, "Йога"),
    (10, "Шейпинг"),
    (11, "Калланетика"),
    (12, "Bodyart");
'''
cur.execute(query)

query = '''
    CREATE TABLE clients(
        id INT PRIMARY KEY,
        first_name VARCHAR(100),
        middle_name VARCHAR(100),
        last_name VARCHAR(100),
        birthday DATE,
        phone_number VARCHAR(100),
        email VARCHAR(100),
        gender_id INT,
        subscription_id INT,
        FOREIGN KEY (gender_id) REFERENCES genders (id),
        FOREIGN KEY (subscription_id) REFERENCES subscriptions (id)
    );
'''
cur.execute(query)

query = '''INSERT INTO clients(id, first_name, middle_name, last_name, birthday, phone_number, email, gender_id, subscription_id) 
    VALUES (1, "Иван", "Александрович", "Волков", "1997-02-01", "+7(342)342-32-43", "bober@gmail.com", 1, 2),
    (2, "Жанна", "Орлеанская", "д'Арк", "1431-05-30", "+7(433)342-43-43", NULL, 2, 3),
    (3, "Изат", "Монобас", "Бар", "1901-01-01", NULL, "tsar@gmail.com", 1, 1),
    (4, "Роберт", "Владиславович", "Волков", "1978-10-01", "+7(932)452-67-32", "folder@gmail.com", 1, 2),
    (5, "Анна", "Вячеславовна", "Боганова", "2001-02-16", "+7(231)643-32-32", NULL, 2, 3),
    (6, "Иван", "Артемович", "Захаров ", "1972-06-01", "+7(321)435-43-23", "grober@gmail.com", 1, 1),
    (7, "Артур", "Владимирович", "Михайлов", "1990-06-01", "7(22)338-85-69", "guzoco_fado12@hotmail.com", 1, 3),
    (8, "Стефания", "Антоновна", "Андреева", "2006-02-01", "7(6216)649-85-34", "gix_ogabeku24@aol.com", 3, 2),
    (9, "Дмитрий", "Сергеевич", "Денисов", "1988-06-01", "7(6035)765-98-92", "rako-wiginu57@list.ru", 1, 3),
    (10, "Варвара", "Дмитриевна", "Жданова", "1984-10-01", "7(7747)108-71-51", "puf-idisigo26@mail.ru", 2, 1),
    (11, "Николай", "Витальевич", "Белкин", "1982-03-01", "7(37)761-80-62", "judohet-ofe40@yandex.ru", 1, 2),
    (12, "Кира", "Дмитриевна", "Кузнецова", "1995-06-01", "7(3862)895-64-32", "ziwij_acaca38@bk.ru", 2, 3),
    (13, "Андрей", "Тимофеевич", "Астахов", "1990-05-03", "7(302)647-92-17", "yuha_kovowo14@hotmail.com", 1, 2),
    (14, "Ольга", "Владимировна", "Харитонова", "2008-10-01", "7(3690)646-36-32", "yupake_doga9@bk.ru", 2, 3),
    (15, "Лев", "Егорович", "Ершов", "1968-10-01", "7(980)165-28-08", "helula_jage90@bk.ru", 1, 1),
    (16, "Серафима", "Сергеевна", "Соколова", "1989-10-12", "7(785)543-14-40", "cutaka_zuze39@gmail.com", 2, 2),
    (17, "Артем", "Павлович", "Алексеев", "1998-06-01", NULL, "wuwer-oxiju22@hotmail.com", 1, 3),
    (18, "Мелания", "Романовна", "Прокофьева", "2003-06-01", "7(76)841-29-36", "pojo-perigu53@yahoo.com", 2, 1),
    (19, "Мирон", "Григорьевич", "Ермолаев", "1993-10-01", "7(852)797-65-35", "luyuz_emifo92@hotmail.com", 1, 1),
    (20, "Григорий", "Эмильевич", "Марков", "2001-10-01", "7(39)128-15-67", NULL, 1, 2),
    (21, "Виктория", "Ярославовна", "Герасимова", "2007-06-08", "7(516)194-57-98", "hohoti-cufe91@mail.ru", 2, 3),
    (22, "Константин", "Иванович", "Гаврилов", "2005-09-01", "7(7874)106-49-05", "buzu-joteye7@yahoo.com", 1, 2),
    (23, "Евдокия", "Леонидовна", "Коровина", "1994-06-01", "7(96)531-05-78", "novegot-ato84@bk.ru", 1, 3),
    (24, "Алиса", "Семеновна", "Исаева", "1998-06-01", "7(7234)149-92-33", "pohe-xibumi4@hotmail.com", 2, 1),
    (25, "Дмитрий", "Владиславович", "Костин", "1999-06-01", "7(49)393-59-03", "debe_zukeza64@gmail.com", 1, 1);
'''
cur.execute(query)

query = '''
    CREATE TABLE trainers(
        id INT PRIMARY KEY,
        first_name VARCHAR(100),
        middle_name VARCHAR(100),
        last_name VARCHAR(100),
        birthday DATE,
        phone_number VARCHAR(100),
        email VARCHAR(100),
        address VARCHAR(100),
        gender_id INT,
        passport_details VARCHAR(100),
        hiring_date VARCHAR(100),
        experience_year INT,
        FOREIGN KEY (gender_id) REFERENCES genders (id)
    );
'''
cur.execute(query)

query = '''INSERT INTO trainers(id, first_name, middle_name, last_name, birthday, phone_number, email, address, gender_id, passport_details, hiring_date, experience_year) 
    VALUES (1, "Билли", "Райский", "Херрингтон", "1969-07-14", NULL, "RestInPeace@heaven.com", "Калифорния, Катидрал-Сити, кладбище Форест- Лаун.", 1, "5434654323", "2008-02-20", 28),
    (2, "Рональд", "Дин", "Коулмэн", "1964-05-13", "+7(323)324-43-12", NULL, "602 3rd Ave, Bessemer, Michigan 49911, USA", 1, "2135732951", "1938-06-25", 7),
    (3, "Алина", "Молинари", "Попа", "1978-10-12", "+7(543)543-54-12", NULL, "2337 North St, Milford, Michigan 48380, USA", 2, "5431379064", "2010-02-25", 8),
    (4, "Владимир ", "Михайлович", "Скворцов", "1988-10-01", "7(355)337-06-05", "pokir_ojato40@aol.com", "244 W Amy St, Hastings, Michigan 49058, USA", 1, "9954618826", "2023-06-01", 5),
    (5, "Аврора", "Арсентьевна", "Виноградова", "1996-05-01", "7(2982)265-65-30", "gayeya-sezo99@mail.ru", "433 S Ashley St, Ann Arbor, Michigan 48103, USA", 2, "1772620848", "2022-06-01", 2),
    (6, "Кирил", "Львович", "Краснов ", "1996-05-01", NULL, "kobiho_mune60@aol.com", "13989 Hearthstone Ln, Hartland, Michigan 483, USA", 1, "3155260973", "2022-06-01", 3),
    (7, "Ксения", "Кирилловна", "Колосова", "1996-10-13", "7(63)952-57-89", "hibi_becoze74@mail.ru", "218 Highland Dr, Highland, Michigan 48357, USA", 2, "2045376636", "2024-06-01", 3),
    (8, "Максим", "Алексеевич", "Сергеев", "2000-07-01", "7(5000)155-89-52", "jubosid-iye9@internet.ru", "5494 Wildwood Dr, Howell, Michigan 48843, USA", 1, "1389701980", "2023-06-01", 3),
    (9, "Мария", "Леонидовна", "Козлова", "1994-06-01", "7(17)981-24-50", "nopupa_vogu70@list.ru", "1311 Glen Park Dr, Sparta, Michigan 49345, USA", 2, "433363557", "2025-01-01", 1),
    (10, "Давид", "Иванович", "Гусев", "1991-05-01", "7(020)195-69-57", "vuc-ekowuwu19@gmail.com", "23225 Johnston Ave, Eastpointe, Michigan 021, USA", 1, "1190750558", "2023-06-15", 3);
'''
cur.execute(query)

query = '''
    CREATE TABLE workouts(
        id INT PRIMARY KEY,
        training_type_id INT,
        programm_type_id INT,
        duration TIME,
        trainer_id INT,
        price DECIMAL,
        promotion_id INT,
        FOREIGN KEY (training_type_id) REFERENCES training_types (id),
        FOREIGN KEY (programm_type_id) REFERENCES program_types (id),
        FOREIGN KEY (trainer_id) REFERENCES trainers (id),
        FOREIGN KEY (promotion_id) REFERENCES promotions (id)
    );
'''
cur.execute(query)

query = '''INSERT INTO workouts(id, training_type_id, programm_type_id, duration, trainer_id, price, promotion_id) 
    VALUES (1, 1, 2, "01:00:00", 1, 10000, 1),
    (2, 3, 1, "01:20:00", 2, 5000, 2),
    (3, 2, 1, "12:00:00", 3, 20000, NULL),
    (4, 6, 1, "01:20:00", 10, 5000, NULL),
    (5, 2, 2, "01:00:00", 7, 2000, 2),
    (6, 6, 1, "02:00:00", 6, 3000, NULL),
    (7, 8, 1, "02:00:00", 8, 2000, 1),
    (8, 5, 2, "01:20:00", 5, 2000, NULL),
    (9, 1, 1, "02:00:00", 10, 2000, NULL),
    (10, 4, 1, "01:20:00", 5, 1000, NULL),
    (11, 3, 2, "02:00:00", 6, 3000, 1),
    (12, 4, 1, "01:20:00", 4, 3000, NULL),
    (13, 5, 1, "01:20:00", 8, 3000, NULL),
    (14, 3, 1, "02:00:00", 1, 4000, NULL),
    (15, 4, 2, "03:00:00", 2, 2000, NULL),
    (16, 5, 2, "02:00:00", 5, 4000, NULL),
    (17, 3, 1, "02:00:00", 5, 3000, NULL),
    (18, 1, 1, "02:00:00", 6, 5000, NULL),
    (19, 10, 1, "02:00:00", 7, 2000, NULL),
    (20, 4, 1, "01:00:00", 5, 3000, NULL),
    (21, 5, 1, "02:00:00", 8, 2000, NULL),
    (22, 5, 1, "02:00:00", 7, 2000, NULL),
    (23, 11, 1, "01:20:00", 8, 1000, NULL),
    (24, 7, 2, "01:20:00", 10, 3000, NULL),
    (25, 8, 2, "02:30:00", 7, 4000, NULL);
'''
cur.execute(query)

query = '''
    CREATE TABLE clients_in_training(
        id INT PRIMARY KEY,
        workout_id INT,
        client_id INT,
        FOREIGN KEY (workout_id) REFERENCES workouts (id),
        FOREIGN KEY (client_id) REFERENCES clients (id)
    );
'''
cur.execute(query)

query = '''INSERT INTO clients_in_training(id, workout_id, client_id) 
    VALUES (1, 1, 1),
    (2, 1, 2),
    (3, 3, 3),
    (4, 3, 16),
    (5, 1, 23),
    (6, 2, 22),
    (7, 3, 9),
    (8, 1, 19),
    (9, 2, 16),
    (10, 3, 5),
    (11, 1, 25),
    (12, 2, 7),
    (13, 3, 6),
    (14, 2, 20),
    (15, 2, 17),
    (16, 3, 9),
    (17, 3, 5),
    (18, 2, 24),
    (19, 2, 7),
    (20, 2, 7),
    (21, 3, 20),
    (22, 2, 7),
    (23, 3, 4),
    (24, 2, 20),
    (25, 3, 24);
'''
cur.execute(query)

print(cur.fetchall())

con.commit()
con.close()