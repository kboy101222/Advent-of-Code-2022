import constants as cons

def check_win(input):
    offense = input[0]
    defense = input[1]
    match offense:
        case cons.OFF_ROCK:
            match defense:
                case cons.DRAW: return cons.VAL_DRAW + cons.VAL_ROCK
                case cons.WIN: return cons.VAL_WIN + cons.VAL_PAPER
                case cons.LOSE: return cons.VAL_LOSS + cons.VAL_SCIS
        case cons.OFF_PAPER:
            match defense:
                case cons.LOSE: return cons.VAL_LOSS + cons.VAL_ROCK
                case cons.DRAW: return cons.VAL_DRAW + cons.VAL_PAPER
                case cons.WIN: return cons.VAL_WIN + cons.VAL_SCIS
        case cons.OFF_SCIS:
            match defense:
                case cons.WIN: return cons.VAL_WIN + cons.VAL_ROCK
                case cons.LOSE: return cons.VAL_LOSS + cons.VAL_PAPER
                case cons.DRAW: return cons.VAL_DRAW + cons.VAL_SCIS

with open("day-two-data.txt") as in_list:
    total_score = 0
    for line in in_list.readlines():
        input = line.strip().split()
        score = check_win(input)
        # match input[1]:
        #     case cons.DEF_ROCK: play_val = cons.VAL_ROCK
        #     case cons.DEF_PAPER: play_val = cons.VAL_PAPER
        #     case cons.DEF_SCIS: play_val = cons.VAL_SCIS
        
        total_score += score
    
    print(f'Total score: {total_score}')
        