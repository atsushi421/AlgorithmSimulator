#～受け取ったタスクの前任タスクがすべて実行済みだったら、1を返す。そうでなければ0を返す。～
def legal(executed_tasks, pred, num_t):
    for pred_t in pred[num_t]:
        if(pred_t not in executed_tasks):
            return False
    
    return True


#～コアにタスクを割り当てる。
# sが何番目のクラスタか、kが何番目のコアか,～
def allocate_core(node, will_allocate_time, s, k, num_t, target, result, sl):
    target[s][k][0] = num_t
    target[s][k][1] = node[num_t]
        
    result[num_t][0] = s
    result[num_t][1] = k
    result[num_t][2] = will_allocate_time
    result[num_t][3] = will_allocate_time + node[num_t]  #実行終了時間は、「割り当てられた時刻+処理時間」
        
    if(len(sl) != 0):
        del sl[0]


#～s秒、矛盾が無いように時間を進める～
def advance_time(num_of_cc, num_of_core, current_time, target, result, executed_tasks):
    for i in range(num_of_cc):
        for j in range(num_of_core):
                if(target[i][j][0] != -1 and current_time >= result[target[i][j][0]][2]):  #そのコアにタスクが割り当てられていて、開始時刻になったら
                    target[i][j][1] -= 1  #1秒分処理
                    if(target[i][j][1] == 0):
                        executed_tasks.append(target[i][j][0])  #そのタスクを実行済みにする
                        target[i][j][0] = -1  #コアをアイドル状態にする
                        target[i][j][1] = 0  #初期状態に戻す


#-----～スケジューリングリストを受け取って、メイクスパンを計算する。
#-------クラスタの数と1クラスタ何コアで構成されているかは指定できる。
#-------割り当ての結果も返す。
#-------sはクラスタ数、kは1クラスタを構成するコア数、slはスケジューリングリスト～
def culc_makespan(node, edge, pred, succ, s, k, ratio, sl):
    
    #↓-----～初期設定～----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    node = node
    edge = edge
    pred = pred
    succ = succ
    NUM_OF_CCs = s  #クラスタ数
    NUM_OF_CORES = k  #1クラスタを構成するコア数
    NUM_OF_TASKS = len(node)  #タスク数
    SAME_DIFF_RATIO = ratio  #クラスタ内の通信時間とクラスタ外の通信時間の比率
    sl = sl
    
    #- 割り当てる対象のコア構成を示す3次元リスト。
    #- [どのクラスタ][どのコア][コア情報　→　実行中のタスク(アイドル状態の時は-1), 実行中のタスクの残り実行時間]
    target = [[[-1, 0] for i in range(NUM_OF_CORES)] for j in range(NUM_OF_CCs)]
    
    #- スケジューリング結果。
    #- [どのクラスタ, どのコア, 実行開始時間, 実行終了時間]
    #- 添え字がタスク番号を表す
    result = [[-1, -1, -1, -1] for i in range(len(sl))]
    
    executed_tasks = []  #実行済みのタスクの集合
    #↑----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    #↓(1)-----～タスク割り当て～-------------------------------------------------------------------------------------------------------------------------------------------------------
    t = 0  #現在の時刻

    while(len(executed_tasks) != NUM_OF_TASKS):  #すべてのタスクの実行が終了したら、ループ終了
        
        if(len(sl) != 0):
            head = sl[0]  #headはスケジューリングリストの先頭
        else:  #スケジューリングリストが空の場合
            #↓-----すべてのタスクが終了するまで時間を進める---------------------------------------
            advance_time(NUM_OF_CCs, NUM_OF_CORES, t, target, result, executed_tasks)
            t += 1
            continue
            #↑-----すべてのタスクが終了するまで時間を進める---------------------------------------
        
        #↓(2)------headがlegal-------------------------------------------------------------------------------------------------
        if(legal(executed_tasks, pred, head)):
            
            earliest_CC = -1  #EFTが最小となるクラスタ番号
            earliest_core = -1  #EFTが最小となるコア番号
            min_eft = 99999999999  #EFTの最小値
        
            #↓-----全部のクラスタを総当たり---------------------------------------------------------------------------------
            for i in range(NUM_OF_CCs):  #headをクラスタiに割り当てたとして、EFTを計算する
                eft = 0  #クラスタiにおけるeft
                
                #↓(3)-----クラスタiに空きがあるか調べる-----------------------------------------------
                vacant_flag = -1  #クラスタiに空きがあれば、1。そうでなければ-1
                
                for j in range(NUM_OF_CORES):
                    if(target[i][j][0] == -1):  #クラスタiに空きがある
                        vacant_flag = 1
                        will_allocate_core = j  #このクラスタの中で、おそらく割り当てるコア
                        break
                #↑(3)-------------------------------------------------------------------------------
                
                #↓(6)-----クラスタiに空きがない場合、最速のATをしらべる--------------------------------
                if(vacant_flag == -1):
                    earliest_at = 999999999
                    
                    for j in range(NUM_OF_CORES):
                        if(earliest_at > result[target[i][j][0]][3]):
                            earliest_at = result[target[i][j][0]][3]
                            will_allocate_core = j  #このクラスタの中で、おそらく割り当てるコア
                #↑(6)-------------------------------------------------------------------------------
                
                #↓(4)-----headの前任タスクをすべて調べる----------------------------------------------
                for pred_head in pred[head]:
                    
                    pred_cc = result[pred_head][0]  #pred_headが割り当てられているクラスタ番号
                    pred_finish = result[pred_head][3]  #pred_headの実行終了時刻
                    
                    #↓(5)-----pred_headが割り当てられているクラスタ番号とiが同じ--------------
                    if(pred_cc == i):
                        communication_cost = edge[pred_head][head]  #通信時間はクラスタ内の通信時間
                        
                        if(vacant_flag == 1):  #クラスタiに空きがある
                            if(t > pred_finish + communication_cost):
                                consider_time = t
                            else:
                                consider_time = pred_finish + communication_cost
                            
                            if(eft < consider_time):
                                eft = consider_time
                        
                        else:  #クラスタiに空きがない
                            #2つの時間点で遅い方を採用する
                            if(earliest_at > (pred_finish + communication_cost)):
                                consider_time = earliest_at
                            else:
                                consider_time = pred_finish + communication_cost
                        
                            if(eft < consider_time):
                                eft = consider_time
                    #↑(5)------------------------------------------------------------------
                    
                    #↓(7)-----pred_headが割り当てられているクラスタ番号とiが違う-------------
                    else:
                        communication_cost = edge[pred_head][head] * SAME_DIFF_RATIO  #通信時間はクラスタ外の通信時間
                        
                        if(vacant_flag == 1):  #クラスタiに空きがある
                            if(t > pred_finish + communication_cost):
                                consider_time = t
                            else:
                                consider_time = pred_finish + communication_cost
                            
                            if(eft < consider_time):
                                eft = consider_time
                        
                        else:  #クラスタiに空きがない
                            #2つの時間点で遅い方を採用する
                            if(earliest_at > (pred_finish + communication_cost)):
                                consider_time = earliest_at
                            else:
                                consider_time = pred_finish + communication_cost
                            
                            if(eft < consider_time):
                                eft = consider_time
                    #↑(7)------------------------------------------------------------------
                        
                #↑(4)-------------------------------------------------------------------------------

                #↓(8)-----min_eftが更新されたか調べる-------------------------------
                if(min_eft > eft):
                    min_eft = eft
                    earliest_CC = i
                    earliest_core = will_allocate_core
                #↑(8)----------------------------------------------------------
            
            #↑-----全部のクラスタを総当たり---------------------------------------------------------------------------------
            
            #↓(9)-----割り当てる対象のコアがアイドル状態になるまで待つ---------------------------
            while(target[earliest_CC][earliest_core][0] != -1):
                advance_time(NUM_OF_CCs, NUM_OF_CORES, t, target, result, executed_tasks)
                t += 1
            #↑(9)-----割り当てる対象のコアがアイドル状態になるまで待つ---------------------------

            allocate_core(node, min_eft, earliest_CC, earliest_core, head, target, result, sl)  #headを割り当てる
            
        #↑(2)------------------------------------------------------------------------------------------------------------------
            
        else:  #headがlegalでなはいなら
            #スケジューリングリストの先頭が実行可能になるまで待つ
            advance_time(NUM_OF_CCs, NUM_OF_CORES, t, target, result, executed_tasks)
            t += 1

    #↑(1)-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    makespan = t
    #↓-----結果の出力-------------------------------
    print('result = ', end = '')
    for i in result:
        print(i)
    print('makespan = ', end = '')
    print(makespan)
    #↑-----結果の出力-------------------------------
    
    return result, makespan