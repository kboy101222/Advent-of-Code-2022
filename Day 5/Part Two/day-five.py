import re  # If you have a problem and choose to solve it using RegEx, you now have 2 problems

import constants as cons
import os


def check_line_type(line):
    if len(re.findall(cons.BOX_LINE, line)) > 0:
        return "BOX_LINE"
    elif len(re.findall(cons.INST_LINE, line)) > 0:
        return "INST_LINE"
    elif len(re.findall(cons.NEW_LINE, line)) > 0:
        return "NEW_LINE"
    elif len(re.findall(cons.NUMS_LINE, line)) > 0:
        return "NUMS_LINE"
    else:
        return "INVALID LINE!!!!"


def get_top_boxes(list, count):
    return list[-count:]

def print_full_stack(list):
    for item in list:
        print(item)

def move_boxes(box_list, count, from_index, to_index):
    boxes_to_move = box_list[from_index -1][-count::]
    print(f'boxes to move: {boxes_to_move}')
    
    for box in boxes_to_move:
        box_list[to_index -1].append(box)
    
    print(f'new pile: {box_list[to_index-1]}')

    items_to_remove = len(box_list[from_index-1]) - count
    box_list[from_index -1] = box_list[from_index-1][:items_to_remove]
    print_full_stack(box_list)
    return box_list

with open("day-5-data.txt") as in_list:
    os.system("cls")
    box_rows = []
    box_cols = []
    instructions = []
    print("┌─────────────────────────────────────┐")
    print("|          Crate Mover 9000           |")
    for line in in_list.readlines():
        line_type = check_line_type(line)

        match line_type:
            case "BOX_LINE":
                line = line.replace("\n", "")
                print("├".ljust(38,"─"), end="┤\n")
                print(f'| {line.replace(" ", " ")} '.ljust(38, " "), end="|\n")
                box_list = re.findall(cons.BOXES, line)
                box_rows.append([])
                for i in box_list:
                    box_rows[-1].append(i[0])
            case "NUMS_LINE":
                continue
            case "NEW_LINE":
                continue
            case "INST_LINE":
                inst_nums = re.findall(cons.INST_NUMS, line)
                print(inst_nums)
                if len(inst_nums) == 4:
                    inst_nums = [inst_nums[0] + inst_nums[1], inst_nums[2], inst_nums[3]]
                instructions.append(inst_nums)
            case _:
                print("INVALID LINE!")

    print("├─────────────────────────────────────┤")
    print("| [1] [2] [3] [4] [5] [6] [7] [8] [9] |")
    print("├─────────────────────────────────────┤")
    print(f'| There are {len(box_rows[0])} columns'.ljust(38, " "), end="|\n")
    print("└─────────────────────────────────────┘")
    for i in range(0, len(box_rows[0])):
        box_cols.insert(i, [])

    for row in box_rows:
        c_index = 0

        for box in row:
            if not (box == "   "):
                box_cols[c_index].insert(0, box)
            c_index += 1
    
    for inst in instructions:
        
        count = int(inst[0])
        from_pile = int(inst[1])
        to_pile = int(inst[2])

        inst_text = f'| [instruction] move {count} from {from_pile} to {to_pile} |'
        top_bar = "┌".ljust(len(inst_text)-1, "─")
        top_bar += "┬".ljust(150 - len(top_bar), "─")

        bottom_bar = "├".ljust(len(inst_text)-1, "─")
        bottom_bar += "┘".ljust(150 - len(bottom_bar), " ")
        print(top_bar , end="┐\n")
        print(inst_text.ljust(150, " "), end="|\n")
        print(bottom_bar , end="|\n")

        box_cols = move_boxes(box_cols, count, from_pile, to_pile)

    final_letters = ""
    print("Final solution:")
    for col in box_cols:
        final_letters += col[-1].replace("[", "").replace("]","")
        for box in col:
            print(box, end=" ")
        print("")

    print(f'\nfinal letters: {final_letters}')