import requests

BASE_URL = "http://127.0.0.1:8000/"
POST_ENDPOINT = "function-based/create-employee/"
DELETE_ENDPOINT = "function-based/delete-employee/"


class APIRequest:
    employee_payload = {
        "first_name": "Neeraj",
        "last_name": "Shankar",
        "email": "test_email@django.com",
        "salary": "2000.80",
        "hire_date": "2023-10-30",
    }

    def post_request(self):
        response = requests.post(
            url=f"{BASE_URL}{POST_ENDPOINT}", data=self.employee_payload
        )
        print(f"Response: {response}")

        if response.status_code == 200:
            print(f"The request sent successfully")

    def delete_request(self, id):
        delete_data = {"pk": id}
        response = requests.delete(url=f"{BASE_URL}{DELETE_ENDPOINT}", data=delete_data)
        print(response)

"""
Class Object and function call
"""

test = APIRequest()
test.delete_request(1)



