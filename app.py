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
    