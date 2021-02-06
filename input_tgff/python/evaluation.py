import statistics

def calc_speedup():
    
    #単一実行時間 task_100
    single_makespan = [154452, 149030, 159854, 153382, 134666, 169458, 132234, 125310]
    
    
    #↓-----Speedup_HEFT_2-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_makespan = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_makespan_60/makespan_heft/makespan_2.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        # 空行はスキップ
        if(line == '\n'):
            continue
        
        get_makespan.append(int(line_list[0]))
        
    
    #計算結果
    speedup_heft_2 = []
    
    for i in range(len(single_makespan)):
        speedup_heft_2.append(single_makespan[i] / get_makespan[i])
    
    #結果の書き込み（wは上書きモード）
    #ファイルを開く
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_speedup_60/speedup_heft/speedup_2.txt", "w")
    
    for i in speedup_heft_2:
        result = str(i)
        f.write(result + '\n')
    #↑-----Speedup_HEFT_2-----------------------------------------------------------------------------------------------------------------------

    #↓-----Speedup_HEFT_3-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_makespan = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_makespan_60/makespan_heft/makespan_3.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_makespan.append(int(line_list[0]))
        
    
    #計算結果
    speedup_heft_3 = []
    
    for i in range(len(single_makespan)):
        speedup_heft_3.append(single_makespan[i] / get_makespan[i])
    
    #結果の書き込み（wは上書きモード）
    #ファイルを開く
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_speedup_60/speedup_heft/speedup_3.txt", "w")
    
    for i in speedup_heft_3:
        result = str(i)
        f.write(result + '\n')
    #↑-----Speedup_HEFT_3-----------------------------------------------------------------------------------------------------------------------
    
    #↓-----Speedup_HEFT_4-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_makespan = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_makespan_60/makespan_heft/makespan_4.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        # 空行はスキップ
        if(line == '\n'):
            continue
        
        get_makespan.append(int(line_list[0]))
        
    
    #計算結果
    speedup_heft_4 = []
    
    for i in range(len(single_makespan)):
        speedup_heft_4.append(single_makespan[i] / get_makespan[i])
    
    #結果の書き込み（wは上書きモード）
    #ファイルを開く
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_speedup_60/speedup_heft/speedup_4.txt", "w")
    
    for i in speedup_heft_4:
        result = str(i)
        f.write(result + '\n')
    #↑-----Speedup_HEFT_4-----------------------------------------------------------------------------------------------------------------------
    
    #↓-----Speedup_HEFT_5-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_makespan = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_makespan_60/makespan_heft/makespan_5.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_makespan.append(int(line_list[0]))
        
    
    #計算結果
    speedup_heft_5 = []
    
    for i in range(len(single_makespan)):
        speedup_heft_5.append(single_makespan[i] / get_makespan[i])
    
    #結果の書き込み（wは上書きモード）
    #ファイルを開く
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_speedup_60/speedup_heft/speedup_5.txt", "w")
    
    for i in speedup_heft_5:
        result = str(i)
        f.write(result + '\n')
    #↑-----Speedup_HEFT_5-----------------------------------------------------------------------------------------------------------------------


    #↓-----Speedup_Propose_2-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_makespan = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_makespan_60/makespan_propose/makespan_2.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_makespan.append(int(line_list[0]))
        
    
    #計算結果
    speedup_propose_2 = []
    
    for i in range(len(single_makespan)):
        speedup_propose_2.append(single_makespan[i] / get_makespan[i])
    
    #結果の書き込み（wは上書きモード）
    #ファイルを開く
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_speedup_60/speedup_propose/speedup_2.txt", "w")
    
    for i in speedup_propose_2:
        result = str(i)
        f.write(result + '\n')
    #↑-----Speedup_propose_2-----------------------------------------------------------------------------------------------------------------------
    
    #↓-----Speedup_Propose_3-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_makespan = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_makespan_60/makespan_propose/makespan_3.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_makespan.append(int(line_list[0]))
        
    
    #計算結果
    speedup_propose_3 = []
    
    for i in range(len(single_makespan)):
        speedup_propose_3.append(single_makespan[i] / get_makespan[i])
    
    #結果の書き込み（wは上書きモード）
    #ファイルを開く
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_speedup_60/speedup_propose/speedup_3.txt", "w")
    
    for i in speedup_propose_3:
        result = str(i)
        f.write(result + '\n')
    #↑-----Speedup_propose_3-----------------------------------------------------------------------------------------------------------------------
    
    #↓-----Speedup_Propose_4-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_makespan = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_makespan_60/makespan_propose/makespan_4.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_makespan.append(int(line_list[0]))
        
    
    #計算結果
    speedup_propose_4 = []
    
    for i in range(len(single_makespan)):
        speedup_propose_4.append(single_makespan[i] / get_makespan[i])
    
    #結果の書き込み（wは上書きモード）
    #ファイルを開く
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_speedup_60/speedup_propose/speedup_4.txt", "w")
    
    for i in speedup_propose_4:
        result = str(i)
        f.write(result + '\n')
    #↑-----Speedup_propose_4-----------------------------------------------------------------------------------------------------------------------
    
    #↓-----Speedup_Propose_5-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_makespan = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_makespan_60/makespan_propose/makespan_5.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_makespan.append(int(line_list[0]))
        
    
    #計算結果
    speedup_propose_5 = []
    
    for i in range(len(single_makespan)):
        speedup_propose_5.append(single_makespan[i] / get_makespan[i])
    
    #結果の書き込み（wは上書きモード）
    #ファイルを開く
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_speedup_60/speedup_propose/speedup_5.txt", "w")
    
    for i in speedup_propose_5:
        result = str(i)
        f.write(result + '\n')
    #↑-----Speedup_propose_5-----------------------------------------------------------------------------------------------------------------------
    
    
    #↓-----Speedup_QLHEFT_2-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_makespan = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_makespan_60/makespan_qlheft/makespan_2.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_makespan.append(int(line_list[0]))
        
    
    #計算結果
    speedup_qlheft_2 = []
    
    for i in range(len(single_makespan)):
        speedup_qlheft_2.append(single_makespan[i] / get_makespan[i])
    
    #結果の書き込み（wは上書きモード）
    #ファイルを開く
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_speedup_60/speedup_qlheft/speedup_2.txt", "w")
    
    for i in speedup_qlheft_2:
        result = str(i)
        f.write(result + '\n')
    #↑-----Speedup_qlheft_2-----------------------------------------------------------------------------------------------------------------------
    
    #↓-----Speedup_QLHEFT_3-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_makespan = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_makespan_60/makespan_qlheft/makespan_3.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_makespan.append(int(line_list[0]))
        
    
    #計算結果
    speedup_qlheft_3 = []
    
    for i in range(len(single_makespan)):
        speedup_qlheft_3.append(single_makespan[i] / get_makespan[i])
    
    #結果の書き込み（wは上書きモード）
    #ファイルを開く
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_speedup_60/speedup_qlheft/speedup_3.txt", "w")
    
    for i in speedup_qlheft_3:
        result = str(i)
        f.write(result + '\n')
    #↑-----Speedup_qlheft_3-----------------------------------------------------------------------------------------------------------------------
    
    #↓-----Speedup_QLHEFT_4-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_makespan = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_makespan_60/makespan_qlheft/makespan_4.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_makespan.append(int(line_list[0]))
        
    
    #計算結果
    speedup_qlheft_4 = []
    
    for i in range(len(single_makespan)):
        speedup_qlheft_4.append(single_makespan[i] / get_makespan[i])
    
    #結果の書き込み（wは上書きモード）
    #ファイルを開く
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_speedup_60/speedup_qlheft/speedup_4.txt", "w")
    
    for i in speedup_qlheft_4:
        result = str(i)
        f.write(result + '\n')
    #↑-----Speedup_qlheft_4-----------------------------------------------------------------------------------------------------------------------
    
    #↓-----Speedup_QLHEFT_5-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_makespan = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_makespan_60/makespan_qlheft/makespan_5.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_makespan.append(int(line_list[0]))
        
    
    #計算結果
    speedup_qlheft_5 = []
    
    for i in range(len(single_makespan)):
        speedup_qlheft_5.append(single_makespan[i] / get_makespan[i])
    
    #結果の書き込み（wは上書きモード）
    #ファイルを開く
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_speedup_60/speedup_qlheft/speedup_5.txt", "w")
    
    for i in speedup_qlheft_5:
        result = str(i)
        f.write(result + '\n')
    #↑-----Speedup_qlheft_5-----------------------------------------------------------------------------------------------------------------------


def calc_efficiency():
    
    #↓-----Efficiency_HEFT_2-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_speedup = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_speedup_60/speedup_heft/speedup_2.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_speedup.append(float(line_list[0]))
        
    
    #計算結果
    efficiency_heft_2 = []
    
    for i in range(len(get_speedup)):
        efficiency_heft_2.append(get_speedup[i] / 4)
    
    #結果の書き込み（wは上書きモード）
    #ファイルを開く
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_efficiency_60/efficiency_heft/efficiency_2.txt", "w")
    
    for i in efficiency_heft_2:
        result = str(i)
        f.write(result + '\n')
    #↑-----Efficiency_HEFT_2-----------------------------------------------------------------------------------------------------------------------

    #↓-----Efficiency_HEFT_3-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_speedup = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_speedup_60/speedup_heft/speedup_3.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_speedup.append(float(line_list[0]))
        
    
    #計算結果
    efficiency_heft_3 = []
    
    for i in range(len(get_speedup)):
        efficiency_heft_3.append(get_speedup[i] / 6)
    
    #結果の書き込み（wは上書きモード）
    #ファイルを開く
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_efficiency_60/efficiency_heft/efficiency_3.txt", "w")
    
    for i in efficiency_heft_3:
        result = str(i)
        f.write(result + '\n')
    #↑-----Efficiency_HEFT_3-----------------------------------------------------------------------------------------------------------------------
    
    #↓-----Efficiency_HEFT_4-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_speedup = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_speedup_60/speedup_heft/speedup_4.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_speedup.append(float(line_list[0]))
        
    
    #計算結果
    efficiency_heft_4 = []
    
    for i in range(len(get_speedup)):
        efficiency_heft_4.append(get_speedup[i] / 8)
    
    #結果の書き込み（wは上書きモード）
    #ファイルを開く
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_efficiency_60/efficiency_heft/efficiency_4.txt", "w")
    
    for i in efficiency_heft_4:
        result = str(i)
        f.write(result + '\n')
    #↑-----Efficiency_HEFT_4-----------------------------------------------------------------------------------------------------------------------
    
    #↓-----Efficiency_HEFT_5-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_speedup = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_speedup_60/speedup_heft/speedup_5.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_speedup.append(float(line_list[0]))
        
    
    #計算結果
    efficiency_heft_5 = []
    
    for i in range(len(get_speedup)):
        efficiency_heft_5.append(get_speedup[i] / 10)
    
    #結果の書き込み（wは上書きモード）
    #ファイルを開く
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_efficiency_60/efficiency_heft/efficiency_5.txt", "w")
    
    for i in efficiency_heft_5:
        result = str(i)
        f.write(result + '\n')
    #↑-----Efficiency_HEFT_5-----------------------------------------------------------------------------------------------------------------------
    
    
    #↓-----Efficiency_Propose_2-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_speedup = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_speedup_60/speedup_propose/speedup_2.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_speedup.append(float(line_list[0]))
        
    
    #計算結果
    efficiency_propose_2 = []
    
    for i in range(len(get_speedup)):
        efficiency_propose_2.append(get_speedup[i] / 4)
    
    #結果の書き込み（wは上書きモード）
    #ファイルを開く
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_efficiency_60/efficiency_propose/efficiency_2.txt", "w")
    
    for i in efficiency_propose_2:
        result = str(i)
        f.write(result + '\n')
    #↑-----Efficiency_Propose_2-----------------------------------------------------------------------------------------------------------------------
    
    #↓-----Efficiency_Propose_3-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_speedup = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_speedup_60/speedup_propose/speedup_3.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_speedup.append(float(line_list[0]))
        
    
    #計算結果
    efficiency_propose_3 = []
    
    for i in range(len(get_speedup)):
        efficiency_propose_3.append(get_speedup[i] / 6)
    
    #結果の書き込み（wは上書きモード）
    #ファイルを開く
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_efficiency_60/efficiency_propose/efficiency_3.txt", "w")
    
    for i in efficiency_propose_3:
        result = str(i)
        f.write(result + '\n')
    #↑-----Efficiency_Propose_3-----------------------------------------------------------------------------------------------------------------------
    
    #↓-----Efficiency_Propose_4-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_speedup = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_speedup_60/speedup_propose/speedup_4.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_speedup.append(float(line_list[0]))
        
    
    #計算結果
    efficiency_propose_4 = []
    
    for i in range(len(get_speedup)):
        efficiency_propose_4.append(get_speedup[i] / 8)
    
    #結果の書き込み（wは上書きモード）
    #ファイルを開く
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_efficiency_60/efficiency_propose/efficiency_4.txt", "w")
    
    for i in efficiency_propose_4:
        result = str(i)
        f.write(result + '\n')
    #↑-----Efficiency_Propose_4-----------------------------------------------------------------------------------------------------------------------
    
    #↓-----Efficiency_Propose_5-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_speedup = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_speedup_60/speedup_propose/speedup_5.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_speedup.append(float(line_list[0]))
        
    
    #計算結果
    efficiency_propose_5 = []
    
    for i in range(len(get_speedup)):
        efficiency_propose_5.append(get_speedup[i] / 10)
    
    #結果の書き込み（wは上書きモード）
    #ファイルを開く
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_efficiency_60/efficiency_propose/efficiency_5.txt", "w")
    
    for i in efficiency_propose_5:
        result = str(i)
        f.write(result + '\n')
    #↑-----Efficiency_Propose_5-----------------------------------------------------------------------------------------------------------------------
    
    
    #↓-----Efficiency_QLHEFT_2-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_speedup = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_speedup_60/speedup_qlheft/speedup_2.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_speedup.append(float(line_list[0]))
        
    
    #計算結果
    efficiency_qlheft_2 = []
    
    for i in range(len(get_speedup)):
        efficiency_qlheft_2.append(get_speedup[i] / 4)
    
    #結果の書き込み（wは上書きモード）
    #ファイルを開く
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_efficiency_60/efficiency_qlheft/efficiency_2.txt", "w")
    
    for i in efficiency_qlheft_2:
        result = str(i)
        f.write(result + '\n')
    #↑-----Efficiency_QLHEFT_2-----------------------------------------------------------------------------------------------------------------------
    
    #↓-----Efficiency_QLHEFT_3-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_speedup = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_speedup_60/speedup_qlheft/speedup_3.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_speedup.append(float(line_list[0]))
        
    
    #計算結果
    efficiency_qlheft_3 = []
    
    for i in range(len(get_speedup)):
        efficiency_qlheft_3.append(get_speedup[i] / 6)
    
    #結果の書き込み（wは上書きモード）
    #ファイルを開く
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_efficiency_60/efficiency_qlheft/efficiency_3.txt", "w")
    
    for i in efficiency_qlheft_3:
        result = str(i)
        f.write(result + '\n')
    #↑-----Efficiency_QLHEFT_3-----------------------------------------------------------------------------------------------------------------------
    
    #↓-----Efficiency_QLHEFT_4-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_speedup = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_speedup_60/speedup_qlheft/speedup_4.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_speedup.append(float(line_list[0]))
        
    
    #計算結果
    efficiency_qlheft_4 = []
    
    for i in range(len(get_speedup)):
        efficiency_qlheft_4.append(get_speedup[i] / 8)
    
    #結果の書き込み（wは上書きモード）
    #ファイルを開く
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_efficiency_60/efficiency_qlheft/efficiency_4.txt", "w")
    
    for i in efficiency_qlheft_4:
        result = str(i)
        f.write(result + '\n')
    #↑-----Efficiency_QLHEFT_4-----------------------------------------------------------------------------------------------------------------------
    
    #↓-----Efficiency_QLHEFT_5-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_speedup = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_speedup_60/speedup_qlheft/speedup_5.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_speedup.append(float(line_list[0]))
        
    
    #計算結果
    efficiency_qlheft_5 = []
    
    for i in range(len(get_speedup)):
        efficiency_qlheft_5.append(get_speedup[i] / 10)
    
    #結果の書き込み（wは上書きモード）
    #ファイルを開く
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_corenum_efficiency_60/efficiency_qlheft/efficiency_5.txt", "w")
    
    for i in efficiency_qlheft_5:
        result = str(i)
        f.write(result + '\n')
    #↑-----Efficiency_QLHEFT_5-----------------------------------------------------------------------------------------------------------------------

#CCR変化の中央値を取得する
def CCR_median_heft():
    
    #↓-----HEFT_0.05------------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_data = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_CCR_makespan/makespan_heft/makespan_0.05.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_data.append(float(line_list[0]))
    
    print('median_low_', end = '')
    print('0.05 = ', end = '')
    print(statistics.median_low(get_data))
    print('median_high_', end = '')
    print('0.05 = ', end = '')
    print(statistics.median_high(get_data))
    #↑-----HEFT_0.05------------------------------------------------------------------------------------------------------------------------
    
    #↓-----HEFT_0.1------------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_data = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_CCR_makespan/makespan_heft/makespan_0.1.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_data.append(float(line_list[0]))
    
    print('median_low_', end = '')
    print('0.1 = ', end = '')
    print(statistics.median_low(get_data))
    print('median_high_', end = '')
    print('0.1 = ', end = '')
    print(statistics.median_high(get_data))
    #↑-----HEFT_0.1------------------------------------------------------------------------------------------------------------------------
    
    #↓-----HEFT_0.25------------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_data = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_CCR_makespan/makespan_heft/makespan_0.25.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_data.append(float(line_list[0]))
    
    print('median_low_', end = '')
    print('0.25 = ', end = '')
    print(statistics.median_low(get_data))
    print('median_high_', end = '')
    print('0.25 = ', end = '')
    print(statistics.median_high(get_data))
    #↑-----HEFT_0.25------------------------------------------------------------------------------------------------------------------------
    
    #↓-----HEFT_0.5------------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_data = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_CCR_makespan/makespan_heft/makespan_0.5.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_data.append(float(line_list[0]))
    
    print('median_low_', end = '')
    print('0.5 = ', end = '')
    print(statistics.median_low(get_data))
    print('median_high_', end = '')
    print('0.5 = ', end = '')
    print(statistics.median_high(get_data))
    #↑-----HEFT_0.5------------------------------------------------------------------------------------------------------------------------
    
    #↓-----HEFT_1.0------------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_data = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_CCR_makespan/makespan_heft/makespan_1.0.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_data.append(float(line_list[0]))
    
    print('median_low_', end = '')
    print('1.0 = ', end = '')
    print(statistics.median_low(get_data))
    print('median_high_', end = '')
    print('1.0 = ', end = '')
    print(statistics.median_high(get_data))
    #↑-----HEFT_1.0------------------------------------------------------------------------------------------------------------------------
    
    #↓-----HEFT_2.0------------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_data = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_CCR_makespan/makespan_heft/makespan_2.0.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_data.append(float(line_list[0]))
    
    print('median_low_', end = '')
    print('2.0 = ', end = '')
    print(statistics.median_low(get_data))
    print('median_high_', end = '')
    print('2.0 = ', end = '')
    print(statistics.median_high(get_data))
    #↑-----HEFT_2.0------------------------------------------------------------------------------------------------------------------------


#タスク数変化の中央値を取得する
def tasknum_median_heft():
    
    #↓-----HEFT_20------------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_data = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_tasknum_makespan/makespan_heft/makespan_20.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_data.append(float(line_list[0]))
    
    print('median_low_', end = '')
    print('20 = ', end = '')
    print(statistics.median_low(get_data))
    print('median_high_', end = '')
    print('20 = ', end = '')
    print(statistics.median_high(get_data))
    #↑-----HEFT_20------------------------------------------------------------------------------------------------------------------------

    #↓-----HEFT_50------------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_data = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_tasknum_makespan/makespan_heft/makespan_50.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_data.append(float(line_list[0]))
    
    print('median_low_', end = '')
    print('50 = ', end = '')
    print(statistics.median_low(get_data))
    print('median_high_', end = '')
    print('50 = ', end = '')
    print(statistics.median_high(get_data))
    #↑-----HEFT_50------------------------------------------------------------------------------------------------------------------------
    
    #↓-----HEFT_100------------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_data = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_tasknum_makespan/makespan_heft/makespan_100.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_data.append(float(line_list[0]))
    
    print('median_low_', end = '')
    print('100 = ', end = '')
    print(statistics.median_low(get_data))
    print('median_high_', end = '')
    print('100 = ', end = '')
    print(statistics.median_high(get_data))
    #↑-----HEFT_100------------------------------------------------------------------------------------------------------------------------
    
    #↓-----HEFT_200------------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_data = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_tasknum_makespan/makespan_heft/makespan_200.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_data.append(float(line_list[0]))
    
    print('median_low_', end = '')
    print('200 = ', end = '')
    print(statistics.median_low(get_data))
    print('median_high_', end = '')
    print('200 = ', end = '')
    print(statistics.median_high(get_data))
    #↑-----HEFT_200------------------------------------------------------------------------------------------------------------------------


#CCR変化の中央値を取得する
def CCR_median_qlheft():
    
    #↓-----QLHEFT_0.05------------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_data = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_CCR_makespan/makespan_qlheft/makespan_0.05.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_data.append(float(line_list[0]))
    
    print('median_low_', end = '')
    print('0.05 = ', end = '')
    print(statistics.median_low(get_data))
    print('median_high_', end = '')
    print('0.05 = ', end = '')
    print(statistics.median_high(get_data))
    #↑-----QLHEFT_0.05------------------------------------------------------------------------------------------------------------------------
    
    #↓-----QLHEFT_0.1------------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_data = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_CCR_makespan/makespan_qlheft/makespan_0.1.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_data.append(float(line_list[0]))
    
    print('median_low_', end = '')
    print('0.1 = ', end = '')
    print(statistics.median_low(get_data))
    print('median_high_', end = '')
    print('0.1 = ', end = '')
    print(statistics.median_high(get_data))
    #↑-----QLHEFT_0.1------------------------------------------------------------------------------------------------------------------------
    
    #↓-----QLHEFT_0.25------------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_data = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_CCR_makespan/makespan_qlheft/makespan_0.25.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_data.append(float(line_list[0]))
    
    print('median_low_', end = '')
    print('0.25 = ', end = '')
    print(statistics.median_low(get_data))
    print('median_high_', end = '')
    print('0.25 = ', end = '')
    print(statistics.median_high(get_data))
    #↑-----QLHEFT_0.25------------------------------------------------------------------------------------------------------------------------
    
    #↓-----QLHEFT_0.5------------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_data = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_CCR_makespan/makespan_qlheft/makespan_0.5.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_data.append(float(line_list[0]))
    
    print('median_low_', end = '')
    print('0.5 = ', end = '')
    print(statistics.median_low(get_data))
    print('median_high_', end = '')
    print('0.5 = ', end = '')
    print(statistics.median_high(get_data))
    #↑-----QLHEFT_0.5------------------------------------------------------------------------------------------------------------------------
    
    #↓-----QLHEFT_1.0------------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_data = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_CCR_makespan/makespan_qlheft/makespan_1.0.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_data.append(float(line_list[0]))
    
    print('median_low_', end = '')
    print('1.0 = ', end = '')
    print(statistics.median_low(get_data))
    print('median_high_', end = '')
    print('1.0 = ', end = '')
    print(statistics.median_high(get_data))
    #↑-----QLHEFT_1.0------------------------------------------------------------------------------------------------------------------------
    
    #↓-----QLHEFT_2.0------------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_data = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_CCR_makespan/makespan_qlheft/makespan_2.0.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_data.append(float(line_list[0]))
    
    print('median_low_', end = '')
    print('2.0 = ', end = '')
    print(statistics.median_low(get_data))
    print('median_high_', end = '')
    print('2.0 = ', end = '')
    print(statistics.median_high(get_data))
    #↑-----QLHEFT_2.0------------------------------------------------------------------------------------------------------------------------
    
    #↓-----QLHEFT_4.0------------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_data = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_CCR_makespan/makespan_qlheft/makespan_4.0.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_data.append(float(line_list[0]))
    
    print('median_low_', end = '')
    print('4.0 = ', end = '')
    print(statistics.median_low(get_data))
    print('median_high_', end = '')
    print('4.0 = ', end = '')
    print(statistics.median_high(get_data))
    #↑-----QLHEFT_4.0------------------------------------------------------------------------------------------------------------------------

#タスク数変化の中央値を取得する
def tasknum_median_qlheft():
    
    #↓-----QLHEFT_20------------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_data = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_tasknum_makespan/makespan_qlheft/makespan_20.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_data.append(float(line_list[0]))
    
    print('median_low_', end = '')
    print('20 = ', end = '')
    print(statistics.median_low(get_data))
    print('median_high_', end = '')
    print('20 = ', end = '')
    print(statistics.median_high(get_data))
    #↑-----QLHEFT_20------------------------------------------------------------------------------------------------------------------------

    #↓-----QLHEFT_50------------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_data = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_tasknum_makespan/makespan_qlheft/makespan_50.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_data.append(float(line_list[0]))
    
    print('median_low_', end = '')
    print('50 = ', end = '')
    print(statistics.median_low(get_data))
    print('median_high_', end = '')
    print('50 = ', end = '')
    print(statistics.median_high(get_data))
    #↑-----QLHEFT_50------------------------------------------------------------------------------------------------------------------------
    
    #↓-----QLHEFT_100------------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_data = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_tasknum_makespan/makespan_qlheft/makespan_100.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_data.append(float(line_list[0]))
    
    print('median_low_', end = '')
    print('100 = ', end = '')
    print(statistics.median_low(get_data))
    print('median_high_', end = '')
    print('100 = ', end = '')
    print(statistics.median_high(get_data))
    #↑-----QLHEFT_100------------------------------------------------------------------------------------------------------------------------
    
    #↓-----QLHEFT_200------------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_data = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/new_change_tasknum_makespan/makespan_qlheft/makespan_200.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_data.append(float(line_list[0]))
    
    print('median_low_', end = '')
    print('200 = ', end = '')
    print(statistics.median_low(get_data))
    print('median_high_', end = '')
    print('200 = ', end = '')
    print(statistics.median_high(get_data))
    #↑-----QLHEFT_200------------------------------------------------------------------------------------------------------------------------

#tasknum_median_qlheft()
#CCR_median_qlheft()
#tasknum_median_heft()
#CCR_median_heft()
calc_speedup()
calc_efficiency()