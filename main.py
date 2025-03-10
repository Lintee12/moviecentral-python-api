import src.moviecentral as moviecentral

# usage example

def main():
    # get family guy episode 1 sources
    search = moviecentral.search("movieorca", "Family Guy") # media_id found in search results
    seasons = moviecentral.get_seasons("movieorca", "tv/family-guy-39549")
    episodes = moviecentral.get_episodes("movieorca", seasons[0].season_id)
    servers = moviecentral.get_episode_servers("movieorca", episodes[0].episode_id)
    sources = moviecentral.get_sources("movieorca", servers[0].server_id)
    print(sources[0].embed)

if __name__ == "__main__":
    main()