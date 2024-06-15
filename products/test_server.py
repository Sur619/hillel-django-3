import requests


def test_product_get():
    response = requests.get('http://127.0.0.1:8000/api/products/')

    print(response.json())
    print(response.status_code)


if __name__ == '__main__':
    test_product_get()