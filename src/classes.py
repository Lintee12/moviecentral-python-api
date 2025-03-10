from typing import Literal

MediaType = Literal["tv", "movie"]
ProviderType = Literal["movieorca"]
ResponseType = Literal["default", "json"]


class SearchResult:
    def __init__(self, title: str, media_type: MediaType, media_id: str, poster: str):
        self.title: str = title
        self.media_type: MediaType = media_type
        self.media_id: str = media_id
        self.poster: str = poster
    
    def to_dict(self):
        return {
            "title": self.title,
            "media_type": self.media_type,
            "media_id": self.media_id,
            "poster": self.poster,
        }

class Season:
    def __init__(self, season_number: int, season_id: str):
        self.season_number: int = season_number
        self.season_id: str = season_id
    
    def to_dict(self):
        return {
            "season_number": self.season_number,
            "season_id": self.season_id
        }
        
class Episode:
    def __init__(self, episode_number: int, episode_id: str):
        self.episode_number: int = episode_number
        self.episode_id: str = episode_id
    
    def to_dict(self):
        return {
            "episode_number": self.episode_number,
            "episode_id": self.episode_id
        }
    
class Server: 
    def __init__(self, server_name: str, server_id: str):
        self.server_name: str = server_name
        self.server_id: str = server_id

    def to_dict(self):
        return {
            "server_name": self.server_name,
            "server_id": self.server_id
        }
        
class Source:
    def __init__(self, embed: str):
        self.embed: str = embed

    def to_dict(self):
        return {
            "embed": self.embed,
        }