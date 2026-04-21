def init_app(app):
    @app.route("/contact")
    def contact():
        return """
        <h1>Contact Page</h1>
        <p>Email: example@email.com</p>
        <a href="/">Back to Home</a>
        """