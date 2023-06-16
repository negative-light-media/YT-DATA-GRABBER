class Channel:
    def __init__(self, channel_data_json):
        self.raw_data = channel_data_json
        channel_data = channel_data_json['items'][0]
        self.id = channel_data['id']
        self.name = channel_data['snippet']['title']
        self.description = channel_data['snippet']['description']
        self.customUrl = channel_data['snippet'].get('customUrl', '')
        self.publishedAt = channel_data['snippet']['publishedAt']
        self.thumbnails = channel_data['snippet']['thumbnails']
        self.defaultLanguage = channel_data['snippet'].get('defaultLanguage', '')
        self.localized = channel_data['snippet']['localized']
        self.country = channel_data['snippet'].get('country', '')
        self.viewCount = int(channel_data['statistics']['viewCount'])
        self.subscribers = int(channel_data['statistics']['subscriberCount'])
        self.hiddenSubscribers = channel_data['statistics']['hiddenSubscriberCount']
        self.videoCount = int(channel_data['statistics']['videoCount'])

    def __str__(self):
        return f'Channel: {self.name}\nCountry: {self.country}\nViews: {self.viewCount}\nSubcribers: {self.subscribers}\nVideoes: {self.videoCount}'
    
    def getRaw(self):
        return self.raw_data