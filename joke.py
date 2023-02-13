import requests
from abc import ABC


class Joke(ABC):
    @abstractmethod
    def get_random_joke(self):
        pass

class A (Joke):
    def __init__(self):
        self.url = "https://dad-jokes.p.rapidapi.com/random/joke"
        self.headers = {
            "X-RapidAPI-Key": "5023817230msh89cee98fc8ddbc4p1e0eaejsn36f46f61d859",
            "X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"
            }
    def get_random_joke(self):
        response = requests.request("GET", self.url, headers=self.headers)
        print(response.text)
class B (Joke):
    def __init__(self):
        self.url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"
        self.headers = {
            "accept": "application/json",
            "X-RapidAPI-Key": "5023817230msh89cee98fc8ddbc4p1e0eaejsn36f46f61d859",
            "X-RapidAPI-Host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
            }
    def get_random_joke(self):
        response = requests.request("GET", self.url, headers=self.headers)
        print(response.text)
class C (Joke):
    def __init__(self):
        self.url = "https://webknox-jokes.p.rapidapi.com/jokes/search"
        self.headers = {
            "X-RapidAPI-Key": "5023817230msh89cee98fc8ddbc4p1e0eaejsn36f46f61d859",
	        "X-RapidAPI-Host": "webknox-jokes.p.rapidapi.com"
            }
        self.querystring = {"keywords":"kick, hard","numJokes":"5","category":"Chuck Norris","minRating":"5"}
    def get_random_joke(self):
        response = requests.request("GET", self.url, headers=self.headers, params=self.querystring)
        print(response.text)

