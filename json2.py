import json
import urllib
import urllib.request, urllib.parse, urllib.error

count=0
url = "http://py4e-data.dr-chuck.net/comments_1507617.json"
uh = urllib.request.urlopen(url)
data = uh.read()

info = json.loads(data)

for item in info["comments"]:
    number = int(item["count"])
    count += number

print (count)