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


#changeを受け取り、クラスタ外の通信が必要な部分の通信時間(edge)を更新
def recalc(result, edge_original, edge, ratio, change):
    edge = copy.deepcopy(edge_original)  #まずもとに戻す

    for change_edge in change:
        edge[change_edge[0]][change_edge[1]] = edge_original[change_edge[0]][change_edge[1]] * ratio
    
    return edge


#スケジューリング結果から、クラスタ外の通信が必要な部分の通信時間(edge)を更新
def diff_edge(result, edge_original, edge, pred, num_of_node):
    change = []
    
    for task in range(num_of_node):  #スケジューリングリストを全探索
        for pred_task in pred[task]:  #taskの前任タスクを全探索
            if(result[pred_task][0] != result[task][0]):  #前任タスクと割り当てられたクラスタが異なる場合
                change.append([pred_task, task])

    return change


#↓(1)-----開始---------------------------------------------------------------------------------------------------
#↓-----初期設定----------------------------------------------------------------------------------------------
NUM_OF_NODE, node, edge, pred, succ, entry, exit = read_dag()  #DAGの読み込み

#↓-----実行時間を一部だけ大きくする----------------------------------------
for i in range(NUM_OF_NODE):
    if(i % 5 == 0):
        node[i] = int(node[i] * 10)
#↑-----実行時間を一部だけ大きくする----------------------------------------

"""
num_of_edge = 0  #DAGのエッジの総数
for i in range(NUM_OF_NODE):
	for j in range(NUM_OF_NODE):
		if(edge[i][j] != 0):  #エッジがあれば
			num_of_edge += 1

			if(num_of_edge % 5 == 0):
				edge[i][j] = int(edge[i][j] * 5)
"""

#↓-----CCRの設定---------------------------------------------------
for i in range(NUM_OF_NODE):
    for j in range(NUM_OF_NODE):
        edge[i][j] = int(edge[i][j] * 1.5)
for i in range(NUM_OF_NODE):
    node[i] = int(node[i] * 3)
#↑-----CCRの設定---------------------------------------------------

NUM_OF_CCs = 2  #クラスタ数
NUM_OF_CORES = 3  #コア数
SAME_DIFF_RATIO = 3  #クラスタ内の通信時間とクラスタ外の通信時間の比率

#初期通信時間を保存
edge_original = copy.deepcopy(edge)
#↑-----初期設定----------------------------------------------------------------------------------------------


#↓(2)-----ranku値の計算-----------------------------------------------------
#↓-----通信時間を平均にする----------------------------
for i in range(NUM_OF_NODE):
    for j in range(NUM_OF_NODE):
        edge[i][j] = int((edge[i][j] + (edge[i][j] * SAME_DIFF_RATIO)) / 2)
#↑-----通信時間を平均にする----------------------------

ranku = [0] * NUM_OF_NODE
for i in range(len(entry)):
	if(entry[i] == 1):
		ranku_calc(i)
#↑(2)----------------------------------------------------------------------


#↓(3)-----強化学習--------------------------------------------------------------------------------------
sl = ql(NUM_OF_NODE, node, pred, succ, entry, exit, ranku, 0, 1.0, 0.8, 10000000000)
#↑(3)-----強化学習--------------------------------------------------------------------------------------


#↓(4)-----メイクスパンの計算----------------------------------------------------
best_result, best_makespan = culc_makespan(node, edge_original, pred, succ, NUM_OF_CCs, NUM_OF_CORES, SAME_DIFF_RATIO, sl)
#↑(4)-----メイクスパンの計算----------------------------------------------------
#↑(1)------------------------------------------------------------------------------------------------------------