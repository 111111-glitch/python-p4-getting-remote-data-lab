import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content  # Return the content of the response

    def load_json(self):
        response = self.get_response_body()
        return json.loads(response)  # Convert the response content to JSON
