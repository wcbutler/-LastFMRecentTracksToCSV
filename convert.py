import requests
import time
url = "https://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=xprotectrx&api_key={YOURAPIKEY}&format=json" #change user as needed, add your API key in here for this to work at all
user_data = requests.get(url).json()
print ('GUID, Artist, Track, Album, Date')
for x in range(len (user_data['recenttracks']['track'])):
    print (str(round(time.time()))+str(x+1).zfill(2) +',' 
           + user_data['recenttracks']['track'][x]['artist']['#text'] + ',' 
           + user_data['recenttracks']['track'][x]['name'], ',' 
           + user_data['recenttracks']['track'][x]['album']['#text'] + ',' 
           + user_data['recenttracks']['track'][x]['date']['#text'])
