from flask_sqlalchemy import SQLAlchemy

# A best practice is to initialise SQLAlchemy here and then call init_app() during app creation.
db = SQLAlchemy()


class Inventarnummer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    institution = db.Column(db.String)
    prefix = db.Column(db.String, primary_key=True)

    def __repr__(self):
        return "<Inventarnummer (id='%d', institution='%s', prefix='%s')>" % self.id, self.institution, self.prefix
