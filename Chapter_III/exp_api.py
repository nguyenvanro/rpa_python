import requests

def api_get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)

api_get_posts()

def api_create_posts(title, body, user_id):
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        'title': title,
        'body': body,
        'userId': user_id}
    files=[]
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response.text)

api_create_posts(title="Tiêu đề 1", body='Nội dung 1', user_id="1")
api_create_posts(title="Tiêu đề 2", body='Nội dung 2', user_id="10")
api_create_posts(title="Tiêu đề 3", body='Nội dung 3', user_id="5")

