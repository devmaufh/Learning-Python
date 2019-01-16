content="Today is your birthday, and I just wanted to take a moment to tell you how much I love you. Just being with you has made all my dreams come true, and I want to do everything I can to make you feel that way too. You deserve to be treasured for being the sweetest, kindest, most thoughtful boyfriend any girl could ask for and believe me, I do treasure you. I hope we will celebrate your birthday together each year for the rest of our lives"
dictionary={}
for char in content:
    if char in dictionary.keys():
        dictionary[char]+=1
    else:
        dictionary[char]=1
print (dictionary)