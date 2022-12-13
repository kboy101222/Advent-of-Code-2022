with open("day-six-data.txt") as in_list:
    print("Day Six!")
    f_s = in_list.readline() # full string
    
    for i in range(13, len(f_s)):
        full_list = [f_s[i - 13], f_s[i - 12], f_s[i - 11], f_s[i - 10], f_s[i - 9], f_s[i - 8], f_s[i - 7], f_s[i - 6], f_s[i - 5], f_s[i - 4], f_s[i - 3], f_s[i - 2], f_s[i - 1], f_s[i]]
        if (len(set(full_list)) == len(full_list)):
            print(f'The first message begins at character #{i+1}')
            break
        else:
            continue