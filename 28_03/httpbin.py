import requests

def basic_auth(username, password):
    url = f"https://httpbin.org/basic-auth/{username}/{password}"
    response = requests.get(url, auth=(username, password))

    return response.json()


def brear(token):
    url = "https://httpbin.org/bearer"
    jwt_token = f"Bearer {token}"
    headers = {"Authorization": jwt_token}
    response = requests.get(url, headers=headers)

    return response.json()

    
def digest_auth(username, password):
    url = f"https://httpbin.org/digest-auth/auth/{username}/{password}"
    response = requests.get(url, auth=requests.auth.HTTPDigestAuth(username, password))
    
    return response.json()


print(basic_auth('admin', 'admin'))
print(brear('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6InNrZWJvYjEyMyIsImFkbWluIjp0cnVlLCJpYXQiOjE1MTYyMzkwMjJ9.UlIC33Qzg93d8OjgkaRPAP-HxAeVeap902NHRQpGR_8'))
print(digest_auth('admin', 'admin'))