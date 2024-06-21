from random import randint #nag import ko og randint from random kay randint man ang gamiton

player = input("FOLD OR UNFOLD? ").upper() #nangayo og player input nga ang data type kay string then gi convert into upper case ang player input
print(f"Player: {player}") #gi print ang player input gamit f-string

C2 = "FOLD" if randint(1, 2) == 1 else "UNFOLD" #randomize ang pag generate og result sa c2, tapos e print ang fold if 1 then unfold if 2
print(f"C2: {C2}") #gi print ang result sa c2

C3 = "FOLD" if randint(1, 2) == 1 else "UNFOLD" #randomize ang pag generate og result sa c3, tapos e print ang fold if 1 then unfold if 2
print(f"C3: {C3}") #gi print ang result sa c3

if player == C2 == C3: # nag condition ta nga kung same ang result sa player, c2, ug c3
    print("DRAW") # e print ang iyahang output kung nag meet ang condition
elif player == C2 and player != C3: #nag elif condition ko kung same ang result sa player og c2 pero dili same sa c3
    print("C3 wins") #e print ang iyahang output kung nag meet ang condition
elif player != C2 and player == C3: # nag elif condition kung dili same og result si user og c2 pero same si user og c3
    print("C2 wins") #e print ang iyahang output kung nag meet ang condition
else: #else condition kay ang tig salo sa mga condition nga wala na meet
    print("User wins") #e print ang iyahang output sa wala na meet nga mga condition