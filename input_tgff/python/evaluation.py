def calc_speedup():
    
    #単一実行時間 task_100
    single_makespan = [23422, 27312, 29159, 21523, 26043, 23705, 26506, 24345]
    
    
    #↓-----Speedup_HEFT_2-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_makespan = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_makespan/makespan_heft/makespan_2.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_makespan.append(int(line_list[0]))
        
    
    #計算結果
    speedup_heft_2 = []
    
    for i in range(len(single_makespan)):
        speedup_heft_2.append(single_makespan[i] / get_makespan[i])
    
    #結果の書き込み（wは上書きモード）
    #ファイルを開く
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_speedup/speedup_heft/speedup_2.txt", "w")
    
    for i in speedup_heft_2:
        result = str(i)
        f.write(result + '\n')
    #↑-----Speedup_HEFT_2-----------------------------------------------------------------------------------------------------------------------

    #↓-----Speedup_HEFT_3-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_makespan = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_makespan/makespan_heft/makespan_3.txt", "r")
    
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
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_speedup/speedup_heft/speedup_3.txt", "w")
    
    for i in speedup_heft_3:
        result = str(i)
        f.write(result + '\n')
    #↑-----Speedup_HEFT_3-----------------------------------------------------------------------------------------------------------------------
    
    #↓-----Speedup_HEFT_4-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_makespan = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_makespan/makespan_heft/makespan_4.txt", "r")
    
    # 1行ずつ読み込む
    for line in tgff_file:
        # 文字列の半角スペース・タブ区切りで区切ったリストを取得
        line_list = line.split()
        
        get_makespan.append(int(line_list[0]))
        
    
    #計算結果
    speedup_heft_4 = []
    
    for i in range(len(single_makespan)):
        speedup_heft_4.append(single_makespan[i] / get_makespan[i])
    
    #結果の書き込み（wは上書きモード）
    #ファイルを開く
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_speedup/speedup_heft/speedup_4.txt", "w")
    
    for i in speedup_heft_4:
        result = str(i)
        f.write(result + '\n')
    #↑-----Speedup_HEFT_4-----------------------------------------------------------------------------------------------------------------------
    
    #↓-----Speedup_HEFT_5-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_makespan = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_makespan/makespan_heft/makespan_5.txt", "r")
    
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
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_speedup/speedup_heft/speedup_5.txt", "w")
    
    for i in speedup_heft_5:
        result = str(i)
        f.write(result + '\n')
    #↑-----Speedup_HEFT_5-----------------------------------------------------------------------------------------------------------------------


    #↓-----Speedup_Propose_2-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_makespan = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_makespan/makespan_propose/makespan_2.txt", "r")
    
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
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_speedup/speedup_propose/speedup_2.txt", "w")
    
    for i in speedup_propose_2:
        result = str(i)
        f.write(result + '\n')
    #↑-----Speedup_propose_2-----------------------------------------------------------------------------------------------------------------------
    
    #↓-----Speedup_Propose_3-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_makespan = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_makespan/makespan_propose/makespan_3.txt", "r")
    
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
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_speedup/speedup_propose/speedup_3.txt", "w")
    
    for i in speedup_propose_3:
        result = str(i)
        f.write(result + '\n')
    #↑-----Speedup_propose_3-----------------------------------------------------------------------------------------------------------------------
    
    #↓-----Speedup_Propose_4-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_makespan = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_makespan/makespan_propose/makespan_4.txt", "r")
    
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
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_speedup/speedup_propose/speedup_4.txt", "w")
    
    for i in speedup_propose_4:
        result = str(i)
        f.write(result + '\n')
    #↑-----Speedup_propose_4-----------------------------------------------------------------------------------------------------------------------
    
    #↓-----Speedup_Propose_5-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_makespan = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_makespan/makespan_propose/makespan_5.txt", "r")
    
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
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_speedup/speedup_propose/speedup_5.txt", "w")
    
    for i in speedup_propose_5:
        result = str(i)
        f.write(result + '\n')
    #↑-----Speedup_propose_5-----------------------------------------------------------------------------------------------------------------------
    
    
    #↓-----Speedup_QLHEFT_2-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_makespan = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_makespan/makespan_qlheft/makespan_2.txt", "r")
    
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
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_speedup/speedup_qlheft/speedup_2.txt", "w")
    
    for i in speedup_qlheft_2:
        result = str(i)
        f.write(result + '\n')
    #↑-----Speedup_qlheft_2-----------------------------------------------------------------------------------------------------------------------
    
    #↓-----Speedup_QLHEFT_3-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_makespan = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_makespan/makespan_qlheft/makespan_3.txt", "r")
    
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
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_speedup/speedup_qlheft/speedup_3.txt", "w")
    
    for i in speedup_qlheft_3:
        result = str(i)
        f.write(result + '\n')
    #↑-----Speedup_qlheft_3-----------------------------------------------------------------------------------------------------------------------
    
    #↓-----Speedup_QLHEFT_4-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_makespan = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_makespan/makespan_qlheft/makespan_4.txt", "r")
    
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
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_speedup/speedup_qlheft/speedup_4.txt", "w")
    
    for i in speedup_qlheft_4:
        result = str(i)
        f.write(result + '\n')
    #↑-----Speedup_qlheft_4-----------------------------------------------------------------------------------------------------------------------
    
    #↓-----Speedup_QLHEFT_5-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_makespan = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_makespan/makespan_qlheft/makespan_5.txt", "r")
    
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
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_speedup/speedup_qlheft/speedup_5.txt", "w")
    
    for i in speedup_qlheft_5:
        result = str(i)
        f.write(result + '\n')
    #↑-----Speedup_qlheft_5-----------------------------------------------------------------------------------------------------------------------


def calc_efficiency():
    
    #↓-----Efficiency_HEFT_2-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_speedup = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_speedup/speedup_heft/speedup_2.txt", "r")
    
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
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_efficiency/efficiency_heft/efficiency_2.txt", "w")
    
    for i in efficiency_heft_2:
        result = str(i)
        f.write(result + '\n')
    #↑-----Efficiency_HEFT_2-----------------------------------------------------------------------------------------------------------------------

    #↓-----Efficiency_HEFT_3-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_speedup = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_speedup/speedup_heft/speedup_3.txt", "r")
    
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
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_efficiency/efficiency_heft/efficiency_3.txt", "w")
    
    for i in efficiency_heft_3:
        result = str(i)
        f.write(result + '\n')
    #↑-----Efficiency_HEFT_3-----------------------------------------------------------------------------------------------------------------------
    
    #↓-----Efficiency_HEFT_4-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_speedup = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_speedup/speedup_heft/speedup_4.txt", "r")
    
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
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_efficiency/efficiency_heft/efficiency_4.txt", "w")
    
    for i in efficiency_heft_4:
        result = str(i)
        f.write(result + '\n')
    #↑-----Efficiency_HEFT_4-----------------------------------------------------------------------------------------------------------------------
    
    #↓-----Efficiency_HEFT_5-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_speedup = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_speedup/speedup_heft/speedup_5.txt", "r")
    
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
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_efficiency/efficiency_heft/efficiency_5.txt", "w")
    
    for i in efficiency_heft_5:
        result = str(i)
        f.write(result + '\n')
    #↑-----Efficiency_HEFT_5-----------------------------------------------------------------------------------------------------------------------
    
    
    #↓-----Efficiency_Propose_2-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_speedup = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_speedup/speedup_propose/speedup_2.txt", "r")
    
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
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_efficiency/efficiency_propose/efficiency_2.txt", "w")
    
    for i in efficiency_propose_2:
        result = str(i)
        f.write(result + '\n')
    #↑-----Efficiency_Propose_2-----------------------------------------------------------------------------------------------------------------------
    
    #↓-----Efficiency_Propose_3-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_speedup = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_speedup/speedup_propose/speedup_3.txt", "r")
    
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
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_efficiency/efficiency_propose/efficiency_3.txt", "w")
    
    for i in efficiency_propose_3:
        result = str(i)
        f.write(result + '\n')
    #↑-----Efficiency_Propose_3-----------------------------------------------------------------------------------------------------------------------
    
    #↓-----Efficiency_Propose_4-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_speedup = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_speedup/speedup_propose/speedup_4.txt", "r")
    
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
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_efficiency/efficiency_propose/efficiency_4.txt", "w")
    
    for i in efficiency_propose_4:
        result = str(i)
        f.write(result + '\n')
    #↑-----Efficiency_Propose_4-----------------------------------------------------------------------------------------------------------------------
    
    #↓-----Efficiency_Propose_5-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_speedup = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_speedup/speedup_propose/speedup_5.txt", "r")
    
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
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_efficiency/efficiency_propose/efficiency_5.txt", "w")
    
    for i in efficiency_propose_5:
        result = str(i)
        f.write(result + '\n')
    #↑-----Efficiency_Propose_5-----------------------------------------------------------------------------------------------------------------------
    
    
    #↓-----Efficiency_QLHEFT_2-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_speedup = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_speedup/speedup_qlheft/speedup_2.txt", "r")
    
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
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_efficiency/efficiency_qlheft/efficiency_2.txt", "w")
    
    for i in efficiency_qlheft_2:
        result = str(i)
        f.write(result + '\n')
    #↑-----Efficiency_QLHEFT_2-----------------------------------------------------------------------------------------------------------------------
    
    #↓-----Efficiency_QLHEFT_3-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_speedup = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_speedup/speedup_qlheft/speedup_3.txt", "r")
    
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
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_efficiency/efficiency_qlheft/efficiency_3.txt", "w")
    
    for i in efficiency_qlheft_3:
        result = str(i)
        f.write(result + '\n')
    #↑-----Efficiency_QLHEFT_3-----------------------------------------------------------------------------------------------------------------------
    
    #↓-----Efficiency_QLHEFT_4-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_speedup = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_speedup/speedup_qlheft/speedup_4.txt", "r")
    
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
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_efficiency/efficiency_qlheft/efficiency_4.txt", "w")
    
    for i in efficiency_qlheft_4:
        result = str(i)
        f.write(result + '\n')
    #↑-----Efficiency_QLHEFT_4-----------------------------------------------------------------------------------------------------------------------
    
    #↓-----Efficiency_QLHEFT_5-----------------------------------------------------------------------------------------------------------------------
    #ファイルから取得したメイクスパン
    get_speedup = []
    
    # ファイルを開く
    tgff_file = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_speedup/speedup_qlheft/speedup_5.txt", "r")
    
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
    f = open("C:/Users/atsushi/Documents/研究/論文投稿/卒論/tex/figure/R/change_corenum_efficiency/efficiency_qlheft/efficiency_5.txt", "w")
    
    for i in efficiency_qlheft_5:
        result = str(i)
        f.write(result + '\n')
    #↑-----Efficiency_QLHEFT_5-----------------------------------------------------------------------------------------------------------------------

calc_speedup()
calc_efficiency()