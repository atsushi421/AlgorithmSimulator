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
#↓-----初期設定----------------------------------------------------------------------------------------------
NUM_OF_NODE, node, edge, pred, succ, entry, exit = read_dag()  #DAGの読み込み

#↓-----CCRの設定---------------------------------------------------
for i in range(NUM_OF_NODE):
    for j in range(NUM_OF_NODE):
        edge[i][j] = int(edge[i][j] * 4.8)
for i in range(NUM_OF_NODE):
    node[i] = int(node[i] / 1.163)
#↑-----CCRの設定---------------------------------------------------

NUM_OF_CCs = 1  #クラスタ数
NUM_OF_CORES = 1  #コア数
SAME_DIFF_RATIO = 3  #クラスタ内の通信時間とクラスタ外の通信時間の比率

#初期通信時間を保存
edge_original = copy.deepcopy(edge)
#↑-----初期設定----------------------------------------------------------------------------------------------

#↓-----CCRの計算--------------------------------------------------------
num_of_edge = 0  #DAGのエッジの総数
sum_comm = 0
for i in range(NUM_OF_NODE):
	for j in range(NUM_OF_NODE):
		if(edge[i][j] != 0):  #エッジがあれば
			sum_comm += edge[i][j]
			num_of_edge += 1

ave_comm = sum_comm / num_of_edge  #平均通信時間

sum_exec = 0
for i in range(NUM_OF_NODE):
    sum_exec += node[i]

ave_exec = sum_exec / NUM_OF_NODE  #平均実行時間

print('CCR = ', end = '')
CCR = ave_comm / ave_exec
print(CCR)
#↑-----CCRの計算--------------------------------------------------------

#↓(2)-----ranku値の計算-----------------
#↓-----通信時間を平均にする----------------------------
for i in range(NUM_OF_NODE):
    for j in range(NUM_OF_NODE):
        edge[i][j] = int((edge[i][j] + (edge[i][j] * SAME_DIFF_RATIO)) / 2)
#↑-----通信時間を平均にする----------------------------

ranku = [0] * NUM_OF_NODE
for i in range(len(entry)):
	if(entry[i] == 1):
		ranku_calc(i)
#↑(2)----------------------------------


#↓-----rank値の昇順にソートしたものがスケジューリングリスト-------------------------
temp = []
for i in range(len(ranku)):
    temp.append([i, ranku[i]])

temp = sorted(temp, reverse=True, key=lambda x: x[1])  #昇順にソート

sl = []
for i in range(len(temp)):
    sl.append(temp[i][0])

#↓-----結果の出力---------------------
print('sl = ', end = '')
print(sl)
#↑-----結果の出力---------------------

#↓(4)-----メイクスパンの計算----------------------------------------------------
best_result, best_makespan = culc_makespan(node, edge_original, pred, succ, NUM_OF_CCs, NUM_OF_CORES, SAME_DIFF_RATIO, sl)
#↑(4)-----メイクスパンの計算----------------------------------------------------

#↑(1)------------------------------------------------------------------------------------------------------------