import requests
from requests.exceptions import HTTPError

leagueURL = 'https://www.pathofexile.com/api/trade/data/leagues'
leagueJsonResult = 'result'
leagueJsonText = 'text'

def getLeagues():
    try:
        r = requests.get(leagueURL)
    except HTTPError as httperr: 
        return None
        
    leagueJson = r.json()
    leaguesJsonList = list(leagueJson[leagueJsonResult])

    leaguesList = []

    for keypair in  leaguesJsonList:
        league = dict(keypair)[leagueJsonText]
        leaguesList.append(league)

    return leaguesList

# p = requests.post("https://www.pathofexile.com/api/trade/search/YOUR_LEAGUE")
# print(r.text);