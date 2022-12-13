import sys


tree_list = []

with open("day-eight-data.txt") as in_list:
    c_index = 0
    for line in in_list.readlines():
        line = line.replace("\n", "")
        tree_list.append([])
        for char in line:
            tree_list[c_index].append(int(char))
        print(tree_list[c_index])
        c_index += 1

vert_index = 0
horiz_index = 0
highest_scenic_score = -sys.maxsize - 1
while vert_index < len(tree_list):
    print(f'Vertical Index: {vert_index}')
    print(f'Horizontal Index: {horiz_index}')
    print(f'Current Tree Height: {tree_list[vert_index][horiz_index]}')
    
    # check left
    left_scenic_score = 0
    if (horiz_index > 0):
        for i in range(horiz_index-1, -1, -1):
            if (tree_list[vert_index][i] >= tree_list[vert_index][horiz_index]):
                left_scenic_score += 1
                break
            else:
                left_scenic_score += 1

    # check right
    right_scenic_score = 0
    if (horiz_index < len(tree_list[vert_index]) - 1):
        for i in range(horiz_index+1, len(tree_list[vert_index])):
            if (tree_list[vert_index][i] >= tree_list[vert_index][horiz_index]):
                right_scenic_score += 1
                break
            else:
                right_scenic_score += 1

    # check up
    up_scenic_score = 0
    if (vert_index > 0):
        for i in range(vert_index-1, -1, -1):
            if (tree_list[i][horiz_index] >= tree_list[vert_index][horiz_index]):
                up_scenic_score += 1
                break
            else:
                up_scenic_score += 1

    # check down
    down_scenic_score = 0
    if (vert_index < len(tree_list) - 1):
        for i in range(vert_index+1, len(tree_list)):
            if (tree_list[i][horiz_index] >= tree_list[vert_index][horiz_index]):
                down_scenic_score += 1
                break
            else:
                down_scenic_score += 1

    # if (is_visible_left or is_visible_right or is_visible_up or is_visible_down):
    #     tree_count += 1
    #     print("Tree at: " + str(vert_index) + ", " + str(horiz_index) + " is visible")
        # print(f'is_visible_left: {is_visible_left}')
        # print(f'is_visible_right: {is_visible_right}')
        # print(f'is_visible_up: {is_visible_up}')
        # print(f'is_visible_down: {is_visible_down}')

    total_scenic_score = left_scenic_score * right_scenic_score * up_scenic_score * down_scenic_score
    print(f'left_scenic_score: {left_scenic_score}')
    print(f'right_scenic_score: {right_scenic_score}')
    print(f'up_scenic_score: {up_scenic_score}')
    print(f'down_scenic_score: {down_scenic_score}')

    print(f'total_scenic_score: {total_scenic_score}')
    if (total_scenic_score > highest_scenic_score):
        highest_scenic_score = total_scenic_score
        print(f'highest_scenic_score: {highest_scenic_score}')

    if (horiz_index == len(tree_list[vert_index]) - 1):
        horiz_index = 0
        vert_index += 1
    else:
        horiz_index += 1

    print("----------")

print(f'highest_scenic_score: {highest_scenic_score}')