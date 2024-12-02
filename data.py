import requests
from requests import post
import json

# Pulls authorization code everytime to prevent timing out
ourl = "https://id.twitch.tv/oauth2/token?client_id=h730xa66skz2uolwot80wok0ghjlt4&client_secret=qw3p00o5yvtyvyyhn45na7mvzckl5z&grant_type=client_credentials"
rauthcode = post(ourl)
sauthcode = rauthcode.text
authcode = sauthcode[17:47]


# Uses authorization code to pull data
url = "https://api.igdb.com/v4/games"
headers = {
    "Client-ID": "h730xa66skz2uolwot80wok0ghjlt4",
    "Authorization": "Bearer " + authcode
}
data = "fields name; limit 10;"

# Generates the data into a response and prints it out
response = post(url, headers=headers, data=data)
print(json.dumps(response.json(), indent=4))

