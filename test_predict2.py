import requests

session = requests.Session()
# Login
session.post('http://localhost:8000/api/login', json={'email': 'test@test.com', 'password': 'password'})

# Upload
with open('CropDoctor/static/diseased_leaf.png', 'rb') as f:
    files = {'image': ('rust_leaf.png', f, 'image/png')}
    response = session.post('http://localhost:8000/api/predict', files=files)
    print(response.status_code)
    print(response.text)
