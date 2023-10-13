'''
Created on 2023/10/13

@author: t21cs051
'''
import random

# じゃんけんの手を表す定数
ROCK = 0
SCISSORS = 1
PAPER = 2

# 手の名前を取得する関数
def get_hand_name(hand):
    if hand == ROCK:
        return "グー"
    elif hand == SCISSORS:
        return "チョキ"
    elif hand == PAPER:
        return "パー"

# 勝敗の手を判定する関数
def judge_winner_hand(player_hands):
    unique_hands = set(player_hands)
    
    if len(unique_hands) == 1:
        return None
    elif len(unique_hands) == 3:
        return None
    else:
        if ROCK in unique_hands and SCISSORS in unique_hands:
            return ROCK
        elif SCISSORS in unique_hands and PAPER in unique_hands:
            return SCISSORS
        else:
            return PAPER

def get_player_name(winner):
    winner = []
    if(list is None):
        winner.append("引き分け")
    for i in winner:
        if(i == 0):
            winner.append("A")
        if(i == 1):
            winner.append("B")
        if(i == 1):
            winner.append("C")

# 3人じゃんけんゲームをシミュレートする関数
def play_rock_paper_scissors_3players():
    player_a = random.randint(0, 2)
    player_b = random.randint(0, 2)
    player_c = random.randint(0, 2)
    
    win_hand = judge_winner_hand([player_a, player_b, player_c])
    result = [i for i in [player_a, player_b, player_c] if i == win_hand]
    result = get_player_name(result)
    hand_a = get_hand_name(player_a)
    hand_b = get_hand_name(player_b)
    hand_c = get_hand_name(player_c)
    
    print(f"Aの手：{hand_a}, Bの手：{hand_b}, Cの手：{hand_c} → {result}")

if __name__ == '__main__':
    # 3人じゃんけんゲームを実行
    play_rock_paper_scissors_3players()
    
    