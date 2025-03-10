import json
from .providers.movieorca import Movieorca
from .classes import ProviderType, ResponseType, SearchResult, Season, Episode, Server, Source
from typing import Union, Callable, List

_provider_methods = {
    "movieorca": Movieorca
}

def _handle_response(data: Union[List, Callable], response_type: ResponseType) -> Union[str, List]:
    if response_type == "json":
        return json.dumps([item.to_dict() for item in data], indent=4)
    return data

def _get_provider_data(provider: ProviderType, response_type: ResponseType, method_name: str, *args) -> Union[str, List]:
    provider_class = _provider_methods.get(provider)
    if provider_class:
        provider_instance = provider_class()
        method = getattr(provider_instance, method_name) 
        data = method(*args)  
        return _handle_response(data, response_type)
    return "Provider not found"

# Search
def search(provider: ProviderType, query: str, response_type: ResponseType = "default") -> Union[List[SearchResult], str]:
    return _get_provider_data(provider, response_type, "search", query)

# Get Seasons
def get_seasons(provider: ProviderType, media_id: str, response_type: ResponseType = "default") -> Union[List[Season], str]:
    return _get_provider_data(provider, response_type, "get_seasons", media_id)

# Get Episodes
def get_episodes(provider: ProviderType, season_id: str, response_type: ResponseType = "default") -> Union[List[Episode], str]:
    return _get_provider_data(provider, response_type, "get_episodes", season_id)

# Get Episode Servers
def get_episode_servers(provider: ProviderType, episode_id: str, response_type: ResponseType = "default") -> Union[List[Server], str]:
    return _get_provider_data(provider, response_type, "get_episode_servers", episode_id)

# Get Movie Servers
def get_movie_servers(provider: ProviderType, media_id: str, response_type: ResponseType = "default") -> Union[List[Server], str]:
    return _get_provider_data(provider, response_type, "get_movie_servers", media_id)

# Get Sources
def get_sources(provider: ProviderType, server_id: str, response_type: ResponseType = "default") -> Union[List[Source], str]:
    return _get_provider_data(provider, response_type, "get_sources", server_id)
