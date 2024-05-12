import requests as rq
import re


response = rq.post("https://pagina-web-production-4d43.up.railway.app/login", data = {"username": "ivanna.risaro@hotmail.com", "password": "123456789"}, headers={"Content-Type":"application/json"})
print(response)
print(response.status_code)