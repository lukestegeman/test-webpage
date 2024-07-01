from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# Database file will be stored in a temporary directory
DATABASE = '/tmp/subscribers.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subscribers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.before_first_request
def initialize():
    init_db()

@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.get_json()
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    email = data.get('email')

    if not first_name or not last_name or not email:
        return jsonify({'message': 'Missing data'}), 400

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO subscribers (first_name, last_name, email)
        VALUES (?, ?, ?)
    ''', (first_name, last_name, email))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Subscription successful'})

if __name__ == '__main__':
    app.run()


