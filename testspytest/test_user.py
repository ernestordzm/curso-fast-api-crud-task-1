
# from httpx import AsyncClient, 
import httpx
import pytest


@pytest.mark.asyncio
async def test_create_token( default_client: httpx.AsyncClient) -> None:
    payload = {
        'usernam': 'admintestadmin@gmail.com',
        'password': '12345'
    }

    headers = {
        'accept': 'application/json'
        # 'Content-Type': 'application/json'
    }

    response = await default_client.post('/token', data=payload, headers=headers)

    assert response.status_code == 200
    # assert response.json() == {
    #     'message': 'User created successfully'
    # }    


# @pytest.mark.asyncio
# # @pytest.mark.anyio
# async def test_sign_new_user( default_client: httpx.AsyncClient) -> None:
#     payload = {
#         'email' : 'admintest@admin.com',
#         'name': 'Ernesto',
#         'surname': 'Rodriguez',
#         'website': 'https://www.elnorte.com/',
#         'password': '12345'
#     }

#     headers = {
#         'accept': 'application/json',
#         'Content-Type': 'application/json'
#     }

#     response = await default_client.post('/register', json=payload, headers=headers)

#     assert response.status_code == 201
#     assert response.json() == {
#         'message': 'User created successfully'
#     }