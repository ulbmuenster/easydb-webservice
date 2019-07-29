import requests

easydb_context = {'data': {'invnr': ''}}  # json mock
easydb_info = ''


# Test-Funktion
def pre_update_function(easydb_context, easydb_info):
    data = easydb_context['data']
    url = "http://localhost:5000/generate"
    jsonwebtoken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjQ0MDgxMzAsIm5iZiI6MTU2NDQwODEzMCwianRpIjoiZTIwYWI4NGEtMzNhZS00M2ZlLTk1ZjEtYjc1ZWIwZTRjODcyIiwiZXhwIjoxNTY0NDA5MDMwLCJpZGVudGl0eSI6ImVhc3lkYjUiLCJmcmVzaCI6dHJ1ZSwidHlwZSI6ImFjY2VzcyJ9.emWz4pHPlV8or7tWWrQEFkMT3Y6zbHYjWfoTKGuTIxY"
    result = requests.get(url = url, headers={'Authorization': 'Bearer '+jsonwebtoken})
    json_data = result.json()
    if "id" in json_data:
        data['invnr'] = json_data["id"]
        print (json_data)
        print (data)
        return data
    else:
        print (json_data)


pre_update_function(easydb_context=easydb_context, easydb_info=easydb_info)
