import random as r
import math
Uscore=0
Cscore=0
user=input(" Enter Player Name.! ")
print(" Welcome",user)

while True:
    while True:
        print(" Press 0 for Snake\n","Press 1 for Water\n","Press 2 for Gun")
        userSelection=int(input(" Press 3 for Exit "))
        if(userSelection<0 or userSelection>3):
            print(" Please Enter a Valid Selection..")
        else:
            break
    if(userSelection==3):
        break

    list=['Snake','Water','Gun']
    computer=int((r.random()*10)%3)
    matrix=[['draw',user,'Computer'],['Computer','draw',user],[user,'Computer','draw']]

    print(" User Selection :- ",list[userSelection])
    print(" Computer Selection :- ",list[computer])
    if(matrix[userSelection][computer]=='draw'):
        print(" Match Draw.")
    elif(matrix[userSelection][computer]==user):
        print("",matrix[userSelection][computer],'Wins')
        Uscore=Uscore+1
    else:
         print("",matrix[userSelection][computer],'Wins')
         Cscore=Cscore+1
print(user,",your Total Scores are ",Uscore)
print("Computer Total Scores are ",Cscore)



