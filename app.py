from flask import Flask
import about
import contact

app = Flask(__name__)

# Home route with navigation
@app.route("/")
def home():
    return """
    <h1>Home Page</h1>
    <a href="/about">Go to About</a><br>
    <a href="/contact">Go to Contact</a>
    """

# Register routes
about.init_app(app)
contact.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)