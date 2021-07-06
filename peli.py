
quiz = {
    1: {"question": "Who was the leader fo the group?", "answer": "Rick"},
    2: {"question": "Who is Carols best friend?", "answer" : "Deryl"}
}

score = 0

for question in quiz:
    print(quiz[question]["question"])
    answer = input("Enter your answer: ")

    if answer == quiz[question]["answer"]:
        score += 1

print(score)