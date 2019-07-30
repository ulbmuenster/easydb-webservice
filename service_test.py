import requests

easydb_context = {'data': {'invnr': ''}}  # json mock
easydb_info = ''


# Test-Funktion
def pre_update_function(easydb_context, easydb_info):
    data = easydb_context['data']
    url = "http://localhost:5000/generate"
    jsonwebtoken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjQ0ODcwOTQsIm5iZiI6MTU2NDQ4NzA5NCwianRpIjoiNDVjYzQ2Y2MtMzJiZC00MmFkLWFlNzAtNTQxY2Y5OTNhZGQ3IiwiZXhwIjoxNTY0NDg3OTk0LCJpZGVudGl0eSI6ImVhc3lkYjUiLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.9kjb8nC49QIquHt9ENbeGV1xdmomfe6ZbGqMft39-pQ"
    try:
        result = requests.get(url = url, headers={'Authorization': 'Bearer '+jsonwebtoken})
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
