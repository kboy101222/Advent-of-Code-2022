import constants as cons

def check_win(input):
    offense = input[0]
    defense = input[1]
    match offense:
        case cons.OFF_ROCK:
            match defense:
                case cons.DEF_ROCK: return cons.VAL_DRAW
                case cons.DEF_PAPER: return cons.VAL_WIN
                case cons.DEF_SCIS: return cons.VAL_LOSS
        case cons.OFF_PAPER:
            match defense:
                case cons.DEF_ROCK: return cons.VAL_LOSS
                case cons.DEF_PAPER: return cons.VAL_DRAW
                case cons.DEF_SCIS: return cons.VAL_WIN
        case cons.OFF_SCIS:
            match defense:
                case cons.DEF_ROCK: return cons.VAL_WIN
                case cons.DEF_PAPER: return cons.VAL_LOSS
                case cons.DEF_SCIS: return cons.VAL_DRAW

with open("day-two-data.txt") as in_list:
    total_score = 0
    for line in in_list.readlines():
        input = line.strip().split()
        score = check_win(input)
        match input[1]:
            case cons.DEF_ROCK: play_val = cons.VAL_ROCK
            case cons.DEF_PAPER: play_val = cons.VAL_PAPER
            case cons.DEF_SCIS: play_val = cons.VAL_SCIS
        
        total_score += score + play_val
    
    print(f'Total score: {total_score}')
        