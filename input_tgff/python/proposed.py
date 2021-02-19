# -*- coding: utf-8 -*-

import time
import math
import copy
import sys
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

#↓-----コマンドライン引数の読み込み----------------------------------------------
args = sys.argv

NUM_OF_CCs = int(args[2])  #クラスタ数
NUM_OF_CORES = int(args[3])  #コア数
SAME_DIFF_RATIO = float(args[4])  #クラスタ内の通信時間とクラスタ外の通信時間の比率
dag_name = args[5]  #実行するDAGのファイル名
factor_edge = float(args[6])  #すべてのedgeに掛ける係数
factor_node = float(args[7])  #すべてのnodeに掛ける係数
#↑-----コマンドライン引数の読み込み----------------------------------------------

NUM_OF_NODE, node, edge, pred, succ, entry, exit = read_dag(dag_name)  #DAGの読み込み

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
        edge[i][j] = int(edge[i][j] * factor_edge)
for i in range(NUM_OF_NODE):
    node[i] = int(node[i] * factor_node)
#↑-----CCRの設定---------------------------------------------------

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

##print('CCR = ', end = '')
CCR = ave_comm / ave_exec
##print(CCR)
#↑-----CCRの計算--------------------------------------------------------

#初期通信時間を保存
edge_original = copy.deepcopy(edge)

#↓-----通信時間を平均にする----------------------------
for i in range(NUM_OF_NODE):
    for j in range(NUM_OF_NODE):
        edge[i][j] = int((edge[i][j] + (edge[i][j] * SAME_DIFF_RATIO)) / 2)
#↑-----通信時間を平均にする----------------------------

#↓(2)-----ranku値の計算-----------------
ranku = [0] * NUM_OF_NODE
for i in range(len(entry)):
	if(entry[i] == 1):
		ranku_calc(i)
#↑(2)----------------------------------

#↓(3)-----強化学習--------------------------------------------------------------------------------------
sl = ql(NUM_OF_NODE, node, pred, succ, entry, exit, ranku, 0, 1.0, 0.8, 10000000000)
#↑(3)-----強化学習--------------------------------------------------------------------------------------

sl_result = copy.deepcopy(sl)

#↓(4)-----メイクスパンの計算----------------------------------------------------
best_result, best_makespan, ave_use = culc_makespan(node, edge_original, pred, succ, NUM_OF_CCs, NUM_OF_CORES, SAME_DIFF_RATIO, sl)

num_of_edge = 0  #DAGのエッジの総数
for i in range(NUM_OF_NODE):
	for j in range(NUM_OF_NODE):
		if(edge[i][j] != 0):  #エッジがあれば
			num_of_edge += 1

change = diff_edge(best_result, pred, NUM_OF_NODE)  #クラスタ外の通信をしている部分を特定
num_change = len(change)  #クラスタ外の通信が必要な回数

#↓-----ログの出力(QLHEFT)----------------------------------------------------------------------------------------------
#書き込むファイルのファイル名を生成
file_name = args[2] + '_' + args[3] + '_' + args[4] + '_' + args[5] + '_' + args[6] + '_' + args[7] + '.txt'

#ログを生成するファイルのパスを生成
log_path = '../result/' + args[1] + '/QLHEFT/log/' + file_name


#↓-----ログファイルの生成--------------------------------------------------------
f = open(log_path, 'w')  #wモードは、ファイルがなければ生成。あれば、内容をすべてクリアして上書き

f.write('↓----実験パラメータ--------------------------------------------------------------------------------------\n')
f.write('NUM_OF_CCs = ')
f.write(args[2] + '\n')
f.write('NUM_OF_COREs = ')
f.write(args[3] + '\n')
f.write('SAME_DIFF_RATIO = ')
f.write(args[4] + '\n')
f.write('DAG_name = ')
f.write(args[5] + '\n')
f.write('factor_edge = ')
f.write(args[6] + '\n')
f.write('factor_node = ')
f.write(args[7] + '\n')
f.write('CCR = ')
f.write(str(CCR) + '\n')
f.write('↑----実験パラメータ--------------------------------------------------------------------------------------\n')

f.write('\n')

f.write('↓----結果-----------------------------------------------------------------------------------------------\n')
f.write('Scheduling_list = ')
f.write(','.join(map(str, sl_result)))
f.write('\n')
f.write('Makespan = ')
f.write(str(best_makespan) + '\n')
f.write('エッジの総数 = ')
f.write(str(num_of_edge) + '\n')
f.write('クラスタ外の通信回数 = ')
f.write(str(num_change) + '\n')
f.write('コアの平均利用率 = ')
f.write(str(ave_use) + '\n')
f.write('↑----結果-----------------------------------------------------------------------------------------------\n')

f.close()  #ファイルを閉じる
#↑-----ログファイルの生成--------------------------------------------------------

#↑-----ログの出力(QLHEFT)----------------------------------------------------------------------------------------------


#↓-----結果の出力(QLHEFT)---------------------------------------------------------------------------------------------
#メイクスパン結果を出力するファイルのパスを指定
if(args[1] == 'change_corenum'):
	result_path = '../result/change_corenum/QLHEFT/' + args[3] + '.txt'

elif(args[1] == 'change_ratio'):
	result_path = '../result/change_ratio/QLHEFT/' + args[4] + '.txt'

elif(args[1] == 'change_tasknum'):
	if('20' in args[5]):
		result_path = '../result/change_tasknum/QLHEFT/20.txt'
	if('50' in args[5]):
		result_path = '../result/change_tasknum/QLHEFT/50.txt'
	if('100' in args[5]):
		result_path = '../result/change_tasknum/QLHEFT/100.txt'
	if('200' in args[5]):
		result_path = '../result/change_tasknum/QLHEFT/200.txt'

elif(args[1] == 'change_CCR'):
	if(factor_edge == 2 and factor_node == 2):
		result_path = '../result/change_CCR/QLHEFT/0.25.txt'
	if(factor_edge == 3 and factor_node == 1):
		result_path = '../result/change_CCR/QLHEFT/0.5.txt'
	if(factor_edge == 1 and factor_node == 0.67):
		result_path = '../result/change_CCR/QLHEFT/1.0.txt'
	if(factor_edge == 5 and factor_node == 0.5):
		result_path = '../result/change_CCR/QLHEFT/2.0.txt'
	if(factor_edge == 5.5 and factor_node == 0.34):
		result_path = '../result/change_CCR/QLHEFT/4.0.txt'

elif(args[1] == 'random'):
	if(args[5] == '100_0' or args[5] == '100_1' or args[5] == '100_2' or args[5] == '100_3' or args[5] == '100_4' or args[5] == '100_5' or args[5] == '100_6' or args[5] == '100_7'):
		result_path = '../result/random/QLHEFT/0-7.txt'
	if(args[5] == '100_8' or args[5] == '100_9' or args[5] == '100_10' or args[5] == '100_11' or args[5] == '100_12' or args[5] == '100_13' or args[5] == '100_14' or args[5] == '100_15'):
		result_path = '../result/random/QLHEFT/8-15.txt'
	if(args[5] == '100_16' or args[5] == '100_17' or args[5] == '100_18' or args[5] == '100_19' or args[5] == '100_20' or args[5] == '100_21' or args[5] == '100_22' or args[5] == '100_23'):
		result_path = '../result/random/QLHEFT/16-23.txt'
	if(args[5] == '100_24' or args[5] == '100_25' or args[5] == '100_26' or args[5] == '100_27' or args[5] == '100_28' or args[5] == '100_29' or args[5] == '100_30' or args[5] == '100_31'):
		result_path = '../result/random/QLHEFT/24-31.txt'
	if(args[5] == '100_32' or args[5] == '100_33' or args[5] == '100_34' or args[5] == '100_35' or args[5] == '100_36' or args[5] == '100_37' or args[5] == '100_38' or args[5] == '100_39'):
		result_path = '../result/random/QLHEFT/32-39.txt'

#↑-----結果ファイルの生成--------------------------------------------------------
f = open(result_path, 'a')

f.write(str(best_makespan) + '\n')
#↑-----結果ファイルの生成--------------------------------------------------------

#↑-----結果の出力(QLHEFT)---------------------------------------------------------------------------------------------


#↓-----ログの出力(Propose)----------------------------------------------------------------------------------------------
#書き込むファイルのファイル名を生成
file_name = args[2] + '_' + args[3] + '_' + args[4] + '_' + args[5] + '_' + args[6] + '_' + args[7] + '.txt'

#ログを生成するファイルのパスを生成
log_path = '../result/' + args[1] + '/Propose/log/' + file_name


#↓-----ログファイルの生成--------------------------------------------------------
f = open(log_path, 'w')  #wモードは、ファイルがなければ生成。あれば、内容をすべてクリアして上書き

f.write('↓----実験パラメータ--------------------------------------------------------------------------------------\n')
f.write('NUM_OF_CCs = ')
f.write(args[2] + '\n')
f.write('NUM_OF_COREs = ')
f.write(args[3] + '\n')
f.write('SAME_DIFF_RATIO = ')
f.write(args[4] + '\n')
f.write('DAG_name = ')
f.write(args[5] + '\n')
f.write('factor_edge = ')
f.write(args[6] + '\n')
f.write('factor_node = ')
f.write(args[7] + '\n')
f.write('CCR = ')
f.write(str(CCR) + '\n')
f.write('↑----実験パラメータ--------------------------------------------------------------------------------------\n')

f.write('\n')

f.write('↓----1回目-----------------------------------------------------------------------------------------------\n')
f.write('Scheduling_list = ')
f.write(','.join(map(str, sl_result)))
f.write('\n')
f.write('Makespan = ')
f.write(str(best_makespan) + '\n')
f.write('エッジの総数 = ')
f.write(str(num_of_edge) + '\n')
f.write('クラスタ外の通信回数 = ')
f.write(str(num_change) + '\n')
f.write('コアの平均利用率 = ')
f.write(str(ave_use) + '\n')
f.write('↑----1回目-----------------------------------------------------------------------------------------------\n')

f.close()  #ファイルを閉じる
#↑-----ログファイルの生成--------------------------------------------------------
#↑-----ログの出力(Propose)----------------------------------------------------------------------------------------------

#↑(4)-----メイクスパンの計算----------------------------------------------------


#↓(5)-----通信時間再計算------------------------------------------------------------------------
#↓-----通信時間を更新----------------------------------------------------------
for i in range(NUM_OF_NODE):
	for j in range(NUM_OF_NODE):
		edge[i][j] = int((edge_original[i][j] * (1 - num_change/num_of_edge)) + (edge_original[i][j] * SAME_DIFF_RATIO * (num_change/num_of_edge)))
#↑-----通信時間を更新----------------------------------------------------------

before_change = num_change  #前回のクラスタ外の通信回数。終了判定に使用する
finish_flag = 0  #終了判定フラグ。3回連続でメイクスパンが短縮されなければ終了
count = 1  #再計算を行った回数。QLHEFTで1回やっている。

#↓-----メイクスパンが最短になるまで繰り返す----------------------------------------------------
while(True):

	count += 1

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
	result, makespan, ave_use = culc_makespan(node, edge_original, pred, succ, NUM_OF_CCs, NUM_OF_CORES, SAME_DIFF_RATIO, sl)
	#↑(6)-----メイクスパンの計算----------------------------------------------------


	#↓-----終了判定--------------------------------------------------------------------------------------------------
	if(best_makespan > makespan):  #より良いメイクスパンを得たら
     
		#↓----bestの更新---------------------------
		best_makespan = makespan
		best_result = copy.deepcopy(result)
		#↑----bestの更新---------------------------
  
		#↓-----通信時間を更新----------------------------------------------------------
		change = diff_edge(best_result, pred, NUM_OF_NODE)  #クラスタ外の通信をしている部分を特定
		num_change = len(change)  #クラスタ外の通信が必要な回数


		#↓-----ログの出力(Propose)----------------------------------------------------------------------------------------------
		#↓-----ログファイルの生成--------------------------------------------------------
		f = open(log_path, 'a')  #2回目以降は追記

		f.write('\n')

		f.write('↓----' + str(count) + '回目-----------------------------------------------------------------------------------------------\n')
		f.write('Scheduling_list = ')
		f.write(','.join(map(str, sl_result)))
		f.write('\n')
		f.write('Makespan = ')
		f.write(str(best_makespan) + '\n')
		f.write('エッジの総数 = ')
		f.write(str(num_of_edge) + '\n')
		f.write('クラスタ外の通信回数 = ')
		f.write(str(num_change) + '\n')
		f.write('コアの平均利用率 = ')
		f.write(str(ave_use) + '\n')
		f.write('↑----' + str(count) + '回目-----------------------------------------------------------------------------------------------\n')

		f.close()  #ファイルを閉じる
		#↑-----ログファイルの生成--------------------------------------------------------
		#↑-----ログの出力(Propose)----------------------------------------------------------------------------------------------
  
		if(before_change == num_change):  #前回とクラスタ外の通信回数が等しいなら
			break  #終了
		else:
			before_change = num_change  #クラスタ外の通信回数を保存

		for i in range(NUM_OF_NODE):
			for j in range(NUM_OF_NODE):
				edge[i][j] = int((edge_original[i][j] * (1 - num_change/num_of_edge)) + (edge_original[i][j] * SAME_DIFF_RATIO * (num_change/num_of_edge)))
		#↑-----通信時間を更新----------------------------------------------------------

		finish_flag = 0  #フラグのリセット

	elif(best_makespan == makespan):  #メイクスパンが同じなら
		#↓----bestの更新---------------------------
		best_makespan = makespan
		best_result = copy.deepcopy(result)
		#↑----bestの更新---------------------------
		
		#↓-----通信時間を更新----------------------------------------------------------
		change = diff_edge(best_result, pred, NUM_OF_NODE)  #クラスタ外の通信をしている部分を特定
		num_change = len(change)  #クラスタ外の通信が必要な回数


		#↓-----ログの出力(Propose)----------------------------------------------------------------------------------------------
		#↓-----ログファイルの生成--------------------------------------------------------
		f = open(log_path, 'a')  #2回目以降は追記

		f.write('\n')

		f.write('↓----' + str(count) + '回目-----------------------------------------------------------------------------------------------\n')
		f.write('Scheduling_list = ')
		f.write(','.join(map(str, sl_result)))
		f.write('\n')
		f.write('Makespan = ')
		f.write(str(best_makespan) + '\n')
		f.write('エッジの総数 = ')
		f.write(str(num_of_edge) + '\n')
		f.write('クラスタ外の通信回数 = ')
		f.write(str(num_change) + '\n')
		f.write('コアの平均利用率 = ')
		f.write(str(ave_use) + '\n')
		f.write('↑----' + str(count) + '回目-----------------------------------------------------------------------------------------------\n')

		f.close()  #ファイルを閉じる
		#↑-----ログファイルの生成--------------------------------------------------------
		#↑-----ログの出力(Propose)----------------------------------------------------------------------------------------------
		
		if(before_change == num_change):  #前回とクラスタ外の通信回数が等しいなら
			break  #終了
		else:
			before_change = num_change  #クラスタ外の通信回数を保存

		for i in range(NUM_OF_NODE):
			for j in range(NUM_OF_NODE):
				edge[i][j] = int((edge_original[i][j] * (1 - num_change/num_of_edge)) + (edge_original[i][j] * SAME_DIFF_RATIO * (num_change/num_of_edge)))

		finish_flag += 1

		if(finish_flag == 5):
			break  #終了

	else:
		#↓-----通信時間を更新----------------------------------------------------------
		change = diff_edge(best_result, pred, NUM_OF_NODE)  #クラスタ外の通信をしている部分を特定
		num_change = len(change)  #クラスタ外の通信が必要な回数
  
		#↓-----ログの出力(Propose)----------------------------------------------------------------------------------------------
		#↓-----ログファイルの生成--------------------------------------------------------
		f = open(log_path, 'a')  #2回目以降は追記

		f.write('\n')

		f.write('↓----' + str(count) + '回目-----------------------------------------------------------------------------------------------\n')
		f.write('Scheduling_list = ')
		f.write(','.join(map(str, sl_result)))
		f.write('\n')
		f.write('Makespan = ')
		f.write(str(best_makespan) + '\n')
		f.write('エッジの総数 = ')
		f.write(str(num_of_edge) + '\n')
		f.write('クラスタ外の通信回数 = ')
		f.write(str(num_change) + '\n')
		f.write('コアの平均利用率 = ')
		f.write(str(ave_use) + '\n')
		f.write('↑----' + str(count) + '回目-----------------------------------------------------------------------------------------------\n')

		f.close()  #ファイルを閉じる
		#↑-----ログファイルの生成--------------------------------------------------------
		#↑-----ログの出力(Propose)----------------------------------------------------------------------------------------------
  
		if(before_change == num_change):  #前回とクラスタ外の通信回数が等しいなら
			break  #終了
		else:
			before_change = num_change  #クラスタ外の通信回数を保存

		for i in range(NUM_OF_NODE):
			for j in range(NUM_OF_NODE):
				edge[i][j] = int((edge_original[i][j] * (1 - num_change/num_of_edge)) + (edge_original[i][j] * SAME_DIFF_RATIO * (num_change/num_of_edge)))
		#↑-----通信時間を更新----------------------------------------------------------

		finish_flag += 1

		if(finish_flag == 5):
			break  #終了
	#↑-----終了判定--------------------------------------------------------------------------------------------------

	#print("-------------------------------------再計算中-----------------------------------------")
#↑-----メイクスパンが最短になるまで繰り返す----------------------------------------------------

#↑(5)-----通信時間再計算------------------------------------------------------------------------

#↓-----ログの出力(Propose)----------------------------------------------------------------------------------------------
#↓-----ログファイルの生成--------------------------------------------------------
f = open(log_path, 'a')  #2回目以降は追記

f.write('\n')

f.write('↓----最終結果-----------------------------------------------------------------------------------------------\n')
f.write('Scheduling_list = ')
f.write(','.join(map(str, sl_result)))
f.write('\n')
f.write('Makespan = ')
f.write(str(best_makespan) + '\n')
f.write('エッジの総数 = ')
f.write(str(num_of_edge) + '\n')
f.write('クラスタ外の通信回数 = ')
f.write(str(num_change) + '\n')
f.write('コアの平均利用率 = ')
f.write(str(ave_use) + '\n')
f.write('↑----最終結果-----------------------------------------------------------------------------------------------\n')

f.close()  #ファイルを閉じる
#↑-----ログファイルの生成--------------------------------------------------------
#↑-----ログの出力(Propose)----------------------------------------------------------------------------------------------

#↓-----結果の出力(Propose)---------------------------------------------------------------------------------------------
#メイクスパン結果を出力するファイルのパスを指定
if(args[1] == 'change_corenum'):
	result_path = '../result/change_corenum/Propose/' + args[3] + '.txt'

elif(args[1] == 'change_ratio'):
	result_path = '../result/change_ratio/Propose/' + args[4] + '.txt'

elif(args[1] == 'change_tasknum'):
	if('20' in args[5]):
		result_path = '../result/change_tasknum/Propose/20.txt'
	if('50' in args[5]):
		result_path = '../result/change_tasknum/Propose/50.txt'
	if('100' in args[5]):
		result_path = '../result/change_tasknum/Propose/100.txt'
	if('200' in args[5]):
		result_path = '../result/change_tasknum/Propose/200.txt'

elif(args[1] == 'change_CCR'):
	if(factor_edge == 2 and factor_node == 2):
		result_path = '../result/change_CCR/Propose/0.25.txt'
	if(factor_edge == 3 and factor_node == 1):
		result_path = '../result/change_CCR/Propose/0.5.txt'
	if(factor_edge == 1 and factor_node == 0.67):
		result_path = '../result/change_CCR/Propose/1.0.txt'
	if(factor_edge == 5 and factor_node == 0.5):
		result_path = '../result/change_CCR/Propose/2.0.txt'
	if(factor_edge == 5.5 and factor_node == 0.34):
		result_path = '../result/change_CCR/Propose/4.0.txt'

elif(args[1] == 'random'):
	if(args[5] == '100_0' or args[5] == '100_1' or args[5] == '100_2' or args[5] == '100_3' or args[5] == '100_4' or args[5] == '100_5' or args[5] == '100_6' or args[5] == '100_7'):
		result_path = '../result/random/Propose/0-7.txt'
	if(args[5] == '100_8' or args[5] == '100_9' or args[5] == '100_10' or args[5] == '100_11' or args[5] == '100_12' or args[5] == '100_13' or args[5] == '100_14' or args[5] == '100_15'):
		result_path = '../result/random/Propose/8-15.txt'
	if(args[5] == '100_16' or args[5] == '100_17' or args[5] == '100_18' or args[5] == '100_19' or args[5] == '100_20' or args[5] == '100_21' or args[5] == '100_22' or args[5] == '100_23'):
		result_path = '../result/random/Propose/16-23.txt'
	if(args[5] == '100_24' or args[5] == '100_25' or args[5] == '100_26' or args[5] == '100_27' or args[5] == '100_28' or args[5] == '100_29' or args[5] == '100_30' or args[5] == '100_31'):
		result_path = '../result/random/Propose/24-31.txt'
	if(args[5] == '100_32' or args[5] == '100_33' or args[5] == '100_34' or args[5] == '100_35' or args[5] == '100_36' or args[5] == '100_37' or args[5] == '100_38' or args[5] == '100_39'):
		result_path = '../result/random/Propose/32-39.txt'

#↑-----結果ファイルの生成--------------------------------------------------------
f = open(result_path, 'a')

f.write(str(best_makespan) + '\n')
#↑-----結果ファイルの生成--------------------------------------------------------
#↑-----結果の出力(Propose)---------------------------------------------------------------------------------------------

#↑(1)------------------------------------------------------------------------------------------------------------