import requests
from pprint import pprint


# Vi vill kunna skapa en header Authorization: Bearer 198472873657265
# 1. Läs in token från textfilen
# 2. Skapa en dict för alla headers
# 3. Ta med headersdict i anrop mot APIet

GOREST_USERS = "https://gorest.co.in/public/v2/users"


def api_token() -> str:
    with open('token') as f:
        return f.read().strip()


header = {'authorization': f"Bearer {api_token()}"}


# Skapa en användare
# Json med:
#   namn
#   unik epost
#   gender
#   status
# Post mot "https://gorest.co.in/public/v2/users"
# Skriv ut result-json för att hitta userid

userdata = {"name": "Min testuser",
            "email": "en_ny@mailadress.se",
            "gender": "male",
            "status": "active"}


def create_user(user_data: dict) -> dict:
    res = requests.post("%s" % GOREST_USERS, data=userdata, headers=header)
    return res.json()


# res = requests.get("%s" % GOREST_USERS, headers=header)
# pprint(res.json())
#
#
# "https://gorest.co.in/public/v2/users/4695"
def get_user(user_id: int) -> dict:
    res = requests.get(GOREST_USERS + f"/{user_id}", headers=header)
    return res.json()

# Skapa en funktion delete_user(user_id: int)

if __name__ == '__main__':
     user_dict = get_user(4776)

     print(user_dict['id'])
