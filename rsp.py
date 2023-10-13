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

# 勝敗を判定する関数
def judge_winner(player_a, player_b):
    if player_a == player_b:
        return "引き分け"
    elif (player_a == ROCK and player_b == SCISSORS) or \
         (player_a == SCISSORS and player_b == PAPER) or \
         (player_a == PAPER and player_b == ROCK):
        return "Aの勝ち"
    else:
        return "Bの勝ち"

# じゃんけんゲームをシミュレートする関数
def play_rock_paper_scissors():
    player_a = random.randint(0, 2)
    player_b = random.randint(0, 2)
    
    result = judge_winner(player_a, player_b)
    
    hand_a = get_hand_name(player_a)
    hand_b = get_hand_name(player_b)
    
    print(f"Aの手：{hand_a} v.s. Bの手：{hand_b} → {result}")


if __name__ == '__main__':
    # じゃんけんゲームを実行
    play_rock_paper_scissors()

