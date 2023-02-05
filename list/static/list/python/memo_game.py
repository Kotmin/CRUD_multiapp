import streamlit as st
import random
import re

"""
Hello, can u remember me?


"""


text_to_guess = '''
Organizacja komputera - obejmuje wzajemne powiązania, i współdziałanie jego, poszczególnych bloków funkcjonalnych.

'''

text_with_e = text_to_guess


how_many_blank = 3
text_len = len(text_to_guess)
blank_indexes = []
blank_values = []

def make_guesses(text=text_with_e,c_blank=how_many_blank):
    while c_blank:
        random_index=random.randint(0,text_len)
        if random_index in blank_indexes:
            continue
        if len(re.findall("[]",text[random_index]))




if text_to_guess:
    st.write(text_with_e)

ans = st.text_input("Type here:")



# f = open("text_to_remind.txt","r")

# data=f.read()
# f.close()

# print(data)
# print(len(data))
# print(data[2])

# print(data[2])
# print(data)
# print(data)
# linijka=data.str(data)
# print(linijka)
# print(type(data))
# print(data.capitalize())



def print_underscored(indexes,word):
    tmp=word.copy()
    for i in indexes:
        tmp[i]='_'*len(tmp[i])
    # print(word)
    print(' '.join(tmp))

# def is_correct(answer,question):
#     if answer.replace(' ','').lower() == question.lower():
#         return True
#     return False

# with open('text_to_remind.txt') as f:
#     flat_list=[word for line in f for word in line.replace('.','').replace(',','').split()]

# # with open('text_to_remind.txt') as f:
# #     orginal=[word for line in f for word in line.split()]

# len_of_list=len(flat_list)
# how_much_blank=3
# # where_to_start=data.index('-')
# where_to_start=flat_list.index('-')

# # print(len_of_list) #12

# # replace_all_letters_with_underscore(flat_list[1])

# pure_text=' '.join(flat_list)
# # print(pure_text)

# changed=flat_list.copy()

# # print(changed)
# # print(changed[1])
# # replace_all_letters_with_underscore(changed[1])
# print(flat_list)



# which_numbers=[]
# it=0
# while(it<how_much_blank):
#     i=random.randint(where_to_start,len_of_list-1)
#     if flat_list[i]!='-' and i not in which_numbers:
#         which_numbers.append(i)
#         it+=1



# which_numbers.sort()
# print(which_numbers)



# print_underscored(which_numbers,flat_list)
# score=0
# answer=[]
# for i in range(0,how_much_blank):
#     answer.append(input(str(i+1)+". "))
#     if is_correct(answer[i],flat_list[which_numbers[i]]):
#         print("Correct!!!")
#         score+=1
#     else:
#         print("Wrong! It should be: "+flat_list[which_numbers[i]])

# print("Your score: "+str(score))

# print("Original: \n"+' '.join(flat_list))

