#スケジューリング結果から、クラスタ外の通信が必要な部分の通信時間(edge)を更新
def recalc(result, edge_original, edge, ratio, pred, sl):
    
    for task in sl:  #スケジューリングリストを全探索
        for pred_task in pred[task]:  #taskの前任タスクを全探索
            print(result[pred_task][0])
            print(result[task][0])
            if(result[pred_task][0] != result[task][0]):  #前任タスクと割り当てられたクラスタが異なる場合
                edge[pred_task][task] = edge_original[pred_task][task] * ratio  #クラスタ外の通信時間に更新
                
                print("update")
    
    return edge
    
    