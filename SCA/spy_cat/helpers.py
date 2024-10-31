import requests

from rest_framework import status

from .constants import THE_CAT_API_BREEDS_URL


def verify_cat_breed(breed: str) -> bool:
    response = requests.get(THE_CAT_API_BREEDS_URL)
    is_valid = False

    if response.status_code != status.HTTP_200_OK:
        return False

    for record in response.json():
        if record.get('name').lower() == breed.lower():
            is_valid = True
            break
    
    return is_valid
