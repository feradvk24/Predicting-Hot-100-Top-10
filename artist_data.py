import requests
import base64


def get_access_token(client_id, client_secret):
    """Obtain an access token for the Spotify API."""
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    }
    data = {
        "grant_type": "client_credentials"
    }
    response = requests.post(url, headers=headers, data=data)
    response_data = response.json()
    return response_data['access_token']

def get_artist_followers_and_popularity(artist_name, access_token):
    """Search for an artist by name and fetch followers and popularity."""
    search_url = "https://api.spotify.com/v1/search"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    search_params = {
        "q": artist_name,
        "type": "artist",
        "limit": 1
    }
    search_response = requests.get(search_url, headers=headers, params=search_params)
    search_data = search_response.json()
    
    if search_data.get('artists') and search_data['artists']['items']:
        artist = search_data['artists']['items'][0]
        return {
            "artist_name": artist['name'],
            "followers": artist['followers']['total'],
            "popularity": artist['popularity']
        }
    else:
        return None
