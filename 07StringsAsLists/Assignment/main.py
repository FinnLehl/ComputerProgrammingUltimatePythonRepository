def is_alliteration(words1, words2):
    if words1[0] == words2[0]:
            return True
    return False
print("is_alliteration")
print(is_alliteration("haha", "haha"))


def count_vowels(letters):
    total = 0
    for letter in letters:
        if letter in "aeiou":
            total = total + 1
    return total

def count_numbers(nums):
    total = 0 
    for num in nums:
        if num in "1234567890":
            total = total + 1
    return total



def count_target_letters(words, letter):
    total = 0
    for word in words:
        if letter in word:
            total = total + 1




    return total


print("alphabetical order")
def in_alphabetical_order(letters):
    previous = letters[0]
    for letter in letters:
        if letter < previous :
            return False
        previous = letter
    return True

print(in_alphabetical_order("hi"))
print(in_alphabetical_order("ok"))
print(in_alphabetical_order("bin"))
print(in_alphabetical_order("low"))
print(in_alphabetical_order("say"))




print("alternate_case")

def alternate_case(word):
    result = ""
    next_upper = True
    for letter in word:
        if next_upper == True:
            result = result + letter.upper()
            next_upper = False
        elif next_upper == False:
            result = result + letter
            next_upper = True
    return result
            #print(words)


print(alternate_case("hello"))











print("remove_Vowels")
def remove_vowels(letters):
    result = ""
    for letter in letters:
        if letter in "aeiou":
            pass
        else:
            result = result + letter
    return result

print(remove_vowels("hello"))


print("cammelCase")

def to_camel_case(word):
    result = ""
    next_upper = True
    for letter in word:
        if next_upper == True:
            result = result + letter.upper()
            next_upper = False
        elif letter == " ":
            pass
            next_upper = True
            
        else:
            result = result + letter
    return result

print(to_camel_case("a very useful pot"))






print("snake_case")

def to_snake_case(word):
    result = ""
    for letter in word:
        if letter == " ":
           pass
           result = result + "_"
        else:
            result = result + letter
    return result
        

print(to_snake_case("hello there"))








def without_duplicates(numbers):
    result = []
    previous = numbers[0]-1
    for number in numbers:
        if number == previous:
            pass
            previous = number
        else:
            result = result + number
    return result


print(without_duplicates([10, 2, 3, 3, 4]))