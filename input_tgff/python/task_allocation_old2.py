#～受け取ったタスクの前任タスクがすべて実行済みだったら、1を返す。そうでなければ0を返す。～
def legal(executed_tasks, pred, num_t):
    for pred_t in pred[num_t]:
        if(pred_t not in executed_tasks):
            return False
    
    return True


#～s秒、矛盾が無いように時間を進める～
def advance_time(num_of_cc, num_of_core, current_time, target, result, executed_tasks):
    
    #print(current_time)
    
    for i in range(num_of_cc):
        for j in range(num_of_core):
                if(target[i][j][0] != -1 and current_time >= result[target[i][j][0]][2]):  #そのコアにタスクが割り当てられていて、開始時刻になったら
                    target[i][j][1] -= 1  #1秒分処理
                    if(target[i][j][1] == 0):
                        executed_tasks.append(target[i][j][0])  #そのタスクを実行済みにする
                        target[i][j][0] = -1  #コアをアイドル状態にする
                        target[i][j][1] = 0  #初期状態に戻す
    
    #print(executed_tasks)


#～コアにタスクを割り当てる。
# sが何番目のクラスタか、kが何番目のコアか,～
def allocate_core(node, will_allocate_time, s, k, num_t, target, result, sl):
    if(target[s][k][0] == -1):
    
        target[s][k][0] = num_t
        target[s][k][1] = node[num_t]
        
        result[num_t][0] = s
        result[num_t][1] = k
        result[num_t][2] = will_allocate_time
        result[num_t][3] = will_allocate_time + node[num_t]  #実行終了時間は、「割り当てられた時刻+処理時間」
        
        if(len(sl) != 0):
            del sl[0]


#受け取ったタスクが割り当てられているクラスタ番号を返す。割り当てられていなければ、-1を返す
def cluster_number(result, task):
    
    if(result[task][0] != -1):  #受け取ったタスクが割り当てられていたら
        return result[task][0]
    else:
        return -1
    

#クラスタ番号を受け取り、そのクラスタに空きがあるか調べる。
#空いていれば、「1, 空いているコア番号」を返し、空いていなければ、「-1, 最速でアイドル状態になるコア番号」を返す
def vacant_cluster(num_of_core, target, result, cc_num):

    earliest_time_idle = 999999999999
    earliest_idle_core = -1  #最速でアイドル状態になるコア番号
    
    for i in range(num_of_core):
        if(target[cc_num][i][0] == -1):  #コアがアイドル状態なら
            return 1, i
        
        else:
            if(earliest_time_idle >= result[target[cc_num][i][0]][3]):
                earliest_time_idle = result[target[cc_num][i][0]][3]
                earliest_idle_core = i
        
    return -1, earliest_idle_core
    
        


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
    
    while(len(executed_tasks) != len(node)):  #すべてのタスクが実行終了するまで繰り返す

        if(len(sl) != 0):
            head = sl[0]  #スケジューリングリストの先頭のタスク番号

        if(legal(executed_tasks, pred, head)):  #スケジューリングリストの先頭がlegalなら
            
            earliest_time_cluster = -1  #「前任タスクの実行終了時間 + 前任タスクからの通信時間」の最大値が最も早くなるクラスタ番号
            earliest_time = 9999999999  #「前任タスクの実行終了時間 + 前任タスクからの通信時間」の最大値が最も早くなる際の値
            earliest_time_core = -1  #割り当てるクラスタが決まった際の、割り当てるコア番号
            
            for i in range(NUM_OF_CCs):  #すべてのクラスタを探索

                max_time = -1  #「実行終了時間 + 通信時間」が最も遅くなるときの値
                
                ok_flag, core_num = vacant_cluster(NUM_OF_CORES, target, result, i)  #今headを割りあてようとしているクラスタに空きがあるか調べる
            
                for pred_head in pred[head]:  #前任タスクをすべて探索
                    
                    pred_finish = result[pred_head][3]  #実行終了時間
                    communication_cost = -1  #通信時間
                    
                    if(cluster_number(result, pred_head) == i):  #今headを割り当てているクラスタと、pred_headのクラスタが同じなら
                         
                        if(ok_flag == 1):  #クラスタが空いていれば
                            communication_cost = edge[pred_head][head]  #クラスタ内の通信時間で計算
                            
                            if(max_time < (pred_finish + communication_cost)):
                                max_time = pred_finish + communication_cost
                        
                        elif(ok_flag == -1):  #クラスタが空いていなければ
                            communication_cost = edge[pred_head][head]  #クラスタ内の通信時間で計算
                            
                            #↓-----2つの時間店のうち、遅い方を考えなくてはならない-------------------------
                            time1 = pred_finish + communication_cost  #「実行終了時間 + 通信時間」
                            time2 = result[core_num][3]  #最速でアイドル状態となる時間
                            at_flag = 1  #time2のほうが遅ければ、1
                            
                            if(time1 > time2):
                                true_time = time1
                                at_flag = 0
                            else:
                                true_time = time2
                            #↑--------------------------------------------------------------------------
                           
                            if(max_time < true_time):
                                
                                if(at_flag == 1):  #time2の方が遅い
                                    if(max_time < time2):
                                        max_time = time2  #コアがアイドル状態になる時刻
                                else:
                                    if(max_time < time1):
                                        max_time = time1  #「実行終了時間 + 通信時間」
                    
                    
                    else:  #今headを割り当てているクラスタと、pred_headのクラスタが違うなら
                        
                        if(ok_flag == 1):  #クラスタが空いていれば
                            communication_cost = edge[pred_head][head] * 3  #クラスタ外の通信時間で計算
                            
                            if(max_time < (pred_finish + communication_cost)):
                                max_time = pred_finish + communication_cost
                        
                        elif(ok_flag == -1):  #クラスタが空いていなければ
                            communication_cost = edge[pred_head][head] * 3  #クラスタ外の通信時間で計算
                            
                            #↓-----2つの時間店のうち、遅い方を考えなくてはならない-------------------------
                            time1 = pred_finish + communication_cost  #「実行終了時間 + 通信時間」
                            time2 = result[core_num][3]  #最速でアイドル状態となるまでの時間
                            at_flag = 1  #time2のほうが遅ければ、1
                            
                            if(time1 > time2):
                                true_time = time1
                                at_flag = 0
                            else:
                                true_time = time2
                            #↑--------------------------------------------------------------------------
                           
                            if(max_time < true_time):
                                
                                if(at_flag == 1):  #time2の方が遅い
                                    if(max_time < time2):
                                        max_time = time2  #コアがアイドル状態になる時刻
                                else:
                                    if(max_time < time1):
                                        max_time = time1  #「実行終了時間 + 通信時間」


                if(earliest_time > max_time):
                    earliest_time = max_time
                    earliest_time_cluster = i
                    earliest_time_core = core_num
                    
            
            allocate_core(node, earliest_time, earliest_time_cluster, earliest_time_core, head, target, result, sl)  #タスクを割り当てる
            
            #for i in result:
               # print(i)
                
                
            for i in range(NUM_OF_CCs):
                for j in range(NUM_OF_CORES):
                    print(target[i][j])
            print("---------------------------------")
            print(executed_tasks)
            print("---------------------------------")

        #↓-----～この時間でまだ割り当てられるか確認～---------------------------------------
        #if(len(sl) != 0):
           # if(legal(executed_tasks, pred, sl[0])):  #スケジューリングリストの先頭がlegalなら
              #  continue
        #↑--------------------------------------------------------------------------------
            
        #スケジューリングリストの先頭が実行可能になるまで待つ
        advance_time(NUM_OF_CCs, NUM_OF_CORES, s, target, result, executed_tasks)
        s += 1
        
        if(s == 1100):
            break
    
    #↑--------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    return result