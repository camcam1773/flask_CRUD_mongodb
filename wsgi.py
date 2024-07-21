from app import app, mongo

table = mongo.db.flask_crud

if __name__ == "__main__":
    app.run()
