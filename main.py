import requests


def req():
    response = requests.get("https://randomfox.ca/floof")
    print(response.status_code)
    fox = response.json()
    print(fox['image'])


if __name__ == '__main__':
    req()
