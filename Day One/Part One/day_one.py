with open('day_one_input.txt') as in_list:
    highest_elf = 0
    current_count = 0
    lines_read = 0

    for line in in_list.readlines():
        if line == "\n":
            if current_count > highest_elf:
                print(f'current count: {current_count}')
                highest_elf = current_count
                current_count = 0
                print("New highest elf!\nCalories:")
                print(highest_elf)
                print(f'current count: {current_count}')
                print(f'lines read: {lines_read}')
                print("-----")
            else:
                current_count = 0
                lines_read = 0
        else:
            lines_read += 1
            current_count += int(line)
    
    print("Highest count:")
    print(highest_elf)