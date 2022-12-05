def split_ids(id_code): # format: #-#,#-#
    splits = id_code.split(",")
    full_split = []
    for i in splits:
        split_2 = i.split("-")
        work_range = [] 
        work_range.append(int(split_2[0]))
        work_range.append(int(split_2[1]))
        full_split.append(work_range)
    return full_split

print(split_ids("1-6,4-5"))

with open("day-four-data.txt") as in_list:
    total_cont = 0
    for item in in_list.readlines():
        split_range = split_ids(item)
        
        if not (split_range[0][0] < split_range[1][0] or split_range[0][1] > split_range[1][1]):
            print(f'matched range: {split_range}')
            total_cont += 1
        elif not (split_range[1][0] < split_range[0][0] or split_range[1][1] > split_range[0][1]):
            print(f'matched range: {split_range}')
            total_cont += 1
    
    print(total_cont)