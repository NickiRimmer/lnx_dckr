from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# Database connection settings
db_host = os.getenv('DB_HOST', 'postgres')
db_port = os.getenv('DB_PORT', '5432')
db_name = os.getenv('DB_NAME', 'usr_1')
db_user = os.getenv('DB_USER', 'web_usr')
db_password = os.getenv('DB_PASSWORD', '1234')

# Route to fetch users
def get_db_connection():
    return psycopg2.connect(
        host=db_host,
        port=db_port,
        database=db_name,
        user=db_user,
        password=db_password
    )

@app.route('/')
def index():
    return "Welcome for list users GET users"

@app.route('/users', methods=['GET'])
def get_users():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, district FROM usrs;")
        users = cursor.fetchall()
        cursor.close()
        conn.close()
        # Format data as JSON
        users_list = [
            {"id": user[0], "name": user[1], "district": user[2]} for user in users
        ]
        return jsonify(users_list)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
