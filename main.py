import random
import tkinter



answ = ["Guide","sence","Orbit"]

def ext_char(input_list):
    return [str(char) for char in input_list]

answ_char = ext_char(random.choice(answ))
input_char = ext_char(input())

def check_crrspnd(list1,list2):
    crspnd_list = [int(i) for i in range(len(list1)) if list1[i]==list2[i]]
    print(crspnd_list)


print(answ_char)
print(input_char)
check_crrspnd(input_char,answ_char)
