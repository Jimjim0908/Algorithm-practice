target="methinks it is like a weasel"
import random
def generationOne(strlen):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    res = ""
    for i in range(strlen):
        res = res + alphabet[random.randrange(27)]
    return res

def score(goal,teststring):
    numSame = 0
    for i in range(len(goal)):
        if goal[i] == teststring[i]:
            numSame += 1
    return numSame / len(goal)

def main():
    bestscore = 0
    newstring = generationOne(28)
    newscore = score(target, newstring)
    while newscore <1:
        if newscore > bestscore:
            print(newscore, newstring)
            bestscore = newscore
        newstring = generationOne(28)
        newscore = score(target, newstring)

def main2():
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    newstring=""
    while score(target,generationOne(28)) <1:
        new_alphabet = alphabet[random.randrange(27)]
        i=0
        while target[i] == new_alphabet:
            newstring = newstring + target[i]
            i=i+1
            new_alphabet = alphabet[random.randrange(27)]
            
alphabet = "abcdefghijklmnopqrstuvwxyz "
def random_alphabet():
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    new_alphabet = alphabet[random.randrange(27)]
    return new_alphabet
while target[range(28)] == random_alphabet():
    print(target[0])

'''
print generationOne(5)
print len(target)
print (score(target, generationOne(len(target))))
'''