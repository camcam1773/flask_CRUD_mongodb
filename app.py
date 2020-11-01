from flask import Flask, render_template, request, redirect
from flask_pymongo import PyMongo
from datetime import datetime

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/flask_crud"
mongo = PyMongo(app)
table = mongo.db.flask_crud


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        task_content = request.form["content"]
        new_task = {'content': task_content,
                    'date_created': datetime.utcnow()}
        try:
            table.insert_one(new_task)
            return redirect("/")
        except Exception as e:
            print(e)
            return "Commit error"
    else:
        tasks = list(table.find().sort('date_created'))
        return render_template('index.html', tasks=tasks)


@app.route("/delete/<ObjectId:_id>")
def delete(_id):
    try:
        table.delete_one({'_id': _id})
        return redirect('/')
    except Exception as e:
        print(e)
        return 'There was a problem deleting that task'


@app.route('/update/<ObjectId:_id>', methods=['GET', 'POST'])
def update(_id):
    task = table.find_one_or_404({'_id': _id})

    if request.method == 'POST':
        task.update({'content': request.form['content']})
        try:
            table.replace_one({'_id': _id}, task)
            return redirect('/')
        except Exception as e:
            print(e)
            return 'There was an issue updating your task'
    else:
        return render_template('update.html', task=task)


if __name__ == "__main__":
    from waitress import serve
    serve(app, host='0.0.0.0', port=8080)
