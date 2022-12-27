import requests

from characters.models import Character
from rick_and_morty_api import settings


def scrape_characters() -> list[Character]:
    characters_response = requests.get(
        settings.RICK_AND_MORTY_API_CHARACTERS_URL
    ).json()
    characters = []
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
    return characters_response
