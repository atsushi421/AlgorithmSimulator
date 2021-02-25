# AlgorithmSimulator

## python/
- **all.sh** : ランダム以外のすべての評価
- **change_CCR.sh** : CCR変化の評価
- **change_ratio.sh** : ratio変化のすべての評価
- **change_corenum.sh** : コア数変化のすべての評価
- **change_tasknum.sh** : タスク数変化のすべての評価
- **random.sh** : 完全ランダムDAGでの評価
- **heft.py** : HEFT
  - `python heft.py change_CCR 2 3 3 new_100_1 2 2`
    - args[1] : 評価名
    - args[2] : クラスタ数
    - args[3] : コア数
    - args[4] : クラスタ外の通信時間とクラスタ内の通信時間の比率
    - args[5] : DAG名
    - args[6] : 実行時間に掛ける値
    - args[7] : 通信時間に掛ける値
- **proposed.py** : Proposed algorithm
  - `python propose.py change_CCR 2 3 3 new_100_1 2 2`
    - args[1] : 評価名
    - args[2] : クラスタ数
    - args[3] : コア数
    - args[4] : クラスタ外の通信時間とクラスタ内の通信時間の比率
    - args[5] : DAG名
    - args[6] : 実行時間に掛ける値
    - args[7] : 通信時間に掛ける値
- **dag.py** : .tgffファイルの読み込み
  - read_dag() : 読み込みたいDAG名を渡して、読み込む
    - randomの評価をとりたい場合はパスを変更する（要修正）
- **q_learning.py** : 強化学習
- **task_allocation.py** : 割り当てを行い、メイクスパンを計算する
- **calc_speedup.py** : メイクスパン結果からSpeedupを計算し、resultに書き込む
  - 現状はコア数変化で計算
- **calc_efficiency.py** : メイクスパン結果からEfficiencyを計算し、resultに書き込む
  - 現状はコア数変化で計算
- **order_name.py** : resultの結果をDAG名の昇順でソートする

## tgff_auto/
- **random_generate.sh** : 旧アルゴリズムでDAGをランダムにたくさん生成
- **new_random_generate.sh** : 新アルゴリズムでDAGをランダムにたくさん生成
- **test.tgffopt** : random_generate.shで参照するパラメータファイル
- **new.tgffopt** : new_random_generate.shで参照するパラメータファイル
- **change_option.py** : test.tgffoptのパラメータを変更する
- **new_change_option.py** : new.tgffoptのパラメータを変更する
- **change_dag_name.py** : 旧アルゴリズムで生成したDAGの名前を変更する
- **new_change_dag_name.py** : 新アルゴリズムで生成したDAGの名前を変更する
