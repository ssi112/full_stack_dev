from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# connect to db
app.config['SQLAlchemy_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/todoapp'
# instance of our database
db = SQLAlchemy(app)


# db.session - lets us create and manipulate database transactions


# db.Model - lets us map our classes to tables
class Person(db.Model):
    # note SQLAlchemy handles the class init method
    __tablename__ = 'persons'
    __table_args__ = {"schema": "public"}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)


# db.create_all - creates all tables in our model IF they DON'T exist
db.create_all()

@app.route('/')
def index():
    return f'Hello World!'

'''
When we call a script this way, using $ python script.py, the script's
__name__ gets set to __main__ by the Python interpreter, which then runs
through all code found in the script. When it reaches the end, and
finds if __name__ == 'main', it evaluates this to True and therefore
calls app.run() at the end, running the Flask app.
'''
if __name__ == "__main__":
    app.run(debug=True)


