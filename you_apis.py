import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

if __name__ == "__main__":
    app.run()


@app.route('/travel',methods=['GET'])
def travel():
    data = request.get_json()
    answers = data.get('answers')
    url = "https://chat-api.you.com/smart"

    payload = {
        "query" : f"Assume the role of a bot trying to measure the carbon footprint of a person, based on their description of how they travel everyday, rate that person's Carbon Footprint in the range of 0 to 100. The person's description is {answers}. Generate only a two-digit number, no other explanation or reasoning is required.",
        "chat_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a"
    }
    headers = {
        "X-API-Key": "65c95fb3-7f81-4a01-9419-b6f150340e56<__>1PTsFeETU8N2v5f4qmtDZVGS",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    return response.json()


@app.route('/trash',methods=['GET'])
def trash():
    data = request.get_json()
    answers = data.get('answers')
    url = "https://chat-api.you.com/smart"

    payload = {
        "query" : f"Assume the role of a bot trying to measure the carbon footprint of a person, based on their description of how much trash do they produce everyday, rate that person's Carbon Footprint in the range of 0 to 100. The person's description is {answers}. Generate only a two-digit number, no other explanation or reasoning is required.",
        "chat_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a"
    }
    headers = {
        "X-API-Key": "65c95fb3-7f81-4a01-9419-b6f150340e56<__>1PTsFeETU8N2v5f4qmtDZVGS",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    return response.json()


@app.route('/energy',methods=['GET'])
def energy():
    data = request.get_json()
    answers = data.get('answers')
    url = "https://chat-api.you.com/smart"

    payload = {
        "query" : f"Assume the role of a bot trying to measure the carbon footprint of a person, based on their description of how much energy do they consume everyday, rate that person's Carbon Footprint in the range of 0 to 100. The person's description is {answers}. Generate only a two-digit number, no other explanation or reasoning is required.",
        "chat_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a"
    }
    headers = {
        "X-API-Key": "65c95fb3-7f81-4a01-9419-b6f150340e56<__>1PTsFeETU8N2v5f4qmtDZVGS",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    return response.json()


@app.route('/water',methods=['GET'])
def water():
    data = request.get_json()
    answers = data.get('answers')
    url = "https://chat-api.you.com/smart"

    payload = {
        "query" : f"Assume the role of a bot trying to measure the carbon footprint of a person, based on their description of how much water they use everyday, rate that person's Carbon Footprint in the range of 0 to 100. The person's description is {answers}. Generate only a two-digit number, no other explanation or reasoning is required.",
        "chat_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a"
    }
    headers = {
        "X-API-Key": "65c95fb3-7f81-4a01-9419-b6f150340e56<__>1PTsFeETU8N2v5f4qmtDZVGS",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    return response.json()




@app.route('/plants',methods=['GET'])
def plants():
    data = request.get_json()
    answers = data.get('answers')
    url = "https://chat-api.you.com/smart"

    payload = {
        "query" : f"Assume the role of a bot trying to measure the carbon footprint of a person, based on their description about how many plants do they have at home, rate that person's Carbon Footprint in the range of 0 to 100. The person's description is {answers}. Generate only a two-digit number, no other explanation or reasoning is required.",
        "chat_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a"
    }
    headers = {
        "X-API-Key": "65c95fb3-7f81-4a01-9419-b6f150340e56<__>1PTsFeETU8N2v5f4qmtDZVGS",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    return response.json()

@app.route('/test',methods=['GET'])
def test():
    print("HELLO WORLD")
    return "HELLO WORLD"
