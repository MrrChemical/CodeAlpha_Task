###################################### HANGMAN GAME #############################################################

# import random
# words = ["strawberry","keyboard",'mouse','gorilla','fence']
# word=random.choice(words)
# display = ["_"] * len(word)
# attempts = 6

# print('Welcome to Hangman!')
# print('Guess the word:')
# while attempts > 0 and '_' in display:
#     print ('word:',''.join(display))
#     guess = input("Guess a letter: ")

#     if guess in word:
#         for x in range(len(word)):
#             if word [x] == guess:
#                 display[x] = guess
#         print("Good Job!\n")
#     else:
#         attempts -= 1
#     print("Attempts left:", attempts,"\n")
# if "_" not in display:
#     print("You win! The word was:" , word)
# else:
#     print("You Lose! The word was: ", word)


###################################################### END ####################################################



############################################ STOCK PORTFOLIO TRACKER ##########################################


# Assets_price = { "AAPL": 180, "TSLA": 250, "GOOGLE": 140, "AMZN":130, "MSFT": 320}
# Investment = 0
# portfolio = {}

# print("Welcome to CODEALPHA Stock Portfolio Tracker ")
# print(" Available stocks: " ,','.join(Assets_price.keys()))

# while True:
#     asset= input ("Enter stock symbol (or 'done' to finish): ").upper()
#     if asset == 'DONE':
#             break
#     if asset not in Assets_price:
#         print("Stock not found. Try again")
#         continue
#     quantity= int(input(f"Enter quantity of {asset}: "))
#     portfolio[asset] = quantity
#     Investment += Assets_price[asset] * quantity

# print("\nYour Portfolio: ")
# for asset, quantity in portfolio.items():
#     print("\nTotal Assets Value: $ ", Investment)

# Save = input(" Do you want to save this to a file? (yes/no): ").lower()
# if Save == "yes":
#     with open ("portfolio.txt", "a") as file:
#         file.write("\nStock portfolio Summary:\n")
#         for stock, quantity in portfolio.items():
#             file.write(f"{asset} : {quantity} shares at $ {Assets_price[asset]} each\n")
#             file.write(f"Total Assests Value: ${Investment}\n")
#             print("Saved to portfolio.txt")


################################################### END #########################################################

######################################### TASK AUTOMATION WITH PYTHON SCRIPT ###################################
################################## Extract Emails from one file and save it to another #########################

# import re

# input_file = "sample.txt"
# output_file = "emails.txt"

# with open (input_file,"r") as file:
#      text = file.read()
#      print(text)

# emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",text)
# print("found emails", emails)

# with open (output_file,"w")as file:
#      for email in emails:
#           file.write(email +"\n")
# print("Email addresses extracted and saved.")


################################################### END #########################################################


############################################# Basic Chatbot #####################################################

print (" Chatbot: Hello! Type 'bye' to end the chat.")
while True:
    message = input("You:  ").lower()

    if message == "Hello".lower():
        print("Chatbot:  Hi!")
    elif message == "How are you?".lower():
        print(" Chatbot: I'm doing great, Thanks!")
    elif message == "Bye".lower():
        print("Chatbot: Goodbye! :)")
        break
    else:
        print("I don't understand.")

################################################### END #########################################################