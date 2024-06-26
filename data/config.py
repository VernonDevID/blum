# api id, hash
API_ID = 24339884
API_HASH = '9ad37509f5764011937dcbbfb7b52f6f'

DELAYS = {
    'ACCOUNT': [5, 15],  # delay between connections to accounts (the more accounts, the longer the delay)
    'PLAY': [5, 15],   # delay between play in seconds
    'ERROR_PLAY': [60, 180],    # delay between errors in the game in seconds
}
# Use proxies or not
PROXY = False

# Play drop game
PLAY_GAMES = True

# points with each play game; max 280
POINTS = [240, 280]

# title blacklist tasks (do not change)
BLACKLIST_TASKS = ['Farm points']

# session folder (do not change)
WORKDIR = "sessions/"


ACCOUNT_PER_ONCE = 3
