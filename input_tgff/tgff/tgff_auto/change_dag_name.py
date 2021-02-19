# -*- coding: utf-8 -*-


import os


num_fifty = 0
num_one_hundred = 0
num_two_hundred = 0


for i in range(200):

	dag_path = './random_dag/random_' + str(i) + '.tgff'
	eps_path = './random_dag/random_' + str(i) + '.eps'

	# ファイルを開く
	tgff_file = open(dag_path, "r")


	num_of_node = 0

	# 1行ずつ読み込む
	for line in tgff_file:

		# 空行はスキップ
		if(line == '\n'):
			continue
		
		# 文字列の半角スペース・タブ区切りで区切ったリストを取得
		line_list = line.split()

		# TASKの情報の取得
		if(line_list[0] == 'TASK'):
			num_of_node += 1

	# ファイルを閉じる
	tgff_file.close()


	if(num_of_node < 60):
		dag_rename_path = './random_dag/50/50_' + str(num_fifty) + '.tgff'
		eps_rename_path = './random_dag/50/50_' + str(num_fifty) + '.eps'
		os.rename(dag_path, dag_rename_path)
		os.rename(eps_path, eps_rename_path)
		num_fifty += 1
	elif(num_of_node < 110):
		dag_rename_path = './random_dag/100/100_' + str(num_one_hundred) + '.tgff'
		eps_rename_path = './random_dag/100/100_' + str(num_one_hundred) + '.eps'
		os.rename(dag_path, dag_rename_path)
		os.rename(eps_path, eps_rename_path)
		num_one_hundred += 1
	else:
		dag_rename_path = './random_dag/200/200_' + str(num_two_hundred) + '.tgff'
		eps_rename_path = './random_dag/200/200_' + str(num_two_hundred) + '.eps'
		os.rename(dag_path, dag_rename_path)
		os.rename(eps_path, eps_rename_path)
		num_two_hundred += 1