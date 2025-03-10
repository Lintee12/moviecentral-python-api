from src.classes import SearchResult, Season, Episode, Server, Source
from src.utils.fetcher import Fetcher, SourceFetcher
from src.utils.utils import slugify

base_url= "https://www2.movieorca.com"

class Movieorca:
    @staticmethod
    def search(query: str):
        soup = Fetcher.fetch(f"{base_url}/search/{slugify(query)}")
        items = soup.find_all(class_="flw-item")
        results: list[SearchResult] = []

        for item in items:
            title = item.find("a", class_="film-poster-ahref flw-item-tip")["title"]
            media_type = item.find(class_="fdi-type").get_text(strip=True).lower()
            media_id = item.find("a", class_="film-poster-ahref flw-item-tip")["href"].replace(f"/{media_type}", f"{media_type}")
            poster = item.find("img", class_="film-poster-img")["data-src"]
            results.append(SearchResult(title, media_type, media_id, poster))
        
        return results
    
    @staticmethod
    def get_seasons(media_id: str): 
        soup = Fetcher.fetch(f"{base_url}/ajax/season/list/{media_id.split('-')[-1]}")
        items = soup.find_all(class_="ss-item")
        seasons: list[Season] = []

        for i, item in enumerate(items):
            seasons.append(Season(i + 1, item["data-id"]))
        
        return seasons
    
    @staticmethod
    def get_episodes(season_id: str):
        soup = Fetcher.fetch(f"{base_url}/ajax/season/episodes/{season_id}")
        items = soup.find_all(class_="eps-item")
        episodes: list[Episode] = []

        for i, item in enumerate(items):
            episodes.append(Episode(i + 1, item["data-id"]))
        
        return  episodes
    
    @staticmethod
    def get_episode_servers(episode_id: str):
        soup = Fetcher.fetch(f"{base_url}/ajax/episode/servers/{episode_id}")
        items = soup.find_all(class_="link-item")
        servers: list[Server] = []

        for item in items:
            servers.append(Server(item["title"].replace("Server ", ""), item["data-id"]))
        
        return servers
    
    @staticmethod
    def get_movie_servers(media_id: str):
        soup = Fetcher.fetch(f"{base_url}/ajax/episode/list/{media_id.split('-')[-1]}")
        items = soup.find_all(class_="link-item")
        servers: list[Server] = []

        for item in items:
            servers.append(Server(item["title"].replace("Server ", ""), item["data-id"]))
        
        return servers
    
    @staticmethod
    def get_sources(server_id: str):
        sources = SourceFetcher.fetch(f"{base_url}/ajax/episode/sources/{server_id}")

        return [Source(sources["link"].replace("z=", "_debug=true"))]