# -*- coding: utf-8 -*-


import os
import random


file = open('./test.tgffopt', 'r')  # ファイルを開く

lines = file.readlines()  # 1行ずつのデータのリスト


seed = random.randint(0, 1000)  # seedを0~1000でランダムで決める
lines[0] = 'seed ' + str(seed) + '\n'

start_node = random.randint(1, 5)  # start_nodeを1~5でランダムで決める
lines[1] = 'start_node ' + str(start_node) + ' 1' + '\n'

max_in = random.randint(3, 5)  # ノードへの最大入力数を1~5でランダムで決める
max_out = random.randint(2, 3)  # ノードからの最大出力数を2~5でランダムで決める
lines[2] = 'task_degree ' + str(max_in) + ' ' + str(max_out) + '\n'

file.close()


file = open('./test.tgffopt', 'w')

file.writelines(lines)

file.close()


#↓-----ログに生成パラメータを書き込み---------------------

file_name = 'generate_log.txt'

#ログを生成するファイルのパスを生成
log_path = './' + file_name


#↓-----ログファイルの生成--------------------------------------------------------
f = open(log_path, 'a')

f.write('seed=' + str(seed) + ', start_node=' + str(start_node) + ', max_in=' + str(max_in) + ', max_out=' + str(max_out) + '\n')

f.close()  #ファイルを閉じる
#↑-----ログに生成パラメータを書き込み---------------------