from flask import Flask


def define_app():
    """
    This defines the application of the web app
    database doesn't need to be defined (as it is already pre-defined)
    returns the application
    """
    #Flask App
    app = Flask(__name__)
    app.secret_key = "kris"
    return app


if __name__ == "__main__":
    app = define_app()
    app.run(host="0.0.0.0", port=8080, debug=True, threaded=True)
