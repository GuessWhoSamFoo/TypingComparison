from keyLayout import qwertyLayout, dvorakLayout
from string import ascii_lowercase
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

qwertyLetters = {
}    

dvorakLetters = {
}

#Returns distance in px
def distance(position1, position2):
    x = position2[0]-position1[0]
    y = position2[1]-position1[1]
    return (x ** 2 + y ** 2) ** 0.5
    
    
def lookupLetters(textString):
    qwertyDistance = 0
    dvorakDistance = 0
    if len(textString) == 1: #Case for one letter word (a, I, O)
        return qwertyDistance, dvorakDistance
    for index in range(len(textString) - 1):
        qwertyDistance += distance(qwertyLayout[textString[index]],qwertyLayout[textString[index+1]])
        dvorakDistance += distance(dvorakLayout[textString[index]],dvorakLayout[textString[index+1]])
    return qwertyDistance, dvorakDistance

    
def averageKey(results):
    for key in results:
        results[key] = np.mean(results[key])
    return results
    
    
with open("google-10000-english-usa.txt") as f:
    for line in f:
        wordLen = len(line.rstrip('\n'))
        qVal, dVal = lookupLetters(line.rstrip('\n'))
        try:
            #Add number of letters/total movement(key/value) pair if exists
            qwertyLetters[wordLen].append(qVal)
            dvorakLetters[wordLen].append(dVal)
        except KeyError:
            #Create new key/value
            qwertyLetters[wordLen], dvorakLetters[wordLen] = [qVal],[dVal]
            

qwertyResults = averageKey(qwertyLetters)
dvorakResults = averageKey(dvorakLetters)

x_qwerty = qwertyResults.keys()
y_qwerty = qwertyResults.values()

x_dvorak = dvorakResults.keys()
y_dvorak = dvorakResults.values()



#What is the best way to represent this data?
plt.title('Comparison of QWERTY and DVORAK Gesture Typing')
plt.scatter(x_qwerty,y_qwerty,c='r')
plt.scatter(x_dvorak,y_dvorak,c='b')
plt.xlabel('Number of Letters in Word')
plt.ylabel('Total Movement (px)')

red_label = mpatches.Patch(color='red', label='QWERTY')
blue_label = mpatches.Patch(color='blue', label='DVORAK')
plt.legend(handles=[red_label,blue_label],loc=4)
plt.show()

