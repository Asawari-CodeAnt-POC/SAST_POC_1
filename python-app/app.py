from flask import Flask, request
import sqlite3

app = Flask(__name__)

# Vulnerability 1: Hardcoded Secret Key
app.secret_key = "hardcoded_flask_secret"

# Vulnerability 2: SQL Injection
@app.route('/search')
def search():
    """Searches for user records in the database by username from the request query parameters.
    Parameters:
        - None: This function does not take explicit parameters; it reads username from the incoming request's query string.
    Returns:
        - str: A string representation of the query results fetched from the users database."""
    username = request.args.get('username')
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username = '{username}'"
    results = cursor.execute(query).fetchall()

    return str(results)

# Vulnerability 3: Sensitive Data Exposure
@app.route('/config')
def config():
    return {
        "db_password": "Admin@123",
        "api_key": "XYZ-SECRET-KEY"
    }

# Vulnerability 4: Debug Mode Enabled
if __name__ == '__main__':
    app.run(debug=True)