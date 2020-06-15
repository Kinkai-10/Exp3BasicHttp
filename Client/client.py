import urllib.request
import urllib.parse

url = "http://localhost:8080"

headers = {
    "Content-Type" :"text/plain; charset=utf-8"
}

req = urllib.request.Request(url, headers=headers)

with urllib.request.urlopen(req) as res:
    body = res.read().decode("utf-8")
    print(body)
    print(res.headers)
