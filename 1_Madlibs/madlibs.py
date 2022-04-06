# string concatenation (aka how to put strings together)
# # suppose we want to create a string that says "sub scribe to ____"
# youtuber = "kerwin"  # some string variable
#
# # a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adfective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f'Computer programming is so {adj}! It makes me so excited all the time because I　love to {verb2}. ' \
         f'Stay hydrated and {verb2} like you are {famous_person}! '

print(madlib)
