import requests

from characters.models import Character
from rick_and_morty_api import settings


def scrape_characters() -> list[Character]:
    url_to_scrape = settings.RICK_AND_MORTY_API_CHARACTERS_URL

    characters = []
    while url_to_scrape is not None:
        characters_response = requests.get(
            url_to_scrape
        ).json()

        for character_dict in characters_response["results"]:
            characters.append(
                Character(
                    api_id=character_dict["id"],
                    name=character_dict["name"],
                    status=character_dict["status"],
                    species=character_dict["species"],
                    gender=character_dict["gender"],
                    image=character_dict["image"],
                )
            )
        url_to_scrape = characters_response["info"]["next"]
    return characters
