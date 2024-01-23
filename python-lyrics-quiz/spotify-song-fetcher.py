import logging
import os

from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth


class SpotifySongFetcher():
    def __init__(self, client_id: str, client_secret: str):
        pass


if __name__ == '__main__':
    log = logging.getLogger(__name__)

    log.debug('Loading .env file')
    load_dotenv()

    spotipy_client_id = os.getenv("SPOTIFYCLIENTID")
    spotipy_client_secret = os.getenv("SPOTIFYCLIENTSECRET")
