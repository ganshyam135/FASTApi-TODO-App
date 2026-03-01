from TodoApp.models import Users

from .utils import *
from ..routers.users import get_db, get_current_user
from fastapi import status

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_return_user(test_user):
    response = client.get("/users")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['username'] == 'ganshyamtest'
    assert response.json()['email'] == 'ganshyamtest@email.com'
    assert response.json()['first_name'] == 'ganshyam'
    assert response.json()['last_name'] == 'suthar'
    assert response.json()['role'] == 'admin'
    assert response.json()['phone_number'] == '1234567890'

def test_change_password_success(test_user):
    response = client.put("/users/password", json={"current_password": "testpassword", 
                                                 "new_password": "newpassword"})
    assert response.status_code == status.HTTP_204_NO_CONTENT
 
def test_change_password_invalid_current_password(test_user):
    response = client.put("/users/password", json={"current_password": "wrong_password", 
                                                 "new_password": "newpassword"})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail': 'Error on password change'} 

def test_change_phone_number_success(test_user):
    response = client.put("/users/phonenumber/2222222222")
    assert response.status_code == status.HTTP_204_NO_CONTENT