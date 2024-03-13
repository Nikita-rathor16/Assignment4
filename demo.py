# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         return f"{self.name} says hello!"
# a=Animal("honw")
# print(a.speak())

#  Converting an Integer into Decimals
# import decimal
# integer = 10
# print(decimal.Decimal(integer))
# print(type(decimal.Decimal(integer)))
# n=input()
# print(n[::-1]) 
# #Counting Vowels in a Given Word
# vowel = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
# word=input()
# count=0
# for characters in word:
#     if characters in vowel:
#         count+=1
# print(count)

# Counting Consonants in a Given Word
# vowel = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
# w=input()
# count=0
# for chara in w:
#     if chara not in vowel:
#         count+=1
# print(count)

#Counting the Number of Occurances of a Character in a String
# word=input()
# occurene=input()
# count=0
# for letter in word:
#     if letter==occurene:       
#         count+=1
# print(count)
#Comparing Two Strings for Anagrams
# str1=input()
# str2=input()
# str1 = list(str1.upper())
# str2=list(str2.upper())
# str1.sort(),str2.sort()
# if(str1==str2):
#     print("jfr")
# print("fa")
