import os
import sys
script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, '..')
sys.path.append(mymodule_dir)
import pytest
import app


@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    app.app.config["MONGO_URI"] = "mongodb://localhost:27017/flask_crud_test"
    app.table = app.mongo.db.flask_crud_test
    with app.app.test_client() as client:
        yield client
    app.table.drop()
