quiz = {
    1: {"question": "Who was the leader for the group?", "answer" : "rick"},
    2: {"question": "Who is Carol's best friend?", "answer" : "daryl"}, #dAryl, ei deryl
    3: {"question": "Who was killed rather dramatically with a baseball bat in the Walking Dead?", "answer" : "glenn"}, #Also Abraham, but multiple possibilties in a dictionary is hard
    4: {"question": "Who delivered the deadly blow?", "answer" : "negan"}
}
total_questions = len(quiz)

score = 0
print("Welcome to the quiz!\nThis section was made by Krisztina and Mikko :)")
print()

while True:
    for question in quiz: #This was actually a good way to go through them all!
        print(quiz[question]["question"])
        answer = input("Enter your answer: ")

        if answer.lower() == quiz[question]["answer"]:
            print("Correct!") #Tell the player when it goes right.
            score += 1
        else:
            print("Wrong") #Tell the player when it goes wrong.
    print(f"Score: {score} out of {total_questions}") #Score means nothing if you don't know what is the maximum.
    print()
    again = input("Do you want to play again? (Y to play again, N to quit) ")

    if again[0].lower() == "n": #This only checks for a negative answer. Any other answer means yes!
        break
