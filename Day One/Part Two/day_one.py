# Find the top 3 instead

with open('day_one_input.txt') as in_list:
    top_elves = []
    full_data = []
    current_count = 0
    lines_read = 0

    for line in in_list.readlines():
        full_data.append(line.strip())
        lines_read += 1
        if line == "\n":
            print("reached end of an elf")
            print(f'Current count: {current_count}')
            top_elves.append(current_count)
            current_count = 0
            print("---")
        else:
            mod_line = line.strip()
            print(f"Adding to an elf: {mod_line}")
            current_count += int(mod_line)

    print("reached end of document")
    print(f'Current count: {current_count}')
    top_elves.append(current_count)
    current_count = 0
    print("---")

    print(f"Lines read: {lines_read}")
    # print(f'Full data: {full_data}')
    top_elves.sort(reverse=True)
    print(f'Fully sorted list: {top_elves}')
    print(f'Top 3 totals: {top_elves[:3]}')

    highest_elf = 0
    for i in top_elves[:3]:
        highest_elf += i

    print(f'Highest count: {highest_elf}')
