from googleapiclient.discovery import build
from dotenv import load_dotenv
import os, sys
import json

sys.path.insert(0, './classes')

from classes.Channel import Channel



def get_channel_json(api_key, channel_id):
    yt = build('youtube', 'v3', developerKey=api_key)
    request = yt.channels().list(
        part='snippet,contentDetails,statistics',
        id=channel_id
    )
    response = request.execute()
    return response

def get_video_stats_json(api_key, video_id):
    yt = build("youtube", "v3", developerKey=api_key)
    request = yt.videos().list(
        part="statistics",
        id=video_id
    )
    return request.execute()

def get_playlist_videos_json(api_key, playlist_id):
    yt = build('youtube', 'v3', developerKey=api_key)
    request = yt.playListItem().list(
        part="snippet,contentDetails",
        playlistId=playlist_id
    )
    return request.execute()

def get_env_vars():
    load_dotenv()
    retValue = {
        "api" : os.getenv("API_KEY"),
        "channel": os.getenv("CHANNEL_ID")
    }
    return retValue
    
def main():
    env = get_env_vars()
    
    stage = "GETTING CHANNEL INFO"
    print(f"{stage:*^100}")
    
    channel_data = get_channel_json(env['api'], env['channel'])
    channel = Channel(channel_data)
    print(channel)
    
    stage = f"GETTING CHANNEL VIDES FOR {channel.name}"
    print(f"{stage:*^100}")
    #videos = get_playlist_videos_json(env['api'])
    stage = "GETTING VIDEO INFO"
    print(f"{stage:*^100}")
    print(get_video_stats_json(env['api'], "iR48Pc9TA9o&t"))

if __name__ == "__main__":
    print("*"*100)
    main()
    print("*"*100)