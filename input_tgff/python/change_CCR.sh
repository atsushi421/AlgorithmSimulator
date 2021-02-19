#!/usr/bin/bash

#-----remove result---------------------------------------------------------
rm /home/atsushi/evaluation/input_tgff/result/change_CCR/HEFT/*.txt
rm /home/atsushi/evaluation/input_tgff/result/change_CCR/QLHEFT/*.txt
rm /home/atsushi/evaluation/input_tgff/result/change_CCR/Propose/*.txt
#-----remove result---------------------------------------------------------

#-----HEFT-------------------------------------
python3 heft.py change_CCR 2 3 3 new_100_1 2 2
python3 heft.py change_CCR 2 3 3 new_100_2 2 2
python3 heft.py change_CCR 2 3 3 new_100_3 2 2
python3 heft.py change_CCR 2 3 3 new_100_4 2 2
python3 heft.py change_CCR 2 3 3 new_100_5 2 2
python3 heft.py change_CCR 2 3 3 new_100_6 2 2
python3 heft.py change_CCR 2 3 3 new_100_7 2 2
python3 heft.py change_CCR 2 3 3 new_100_8 2 2

python3 heft.py change_CCR 2 3 3 new_100_1 3 1
python3 heft.py change_CCR 2 3 3 new_100_2 3 1
python3 heft.py change_CCR 2 3 3 new_100_3 3 1
python3 heft.py change_CCR 2 3 3 new_100_4 3 1
python3 heft.py change_CCR 2 3 3 new_100_5 3 1
python3 heft.py change_CCR 2 3 3 new_100_6 3 1
python3 heft.py change_CCR 2 3 3 new_100_7 3 1
python3 heft.py change_CCR 2 3 3 new_100_8 3 1

python3 heft.py change_CCR 2 3 3 new_100_1 1 0.67
python3 heft.py change_CCR 2 3 3 new_100_2 1 0.67
python3 heft.py change_CCR 2 3 3 new_100_3 1 0.67
python3 heft.py change_CCR 2 3 3 new_100_4 1 0.67
python3 heft.py change_CCR 2 3 3 new_100_5 1 0.67
python3 heft.py change_CCR 2 3 3 new_100_6 1 0.67
python3 heft.py change_CCR 2 3 3 new_100_7 1 0.67
python3 heft.py change_CCR 2 3 3 new_100_8 1 0.67

python3 heft.py change_CCR 2 3 3 new_100_1 5 0.5
python3 heft.py change_CCR 2 3 3 new_100_2 5 0.5
python3 heft.py change_CCR 2 3 3 new_100_3 5 0.5
python3 heft.py change_CCR 2 3 3 new_100_4 5 0.5
python3 heft.py change_CCR 2 3 3 new_100_5 5 0.5
python3 heft.py change_CCR 2 3 3 new_100_6 5 0.5
python3 heft.py change_CCR 2 3 3 new_100_7 5 0.5
python3 heft.py change_CCR 2 3 3 new_100_8 5 0.5

python3 heft.py change_CCR 2 3 3 new_100_1 5.5 0.34
python3 heft.py change_CCR 2 3 3 new_100_2 5.5 0.34
python3 heft.py change_CCR 2 3 3 new_100_3 5.5 0.34
python3 heft.py change_CCR 2 3 3 new_100_4 5.5 0.34
python3 heft.py change_CCR 2 3 3 new_100_5 5.5 0.34
python3 heft.py change_CCR 2 3 3 new_100_6 5.5 0.34
python3 heft.py change_CCR 2 3 3 new_100_7 5.5 0.34
python3 heft.py change_CCR 2 3 3 new_100_8 5.5 0.34
#-----HEFT-------------------------------------

#-----QLHEFT 2 2 & Propose----------------------------------
python3 proposed.py change_CCR 2 3 3 new_100_1 2 2 &
python3 proposed.py change_CCR 2 3 3 new_100_2 2 2 &
python3 proposed.py change_CCR 2 3 3 new_100_3 2 2 &
python3 proposed.py change_CCR 2 3 3 new_100_4 2 2 &
python3 proposed.py change_CCR 2 3 3 new_100_5 2 2 &
python3 proposed.py change_CCR 2 3 3 new_100_6 2 2 &
python3 proposed.py change_CCR 2 3 3 new_100_7 2 2 &
python3 proposed.py change_CCR 2 3 3 new_100_8 2 2

python3 proposed.py change_CCR 2 3 3 new_100_1 3 1 &
python3 proposed.py change_CCR 2 3 3 new_100_2 3 1 &
python3 proposed.py change_CCR 2 3 3 new_100_3 3 1 &
python3 proposed.py change_CCR 2 3 3 new_100_4 3 1 &
python3 proposed.py change_CCR 2 3 3 new_100_5 3 1 &
python3 proposed.py change_CCR 2 3 3 new_100_6 3 1 &
python3 proposed.py change_CCR 2 3 3 new_100_7 3 1 &
python3 proposed.py change_CCR 2 3 3 new_100_8 3 1

python3 proposed.py change_CCR 2 3 3 new_100_1 1 0.67 &
python3 proposed.py change_CCR 2 3 3 new_100_2 1 0.67 &
python3 proposed.py change_CCR 2 3 3 new_100_3 1 0.67 &
python3 proposed.py change_CCR 2 3 3 new_100_4 1 0.67 &
python3 proposed.py change_CCR 2 3 3 new_100_5 1 0.67 &
python3 proposed.py change_CCR 2 3 3 new_100_6 1 0.67 &
python3 proposed.py change_CCR 2 3 3 new_100_7 1 0.67 &
python3 proposed.py change_CCR 2 3 3 new_100_8 1 0.67

python3 proposed.py change_CCR 2 3 3 new_100_1 5 0.5 &
python3 proposed.py change_CCR 2 3 3 new_100_2 5 0.5 &
python3 proposed.py change_CCR 2 3 3 new_100_3 5 0.5 &
python3 proposed.py change_CCR 2 3 3 new_100_4 5 0.5 &
python3 proposed.py change_CCR 2 3 3 new_100_5 5 0.5 &
python3 proposed.py change_CCR 2 3 3 new_100_6 5 0.5 &
python3 proposed.py change_CCR 2 3 3 new_100_7 5 0.5 &
python3 proposed.py change_CCR 2 3 3 new_100_8 5 0.5

python3 proposed.py change_CCR 2 3 3 new_100_1 5.5 0.34 &
python3 proposed.py change_CCR 2 3 3 new_100_2 5.5 0.34 &
python3 proposed.py change_CCR 2 3 3 new_100_3 5.5 0.34 &
python3 proposed.py change_CCR 2 3 3 new_100_4 5.5 0.34 &
python3 proposed.py change_CCR 2 3 3 new_100_5 5.5 0.34 &
python3 proposed.py change_CCR 2 3 3 new_100_6 5.5 0.34 &
python3 proposed.py change_CCR 2 3 3 new_100_7 5.5 0.34 &
python3 proposed.py change_CCR 2 3 3 new_100_8 5.5 0.34
#-----QLHEFT 2 2 & Propose----------------------------------