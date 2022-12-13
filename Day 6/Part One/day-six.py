with open("day-six-data.txt") as in_list:
    print("Day Six!")
    f_s = in_list.readline() # full string
    
    for i in range(3, len(f_s)):
        full_list = [f_s[i - 3], f_s[i - 2], f_s[i - 1], f_s[i]]
        if (len(set(full_list)) == len(full_list)):
            print(f'Your final string: {full_list[0]}{full_list[1]}{full_list[2]}{full_list[3]}')
            print(f'The first message begins at character #{i+1}')
            break
        else:
            continue