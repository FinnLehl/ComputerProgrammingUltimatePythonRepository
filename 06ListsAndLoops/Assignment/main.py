def count_failing_grades(grades):
    count = 0
    for grade in grades:
        if grade < 60:
            count = count + 1
    return count
        
print("count_failing_grades")
inputlist = [80, 70, 52, 40, 60]
returnvalue = count_failing_grades(inputlist)
print(returnvalue)


def count_act_scores(scores):
    count = 0
    for score in scores:
        if score <= 36 and score >= 1:
            count = count + 1
    return count

print("cout_act_scores")
inputlist = [1, 26, 12, 9, 90]
returnValue = count_act_scores(inputlist)
print(returnValue)



def number_sum(numbers):
    total = 0
    for number in numbers:
       total = total + number
    return total

print("number_sum")
inputlist=[3, 7, 5]
returnValue = number_sum(inputlist)
print(returnValue)


def average_act_score(acts):
    count = 0
    total = 0
    for act in acts:
        if act <= 36 and act >= 1:
           total = total + act
           count = count + 1
    if count == 0:
        return None
    return total / count

print("average_act_score")
inputlist=[1, 26, 90, 34, 18, 5]
returnValue = average_act_score(inputlist)
print(returnValue)



def all_true(booleans):
    for boolean in booleans:
        if boolean not in [True]:
            return False
    return True
print("all_true")
print(all_true([True, True, True, True]))
print(all_true([False, True, False]))




def any_true(booleans):
    for boolean in booleans:
        if boolean in [True]:
            return True
    return False
print("any_true")
print(any_true([True, False, False]))
print(any_true([False, False, False]))


def has_vowel(letters):
    for letter in letters:
        if letter in ["a", "e", "i", "o", "u"]:
            return True
    return False


print("has_vowel")
print(has_vowel(["a", "s", "g", "c"]))
print(has_vowel(["d", "s", "c", "q"]))



def mostly_true(Booleans):
    count = 0
    countF = 0
    for Boolean in Booleans:
        if Boolean == True:
            count += 1
        if Boolean == False:
            countF += 1
    if count > countF:
        return True
    return False
print("mostly_true")
print(mostly_true([True, True, False]))
print(mostly_true([False, False, True]))




def all_the_same(nums):
    first = nums[0]
    for num in nums:
        if num != first:
            return False
    return True


    # repetition = False
    # for num in nums:
    #     if num[0] == num[1] and num[0] == num[2] and num[0] ==
    #     if num == nums[0]:
    #         return True
    #     else:
    #         return False   
print("all_the_same")
print(all_the_same([5, 5, 5, 5]))
print(all_the_same([6, 2, 4, 5])) 




def sum_with_skips(nums):
    total = 0
    ignoring = False

    for num in nums:
        if ignoring == True:
            if num == -1:
                ignoring = False
        elif ignoring == False:
            if num == -1:
                ignoring = True
            else:
                total = total + num
        print(num, ignoring)
    return total

print("sum_with_skips")
print(sum_with_skips([2, 1, -1, 4, -1, 9]))





def increasing(nums):
    previous = nums[0]-1
    for num in nums:
        if num <= previous:
            return False
        previous = num
    return True


print("increasing")
print(increasing([1, 2, 3, 4,]))
print(increasing([1, 2, 3, 2, 4, 5]))
print(increasing([5, 5, 6, 8, 9]))






def is_incrementing(nums):
    previous = nums[0]-1
    for num in nums:
        if num != previous + 1:
            return False
        previous = num
    return True



print(is_incrementing([1, 2, 3, 4]))
print(is_incrementing([1, 3, 5]))







def has_adjacent_repeat(nums):
    previous = nums[0]-1
    for num in nums:
        if num == previous:
            return True
        previous = num
    return False