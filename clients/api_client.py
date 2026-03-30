from requests import Session, Response

import allure


class ApiClient:
    def __init__(self, client: Session):
        self.client = client

    @allure.step("Make GET request to {url}")
    def get(self, url: str, params = None) -> Response:
        return self.client.get(url=url, params=params)

    @allure.step("Make POST request to {url}")
    def post(self, url: str, data = None, json = None) -> Response:
        return self.client.post(url=url, data=data, json=json)
    
    @allure.step("Make DELETE request to {url}")
    def delete(self, url: str) -> Response:
        return self.client.delete(url=url)