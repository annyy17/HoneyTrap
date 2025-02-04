from flask import Flask, request

app = Flask(__name__)

# Log file to store captured credentials and attack details
LOG_FILE = "honeypot.log"

def log_attempt(ip, username, password, user_agent, endpoint):
    """Logs attack details to a file."""
    with open(LOG_FILE, "a") as f:
        f.write(f"[{endpoint}] IP: {ip}, Username: {username}, Password: {password}, User-Agent: {user_agent}\n")

@app.route("/")
def home():
    return '''
        <h1>Welcome to Secure Login</h1>
        <form action='/login' method='post'>
            <input type='text' name='username' placeholder='Username'><br>
            <input type='password' name='password' placeholder='Password'><br>
            <input type='submit' value='Login'>
        </form>
    '''

@app.route("/login", methods=["POST"])
def capture_login():
    username = request.form.get("username")
    password = request.form.get("password")
    ip = request.remote_addr  # Attacker's IP
    user_agent = request.headers.get("User-Agent")  # Browser/User-Agent info

    # Log the attack attempt
    log_attempt(ip, username, password, user_agent, "LOGIN")

    return "<h1>Login Failed</h1>"

@app.route("/admin")
def fake_admin():
    """Fake admin panel to attract bots."""
    return '''
        <h1>Admin Panel</h1>
        <form action='/admin/login' method='post'>
            <input type='text' name='admin_user' placeholder='Admin Username'><br>
            <input type='password' name='admin_pass' placeholder='Admin Password'><br>
            <input type='submit' value='Login'>
        </form>
    '''

@app.route("/admin/login", methods=["POST"])
def capture_admin_login():
    """Captures login attempts on the fake admin panel."""
    username = request.form.get("admin_user")
    password = request.form.get("admin_pass")
    ip = request.remote_addr
    user_agent = request.headers.get("User-Agent")

    # Log the fake admin attack attempt
    log_attempt(ip, username, password, user_agent, "ADMIN")

    return "<h1>Access Denied</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
