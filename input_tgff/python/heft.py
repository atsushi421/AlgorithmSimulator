import time
import math
import copy
from dag import read_dag
from task_allocation import culc_makespan


#受け取ったノードのranku値を計算する関数。nはノード番号。エントリーノードを渡せばよい。再帰を使うので、この関数は実行するファイル内に無いとダメ
def ranku_calc(n):
	if(exit[n] == 1):  #受け取ったノードが出口ノードであれば
		ranku[n] = node[n]  #ランク値は実行時間と等しい

	else:
		#後任ノードのランク値を計算
		for succ_n in succ[n]:  #後任ノードでループ
			if(ranku[succ_n] != 0):  #すでにランク値が計算されていれば、スキップ
				continue

			ranku_calc(succ_n)  #後任ノードのランク値を再帰で計算

		#後任ノードの中で、 "n～succ_nの通信時間＋succ_nのランク値" が最大になるノードを見つけ、その最大値を保持
		max_sum = 0  #通信時間＋ランク値の最大値を格納

		for succ_n in succ[n]:
			tmp = edge[n][succ_n] + ranku[succ_n]
			if(tmp > max_sum):
				max_sum = tmp

		#ランク値を計算
		ranku[n] = node[n] + max_sum


#↓(1)-----開始---------------------------------------------------------------------------------------------------
NUM_OF_NODE, node, edge, pred, succ, exit = read_dag()  #DAGの読み込み

#↓-----通信時間を平均にする--------------------------------
for i in range(NUM_OF_NODE):
    for j in range(NUM_OF_NODE):
        edge[i][j] = int((edge[i][j] + (edge[i][j] * 3)) / 2)
#↑-----通信時間を平均にする--------------------------------


#↓(2)-----ranku値の計算-----------------
ranku = [0] * NUM_OF_NODE
ranku_calc(0)
#↑(2)----------------------------------

temp = []
for i in range(len(ranku)):
    temp.append([i, ranku[i]])

temp = sorted(temp, reverse=True, key=lambda x: x[1])  #昇順にソート

sl = []
for i in range(len(temp)):
    sl.append(temp[i][0])

print(sl)

#↓(4)-----メイクスパンの計算----------------------------------------------------
best_result, best_makespan = culc_makespan(node, edge, pred, succ, 3, 2, 3, sl)

print('result = ', end = '')
for i in best_result:
    print(i)
print('makespan = ', end = '')
print(best_makespan)
#↑(4)-----メイクスパンの計算----------------------------------------------------

#↑(1)------------------------------------------------------------------------------------------------------------