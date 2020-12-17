#～受け取ったタスクの前任タスクがすべて実行済みだったら、1を返す。そうでなければ0を返す。～
def legal(executed_tasks, pred, num_t):
    for pred_t in pred[num_t]:
        if(pred_t not in executed_tasks):
            return False
    
    return True

#～受け取ったタスクが割り当てられているコアを構成するクラスタ内に空いているコアがある場合、そのクラスタの番号を返す。そうでなければ-1を返す。～
def can_same(num_t, result, target):
    
    allocated_CC = result[num_t][0]  #割り当てられたクラスタ

    #↓-----～そのクラスタ内に空いているコアがあるか調べる～-------------------------------------------
    for core in target[allocated_CC]:
         if(core[0] == -1):
            return allocated_CC
    
    return -1
    #↑---------------------------------------------------------------------------------------------
    
#～s秒、矛盾が無いように時間を進める～
def advance_time(s, target, executed_tasks):
    
    for CC in target:
        for core in CC:
            if(core[0] != -1):  #コアが動作中
                core[1] -= s  #s秒分、処理を進める
                if(core[1] <= 0):  #残りの実行時間が0以下になったら
                    executed_tasks.append(core[0])  #そのタスクを実行済みにする
                    core[0] = -1  #コアをアイドル状態にする
                    core[1] = 0  #初期状態に戻す

#～コアにタスクを割り当てる。
# sが何番目のクラスタか、kが何番目のコアか,～
def allocate_core(node, current_time, s, k, num_t, target, result, sl):
    target[s][k][0] = num_t
    target[s][k][1] = node[num_t]
    
    result[num_t][0] = s
    result[num_t][1] = k
    result[num_t][2] = current_time
    result[num_t][3] = current_time + node[num_t]  #実行終了時間は、「割り当てられた時刻+処理時間」
    
    if(len(sl) != 0):
        del sl[0]
            

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
    SAME_DIFF_RATIO = ratio  #クラスタ内の通信時間とクラスタ外の通信時間の比率
    sl = sl
    
    #- 割り当てる対象のコア構成を示す3次元リスト。
    #- [どのクラスタ][どのコア][コア情報　→　実行中のタスク(アイドル状態の時は-1), 実行中のタスクの残り実行時間]
    target = [[[-1, 0] for i in range(NUM_OF_CORES)] for j in range(NUM_OF_CCs)]
    
    #- スケジューリング結果。
    #- [どのクラスタ, どのコア, 割り当てられた時間, 実行終了時間]
    #- 添え字がタスク番号を表す
    result = [[-1, -1, -1, -1] for i in range(len(sl))]
    
    executed_tasks = []
    #↑-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    #↓-----～タスク割り当て～-------------------------------------------------------------------------------------------------------------------------------------------------------
    s = 0  #現在の時刻
    
    while(len(sl) != 0):  #スケジューリングリストが空になるまで繰り返す
        
        for i in target:
            print(i)
        
        head = sl[0]  #スケジューリングリストの先頭のタスク番号

        if(legal(executed_tasks, pred, head)):  #スケジューリングリストの先頭がlegalなら
            
            #↓-----～前任タスクの中で、「実行終了時間+通信時間」が最も遅いタスクを見つける。～------
            max_time_pred = 0  #「実行終了時間+通信時間(クラスタ内で計算)」が最も遅いタスク
            max_time = 0  #「実行終了時間+通信時間(クラスタ内で計算)」の最大値
            
            for pred_head in pred[head]:
                if((result[pred_head][3] + edge[pred_head][head]) >= max_time):
                    max_time_pred = pred_head
                    max_time = result[pred_head][3] + edge[pred_head][head]
            #↑----------------------------------------------------------------------------------
            
            allocate_cc = can_same(max_time_pred, result, target)
            
            if(allocate_cc != -1):  #同じクラスタ内に割り当て可能
                #通信時間分、時間を進める
                s += edge[max_time_pred][head]  
                advance_time(edge[max_time_pred][head], target, executed_tasks)
                
                #～コアにタスクを割り当てる～
                for i in range(NUM_OF_CORES):
                    if(target[allocate_cc][i][0] == -1):  #アイドル状態のコアを見つけたら
                        allocate_core(node, s, allocate_cc, i, head, target, result, sl)  #タスクを割り当てる
                        break
            
            else:  #同じクラスタ内に割り当てできない場合
                
                max_time_pred_CC = result[max_time_pred][0]
                
                #↓-----～max_time_predのクラスタの中のコアで、最速でアイドル状態になるコアを見つけて、それまでの時間を調べる～----
                earliest_idle_core = 0  #最速でアイドル状態になるコア
                earliest_idle_time = 0  #最速でアイドル状態になるコアがアイドル状態になるまでの時間
                
                for i in range(NUM_OF_CORES):  #max_time_predが割り当てられたクラスタを探索
                    if(target[max_time_pred_CC][i][1] >= earliest_idle_time):
                        earliest_idle_core = i
                        earliest_idle_time = target[max_time_pred_CC][i][1]
                #↑-----------------------------------------------------------------------------------------------------------
                
                #クラスタ外の通信時間と、earliest_idle_time + クラスタ内の通信時間を比較して、早い方を選択する
                if((earliest_idle_time + edge[max_time_pred][head]) < (edge[max_time_pred][head] * SAME_DIFF_RATIO)):  #待つ方が早いなら
                    #アイドル状態になるまで、時間を進める
                    s += earliest_idle_time
                    advance_time(earliest_idle_time, target, executed_tasks)
                
                    #～コアにタスクを割り当てる～
                    for i in range(NUM_OF_CORES):
                        if(target[max_time_pred_CC][i][0] == -1):  #アイドル状態のコアを見つけたら
                            allocate_core(node, s, max_time_pred_CC, i, head, target, result, sl)  #タスクを割り当てる
                            break
                            
                else:  #クラスタ外に割り当てた方が早いなら
                    #通信時間分、時間を進める
                    s += edge[max_time_pred][head] * SAME_DIFF_RATIO
                    advance_time(edge[max_time_pred][head] * SAME_DIFF_RATIO, target, executed_tasks)
                
                    #～コアにタスクを割り当てる～
                    allocate_flag = 0  #割り当てが終わったら1
                    
                    for i in range(NUM_OF_CCs):
                        for j in range(NUM_OF_CORES):
                            if(target[i][j][0] == -1):
                                allocate_core(node, s, i, j, head, target, result, sl)
                                allocate_flag = 1
                                break
                            
                        if(allocate_flag == 1):
                            break
        

        #スケジューリングリストの先頭が実行可能になるまで待機
        s += 1
        advance_time(1, target, executed_tasks)
    
    #↑--------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    return result

    
    