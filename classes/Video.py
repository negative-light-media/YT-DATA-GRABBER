class Video:
    def __init__(self, video_data):
        self.kind = video_data.get('kind')
        self.etag = video_data.get('etag')

        # Getting Snippit Information
        snippet = video_data.get('snippet', {})
        self.published_at = snippet.get('publishedAt')
        self.channel_id = snippet.get('channelId')
        self.title = snippet.get('title')
        self.description = snippet.get('description')
        self.thumbnails = snippet.get('thumbnails')
        self.channel_title = snippet.get('channelTitle')
        self.tags = snippet.get('tags')
        self.category_id = snippet.get('categoryId')
        self.live_broadcast_content = snippet.get('liveBroadcastContent')
        self.default_language = snippet.get('defaultLanguage')

        # Getting Content Details
        content_details = video_data.get('contentDetails', {})
        self.duration = content_details.get('duration')
        self.dimension = content_details.get('dimension')
        self.definition = content_details.get('definition')
        self.caption = content_details.get('caption')
        self.licensed_content = content_details.get('licensedContent')
        self.content_rating = content_details.get('contentRating')
        self.projection = content_details.get('projection')

        # Getting Status of Content
        status = video_data.get('status', {})
        self.upload_status = status.get('uploadStatus')
        self.privacy_status = status.get('privacyStatus')
        self.license = status.get('license')
        self.embeddable = status.get('embeddable')
        self.public_stats_viewable = status.get('publicStatsViewable')

        # Public Statistics
        statistics = video_data.get('statistics', {})
        self.view_count = statistics.get('viewCount')
        self.like_count = statistics.get('likeCount')
        self.dislike_count = statistics.get('dislikeCount')
        self.favorite_count = statistics.get('favoriteCount')
        self.comment_count = statistics.get('commentCount')
        
        def to_csv(self):
            data = [
                self.kind,
                self.etag,
                self.published_at,
                self.channel_id,
                self.title,
                self.description,
                self.thumbnails,
                self.channel_title,
                self.tags,
                self.category_id,
                self.live_broadcast_content,
                self.default_language,
                self.duration,
                self.dimension,
                self.definition,
                self.caption,
                self.licensed_content,
                self.content_rating,
                self.projection,
                self.upload_status,
                self.privacy_status,
                self.license,
                self.embeddable,
                self.public_stats_viewable,
                self.view_count,
                self.like_count,
                self.dislike_count,
                self.favorite_count,
                self.comment_count
            ]
            return ",".join(map(str, data))
        
