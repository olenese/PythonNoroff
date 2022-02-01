
print("Hello, welcome to my quiz about Bergen!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Great! Let's play!")

name = input("What is you name? ")

print("Let's get started, "+ name)

answer = input("What is the weather today? ")
if answer == "rain":
    print("Correct answer!")
    else print()