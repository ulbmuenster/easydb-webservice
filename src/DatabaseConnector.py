from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Inventarnummer(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return "<Inventarnummer (id='%d')>" % self.id
