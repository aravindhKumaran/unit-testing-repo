import requests
from typing import *

database = {
    1: "Alice",
    2: "Bob",
    3: "Charlie"
}


def get_user_from_db(user_id: int) -> str:
    return database.get(user_id)


def get_users_api_call() -> List[Dict[str, Any]]:
    response = requests.get("https://jsonplaceholder.typicode.com/users")

    if response.status_code == 200:
        return response.json()
    
    raise requests.HTTPError(response.status_code)