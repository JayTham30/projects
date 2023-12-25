#string concatenation (aka how to put strings together)
#suppose we want to create a string that says "subscribe to _____"
#youtuber = "Kylie Yang" # some string variable

#a few ways to do this
#print("subscribe to " + youtuber)
#print("Subscribe to {}".format(youtuber))
#print(f"Subscribe to {youtuber}")


adj = input("Enter a Adj. ")
verb = input("Enter a verb. ")
verb2 = input("Enter another verb. ")
famous_person = input("Enter a famous person. ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \nI love to {verb}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)

