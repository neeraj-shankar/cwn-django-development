import requests

BASE_URL = "http://127.0.0.1:8000/"
POST_ENDPOINT = "function-based/employee_create/"
DELETE_ENDPOINT = "function-based/employee_delete/"
LIST_ENDPOINT = "function-based/employee-list/"
UPDATE_ENDPOINT = "function-based/employee_update/"


class APIRequest:
    employee_payload = {
        "first_name": "Neeraj",
        "last_name": "Shankar",
        "email": "test_email@django.com",
        "salary": 2000.80,
        "hire_date": 2023-10-30,
    }

    employee_payload_update = {
        "first_name": "Neeraj",
        "last_name": "Shankar",
        "email": "test_update@django.com",
        "salary": "10000.80",
        "hire_date": "2023-10-30",
    }

    def list_request(self):
        delete_data = {"pk": id}
        response = requests.get(url=f"{BASE_URL}{LIST_ENDPOINT}")
        print(response)
        if response.status_code == 200:
            print(f"The request was successful")

    def post_request(self):
        response = requests.post(
            url=f"{BASE_URL}{POST_ENDPOINT}", data=self.employee_payload
        )
        print(f"Response: {response}")

        if response.status_code == 201:
            print(f"The request sent successfully")

    def request_put(self, emp_id):
        response = requests.put(
            url=f"{BASE_URL}{UPDATE_ENDPOINT}/{emp_id}",
            data=self.employee_payload_update,
        )
        # response_json = response.json()
        # print(f"JSON Response: {response_json}")
        response_text_data = response.text
        response_binary_data = response.content
        # print(f"Binary Response: {response_binary_data}")

        # Access the specific header
        content_type = response.headers.get("content-type")
        print(f"Content Type: {content_type}")

        if response.status_code == 404:
            print(f"The request was successful but data not found...")

    def request_delete(self, id):
        delete_data = {"pk": id}
        response = requests.delete(url=f"{BASE_URL}{DELETE_ENDPOINT}{id}", data=delete_data)
        print(response)


"""
Class Object and function call
"""

test = APIRequest()
# test.list_request()
# test.request_put(1)
test.post_request()
# test.request_delete(1)