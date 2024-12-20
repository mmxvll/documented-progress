from quiz import Questions

country_quiz = [
    Questions("What was the capital of Albania? ", "Tirane"),
    Questions("What was the capital of South Africa? ", "Pretoria"),
    Questions("What was the capital of Slovakia? ", "Bratislava"),
    Questions("What was the capital of Romania? ", "Bucharest"),
    Questions("What was the capital of Chile? ", "Santiago")
]

def run_quiz(list):
    score = 0
    for question in list:
        answer = input(question.question)
        if answer == question.answer:
            score += 1
    return str(score)

user_score = run_quiz(country_quiz)  

print("Your score is " + user_score + " out of " + str(len(country_quiz))) 