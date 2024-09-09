#  this code uses Whapi API to send messages to channels using chat/group/channel id and login token
#  it costs 35$/Month 
import requests

url = "https://gate.whapi.cloud/messages/text"

payload = {
    "typing_time": 0,
    "to": "120363321308375718@newsletter",
    "body": "Hello"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "UU1j3pyIU82H9Q9Rp8CvahuMHBehvB6N"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)