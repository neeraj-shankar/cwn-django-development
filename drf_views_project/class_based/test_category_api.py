import requests
import payload
BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "class_based/create-list/"


class APIRequest:
    

    def list_request(self):
        response = requests.get(url=f"{BASE_URL}{ENDPOINT}")
        print(f"Sending Request to --> {BASE_URL}{ENDPOINT}")
        if response.status_code == 200:
            # Access the response data as a Python dictionary
            response_data = response.json()
            print(f"Response Body: {response_data}")

            # Access headers
            headers = response.headers
            print(f"Header Data: {headers}")

            # Access a specific header (e.g., Content-Type)
            content_type = response.headers["Content-Type"]
            print(f"Content Type: {content_type}")
        elif response.status_code == 404:
            # Access headers
            headers = response.headers
            print(f"Header Data: {headers}")

    def post_request(self):
        response = requests.post(
            url=f"{BASE_URL}{ENDPOINT}", data=payload.CREATE_CATEGORY_PAYLOAD
        )
        print(f"Sending Request to --> {BASE_URL}{ENDPOINT}")

        response_data = response.json()
        print(f"Response Body: {response_data}")
        if response.status_code == 201:
            print(f"The request sent successfully")

    def request_patch(self):
        ID = 1
        response = requests.patch(
            url=f"{BASE_URL}{ENDPOINT}{ID}/",
            data=payload.UPDATE_CATEGORY_PAYLOAD,
        )

        # Access the response data as python dictionary data
        response_data = response.json()
        print(f"Response Data: {response_data}")

        # Access the status code
        status_code = response.status_code
        print(f"Status Code: {status_code}")

    def request_delete(self, id):
        delete_data = {"pk": id}
        response = requests.delete(url=f"{BASE_URL}{ENDPOINT}{id}", data=delete_data)
        print(response)


if __name__ == "__main__":
    # # APIRequest().request_patch()
    # APIRequest().list_request()
    # APIRequest().post_request()
    APIRequest().list_request()
    APIRequest().request_patch()
    APIRequest().list_request()
