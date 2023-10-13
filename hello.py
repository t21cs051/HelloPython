'''
Created on 2023/10/13

@author: t21cs051
'''


def quick_sort(data):
    # 要素数が１以下の場合、分割できないのでそのまま返す
    if len(data) <= 1:
        return data
    
    # リストの先頭要素をピボットとして取り出す
    pivot = data.pop(0)
    
    # ピボットより小さいものを取り出したリストを作る
    left = [i for i in data if i <= pivot]
    # ピボットより大きいものを取り出したリストを作る
    right = [i for i in data if i > pivot]
    
    # それぞれのリストについて再帰的にソートを行う
    left = quick_sort(left)
    right = quick_sort(right)
    
    return left + [pivot] + right
