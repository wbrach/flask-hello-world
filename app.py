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

