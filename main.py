from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

def get_channel(api_key, channel_id):
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.channels().list(
        part='snippet,statistics',
        id=channel_id
    )
    response = request.execute()
    return response


def main():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    channel_id = os.getenv("CHANNEL_ID")
    channel_info = get_channel(api_key, channel_id)
    print(channel_info)

if __name__ == "__main__":
    main()