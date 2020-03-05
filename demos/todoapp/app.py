'''
app.py
Flask-Migrate: https://flask-migrate.readthedocs.io/en/latest/

'''
from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys

app = Flask(__name__)

# connect to db
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# instance of our database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# db.session - lets us create and manipulate database transactions


# db.Model - lets us map our classes to tables
class Todo(db.Model):
    # note SQLAlchemy handles the class init method
    __tablename__ = 'todos'
    __table_args__ = {"schema": "public"}
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=True, default=False)

    def __repr__(self):
        return f'<Todo ID: {self.id}, description: {self.description}>'

# if not exist this will create the tables
db.create_all()

@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.order_by(Todo.id).all())


'''
# original method using HTTP Post method - synchronous method
@app.route('/todos/create', methods=['POST'])
def create_todo():
    description = request.form.get('description', '')
    todo = Todo(description=description)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('index'))

new method using AJAX fetch method - asynchronous
'''
@app.route('/todos/create', methods=['POST'])
def create_todo():
    error = False
    saveTodoObj = {}
    try:
        # get the json response object from fetch
        description = request.get_json()['description']
        todo = Todo(description=description, completed=False)
        db.session.add(todo)
        db.session.commit()
        # need all attributes to update list in HTML view
        saveTodoObj['id'] = todo.id
        saveTodoObj['completed'] = todo.completed
        saveTodoObj['description'] = todo.description
    except:
        db.session.rollback()
        error = True
        print("*"*55)
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort (400)
    else:
        return jsonify(saveTodoObj)


# <todo_id> id of item having completed state changed
# set in the view (index.html)
@app.route('/todos/<todo_id>set-completed', methods=['POST'])
def set_completed_todo(todo_id):
    try:
        completed = request.get_json()['completed']
        todo = Todo.query.get(todo_id)
        todo.completed = completed
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    return redirect(url_for('index'))


# <delete_id> id of item that should be deleted
# set in the view (index.html)
@app.route('/todos/<delete_id>delete-item', methods=['DELETE'])
def delete_todo_item(delete_id):
    # print("delete_id =",delete_id)
    try:
        todo = Todo.query.get(delete_id)
        db.session.delete(todo)
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    return jsonify({ 'success': True })


'''
When we call a script this way, using $ python script.py, the script's
__name__ gets set to __main__ by the Python interpreter, which then runs
through all code found in the script. When it reaches the end, and
finds if __name__ == 'main', it evaluates this to True and therefore
calls app.run() at the end, running the Flask app.
'''
if __name__ == "__main__":
    app.run(debug=True)

#********************************************************************

