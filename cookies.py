from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return """
        <h1>Cookie Example</h1>
        <a href="/set-session-cookie">Set Session Cookie</a><br>
        <a href="/set-persistent-cookie">Set Persistent Cookie</a><br>
        <a href="/set-secure-cookie">Set Secure Cookie</a><br>
        <a href="/set-httponly-cookie">Set HttpOnly Cookie</a><br>
        <a href="/set-samesite-cookie">Set SameSite Cookie</a><br>
        <a href="/set-third-party-cookie">Set Third-Party Cookie</a><br>
        <a href="/get-cookies">Get Cookies</a>
    """

# Set a Session Cookie
@app.route('/set-session-cookie')
def set_session_cookie():
    response = make_response("Session cookie has been set!")
    response.set_cookie('session_cookie', 'this_is_a_session_cookie')
    return response

# Set a Persistent Cookie
@app.route('/set-persistent-cookie')
def set_persistent_cookie():
    response = make_response("Persistent cookie has been set!")
    response.set_cookie('persistent_cookie', 'this_is_a_persistent_cookie', max_age=60*60*24)  # 1 day
    return response

# Set a Secure Cookie
@app.route('/set-secure-cookie')
def set_secure_cookie():
    response = make_response("Secure cookie has been set!")
    response.set_cookie('secure_cookie', 'this_is_a_secure_cookie', secure=True)  # Only sent over HTTPS
    return response

# Set an HttpOnly Cookie
@app.route('/set-httponly-cookie')
def set_httponly_cookie():
    response = make_response("HttpOnly cookie has been set!")
    response.set_cookie('httponly_cookie', 'this_is_an_httponly_cookie', httponly=True)  # Not accessible via JavaScript
    return response

# Set a SameSite Cookie
@app.route('/set-samesite-cookie')
def set_samesite_cookie():
    response = make_response("SameSite cookie has been set!")
    response.set_cookie('samesite_cookie', 'this_is_a_samesite_cookie', samesite='Lax')  # Default is 'Lax'
    return response

# Get Cookies
@app.route('/get-cookies')
def get_cookies():
    cookies = request.cookies
    return f"Cookies: {cookies}"

if __name__ == '__main__':
    app.run(debug=True)
