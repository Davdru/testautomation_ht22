from http import HTTPStatus

import requests
import pytest

GOREST_USERS = "https://gorest.co.in/public/v2/users"
GOREST_POSTS = "https://gorest.co.in/public/v2/posts"


@pytest.fixture
def api_token() -> str:
    with open('token') as f:
        return f.read().strip()


@pytest.fixture
def header(api_token):
    return {'authorization': f"Bearer {api_token}"}


@pytest.fixture
def user_data():
    return {'name': "En Testperson",
            "email": "some_mail@mail.fr",
            "gender": "male",
            "status": "active"}


# Ett test kan delas in i 3-4 olika delar.
# 1. Arrange, arrangera, förbereda
# 2. Act, agera. Interagera med SUT, genomför någon handling
# 3. Assert, kontrollera att utfallet blev det förväntade
# 4. Cleanup, städa, rensa, ta bort sådan som kan störa ytterligare tester

def test_create_user_v2(user_data, header):
    res = requests.post(GOREST_USERS, data=user_data, headers=header)
    user_dict = res.json()
    assert res.status_code == HTTPStatus.CREATED
    requests.delete(GOREST_USERS + f"/{user_dict['id']}", headers=header)


# Här finns fortfarande risken att användaren ligger kvar och stör andra tester, det måste vi fixa


# poster, behöver en användare
# Hur vet vi att vi har en användare till vårt test?
# Vi skapar den själva
# 1. Skapa användare
# 2. Skapa post med den nya användarens id
# 3. Gör våra kontroller, t.ex. returkod
# 4. Ta bort posten
# 5. Ta bort användaren

def test_create_post(user_data, header):
    new_user = requests.post(GOREST_USERS, data=user_data, headers=header).json()
    new_post = requests.post(GOREST_POSTS,
                             data={'user_id': new_user['id'], 'title': 'Min titel',
                                   'body': 'Brödtext med en massa tecken'},
                             headers=header)

    assert new_post.status_code != HTTPStatus.CREATED
    requests.delete(GOREST_POSTS + f"/{new_post.json()['id']}", headers=header)
    requests.delete(GOREST_USERS + f"/{new_user['id']}", headers=header)


# Här har vi en massa kod för att skapa och ta bort användare som egentligen inte hör till själva testet
# Vi behöver bara en användare i systemet för att kunna skapa en ny post.
# Helst skall testfunktionen bara skapa en ny post och göra en eller några asserts
# En indikation på att allt inte är så bra är den duplicerade kod vi ser. ex för att skapa användare


# def test_create_user():
#     fails = []
#     # Testdata inne i testfunktion
#     res = requests.post(GOREST_USERS, data={'name': "En Testperson",
#                                             "email": "personens@mail.fr",
#                                             "gender": "male",
#                                             "status": "active"},
#                         headers=HEADER)
#
#     user_json = res.json()
#     # Krånglig kod för att kontrollera utfallet. spridd över flera rader som inte hänger ihop
#     if res.status_code != HTTPStatus.CREATED:
#         fails.append(f"expected {HTTPStatus.CREATED} got {res.status_code}")
#     if 'name' not in user_json:
#         fails.append("key name not in response")
#
#     # Uppstädningen kanske inte alltid utförs, vilket betyder att någon manuellt måste fixa till systemet om vi
#     # om vi får en oväntad krasch
#     requests.delete(GOREST_USERS + f"/{user_json['id']}", headers=HEADER)
#     assert not fails, '\n'.join(fails)


def test_get_all_users(header):
    res = requests.get(GOREST_USERS, headers=header)
    assert res.status_code == HTTPStatus.OK
