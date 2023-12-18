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
print(reader)
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
    gradelevel = int(gradelevel)
    if gradelevel==9:
        total_f = total_f + 1
        fresh_avg = fresh_avg + percent
    elif gradelevel==10:
        total_s = total_s + 1
        soph_avg = soph_avg + percent
    elif gradelevel==11:
        total_j = total_j + 1
        junior_avg = junior_avg + percent
    elif gradelevel ==12:
        total_se = total_se + 1
        senior_avg = senior_avg + percent

print(fresh_avg, total_f)
fresh_avg =fresh_avg / total_f
soph_avg = soph_avg / total_s
junior_avg = junior_avg / total_j
senior_avg = senior_avg / total_se
print(fresh_avg)
print(soph_avg)
print(junior_avg)
print(senior_avg)
f.close()

f = open("../data/1000-largest-us-cities.json", "r")
all_cities = json.load(f)

cities_in_ks = []
for city in all_cities:
    if city["state"] == "Kansas":
        cities_in_ks.append(city["city"])

print("the cities in Kansas are", cities_in_ks)

f.close()

        


   
f = open("../data/1000-largest-us-cities.json", "r")
all_cities = json.load(f) 
longest_name = ""
previous = ""
for city in all_cities:
        if len(city["city"]) > len(previous):
            longest_name = city["city"]
            previous = city["city"]
print(longest_name)



f.close()

f = open("../data/1000-largest-us-cities.json", "r")
all_cities = json.load(f) 


cities = []
lat = all_cities[0]["latitude"]
previous_most_lat = all_cities[0]["latitude"]
low_lat = all_cities[0]["latitude"]
previous_least_lat = all_cities[0]["latitude"]
long = all_cities[0]["longitude"]
longest_long = all_cities[0]["longitude"]
small_long =all_cities[0]["longitude"]
smallest_long = all_cities[0]["longitude"]
for city in all_cities:
    if city["latitude"] > previous_most_lat:
        lat = city["latitude"]
        previous_most_lat = city["latitude"]
        cities = lat
    if city["latitude"] < previous_least_lat:
        low_lat = city["latitude"]
        previous_least_lat = city["latitude"]
        cities = low_lat
    if city["longitude"] > longest_long:
        long = city["longitude"]
        longest_long = city["longitude"]
        cities = long
    if city["longitude"] < smallest_long:
        small_long = city["longitude"]
        smallest_long = city["longitude"]
        cities = small_long
print(lat, low_lat, long, small_long)







    

    

        






