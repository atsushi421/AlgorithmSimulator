import random
import math



#teはエントリーノード。aは学習率。gは割引率。nは反復回数。　＜使用例＞q_sa,s_list = ql(NUM_OF_NODE, node, edge, pred, succ, exit, ranku, 0, 1.0, 0.8, 1000000)
def ql(num_of_node, node, edge, pred, succ, exit, ranku, en, a, g, n):

	count = 0  #何エピソード学習したか


	# 行動価値関数の初期化
	q_sa = [[0 for j in range(num_of_node)] for i in range(num_of_node)]


	# ↓報酬決め--------------------------------------------------------

	#報酬はランク値とする
	reward = []  #reward[i]　→　ノードTiを選択した時の報酬
	for i in range(num_of_node):
		reward.append(ranku[i])

	# ↑---------------------------------------------------------------



	# ↓このループが1エピソード-------------------------------------------------------------------------------------------------------------------------
	for episode in range(n):
	
		# ↓初期設定------------------------------------------------------------------------------------------------------------------------
		current_state = en  #現在の状態はエントリーノード

		executed_nodes = []  #現在までに実行済みのノードの集合
		executed_nodes.append(en)  #エントリーノードは実行済みとする

		wait_nodes = []  #次に実行可能なノードの集合
		#エントリーノードの後続ノードは実行可能
		for succ_n in succ[en]:
			wait_nodes.append(succ_n)

		finish_flag = 0  #1ステップで行動価値関数の更新が0の時+1する。現在の状態が出口ノードになった際に、finish_flag == (num_of_node - 1)であれば、学習終了。
		# ↑-------------------------------------------------------------------------------------------------------------------------------


		# ↓このループが1時間ステップ-------------------------------------------------------------------------------------------------------------

		for k in range(num_of_node - 1):  #すべてのタスクを処理しなければならないので、ノード数-1分回す。　→　エントリーノードは処理済み

			# ↓行動の決定------------------------------------------
			#wait_nodesの中でランダムなノードを選択
			selected_node = random.choice(wait_nodes)
			# ↑---------------------------------------------------


			# ↓状態の観測------------------------------------------------------------
			wait_nodes.remove(selected_node)  #選んだノードを待ちノードから削除
			executed_nodes.append(selected_node)  #選んだノードを実行した
			before_state = current_state  #現在の状態だったノードは、1つ前のノードになる
			current_state = selected_node  #現在の状態が選んだノードになる
			rw = reward[selected_node]  #得た報酬はrw

			#現在の状態の後続ノードがlegalであれば、wait_nodesに加える
			for succ_n in succ[current_state]:

				if(succ_n in wait_nodes):  #すでにそのノードがwait_nodesに入っていたら
					continue  #そのノードはスキップ

				legal_flag = 1  #DAGの依存関係を満たしているかどうか
				for pred_n in pred[succ_n]:  #後続ノードの前任ノードをすべて見る
					if(pred_n not in executed_nodes):  #後続ノードの前任ノードのうち、1つでも実行済みで無かったら
						legal_flag = 0
						break  #そのノードはDAGの依存関係を満たしていない

				if(legal_flag == 1):
					wait_nodes.append(succ_n)  #legalなので、wait_nodesに加える


			# ↓遷移後の状態から見て、行動価値が最大の行動と、その行動価値を観測---------
			max_q_value = 0  #現在の状態における行動価値の最大値を格納
			max_value_action = 0  #行動価値が最大のノード

			for wait_n in wait_nodes:
				if(q_sa[current_state][wait_n] >= max_q_value):
					max_q_value = q_sa[current_state][wait_n]  #行動価値の最大値を更新
					max_value_action = wait_n
			# ↑--------------------------------------------------------------
			# ↑--------------------------------------------------------------------


			# ↓行動価値関数の更新----------------------------------------------------
			tmp = q_sa[before_state][selected_node]  #更新前の値を保持
			q_sa[before_state][selected_node] = q_sa[before_state][selected_node] + a * (rw + g * q_sa[current_state][max_value_action] - q_sa[before_state][selected_node])
			# ↑--------------------------------------------------------------------


			# ~~~~~~~~~~~~~~~~~1時間ステップ終了~~~~~~~~~~~~~~~~~~~~


			# 行動価値関数が更新されなかったら、finish_flagに1を足す
			print(abs(tmp - q_sa[before_state][selected_node]))
			if(abs(tmp - q_sa[before_state][selected_node]) < 0.1):
				finish_flag = finish_flag + 1


		# ↑-------------------------------------------------------------------------------------------------------------------------------


		# ~~~~~~~~~~~~~~~~~~1エピソード終了~~~~~~~~~~~~~~~~~~~~


		count = count + 1
		if((count % 300000) == 0):
			print(count)


		#学習終了の判定
		if(finish_flag == (num_of_node - 1)):
			break


	# ↑-----------------------------------------------------------------------------------------------------------------------------------------


	print('反復回数 = %d' % count)




	# ↓スケジューリングリストを得る----------------------------------------------------------------------------------------------

	# ↓初期設定------------------------------------------------------------------------------------------------------------------------
	current_state = en  #現在の状態はエントリーノード

	executed_nodes = []  #現在までに実行済みのノードの集合
	executed_nodes.append(en)  #エントリーノードは実行済みとする

	wait_nodes = []  #次に実行可能なノードの集合
	#エントリーノードの後続ノードは実行可能
	for succ_n in succ[en]:
		wait_nodes.append(succ_n)
	# ↑-------------------------------------------------------------------------------------------------------------------------------


	# 行動価値の最大値の行動を選び続ける
	for k in range(num_of_node - 1):  #すべてのタスクを処理しなければならないので、ノード数-1分回す。

		# ↓現在の状態から見て、行動価値が最大の行動を選択------------------------------
		max_q_value = 0  #現在の状態における行動価値の最大値を格納
		max_value_action = 0  #行動価値が最大のノード

		for wait_n in wait_nodes:
			if(q_sa[current_state][wait_n] >= max_q_value):
				max_q_value = q_sa[current_state][wait_n]  #行動価値の最大値を更新
				max_value_action = wait_n

		selected_node = max_value_action
		# ↑--------------------------------------------------------------------


		# ↓状態の観測------------------------------------------------------------
		wait_nodes.remove(max_value_action)  #選んだノードを待ちノードから削除
		executed_nodes.append(max_value_action)  #選んだノードを実行した
		current_state = max_value_action  #現在の状態が選んだノードになる


		#選んだノードの後続ノードがlegalであれば、wait_nodesに加える
		for succ_n in succ[selected_node]:

			if(succ_n in wait_nodes):  #すでにそのノードがwait_nodesに入っていたら
				continue  #そのノードはスキップ

			legal_flag = 1  #DAGの依存関係を満たしているかどうか
			for pred_n in pred[succ_n]:  #後続ノードの前任ノードをすべて見る
				if(pred_n not in executed_nodes):  #後続ノードの前任ノードのうち、1つでも実行済みで無かったら
					legal_flag = 0
					break  #そのノードはDAGの依存関係を満たしていない

			if(legal_flag == 1):
				wait_nodes.append(succ_n)  #legalなので、wait_nodesに加える
		# ↑----------------------------------------------------------------------


	s_list = executed_nodes  #スケジューリングリストを得る

	# ↑-----------------------------------------------------------------------------------------------------------------




	return q_sa, s_list