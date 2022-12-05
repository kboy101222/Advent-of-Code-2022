from collections import Counter

letter_vals = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
temp_letters = []
for letter in letter_vals: temp_letters.append(letter.capitalize())
for letter in temp_letters: letter_vals.append(letter)
# I'm being lazy and generating the list of letters at runtime. I'm sure that won't bite me in the ass.

def get_value(letter):
    return letter_vals.index(letter) + 1

def split_bag(bag):
    slice_list = []
    slice_1 = slice(0,len(bag)//2)
    slice_2 = slice(len(bag)//2, len(bag))
    first_half = bag[slice_1]
    second_half = bag[slice_2]

    new_list_1 = []
    new_list_2 = []

    for letter in first_half:
        if letter not in new_list_1:
            new_list_1.append(letter)
    
    for letter in second_half:
        if letter not in new_list_2:
            new_list_2.append(letter)

    slice_list.append(new_list_1)
    slice_list.append(new_list_2)
    return slice_list

# test_bag = split_bag("DMRhDhdvnjhnPnvPMfdZSGTccGJFjGFFpFpFTbTpTW")
# print(f'test_bag: {test_bag}')
# print(f'test_bag[0]: {test_bag[0]}')
# print(f'test_bag[1]: {test_bag[1]}')

with open("day-three-data.txt") as in_list:
    total_value = 0
    for item in in_list.readlines():
        bag = split_bag(item.strip())
        top_half = Counter(bag[0])
        bottom_half = Counter(bag[1])
        full_bag = top_half + bottom_half
        print(full_bag.most_common())
        
        for pair in full_bag.most_common():
            if (pair[1] > 1):
                value = get_value(pair[0])
                print(f'Adding {value} to total_value')
                total_value += get_value(pair[0])
                print(f'New total: {total_value}')

    print(f'Total Value: {total_value}')