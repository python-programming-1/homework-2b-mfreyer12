import random

player_score = 0
computer_score = 0
passed_name = False
while True:
    if not passed_name:
        print('make a move! (r/p/s)')
        player_roll = input()
        if player_roll.lower() not in ('r','s','p'):
            continue
    passed_name = True
    if passed_name:
        random_roll = ''
        for num in range(1):
            random_roll = random.randint(1,3)
            #print(roll)
        hand = ''
        if random_roll == 3:
            computer_roll = 's'
        elif random_roll == 2:
            computer_roll = 'r'
        else: computer_roll = 'p'

        print(computer_roll)

        #player_roll = ''
        #computer_roll = ''
        def results(computer_roll):
            if player_roll == 'p':
                if computer_roll == 'r':
                    return 'you win'
                elif computer_roll == 's':
                    return 'you lose'
                elif computer_roll == 'p':
                    return 'we tie'
            elif player_roll == 'r':
                if computer_roll == 's':
                    return 'you win'
                elif computer_roll == 'p':
                    return 'you lose'
                elif computer_roll == 'r':
                    return 'we tie'
            elif player_roll == 's':
                if computer_roll == 'p':
                    return 'you win'
                elif computer_roll == 'r':
                    return 'you lose'
                elif computer_roll == 's':
                    return 'we tie'
        outcome = results(computer_roll)
        print(outcome)

        #outcome = 'you win'
        if outcome == 'you win':
            player_score = player_score + 1
        elif outcome == 'you lose':
            computer_score = computer_score + 1
        print('player ' + str(player_score) + ' / computer ' + str(computer_score))
        while True:
            print('Would you like to play again? (y/n)')
            continue_playing = input()
            if continue_playing.lower() not in ('y','n'):
                print('please chose y or n')
                continue
            elif continue_playing.lower() == 'y':
                is_no = False
                passed_name = False
                break
            elif continue_playing.lower() == 'n':
                print('thank you for playing, goodbye')
                exit(0)


