from random import choice as pick

a_nouns = ["the stray cat", "the bookshelf", "the bellhop", "the waitress",
    "the bookmark", "a frappacino", "a ring"]

b_nouns = ["macaroni", "a bell", "a snake", "the leaf", "your head", "my leg",
    "a boat"]

a_verbs = ["sneezes", "breathes", "makes", "takes", "tastes", "bakes", "groans",
    "yells"]

b_verbs = ["drops", "swings", "watches", "swims", "runs", "tries", "merges",
    "drops"]

infinitives = ["to create a whirlwind", "to bring a thunderstorm",
    "to give an annoucement", "to lead a band to the parade",
    "to win over the competition"]

print ("Hello stranger...let's play a game. Would you like me to craft you an\
    artisan sentence?")
userAnswer = raw_input()

def sentence_maker(Answer):
    if Answer == "yes":
        print pick(a_nouns).title(), pick(a_verbs), pick(b_nouns).lower(), \
         pick(b_verbs), pick(infinitives).lower() + "!"
        print ("Would you like another sentence?") 
    if Answer != "no":
        print ("No-well then, what do you want to do then?")


sentence_maker(userAnswer)

