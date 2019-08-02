import requests

easydb_context = {'data': {'invnr': ''}}  # json mock
easydb_info = ''


# Test-Funktion
def pre_update_function(easydb_context, easydb_info):
    data = easydb_context['data']
    url = "http://localhost:5000/generate"
    jsonwebtoken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjQ2NTU1NjQsIm5iZiI6MTU2NDY1NTU2NCwianRpIjoiOWU3ZjdiZWYtNTBjYy00ZjFhLThkNDgtZTRkNjZlNjc3ZmZjIiwiZXhwIjoxNTY0NjU2NDY0LCJpZGVudGl0eSI6ImVhc3lkYjUiLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.R3dVowUkwqK7nAkyk2BeWmLlJ8bzggWovViqRJlt_v4"
    try:
        result = requests.post(url = url, headers={'Authorization': 'Bearer '+jsonwebtoken}, json={"institution": "ABC","prefix": "cfg"})
        json_data = result.json()
        if "id" in json_data:
            data['invnr'] = json_data["id"]
            print (data)
            return data
        else:
            print (json_data)
    except requests.exceptions.ConnectionError:
        print("Could not establish a connection to the service.")
        return "Could not establish a connection to the service."


pre_update_function(easydb_context=easydb_context, easydb_info=easydb_info)
