import time
import math
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





NUM_OF_NODE, node, edge, pred, succ, exit = read_dag()  #DAGの読み込み

#read_dagの結果
print('NUM_OF_NODE = %d' % NUM_OF_NODE)
print('\n')
print('node = ', end = '')
print(node)
print('\n')
print('edge = ', end = '')
for i in edge:
	print(i)
print('\n')
print('pred = ', end = '')
print(pred)
print('\n')
print('succ = ', end = '')
print(succ)
print('\n')
print('exit = ', end = '')
print(exit)
print('\n')



#ranku値の計算
ranku = [0] * NUM_OF_NODE
ranku_calc(0)

print('ranku = ', end = '')
print(ranku)
print('\n')


#----------------------------------------------------
start_time = time.perf_counter()  #時間計測開始
#----------------------------------------------------


q_sa, s_list = ql(NUM_OF_NODE, node, edge, pred, succ, exit, ranku, 0, 1.0, 0.8, 10000000000)


#----------------------------------------------------------------
execution_time = time.perf_counter() - start_time  #時間計測終了
print('計算にかかった時間 = %f' % execution_time)
#----------------------------------------------------------------

"""
print('q_sa = ', end = '')
for i in q_sa:
	for j in i:
		print(math.floor(j), end='')
		print(', ', end='')
	print('\n')
"""

print('s_list = ', end = '')
print(s_list)

result = culc_makespan(node, edge, pred, succ, 1, 3, 3, s_list)

for i in result:
    print(i)