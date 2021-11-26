# -*- coding: utf-8 -*-
"""
0J02017 野村勇太
"""
import time
import math

#開始時間
start_time = time.perf_counter()

def get_sosu(n):
    sosu = [True for i in range(n+1)]
    sosu[0] = False
    sosu[1] = False
    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if sosu[i]:
            for j in range(2*i, n+1, i):
                sosu[j] = False
    return sosu

#変数初期化
sosu_sum = 0
#ここのnを変えることで処理範囲を指定、今は200万
n = 2000000

# 素数の列挙、加算
sosu = get_sosu(n)
for s in range(n+1):
    if sosu[s]:
        sosu_sum += s

#終了時間
end_time = time.perf_counter()

# 素数の和
print(n,"以下の素数")
print("合計値：", sosu_sum)

#実行時間出力
elapsed_time = end_time - start_time
print("実行時間（秒）：", elapsed_time)

#画面がすぐ消えるのを防ぐための入力待ち
print("なんか入力して終了")
input()