from flask import Flask
# init file will run automatically whenever the website folder is imported
# whenever you put this inside a folder, it becomes a python folder so it can be imported

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'random string here is key to the app'
    # encrypt the cookies/session data related to the website

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app