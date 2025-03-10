import src.moviecentral as moviecentral

# usage example

def main():
    """ 
    # get family guy episode 1 sources
    search = moviecentral.search("movieorca", "Family Guy") # media_id found in search results
    seasons = moviecentral.get_seasons("movieorca", search[3].media_id)
    episodes = moviecentral.get_episodes("movieorca", seasons[0].season_id)
    servers = moviecentral.get_episode_servers("movieorca", episodes[0].episode_id)
    sources = moviecentral.get_sources("movieorca", servers[0].server_id)
    print(sources[0].embed) 
     """

    # get The Shawshank Redemption movie sources
    search = moviecentral.search("movieorca", "The Shawshank Redemption")
    servers = moviecentral.get_movie_servers("movieorca", search[0].media_id) # use the media_id of the first result
    sources = moviecentral.get_sources("movieorca", servers[0].server_id) # use the server_id of the first server
    print(sources[0].embed)

if __name__ == "__main__":
    main()