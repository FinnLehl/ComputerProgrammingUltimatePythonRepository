import csv
import os
import json
os.chdir(os.path.dirname(os.path.abspath(__file__)))


f = open("../data/4000-most-common-english-words.csv", "r")
words = f.read().split("\n")



            


def find_most_vowels(wordlist):
    most_so_far = ""
    max_vowelcount = 0
    
    for word in wordlist:
        current_vowelcount = 0
        for letter in word:
            if letter== "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
                current_vowelcount = current_vowelcount + 1
        if current_vowelcount > max_vowelcount:
            max_vowelcount = current_vowelcount
            most_so_far = word
    else:
        pass
    return most_so_far

print(find_most_vowels(words))



# def average_word_length(words):
#     totalwords = 0
#     letters = 0
#     avg = 0
#     for word in words:
#         totalwords = totalwords + 1
#         letters = letters + len(word)
#     avg = letters / totalwords
#     return avg

# print(average_word_length(words))

# f.close()


f = open("../data/gradebook_data.csv", "r")
reader = csv.reader(f)
A = 0
B = 0
C = 0
D = 0
F = 0
for row in reader:
    name, gradelevel, percent = row
    percent = int(percent)
    if percent >= 90 and percent <= 100:
        A = A + 1
    elif percent >= 80 and percent <= 90:
        B = B + 1
    elif percent >= 70 and percent <= 80:
        C = C + 1
    elif percent >= 60 and percent <= 70:
        D = D + 1
    elif percent >= 0 and percent <= 60:
        F = F + 1
print(A)
print(B)
print(C)
print(D)
print(F)

f.close()
f = open("../data/gradebook_data.csv", "r")
reader = csv.reader(f)

for row in reader:
    name, gradelevel, percent = row
    percent = int(percent)
    gradelevel = int(gradelevel)
    if gradelevel==12 and percent < 60:
        print(name)
    
f.close()
f = open("../data/gradebook_data.csv", "r")
reader = csv.reader(f)
total_f = 0
total_s =0
total_j = 0
total_se = 0
fresh_avg = 0
soph_avg = 0
junior_avg = 0
senior_avg = 0
for row in reader:
    name, gradelevel, percent = row
    percent = int(percent)
    gradelevel = int(percent)
    if gradelevel==9:
        total_f = total_f + 1
        print(total_f)
        


   
            
        

        






