import requests

easydb_context = {'data': {'invnr': ''}}  # json mock
easydb_info = ''


# Test-Funktion
def pre_update_function(easydb_context, easydb_info):
	data = easydb_context['data']
	url = "http://inventarnr.uni-muenster.de/generate"
	jsonwebtoken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjU4NTI3NTQsIm5iZiI6MTU2NTg1" \
				"Mjc1NCwianRpIjoiNjY2ZmVjYjktZGQ4OS00NjZiLTk2ODAtODdhZjgyZDM0ZjU0IiwiaWRlbnRpdHk" \
				"iOiJlYXN5ZGI1IiwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.aM60lpofPYeIRI2" \
				"ajaBqyQgLyuv1Ygrde7SRo-gduxg"
	try:
		result = requests.post\
			(url=url, headers={'Authorization': 'Bearer '+jsonwebtoken}, json={"institution": "ABC", "prefix": "cfg"})
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