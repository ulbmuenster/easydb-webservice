from flask_sqlalchemy import SQLAlchemy

# A best practice is to initialise SQLAlchemy here and then call init_app() during app creation.
db = SQLAlchemy()


class Inventarnummer(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	institution = db.Column(db.Integer, db.ForeignKey('institution.id'), nullable=False)
	prefix = db.Column(db.String, nullable=False)
	institution_fk = db.relationship('Institution', backref=db.backref('inventarnummer', lazy=True))

	def __repr__(self):
		return "<Inventarnummer (id='%d', institution='%d')>" % self.id, self.institution


class Institution(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	institution_abbrev = db.Column(db.String)
	institution_full = db.Column(db.String)
	min_number = db.Column(db.Integer)
	max_number = db.Column(db.Integer)
	format = db.Column(db.String)

	def __repr__(self):
		return "<Institution (id='%d', institution_abbrev='%s', institution_full='%s'," \
			" prefix='%s', min_number='%d', max_number='%d', format='%s')>" \
			% self.id, self.institution_abbrev, self.institution_full, self.prefix, \
			self.min_number, self.max_number, self.format
