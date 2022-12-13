import time


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
tree_count = 0
while vert_index < len(tree_list):
    # Handle all Edge Cases for the trees
    # pun intended
    if (horiz_index == 0): # First column
        tree_count += 1
        horiz_index += 1
        # print("First column")
    elif (vert_index == 0 and horiz_index != len(tree_list[vert_index]) - 1): # First row, not last column
        tree_count += 1
        horiz_index += 1
        # print("First row, not last column")
    elif (horiz_index == len(tree_list[vert_index]) - 1): # Last column
        tree_count += 1
        horiz_index = 0
        vert_index += 1
        # print("Last column")
    elif (vert_index == len(tree_list) - 1 and horiz_index != len(tree_list[vert_index])): # Last row, not last column
        tree_count += 1
        horiz_index += 1
        # print("Last row, not last column")
    elif (vert_index == len(tree_list) - 1 and horiz_index != len(tree_list[vert_index])): # Last row, last column
        tree_count += 1
        horiz_index = 0
        vert_index += 1
        # print("Last row, last column")
    else:
        # handle inner trees
        # check left
        is_visible_left = True
        for i in range(horiz_index-1, -1, -1):
            if (tree_list[vert_index][i] >= tree_list[vert_index][horiz_index]):
                is_visible_left = False
                break
        
        # check right
        is_visible_right = True
        for i in range(horiz_index+1, len(tree_list[vert_index])):
            if (tree_list[vert_index][i] >= tree_list[vert_index][horiz_index]):
                is_visible_right = False

        # check up
        is_visible_up = True
        for i in range(vert_index-1, -1, -1):
            if (tree_list[i][horiz_index] >= tree_list[vert_index][horiz_index]):
                is_visible_up = False

        # check down
        is_visible_down = True
        for i in range(vert_index+1, len(tree_list)):
            if (tree_list[i][horiz_index] >= tree_list[vert_index][horiz_index]):
                is_visible_down = False

        if (is_visible_left or is_visible_right or is_visible_up or is_visible_down):
            tree_count += 1
            print("Tree at: " + str(vert_index) + ", " + str(horiz_index) + " is visible")
            # print(f'is_visible_left: {is_visible_left}')
            # print(f'is_visible_right: {is_visible_right}')
            # print(f'is_visible_up: {is_visible_up}')
            # print(f'is_visible_down: {is_visible_down}')
            
        horiz_index += 1

print(tree_count)