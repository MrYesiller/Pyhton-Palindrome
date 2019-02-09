# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 11:47:22 2019

@author: Goksel Yesiller - MrYesiller
"""

green = "\033[32m"

print(green + "A word, phrase, or sequence that reads the same backwards as forwards call as PALİNDROME")
print("*****************************************************************************************")
print("This is a basic python program which is controlling word is a palindrome or not palindrome")
print("Only works with words")
print("For exit write 'q'")


while(True):    
    
    NameList=[]             #Create a list for control letters of the word
    
    
    word=input("Word >>>>> :")
    
    if(word=="q"):          #For Exit
        break               

    for i in word:          #Put the letters of the word in list
        NameList.append(i)  
    #print(NameList) 
        
    ResultNormal = str("".join(map(str, NameList)))  #Take back letters from the list
    print("This is our word: "+ResultNormal)

    NameList.reverse()      #Reverse the list


    ResultReverse = str("".join(map(str, NameList))) #Take back letters from the reversed list
    #print(NameList)
    print("This is our reserved word: "+ResultReverse)
    print("***********************************")

    
    if (ResultNormal==ResultReverse):  #Checking the input_word and reversed_word equal or nor equal 
        print("Word is palindrome")     
    else:
        print("Word is not palindrome")
        

        
