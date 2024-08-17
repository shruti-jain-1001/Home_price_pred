import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'area':7420, 'bedroom':4, 'bathroom':2,'mainroad':1})

print(r.json())