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
NUM_OF_NODE, node, edge, pred, succ, exit = read_dag()  #DAGの読み込み

edge_original = copy.deepcopy(edge)  #元の通信時間

#↓(2)-----ranku値の計算-----------------
ranku = [0] * NUM_OF_NODE
ranku_calc(0)
#↑(2)----------------------------------

#↓(3)-----強化学習--------------------------------------------------------------------------------------
q_sa, sl = ql(NUM_OF_NODE, node, edge_original, pred, succ, exit, ranku, 0, 1.0, 0.8, 10000000000)
#↑(3)-----強化学習--------------------------------------------------------------------------------------

#↓(4)-----メイクスパンの計算----------------------------------------------------
best_result, best_makespan = culc_makespan(node, edge_original, pred, succ, 3, 2, 3, sl)

print('makespan_first = ', end = '')
print(best_makespan)
#↑(4)-----メイクスパンの計算----------------------------------------------------

#↓(5)-----通信時間再計算------------------------------------------------------------------------
change = diff_edge(best_result, edge_original, edge, pred, NUM_OF_NODE)  #クラスタ外の通信をしている部分を特定
edge = recalc(best_result, edge_original, edge, 3, change)  #通信時間を再計算

finish_flag = 0

while(True):
	#↓(2)-----ranku値の計算-----------------
	ranku = [0] * NUM_OF_NODE
	ranku_calc(0)
	#↑(2)----------------------------------

	#↓(3)-----強化学習--------------------------------------------------------------------------------------
	q_sa, sl = ql(NUM_OF_NODE, node, edge_original, pred, succ, exit, ranku, 0, 1.0, 0.8, 10000000000)
	#↑(3)-----強化学習--------------------------------------------------------------------------------------

	#↓(6)-----メイクスパンの計算----------------------------------------------------
	result, makespan = culc_makespan(node, edge_original, pred, succ, 3, 2, 3, sl)

	print('makespan = ', end = '')
	print(makespan)
	#↑(6)-----メイクスパンの計算----------------------------------------------------

	if(best_makespan > makespan):  #より良いメイクスパンを得たら
		best_makespan = makespan
		best_result = copy.deepcopy(result)
		change = diff_edge(result, edge_original, edge, pred, NUM_OF_NODE)  #クラスタ外の通信をしている部分を特定
		edge = recalc(result, edge_original, edge, 3, change)  #通信時間を再計算
		finish_flag = 0
	else:
		finish_flag += 1
		if(finish_flag == 5):
			break

	print("-------------------------------------再計算中-----------------------------------------")

#↑(5)-----通信時間再計算------------------------------------------------------------------------

print("終了")
for i in best_result:
    print(i)
print('best_makespan = ', end = '')
print(best_makespan)

#↑(1)------------------------------------------------------------------------------------------------------------