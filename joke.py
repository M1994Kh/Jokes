import requests
from abc import ABC, abstractmethod

# ----------------------------------------------------------------Parameters----------------------------------------------------------------------

A_url = "https://jokeapi-v2.p.rapidapi.com/joke/Any?id=35"
A_headers = {
"X-RapidAPI-Key": "5023817230msh89cee98fc8ddbc4p1e0eaejsn36f46f61d859",
"X-RapidAPI-Host": "jokeapi-v2.p.rapidapi.com"
}
A_querystring = {"format":"json","contains":"C%23","idRange":"0-319"}


B_url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"
B_headers = {
"accept": "application/json",
"X-RapidAPI-Key": "5023817230msh89cee98fc8ddbc4p1e0eaejsn36f46f61d859",
"X-RapidAPI-Host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
}


C_url = "https://cycoshas-mouth-talking-app-v1.p.rapidapi.com/best-mouth-talking-apps/"
C_headers = {
	"X-RapidAPI-Key": "5023817230msh89cee98fc8ddbc4p1e0eaejsn36f46f61d859",
	"X-RapidAPI-Host": "joke3.p.rapidapi.com"
}
# ----------------------------------------------------------------Main Class------------------------------------------------------------------------

class Joke(ABC):
    def __init__(self, url, headers, **kwargs):
        pass
    @abstractmethod
    def get_random_joke(self):
        pass


# --------------------------------------------------------------Child Classes------------------------------------------------------------------------

class A (Joke):
    def __init__(self, url, headers, **kwargs):
        self.url = url
        self.headers = headers
        self.querystring = kwargs.get("Qstring")
    def get_random_joke(self):
        response = requests.request("GET", self.url, headers=self.headers, params=self.querystring)
        j = response.json()
        try:
            if j["type"] == "twopart":
                res = j["setup"]+"\n"+j["delivery"]
                return res
            else:
                return j["setup"]
        except KeyError:
            return str(response.text)



class B (Joke):
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers
    def get_random_joke(self):
        response = requests.request("GET", self.url, headers=self.headers)
        j = response.json()
        try:
            return j["value"]
        except KeyError:
            return str(response.text)



class C (Joke):
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers 
    def get_random_joke(self):
        response = requests.request("GET", self.url, headers=self.headers)
        j = response.json()
        try:
            return j["content"]
        except KeyError:
            return str(response.text)

# --------------------------------------------------------------Main Function---------------------------------------------------------------------------
def main():
    Joke1 = A(A_url, A_headers, Qstring = A_querystring)
    print("Joke 1:"+Joke1.get_random_joke())
    Joke2 = B(B_url, B_headers)
    print("Joke 2:"+Joke2.get_random_joke())
    Joke3 = C(C_url, C_headers)
    print("Joke 3:"+Joke3.get_random_joke())


if __name__ == "__main__":
    main()
