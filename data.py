
from requests import post
import json
from igdb.wrapper import IGDBWrapper

# Pulls authorization code everytime to prevent timing out
ourl = "https://id.twitch.tv/oauth2/token?client_id=h730xa66skz2uolwot80wok0ghjlt4&client_secret=qw3p00o5yvtyvyyhn45na7mvzckl5z&grant_type=client_credentials"
rauthcode = post(ourl)
sauthcode = rauthcode.text
authcode = sauthcode[17:47]
wrapper = IGDBWrapper("h730xa66skz2uolwot80wok0ghjlt4", authcode)

# Transforms json data into a game object making it easier to read
def easy_read(item):
    id = item.get("id")
    name = item.get("name")
    tempgenres = item.get("genres", [])
    genres = []
    for g in tempgenres:
        genres.append(g.get("name"))
    tempthemes = item.get("themes", [])
    themes = []
    for t in tempthemes:
        themes.append(t.get("name"))
    game = Game(id, name, genres, themes)
    return game

def get_game(name):
    r = wrapper.api_request("games", f"fields name, genres.name, themes.name; where name = \"{name}\";  limit {1};")
    raw_data = r.decode("utf-8")
    jdata = json.loads(raw_data)
    if len(jdata) == 0:
        return None
    jdata = json.loads(raw_data)[0]
    game = easy_read(jdata)
    return game



# Game class
class Game:
    def __init__(self, id, name, genres, themes):
        self.name = name
        self.id = id
        self.genres = genres
        self.themes = themes
    def __str__(self):
        sgenres = ""
        for g in self.genres:
            sgenres = sgenres + g + " "
        sthemes = ""
        for t in self.themes:
            sthemes = sthemes + t + " "
        return(
            f"Name: {self.name}\n"
            f"Genres: {sgenres}\n"
            f"Themes: {sthemes}"
        )
    def get_theme_id(self):
        themeID = []
        for t in self.themes:
            r = wrapper.api_request("themes", f"fields id, name; where name = \"{t}\";")
            raw_data = r.decode("utf-8")
            jdata = json.loads(raw_data)
            for item in jdata:
                tid = item.get("id")
                themeID.append(tid)
        return themeID
    def get_genre_id(self):
        genreID = []
        for g in self.genres:
            r = wrapper.api_request("genres", f"fields id, name; where name = \"{g}\";")
            raw_data = r.decode("utf-8")
            jdata = json.loads(raw_data)
            for item in jdata:
                gid = item.get("id")
                genreID.append(gid)
        return genreID

    def get_similar_games(self,limit):
        genre_list = self.get_genre_id()
        theme_list = self.get_theme_id()
        gl = ""
        tl = ""
        for g in genre_list:
            gl = gl + str(g) + ", "
        for t in theme_list:
            tl = tl + str(t) + ", "
        gl = gl[0:(len(gl)-2)]
        tl = tl[0:(len(tl)-2)]
        r = wrapper.api_request("games", f"fields name, genres.name, themes.name; where genres = ({gl}) & themes = ({tl});  limit {limit};")
        raw_data = r.decode("utf-8")
        jdata = json.loads(raw_data)
        return jdata
    # Gets similarity of games that share themes/genres outputs a number from 0-1 decimals included
    def similarity_score(self, game):
        sizea = len(self.get_theme_id()) + len(self.get_genre_id())
        sizeb = len(game.get_theme_id()) + len(game.get_genre_id())
        tot = max(sizea, sizeb)
        stot = 0
        for i in game.get_genre_id():
            for j in self.get_genre_id():
                if i==j :
                    stot = stot + 1
        for i in game.get_theme_id():
            for j in self.get_theme_id():
                if i==j :
                    stot = stot + 1
        return round(stot/tot, 2)



