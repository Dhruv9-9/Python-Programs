#This a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

myString = "Hope is the thing with feathers, that perches in the soul, And sings the tune without the words, And never stops - at all. \
            And sweetest in the gale is heard, And sour must be the storm, That could abash the little bird, That kept so many warm. \
            I've heard it in the chilliest land, And on the strangest sea, Yet - never - in Extremity, It asked a crumb - of me. "

countwords = myString.replace(".", "")
countwords = myString.replace(',', '')
countwords = myString.replace('-', '')
countwords = myString.replace("'", '')
countwords = myString.lower()
countWords = countwords.split()

wordDictionary = {}

for word in countWords :

    if word in wordDictionary :
        wordDictionary[word] += 1
    else :
        wordDictionary[word] = 1

print(wordDictionary)
