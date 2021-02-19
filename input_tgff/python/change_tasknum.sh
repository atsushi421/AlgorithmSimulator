#!/usr/bin/bash

#-----remove result---------------------------------------------------------
rm /home/atsushi/evaluation/input_tgff/result/change_tasknum/HEFT/*.txt
rm /home/atsushi/evaluation/input_tgff/result/change_tasknum/QLHEFT/*.txt
rm /home/atsushi/evaluation/input_tgff/result/change_tasknum/Propose/*.txt
#-----remove result---------------------------------------------------------

#-----HEFT-------------------------------------
python3 heft.py change_tasknum 2 3 3 new_20_1 2 2
python3 heft.py change_tasknum 2 3 3 new_20_2 2 2
python3 heft.py change_tasknum 2 3 3 new_20_3 2 2
python3 heft.py change_tasknum 2 3 3 new_20_4 2 2
python3 heft.py change_tasknum 2 3 3 new_20_5 2 2
python3 heft.py change_tasknum 2 3 3 new_20_6 2 2
python3 heft.py change_tasknum 2 3 3 new_20_7 2 2
python3 heft.py change_tasknum 2 3 3 new_20_8 2 2

python3 heft.py change_tasknum 2 3 3 new_50_1 2 2
python3 heft.py change_tasknum 2 3 3 new_50_2 2 2
python3 heft.py change_tasknum 2 3 3 new_50_3 2 2
python3 heft.py change_tasknum 2 3 3 new_50_4 2 2
python3 heft.py change_tasknum 2 3 3 new_50_5 2 2
python3 heft.py change_tasknum 2 3 3 new_50_6 2 2
python3 heft.py change_tasknum 2 3 3 new_50_7 2 2
python3 heft.py change_tasknum 2 3 3 new_50_8 2 2

python3 heft.py change_tasknum 2 3 3 new_100_1 2 2
python3 heft.py change_tasknum 2 3 3 new_100_2 2 2
python3 heft.py change_tasknum 2 3 3 new_100_3 2 2
python3 heft.py change_tasknum 2 3 3 new_100_4 2 2
python3 heft.py change_tasknum 2 3 3 new_100_5 2 2
python3 heft.py change_tasknum 2 3 3 new_100_6 2 2
python3 heft.py change_tasknum 2 3 3 new_100_7 2 2
python3 heft.py change_tasknum 2 3 3 new_100_8 2 2

python3 heft.py change_tasknum 2 3 3 new_200_1 2 2
python3 heft.py change_tasknum 2 3 3 new_200_2 2 2
python3 heft.py change_tasknum 2 3 3 new_200_3 2 2
python3 heft.py change_tasknum 2 3 3 new_200_4 2 2
python3 heft.py change_tasknum 2 3 3 new_200_5 2 2
python3 heft.py change_tasknum 2 3 3 new_200_6 2 2
python3 heft.py change_tasknum 2 3 3 new_200_7 2 2
python3 heft.py change_tasknum 2 3 3 new_200_8 2 2
#-----HEFT-------------------------------------

#-----QLHEFT 2 2 & Propose----------------------------------
python3 proposed.py change_tasknum 2 3 3 new_20_1 2 2 &
python3 proposed.py change_tasknum 2 3 3 new_20_2 2 2 &
python3 proposed.py change_tasknum 2 3 3 new_20_3 2 2 &
python3 proposed.py change_tasknum 2 3 3 new_20_4 2 2 &
python3 proposed.py change_tasknum 2 3 3 new_20_5 2 2 &
python3 proposed.py change_tasknum 2 3 3 new_20_6 2 2 &
python3 proposed.py change_tasknum 2 3 3 new_20_7 2 2 &
python3 proposed.py change_tasknum 2 3 3 new_20_8 2 2

python3 proposed.py change_tasknum 2 3 3 new_50_1 2 2 &
python3 proposed.py change_tasknum 2 3 3 new_50_2 2 2 &
python3 proposed.py change_tasknum 2 3 3 new_50_3 2 2 &
python3 proposed.py change_tasknum 2 3 3 new_50_4 2 2 &
python3 proposed.py change_tasknum 2 3 3 new_50_5 2 2 &
python3 proposed.py change_tasknum 2 3 3 new_50_6 2 2 &
python3 proposed.py change_tasknum 2 3 3 new_50_7 2 2 &
python3 proposed.py change_tasknum 2 3 3 new_50_8 2 2

python3 proposed.py change_tasknum 2 3 3 new_100_1 2 2 &
python3 proposed.py change_tasknum 2 3 3 new_100_2 2 2 &
python3 proposed.py change_tasknum 2 3 3 new_100_3 2 2 &
python3 proposed.py change_tasknum 2 3 3 new_100_4 2 2 &
python3 proposed.py change_tasknum 2 3 3 new_100_5 2 2 &
python3 proposed.py change_tasknum 2 3 3 new_100_6 2 2 &
python3 proposed.py change_tasknum 2 3 3 new_100_7 2 2 &
python3 proposed.py change_tasknum 2 3 3 new_100_8 2 2

python3 proposed.py change_tasknum 2 3 3 new_200_1 2 2 &
python3 proposed.py change_tasknum 2 3 3 new_200_2 2 2 &
python3 proposed.py change_tasknum 2 3 3 new_200_3 2 2 &
python3 proposed.py change_tasknum 2 3 3 new_200_4 2 2 &
python3 proposed.py change_tasknum 2 3 3 new_200_5 2 2 &
python3 proposed.py change_tasknum 2 3 3 new_200_6 2 2 &
python3 proposed.py change_tasknum 2 3 3 new_200_7 2 2 &
python3 proposed.py change_tasknum 2 3 3 new_200_8 2 2
#-----QLproposed 2 2 & Propose----------------------------------