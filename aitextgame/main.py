import ai as aistory

running = True

while(running):
    userInput = input(">: ")


    if userInput.lower() == "quit":
        running = False

    res = aistory.getNewAIMessage(userInput)
    print(res)