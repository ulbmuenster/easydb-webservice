# !!! WITH EASYDB NOW USING PYTHON 3 FOR PLUGINS, THIS WEBSERVICE IS NOT NEEDED ANYMORE AND THEREFORE WILL NOT BE UPDATED !!!

# Setup flask server
1. mkdir flask
2. cd flask
3. python -m venv venv
4. . venv/bin/activate
5. pip install -r requirements.txt

# Start service
1. cd flask
2. . venv/bin/activate
3. cd easydb-webservice
4. Optional: export FLASK_ENV=development for debug purposes
5. export FLASK_APP=run.py
6. flask run

# Formula converter
This service is also now able to convert chemical formulas of a format like `Ca6(Fe,Al)2(SO4)2(B(OH)4)(OH)12*26H2O`
to something like `Ca₆(Fe,Al)₂(SO₄)₂(B(OH)₄)(OH)₁₂·26H₂O`. To do so, you have to send a post request to yourURL/convert
looking like this:
```
{
	"formula": "Ca6(Fe,Al)2(SO4)2(B(OH)4)(OH)12*26H2O"
}
```
As an answer you will receive the following JSON:
 ```
 {
 	"convertedFormula": "Ca₆(Fe,Al)₂(SO₄)₂(B(OH)₄)(OH)₁₂·26H₂O"
 }
 ```
