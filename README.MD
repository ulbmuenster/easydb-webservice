# Setup flask server
1. mkdir flask
2. cd flask
3. python -m venv venv
4. . venv/bin/activate
5. pip install -r requirements.txt

# Requirements for the service to work
1. cd inventarnummer_service
2. mkdir instance
3. touch config.py
4. In config.py define the database connection string, example:  
```
file = open("path/to/secret/password", "r")
password = file.read()
file.close()
SQLALCHEMY_DATABASE_URI = 'driver://username:'+password+'@url:port/database_name'
```

# Start service
1. cd flask
2. . venv/bin/activate
3. cd inventarnummer_service
4. Optional: export FLASK_ENV=development for debug purposes
5. export FLASK_APP=run.py
6. flask run

# Set generated format
The format of the generated ID can be set via a config file in the cfg folder:
`GENERATED_ID_FORMAT = "PREFIX_INSTITUTION_ID"`.
The placeholders will be replaced with the corresponding values.

# Sending a request
The request has to be send with a valid JSONWebtoken and a json body looking like this:
```
{
	"institution": "ABC",
	"prefix": "cde"
}
```
If you dont want to or cannot generate a Webtoken on your own, call inventarnr.uni-muenster.de/TokenGenerator
and it will return a valid JSONWebToken