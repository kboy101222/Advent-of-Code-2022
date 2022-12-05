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

def make_range(range_list):
    return range(range_list[0], range_list[1]+1)

with open("day-four-data.txt") as in_list:
    total_cont = 0
    for item in in_list.readlines():
        split_range = split_ids(item)
        
        if (split_range[0][0] in make_range(split_range[1]) or split_range[0][1] in make_range(split_range[1])):
            print(f'matched range: {split_range}')
            total_cont += 1
        elif (split_range[1][0] in make_range(split_range[0]) or split_range[1][1] in make_range(split_range[0])):
            print(f'matched range: {split_range}')
            total_cont += 1
    
    print(total_cont)