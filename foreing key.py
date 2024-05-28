import psycopg2 as pc

connect = pc.connect(
    database='Test',
    user='postgres',
    password='Timur',
    port='5432'
)

cursor = connect.cursor()

# Создаем таблицу с работниками, обязательно с Primary key
cursor.execute("""CREATE TABLE IF NOT EXISTS workers( 
            id_fk SERIAL PRIMARY KEY,
            name VARCHAR(250),
            age INT,
            gender TEXT
)""")

# Создаем таблицу с зарплатой, обязательно с Primary key
cursor.execute("""CREATE TABLE IF NOT EXISTS money(
            id SERIAL PRIMARY KEY,
            cost INT
)""")

# Заполняем таблицу с работниками
cursor.execute("""INSERT INTO workers(name, age, gender) VALUES
('Коля', 20, 'м'),
('Яна', 19, 'ж'),
('Денис', 21, 'м'),
('Катя', 27, 'ж')
""")


# Заполняем таблицу с зп
cursor.execute("""INSERT INTO money(cost) VALUES (20000), (30000), (40000), (50000)""")

# В двух таблицах fk у ID, теперь можно их связать
cursor.execute("""ALTER TABLE workers ADD zp BIGINT REFERENCES money (id)""")

# Обращаемся к обьекту с id 1  из таблицы workers, а точнее к столбцу, заполняя значением из таблицы money с id 4
cursor.execute("""UPDATE workers SET zp = 1 WHERE id = 4""")
