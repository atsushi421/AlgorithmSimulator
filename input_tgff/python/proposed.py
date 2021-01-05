import time
import math
import copy
from q_learning import ql
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


#スケジューリング結果から、クラスタ外の通信が必要な部分の通信時間(edge)を更新
def diff_edge(result, pred, num_of_node):
    change = []
    
    for task in range(num_of_node):  #スケジューリングリストを全探索
        for pred_task in pred[task]:  #taskの前任タスクを全探索
            if(result[pred_task][0] != result[task][0]):  #前任タスクと割り当てられたクラスタが異なる場合
                change.append([pred_task, task])

    return change


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

NUM_OF_CCs = 3  #クラスタ数
NUM_OF_CORES = 4  #コア数
SAME_DIFF_RATIO = 3  #クラスタ内の通信時間とクラスタ外の通信時間の比率

#初期通信時間を保存
edge_original = copy.deepcopy(edge)
#↑-----初期設定----------------------------------------------------------------------------------------------


#↓(2)-----ranku値の計算-----------------
ranku = [0] * NUM_OF_NODE
for i in range(len(entry)):
	if(entry[i] == 1):
		ranku_calc(i)
#↑(2)----------------------------------


#↓(3)-----強化学習--------------------------------------------------------------------------------------
sl = ql(NUM_OF_NODE, node, pred, succ, entry, exit, ranku, 0, 1.0, 0.8, 10000000000)
#↑(3)-----強化学習--------------------------------------------------------------------------------------


#↓(4)-----メイクスパンの計算----------------------------------------------------
best_result, best_makespan = culc_makespan(node, edge_original, pred, succ, NUM_OF_CCs, NUM_OF_CORES, SAME_DIFF_RATIO, sl)
#↑(4)-----メイクスパンの計算----------------------------------------------------


#↓(5)-----通信時間再計算------------------------------------------------------------------------
#↓-----通信時間を更新----------------------------------------------------------
num_of_edge = 0  #DAGのエッジの総数
for i in range(NUM_OF_NODE):
	for j in range(NUM_OF_NODE):
		if(edge[i][j] != 0):  #エッジがあれば
			num_of_edge += 1

change = diff_edge(best_result, pred, NUM_OF_NODE)  #クラスタ外の通信をしている部分を特定
num_change = len(change)  #クラスタ外の通信が必要な回数

for i in range(NUM_OF_NODE):
	for j in range(NUM_OF_NODE):
		edge[i][j] = int((edge_original[i][j] * (1 - num_change/num_of_edge)) + (edge_original[i][j] * SAME_DIFF_RATIO * (num_change/num_of_edge)))
#↑-----通信時間を更新----------------------------------------------------------

finish_flag = 0

#↓-----メイクスパンが最短になるまで繰り返す----------------------------------------------------
while(True):
	#↓(2)-----ranku値の計算-----------------
	ranku = [0] * NUM_OF_NODE
	for i in range(len(entry)):
		if(entry[i] == 1):
			ranku_calc(i)
	#↑(2)----------------------------------


	#↓(3)-----強化学習--------------------------------------------------------------------------------------
	sl = ql(NUM_OF_NODE, node, pred, succ, entry, exit, ranku, 0, 1.0, 0.8, 10000000000)
	#↑(3)-----強化学習--------------------------------------------------------------------------------------


	#↓(6)-----メイクスパンの計算----------------------------------------------------
	result, makespan = culc_makespan(node, edge_original, pred, succ, NUM_OF_CCs, NUM_OF_CORES, SAME_DIFF_RATIO, sl)
	#↑(6)-----メイクスパンの計算----------------------------------------------------


	#↓-----終了判定--------------------------------------------------------------------------------------------------
	if(best_makespan >= makespan):  #より良いメイクスパンを得たら
		#↓----bestの更新---------------------------
		best_makespan = makespan
		best_result = copy.deepcopy(result)
		#↑----bestの更新---------------------------
  
		#↓-----通信時間を更新----------------------------------------------------------
		change = diff_edge(best_result, pred, NUM_OF_NODE)  #クラスタ外の通信をしている部分を特定
		num_change = len(change)  #クラスタ外の通信が必要な回数

		for i in range(NUM_OF_NODE):
			for j in range(NUM_OF_NODE):
				edge[i][j] = int((edge_original[i][j] * (1 - num_change/num_of_edge)) + (edge_original[i][j] * SAME_DIFF_RATIO * (num_change/num_of_edge)))
		#↑-----通信時間を更新----------------------------------------------------------
  
		finish_flag = 0
	else:
		finish_flag += 1
		if(finish_flag == 1):
			break  #終了
	#↑-----終了判定--------------------------------------------------------------------------------------------------

	print("-------------------------------------再計算中-----------------------------------------")
#↑-----メイクスパンが最短になるまで繰り返す----------------------------------------------------

#↑(5)-----通信時間再計算------------------------------------------------------------------------

#↓-----結果の出力--------------------------------------
print("終了")
for i in best_result:
    print(i)
print('best_makespan = ', end = '')
print(best_makespan)
#↑-----結果の出力--------------------------------------

#↑(1)------------------------------------------------------------------------------------------------------------