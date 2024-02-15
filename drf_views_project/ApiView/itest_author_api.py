import requests
import payload
import constants


class AuthorApiValidation:
    def test_get_request(self):
        response = requests.get(url=f"{constants.BASE_URL}{constants.AUTHOR_API}")

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
        else:
            # Access Failure status code
            print(f"The Request Failed with Status: {response.status_code}")

            print(f"Failed Response: {response.json()}")

    def test_post_request(self):
        response = requests.post(
            url=f"{constants.BASE_URL}{constants.AUTHOR_API}",
            data=payload.CREATE_AUTHOR_PAYLOAD,
        )

        if response.status_code == 201:
            # Access the response data as a Python dictionary
            response_data = response.json()
            print(f"Response Body: {response_data}")

            # Access headers
            headers = response.headers
            print(f"Header Data: {headers}")

            # Access a specific header (e.g., Content-Type) 
            content_type = response.headers["Content-Type"]
            print(f"Content Type: {content_type}")

            # Access the Response Body
            response_body = response.json()
            print(f"Response Received: {response_body}")

    def test_patch_request(self):
        response = requests.patch(
            url=f"{constants.BASE_URL}{constants.AUTHOR_API}",
            data=self.category_update_payload,
        )

        # Access the response data as python dictionary data
        response_data = response.json()
        print(f"Response Data: {response_data}")

        # Access the status code
        status_code = response.status_code
        print(f"Status Code: {status_code}")

    def test_delete_request(self, id):
        delete_data = {"pk": id}
        response = requests.delete(
            "{constants.BASE_URL}{constants.AUTHOR_API}", data=delete_data
        )
        print(response)


if __name__ == "__main__":
    AuthorApiValidation().test_get_request()
