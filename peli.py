
points = 0
print("Welcome to the quiz!\nThis section was made by Krisztina and Mikko :)")
print()

while True:
    question1 = input("Who was killed rather dramatically with a baseball bat in the Walking Dead? ")
    if question1.lower() == "glenn" or question1.lower() == "glenn rhee":
        points+=1
    question2 = input("Who delivered the deadly blow? ")
    if question2.lower() == "negan" or question2.lower() == "negan smith":
        points+=1
    
    break

print("Points: ", points)