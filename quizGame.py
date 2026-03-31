import time
score = 0
q1 = "Who is the Prime Minister of India? (Only last name)"
q2 = "What is the capital of France?"
q3 = "Who wrote the book 'Harry Potter'?"
q4 = "What is the largest planet in our solar system?"
q5 = "Who discovered gravity?"
q6 = "What is the chemical symbol for water?"
q7 = "Which continent is known as the Dark Continent?"
q8 = "Who is known as the Father of the Nation in India?"
q9 = "What is the fastest land animal?"
q10 = "Who painted the Mona Lisa?"

print("*************************")
print("   LET'S GET QUIZZICAL   ")
print("*************************")
time.sleep(3)
print("Your score: ", score)
print(q1)
a1 = input()
if a1 == "modi":
    score = score + 1
    print("Your score: ", score)
else: 
    print("Incorrect! Proceeding to next question")
    print("Your score: ", score)

print(q2)
a2 = input()
if a2 == "paris":
    score = score + 1
    print("Your score: ", score)
else: 
    print("Incorrect! Proceeding to next question")
    print("Your score: ", score)

print(q3)
a3 = input()
if a3 == "rowling":
    score = score + 1
    print("Your score: ", score)
else: 
    print("Incorrect! Proceeding to next question")
    print("Your score: ", score)

print(q4)
a4 = input()
if a4 == "jupiter":
    score = score + 1
    print("Your score: ", score)
else: 
    print("Incorrect! Proceeding to next question")
    print("Your score: ", score)

print(q5)
a5 = input()
if a5 == "newton":
    score = score + 1
    print("Your score: ", score)
else: 
    print("Incorrect! Proceeding to next question")
    print("Your score: ", score)

print(q6)
a6 = input()
if a6 == "h2o":
    score = score + 1
    print("Your score: ", score)
else: 
    print("Incorrect! Proceeding to next question")
    print("Your score: ", score)

print(q7)
a7 = input()
if a7 == "africa":
    score = score + 1
    print("Your score: ", score)
else: 
    print("Incorrect! Proceeding to next question")
    print("Your score: ", score)

print(q8)
a8 = input()
if a8 == "gandhi":
    score = score + 1
    print("Your score: ", score)
else: 
    print("Incorrect! Proceeding to next question")
    print("Your score: ", score)

print(q9)
a9 = input()
if a9 == "cheetah":
    score = score + 1
    print("Your score: ", score)
else: 
    print("Incorrect! Proceeding to next question")
    print("Your score: ", score)

print(q10)
a10 = input()
if a10 == "da vinci":
    score = score + 1
    print("Your score: ", score)
else: 
    print("Incorrect! Quiz complete")
    print("Your score: ", score)
