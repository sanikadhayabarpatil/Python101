print("Hey Welcome to your Finance Quiz! Hope you learn from your mistakes \n")

#--------helper functions---------#

def normailze(text):
    """Lowercases + remove spaces"""
    return text.lower().replace(" "," ")

def is_yes(user_input):
    yes_variants = ['yes','yea', 'ya', 'YEs','yES','y','hell yeah']
    cleaned = normailze(user_input)
    return any (word in cleaned for word in yes_variants)

def is_closematch(user_answer,correct_answer):
    """
    Allows small spelling mistakes and plural/singular differences
    """
    user= normailze(user_answer)
    correct= normailze(correct_answer)

     # exact or substring match

    if user == correct or user in correct or correct in user:
        return True
    
    # simple typo tolerance (character overlap)
    matches = sum(1 for c in user if c in correct)
    return matches / max(len(correct), 1) >= 0.7

# ---------- game start ----------

playing = input("Ready? ")

if not is_yes(playing):
    print("Your loss 😄")
    quit()

print("\nLet's Play! Get Ready!\n")

score = 0

# ---------- quiz questions ----------

answer = input("What does APR stand for? ")
if is_close_match(answer, "annual percentage rate"):
    print("Yay! You got that right!\n")
    score += 1
else:
    print("Incorrect! You need to learn\n")

answer = input("What is inflation? ")
if is_close_match(answer, "increase in prices over time"):
    print("Correct!\n")
    score += 1
else:
    print("Wrong answer\n")

answer = input("What is a budget? ")
if is_close_match(answer, "plan for managing income and expenses"):
    print("Correct!\n")
    score += 1
else:
    print("Wrong answer\n")

answer = input("What is interest? ")
if is_close_match(answer, "cost of borrowing money"):
    print("Correct!\n")
    score += 1
else:
    print("Wrong answer\n")

answer = input("What does a credit score represent? ")
if is_close_match(answer, "creditworthiness of a person"):
    print("Correct!\n")
    score += 1
else:
    print("Wrong answer\n")


# ---------- results ----------

print(f"You got {score} questions correct")

if score <= 2:
    print("You have to start learning the basics")
elif score < 5:
    print("You can definitely improve")
else:
    print("WOW, YOU ARE AMAZING")

print("\nThanks for playing! Keep learning 🚀")
