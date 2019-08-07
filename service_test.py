import requests

easydb_context = {'data': {'invnr': ''}}  # json mock
easydb_info = ''


# Test-Funktion
def pre_update_function(easydb_context, easydb_info):
    data = easydb_context['data']
    url = "http://inventarnr.uni-muenster.de/generate"
    jsonwebtoken = "Token hier einfügen."
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