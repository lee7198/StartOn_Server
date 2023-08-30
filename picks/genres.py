import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint
 
cid = '8b4aad7d1e34416c8f4bd2ef1968fa5d'
secret = 'fc43caa7fd214df498236058974066c2'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
 
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# artist_albums 기능
search_result = sp.search("iu", limit=1, type="artist")
iu_ID = search_result["artists"]["items"][0]["id"]
album_result = sp.artist_albums(iu_ID, limit=2)
items = album_result["items"]
pprint.pprint(items)

