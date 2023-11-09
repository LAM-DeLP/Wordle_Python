import random
import tkinter

answ = ["guide","sence","orbit"]

def ext_char(input_list):
    return [str(char) for char in input_list]

def create_matrix(list1,list2):
    crspnd_list = [[j for j in range(len(list1)) if list1[i]==list2[j]] for i in range(len(list1))]
    return crspnd_list

answ_char = ext_char(random.choice(answ))
input_char = ext_char(input())

print(answ_char)
print(input_char)
print(create_matrix(input_char,answ_char))

