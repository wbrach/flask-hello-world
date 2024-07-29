import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://database_example_for_lab_user:qvnuRwvx7q2cvBRV1xNY4MECSJnasLsN@dpg-cqjsad6ehbks73chrcl0-a/database_example_for_lab")
    conn.close()
    return "Database connection is successful"

@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgresql://database_example_for_lab_user:qvnuRwvx7q2cvBRV1xNY4MECSJnasLsN@dpg-cqjsad6ehbks73chrcl0-a/database_example_for_lab")
    cur = conn.cursor()
    cur.execute('''
            CREATE TABLE IF NOT EXISTS Basketball(
                First varchar(255),
                Last varchar(255),
                City varchar(255),
                Name varchar(255),
                Number int
            );
        ''')
    
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"


@app.route('/db_insert')
def db_insert():
    conn = psycopg2.connect("postgresql://database_example_for_lab_user:qvnuRwvx7q2cvBRV1xNY4MECSJnasLsN@dpg-cqjsad6ehbks73chrcl0-a/database_example_for_lab")
    cur = conn.cursor()
    cur.execute('''
    INSERT INTO Basketball (First, Last, City, Name, Number)
            VALUES
            ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
            ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
            ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
            ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
        ''')
    
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"
