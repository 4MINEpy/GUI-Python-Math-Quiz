import random
import os

def getUserPoint(name):
    f = open("userScores.txt","r")
    userList = list()
    for x in f :
        ch = x.split()
        ch[0] = ch[0].replace(',','')
        userList.extend(ch)
    for i in range(len(userList)):
        if(userList[i] == name) : 
            return
getUserPoint("B")