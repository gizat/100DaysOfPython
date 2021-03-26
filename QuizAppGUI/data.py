import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]


# question_data = [
#     {
#         "category": data["category"],
#         "type": data["type"],
#         "difficulty": data["difficulty"],
#         "question": data["question"],
#         "correct_answer": data["correct_answer"],
#         "incorrect_answers": data["incorrect_answers"],
#     },
# ]
