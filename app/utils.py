import requests

def fetch_fun_fact(number):
    response = requests.get(f"http://numbersapi.com/{number}/math?json")
    if response.status_code == 200:
        return response.json().get("text", "No fact available")
    return "No fact available"


