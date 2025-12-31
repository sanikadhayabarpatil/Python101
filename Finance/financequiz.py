print("Hey Welcome to your Finance Quiz! Hope you learn from your mistakes")

print("Ready?")
playing = input()

if playing.lower() != "yes":
    print("Your Loss")
    quit()

print("Let's Play! \n Get Ready!")
score = 0
answer =input("What does APR stand for? ")

if answer.lower() != "annual percentage rate":
    print("Incorrect! You need to learn")
    
else:
    print("Yay! You got that right!")
    score +=1 

answer = input("What is inflation?")

if answer.lower() != "increase in prices over time":
    print("Incorrect! You need to learn")
    
else:
    print("Yay! You got that right!")
    score +=1 

answer = input("What does a credit score represent")

if answer.lower() != "creditworthiness":
    print("Incorrect! You need to learn")
    
else:
    print("Yay! You got that right!")
    score +=1 

answer = input("What is a budget")

if answer.lower() != "plan for managing income and expenses":
    print("Incorrect! You need to learn")
    
else:
    print("Yay! You got that right!")
    score +=1 

answer = input("What is a Interest")

if answer.lower() != "cost of borrowing money":
    print("Incorrect! You need to learn")
    
else:
    print("Yay! You got that right!")
    score +=1 

print(" You got " + str(score) + " questions correct")

if score <=2:
    print(" You have to start learning the basics")
if score >= 3 and score != 5:
    print (" You can definitely improve")
else:
    print("WOW, YOU ARE AMAZING")


print("Hope you enjoyed! Keep learning more")