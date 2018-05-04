#!/usr/bin/python3.6

def play_pick_stone(play1, play2, total_stone, max_pick):
    print("\nplayer: ",play1," vs ",play2)
    print("There are",total_stone,"stones, max pick",max_pick,"at once\n")
    current_player = 1
    while (total_stone > 0):
        legal_num = False

        # Switch players
        if current_player == 1:    
            player_text = "Player "+str(current_player)+":"+play1+ \
                            ", choose a number between 1~"+ \
                            str(max_pick)+": "
        else:
            player_text = "Player "+str(current_player)+":"+play2+ \
                            ", choose a number between 1~"+ \
                            str(max_pick)+": "  

        while legal_num == False:
            num = int(input(player_text))
            if 1 <= num and num <= max_pick:
                legal_num = True
            else:
                print("Not legal. Try again.")
        # Update pick
        total_stone = total_stone - num

        if (total_stone < num):
            max_pick = total_stone

        if total_stone == 0:
            if current_player == 1:
                tmp=play1
            else:
                tmp=play2
            print("Player",current_player,":",tmp,"lose!")
            return
        elif total_stone<0:
            print("wrong pick, choose between 1 to",(total_stone+num))
            total_stone = total_stone+num
        else:
            print("There are now",total_stone,\
            "stones remaining.")
        # Switch players
        if current_player == 1:    
            current_player=2
        else:
            current_player=1
            
print("pick game: last pick player is the loser")
play1 = input("name of player1:")
play2 = input("name of player2:")
total_stone = int(input("how many total stone:"))
max_pick = int(input("how many stone pick at once:"))

play_pick_stone(play1,play2,total_stone, max_pick)


