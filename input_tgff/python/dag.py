# tgffファイルを読み込んで、DAGを生成する。＜使用例＞NUM_OF_NODE, node, edge, pred, succ, exit = read_dag()
def read_dag():

	# ↓まずTYPEと実行時間の対応を取得----------------------------------------------------

	# ファイルを開く
	tgff_file = open("../tgff/task_50.tgff", "r")


	type_cost = [] #TYPEと実行時間の対応関係の配列
	read_flag = 0 #PE5の情報だけを読み込むためのフラグ
	info_flag = 0 #余計な部分を読み込まないためのフラグ

	# 1行ずつ読み込む
	for line in tgff_file:

		# 空行はスキップ
		if(line == '\n'):
			continue

		# 文字列の半角スペース・タブ区切りで区切ったリストを取得
		line_list = line.split()

		if(len(line_list) >= 2):
			# 読み込む範囲を限定
			if(line_list[0] == '@PE' and line_list[1] == '5'):
				read_flag = 1

			if(line_list[1] == 'type' and line_list[2] == 'exec_time'):
				info_flag = 1
				continue

			# TYPEの情報取得
			if(read_flag == 1 and info_flag == 1):
				type_cost.append(int(float(line_list[1]))) #TYPEに対応する実行時間をint型で格納

		elif(line_list[0] == '}'):
			read_flag = 0
			info_flag = 0


	# ファイルを閉じる
	tgff_file.close()

	# ↑----------------------------------------------------------------------------
	
	
	# ↓TASKの情報を取得-----------------------------------------------------

	# ファイルを開く
	tgff_file = open("../tgff/task_50.tgff", "r")


	node = [] #各タスクの実行時間を格納

	# 1行ずつ読み込む
	for line in tgff_file:

		# 空行はスキップ
		if(line == '\n'):
			continue
		
		# 文字列の半角スペース・タブ区切りで区切ったリストを取得
		line_list = line.split()

		# TASKの情報の取得
		if(line_list[0] == 'TASK'):
			node.append(type_cost[int(line_list[3])]) #line_list[3]がTYPEなので、それに対応する実行時間を格納


	# ファイルを閉じる
	tgff_file.close()

	# ↑-----------------------------------------------------------------------------


	# タスク数を取得
	num_of_node = len(node)


	# ↓ARCの情報を取得----------------------------------------------------------------

	# ファイルを開く
	tgff_file = open("../tgff/task_50.tgff", "r")


	edge = [[0 for j in range(num_of_node)] for i in range(num_of_node)] #edgeの配列はタスク数(len(node))×タスク数の2次元配列

	# 1行ずつ読み込む
	for line in tgff_file:

		# 空行はスキップ
		if(line == '\n'):
			continue
		
		# 文字列の半角スペース・タブ区切りで区切ったリストを取得
		line_list = line.split()

		# ARC情報の取得
		if(line_list[0] == 'ARC'):
			from_t = int(line_list[3][3:]) #エッジを出すタスク
			to_t = int(line_list[5][3:]) #エッジの先のタスク
			comm_cost = int(type_cost[int(line_list[7])]) #TYPEに書かれている時間を通信時間とする

			edge[from_t][to_t] = comm_cost


	# ファイルを閉じる
	tgff_file.close()

	# ↑-----------------------------------------------------------------------------



	# ↓predリストを求める-------------------------------------------------------------------
	pred = [[] for i in range(num_of_node)]  #pred[i]　→　ノードTiにエッジを入力しているノードのリスト　（例）[4, 6, 7. 9]

	for in_node in range(num_of_node):
		for out_node in range(num_of_node):
			if(edge[in_node][out_node] != 0):  #エッジがあれば
				pred[out_node].append(in_node)
	# ↑-------------------------------------------------------------------------------

	# ↓succリストを求める-------------------------------------------------------------------
	succ = [[] for i in range(num_of_node)]  #succ[i]　→　ノードTiからエッジを出力しているノードのリスト　（例）[4, 6, 7. 9]

	for in_node in range(num_of_node):
		for out_node in range(num_of_node):
			if(edge[in_node][out_node] != 0):  #エッジがあれば
				succ[in_node].append(out_node)
	# ↑-------------------------------------------------------------------------------

	# ↓exitタスクを求める---------------------------------------------------------------
	exit = [0] * num_of_node

	for i in range(num_of_node):
		if(len(succ[i]) == 0):
			exit[i] = 1
	#↑------------------------------------------------------------------------------


	return num_of_node, node, edge, pred, succ, exit