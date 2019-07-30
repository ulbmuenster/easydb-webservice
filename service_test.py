import requests

easydb_context = {'data': {'invnr': ''}}  # json mock
easydb_info = ''


# Test-Funktion
def pre_update_function(easydb_context, easydb_info):
    data = easydb_context['data']
    url = "http://localhost:5000/generate"
    jsonwebtoken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjQ0NzY3NzUsIm5iZiI6MTU2NDQ3Njc3NSwianRpIjoiZmJlODYyOWItNzI3Ni00MjE2LWIwYzQtNzBhZDZkYWMzN2Y5IiwiZXhwIjoxNTY0NDc3Njc1LCJpZGVudGl0eSI6ImVhc3lkYjUiLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.KmNMtdQg3W3LpVzJDnsGxgg44qwv1GVSb-LvOjl8pV8"
    try:
        result = requests.get(url = url, headers={'Authorization': 'Bearer '+jsonwebtoken})
        json_data = result.json()
        if "id" in json_data:
            data['invnr'] = json_data["id"]
            print (json_data)
            print (data)
            return data
        else:
            print (json_data)
    except requests.exceptions.ConnectionError:
        print("Could not establish a connection to the service.")
        return "Could not establish a connection to the service."


pre_update_function(easydb_context=easydb_context, easydb_info=easydb_info)
