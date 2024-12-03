import requests
from requests import post
import json
import codecs
from igdb.wrapper import IGDBWrapper

# Pulls authorization code everytime to prevent timing out
ourl = "https://id.twitch.tv/oauth2/token?client_id=h730xa66skz2uolwot80wok0ghjlt4&client_secret=qw3p00o5yvtyvyyhn45na7mvzckl5z&grant_type=client_credentials"
rauthcode = post(ourl)
sauthcode = rauthcode.text
authcode = sauthcode[17:47]
wrapper = IGDBWrapper("h730xa66skz2uolwot80wok0ghjlt4", authcode)


class Game:
    def __init__(self, name):
        self.name = "\"" + name + "\""
    def get_id(self):
        r = wrapper.api_request("games", f"where name = {self.name};")
        raw_data = r.decode("utf-8")
        data = codecs.decode(raw_data, "unicode_escape")
        endIndex = data.find(" ", 16)
        return data[16:endIndex-1]
    def get_genre(self):
        r = wrapper.api_request("games", f"fields genres.name; where name = {self.name};")
        raw_data = r.decode("utf-8")
        data = codecs.decode(raw_data, "unicode_escape")
        startIndex = data.find("id",20)+5
        endIndex = data.find(" ", startIndex+1)
        return data[startIndex:endIndex-2]
    def get_same_genre_games(self,limit):
        r = wrapper.api_request("games", f"fields name; where genres = {int(self.get_genre())}; limit {limit};")
        raw_data = r.decode("utf-8")
        data = codecs.decode(raw_data, "unicode_escape")
        nameList = []
        i = 0
        while (i != -1):
            i = data.find("name", i)
            if i == -1:
                break
            startIndex = i + 8
            i = data.find("\"", startIndex+1)
            if i == -1:
                break
            endIndex = i
            nameList.append(data[startIndex:endIndex])
            i = endIndex + 1
        return nameList

obj = Game("Arthur's Camping Adventure")
print(obj.get_id())
print(obj.get_genre())
print(obj.get_same_genre_games(3))

