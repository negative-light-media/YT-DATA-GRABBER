from googleapiclient.discovery import build
from dotenv import load_dotenv
import datetime
import os, sys
import json

sys.path.insert(0, './classes')

from classes.Channel import Channel
from classes.Video import Video



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
        part="snippet,contentDetails,statistics",
        id=video_id
    )
    return request.execute()

def get_playlist_video_ids(api_key, playlist_id):
    video_ids = []
    yt = build('youtube', 'v3', developerKey=api_key)
    stage = f"Getting First Request from {playlist_id}"
    print(f"{stage:-^100}")
    request = yt.playlistItems().list(
        part="snippet,contentDetails",
        playlistId=playlist_id,
        maxResults=50
    )
    data = request.execute()
    for item in data['items']:
        video_ids.append(item['contentDetails']['videoId'])
    next_page_token = data['nextPageToken']
    print(f"Total Items: {len(video_ids)}")
    while next_page_token is not None:
        long = "Requesting next 50 items"
        request = yt.playlistItems().list(
            part="snippet,contentDetails",
            playlistId=playlist_id,
            maxResults=50,
            pageToken= next_page_token
        )
        data = request.execute()
        for item in data['items']:
            video_ids.append(item['contentDetails']['videoId'])
        next_page_token = data.get('nextPageToken')
        print(f"Total Items: {len(video_ids)}")
    
    return video_ids

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
    
    stage = f"GETTING CHANNEL VIDEOS FOR {channel.name}"
    print(f"{stage:*^100}")
    video_ids = get_playlist_video_ids(env['api'], channel.uploadPlaylist)
    print(video_ids)
    stage = "GETTING VIDEO INFO"
    print(f"{stage:*^100}")
    videos = []
    for video_id in video_ids:
        videos.append(Video(get_video_stats_json(env['api'], video_id)))

if __name__ == "__main__":
    print("*"*100)
    main()
    print("*"*100)
    os.environ['LAST_RUN'] = str(datetime.datetime.now())