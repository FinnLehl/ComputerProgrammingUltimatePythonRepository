import random

def make_abc():
    result = ["a", "b", "c"]
    return result
print("make_abc")
print(make_abc())




def equal_edges(items):
    first = items[0]
    last = items[-1]

    if first == last:
        return True
    else:
        return False
print("equal_edges")
print(equal_edges([1, 2, 4, 1]))
print(equal_edges([1, 2, 4, 5]))



def common_edge(list1, list2):
    first1 = list1[0]
    first2 = list2[0]
    last1 = list1[2]
    last2 = list2[2]

    if first1 or last1 == first2 or last2:
        return True
    else:
        return False
    

print("Common_edge")   
print(common_edge([1, 2, 3], [3, 2, 1]))









def all_the_same(list1):
    first = list1[0]
    middle = list1[1]
    last = list1[2]

    if first == middle and first == last:
        return True
    else:
        return False
    
print("all_the_same")
print(all_the_same([5, 5, 5]))
print(all_the_same([1, 2, 3]))






def all_unique(list1):
    first = list1[0]
    middle = list1[1]
    last = list1[2]
    if first != middle and first != last and middle != last:
        return True
    else:
        return False
    
print("all_unique")
print(all_unique([5, 5, 5]))
print(all_unique([6, 7, 9]))



def increasing(list1):
    first = list1[0]
    middle = list1[1]
    last = list1[2]

    if first < middle and middle < last:
        return True
    else:
        return False
    
print("increasing")
print(increasing([1, 2, 3]))



def all_true(list1):
    first = list1[0]
    middle = list1[1]
    last = list1[2]

    if first == True and middle == True and last == True:
        return True 
    else:
        return False
    
print("all_true")
print(all_true([True, True, True]))
print(all_true([False, True, True]))


def mostly_true(list1):
    first = list1[0]
    middle = list1[1]
    last = list1[2]
    if first and middle == True or first and last == True or middle and last == True:
        return True
    else:
        return False
    
print("mostly_true")
print(mostly_true([True, True, False]))
print(mostly_true([False, False, True]))
print(mostly_true([True, True, True]))




print("make_copy")
def make_copy(list1):
      first = list1[0]
      middle = list1[1]
      last = list1[2]
      return [first, middle, last]
original_list = [1, 2, 3]
new_list = make_copy(original_list)
print(original_list)
print(new_list)

print("repeat_thrice")
def repeat_thrice(number):
    return [number, number, number]

print(repeat_thrice([1]))
print(repeat_thrice([6]))


print("make_reversed_copy")

def make_reversed_copy(list1):
    first = list1[0]
    middle = list1[1]
    last = list1[2]
    return [last, middle, first]

original_list1 = [5, 3, 0]
new_list1 = make_reversed_copy(original_list1) 
print(original_list1)
print(new_list1)



def reverse_in_place(list1):
    numbers = list1.copy()
    list1[0] = numbers[2]
    list1[2] = numbers[0]

    return list1

print("reverse_in_place")
original_list2 = [random.randint(1,9), random.randint(1,9), random.randint(1,9)]
print(reverse_in_place(original_list2))
print(original_list2)





