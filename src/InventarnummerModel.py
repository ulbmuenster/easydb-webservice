from flask_sqlalchemy import SQLAlchemy

# A best practice is to initialise SQLAlchemy here and then call init_app() during app creation.
db = SQLAlchemy()


class Inventarnummer(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return "<Inventarnummer (id='%d')>" % self.id
