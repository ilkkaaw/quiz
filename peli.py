quiz = {
    1: {"question": "Who was the leader for the group?", "answer" : "rick"},
    2: {"question": "Who is Carol's best friend?", "answer" : "deryl"},
    3: {"question": "Who was killed rather dramatically with a baseball bat in the Walking Dead?", "answer" : "glenn"},
    4: {"question": "Who delivered the deadly blow?", "answer" : "negan"}
}

score = 0
print("Welcome to the quiz!\nThis section was made by Krisztina and Mikko :)")
print()

while True:
    for question in quiz:
        print(quiz[question]["question"])
        answer = input("Enter your answer: ")

        if answer.lower() == quiz[question]["answer"]:
            score += 1

    print("Score:", score)
    print()
    again = input("Do you want to play again? (Y to play again, N to quit) ")

    if again[0].lower() == "n":
        break
