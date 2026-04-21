def init_app(app):
    @app.route("/about")
    def about():
        return """
        <h1>About Page</h1>
        <p>This is a simple Flask application.</p>
        <a href="/">Back to Home</a>
        """