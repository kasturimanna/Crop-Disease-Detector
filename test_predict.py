import requests

session = requests.Session()
# Register
session.post('http://localhost:8000/api/register', json={'email': 'test@test.com', 'password': 'password', 'name': 'test'})
# Login
session.post('http://localhost:8000/api/login', json={'email': 'test@test.com', 'password': 'password'})

# Upload
with open('CropDoctor/static/diseased_leaf.png', 'rb') as f:
    files = {'image': f}
    response = session.post('http://localhost:8000/api/predict', files=files)
    print(response.status_code)
    print(response.text)
