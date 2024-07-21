from app import app, mongo

if __name__ == "__main__":
    table = mongo.db.flask_crud
    app.run()
