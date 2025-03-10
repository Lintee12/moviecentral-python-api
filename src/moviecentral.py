import json
from .providers.movieorca import Movieorca
from .classes import ProviderType, ResponseType, SearchResult, Season, Episode, Server, Source
from typing import Union

movieorca = Movieorca

def search(provider: ProviderType, query: str, response_type: ResponseType = "default") -> Union[list[SearchResult], str]:
    results: list[SearchResult]
    if(provider == "movieorca"):
        results = movieorca.search(query)
    
    if(response_type == "json"):
        return json.dumps([result.to_dict() for result in results], indent=4)
    return results

def get_seasons(provider: ProviderType, media_id: str, response_type: ResponseType = "default") -> Union[list[Season], str]:
    seasons: list[Season]
    if(provider == "movieorca"):
        seasons = movieorca.get_seasons(media_id)
    
    if(response_type == "json"):
        return json.dumps([season.to_dict() for season in seasons], indent=4)
    return seasons

def get_episodes(provider: ProviderType, season_id: str, response_type: ResponseType = "default") -> Union[list[Episode], str]:
    episodes: list[Episode]
    if(provider == "movieorca"):
        episodes = movieorca.get_episodes(season_id)
    
    if(response_type == "json"):
        return json.dumps([episode.to_dict() for episode in episodes], indent=4)
    return episodes

def get_episode_servers(provider: ProviderType, episode_id: str, response_type: ResponseType = "default") -> Union[list[Server], str]:
    servers: list[Server]
    if(provider == "movieorca"):
        servers = movieorca.get_episode_servers(episode_id)
    
    if(response_type == "json"):
        return json.dumps([server.to_dict() for server in servers], indent=4)
    return servers

def get_movie_servers(provider: ProviderType, media_id: str, response_type: ResponseType = "default") -> Union[list[Server], str]:
    servers: list[Server]
    if(provider == "movieorca"):
        servers = movieorca.get_movie_servers(media_id)
    
    if(response_type == "json"):
        return json.dumps([server.to_dict() for server in servers], indent=4)
    return servers

def get_sources(provider: ProviderType, server_id: str, response_type: ResponseType = "default") -> Union[list[Source], str]:
    sources: list[Source]
    if(provider == "movieorca"):
        sources = movieorca.get_sources(server_id)
    
    if(response_type == "json"):
        return json.dumps([source.to_dict() for source in sources], indent=4)
    return sources
