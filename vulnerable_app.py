import os
import sqlite3
import hashlib
from flask import Flask, request, make_response

app = Flask(__name__)
@app.route("/")
def index():
    return """
    <h1>Vulnerable App - ZAP Target</h1>
    <ul>
        <li><a href="/user?username=admin">Test SQL Injection</a></li>
        <li><a href="/ping?ip=127.0.0.1">Test Command Injection</a></li>
        <li><a href="/hello?name=ZAP">Test XSS</a></li>
        <li><a href="/calc?expr=1%2B1">Test Eval</a></li>
    </ul>
    """
# 1. MAUVAISE PRATIQUE : Secret / Mot de passe en dur
DB_PASSWORD = "SuperSecretAdminPassword123!"

# 2. INJECTION SQL (CWE-89)
@app.route("/user")
def get_user():
    username = request.args.get("username", "")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # Vulnérable à l'injection SQL
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return str(rows)

# 3. INJECTION DE COMMANDE OS
@app.route("/ping")
def ping():
    ip = request.args.get("ip", "127.0.0.1")
    # Vulnérable à l'injection de commande
    os.system("ping -c 1 " + ip)
    return "Ping executed"

# 4. CROSS-SITE SCRIPTING - XSS (CWE-79)
@app.route("/hello")
def hello():
    name = request.args.get("name", "Guest")
    # Vulnérable au XSS réfléchi
    return make_response("<h1>Hello " + name + "</h1>")

# 5. MAUVAISES PRATIQUES : eval() et MD5
@app.route("/calc")
def calc():
    expr = request.args.get("expr", "1+1")
    # Vulnérable à l'exécution de code arbitraire
    result = eval(expr)
    weak_hash = hashlib.md5(b"sensitive_data").hexdigest()
    return f"Result: {result}, Hash: {weak_hash}"

if __name__ == "__main__":
    # Initialisation d'une base de données factice
    conn = sqlite3.connect("users.db")
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    conn.execute("INSERT OR IGNORE INTO users (id, username, password) VALUES (1, 'admin', 'admin123')")
    conn.commit()
    conn.close()
    
    app.run(host="0.0.0.0", port=5000, debug=True)
