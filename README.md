# AlgorithmSimulator

## python/
- dag.py : .tgffファイルの読み込み
  - read_dag() : 読み込みたいDAG名を渡して、読み込む
    - randomの評価をとりたい場合はパスを変更する（要修正）
- heft.py : HEFT
  - 'python heft.py change_CCR 2 3 3 new_100_1 2 2'
    - args[1] : 評価名
    - args[2] : クラスタ数
    - args[3] : コア数
    - args[4] : クラスタ外の通信時間とクラスタ内の通信時間の比率
    - args[5] : DAG名
    - args[6] : 実行時間に掛ける値
    - args[7] : 通信時間に掛ける値
