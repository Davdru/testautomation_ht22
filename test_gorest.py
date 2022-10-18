from http import HTTPStatus

import requests
import pytest

GOREST_USERS = "https://gorest.co.in/public/v2/users"
GOREST_POSTS = "https://gorest.co.in/public/v2/posts"

TESTDATA = {"name": "Min Testuser",
            "email": "dennesadress@gmail.com",
            "gender": "male",
            "status": "active"}

with open("token") as f:
    TOKEN = f.read().strip()

HEADER = {"authorization": f"Bearer {TOKEN}"}


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


# Go rest har följande resurser
# 1. Users, kräver unik epost
# 2. Posts, kräver en existerande användare
# 3. Comments
# 4. Todos

# Vi skall testa CRUD, skapa, läsa, ändra, ta bort var och en av resurserna.
# Vi skall testa att hämta både en och flera av varje resurs.
# Vi skall testa att systemet hanterar exempelvis svenska tecken. Fler uppslag?
# Vi skall testa responskoder och svarstider.
# Kontrollera responskoder när vi skall få fel.

# För att arbeta mot gorest.co.in behöver vi ett token, detta berättar att vi har rätt att skapa
# och ändra på resurser. Vi har lagt den i en separat fil som inte är under versionshantering
# för att undvika att vi oavsiktligt läcker känslig information.
# Token skickas med i headern vid anrop mot gorest.co.in


# Users
#   Skapa

# Vad behöver vi för att skapa en användare?
# name, email, gender, status
# header med token
#
# 1. Skapa testdata, en dictionary med name, email, gender, status
# 2. Skapa en header med bearer token.
# 3. Gör http POST mot resursen(users)
# 4. Tolka resultatet som json
# 5. Kontrollera att det vi fick tillbaks var samma sak som det vi skickade in
# 6. Kontrollera statuskod, HTTP CREATED
# 7. Ta bort användaren igen så att testet kan köras igen.
#
# TODO vilka andra statusar finns, hur kan vi ändra

def test_create_user():
    response = requests.post(GOREST_USERS, data=TESTDATA, headers=HEADER)
    response_json = response.json()

    assert response.status_code == HTTPStatus.CREATED
    assert response_json['name'] == TESTDATA['name']
    assert response_json['email'] == TESTDATA['email']
    assert response_json['gender'] == TESTDATA['gender']
    assert response_json['status'] == TESTDATA['status']

    # För att ta bort en användare använder vi en DELETE request mot den specifika användaren
    # https://gorest.co.in/public/v2/users/123  <- den specifika användaren 123
    delete_response = requests.delete(GOREST_USERS + f"/{response_json['id']}", headers=HEADER)


# Uppgift 1.
# Skriv test som skapar en ny användare och därefter hämtar användaren med  hjälp av en get-request
# kontrollera att användaren har rätt data.

# Skriv test som skapar en ny användare och därefter uppdaterar namnet med en patch-request
# kontrollera att användaren därefter har uppdaterats med hjälp av en get-request


@pytest.fixture
def new_user():
    user = requests.post(GOREST_USERS, data=TESTDATA, headers=HEADER).json()
    yield user
    requests.delete(GOREST_USERS + f"/{user['id']}", headers=HEADER)


# Uppgift 2.
# Skriv om några av dina tester med fixturen new_user istället för att själv skapa användare
#
# Försök skapa en ny fixtur som ger en ny post

def test_create_post():
    # 1. Skapa en ny användare
    # 2. Skapa en ny post med id från användaren från steg 1.
    #   1. Skapa post-data, user_id, title, body
    # 3. Asserts
    # 4. Ta bort posten
    # 5. Ta bort användaren från steg 1.
    new_user = requests.post(GOREST_USERS, data=TESTDATA, headers=HEADER).json()
    post_data = {"user_id": new_user['id'], "title": "Postens titel", "body": "Postens brödtext"}

    new_post_response = requests.post(GOREST_POSTS, data=post_data, headers=HEADER)
    new_post = new_post_response.json()

    assert new_post['user_id'] == new_user['id']

    requests.delete(GOREST_POSTS + f"/{new_post['id']}", headers=HEADER)
    requests.delete(GOREST_USERS + f"/{new_user['id']}", headers=HEADER)


def test_create_post2(new_user):
    post_data = {"user_id": new_user['id'], "title": "Postens titel", "body": "Postens brödtext"}
    new_post_response = requests.post(GOREST_POSTS, data=post_data, headers=HEADER)
    new_post = new_post_response.json()

    assert new_post['user_id'] == new_user['id']

    requests.delete(GOREST_POSTS + f"/{new_post['id']}", headers=HEADER)
