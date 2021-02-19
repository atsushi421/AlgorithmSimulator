#!/usr/bin/bash

#-----remove result---------------------------------------------------------
rm /home/atsushi/evaluation/input_tgff/result/change_ratio/HEFT/*.txt
rm /home/atsushi/evaluation/input_tgff/result/change_ratio/QLHEFT/*.txt
rm /home/atsushi/evaluation/input_tgff/result/change_ratio/Propose/*.txt
#-----remove result---------------------------------------------------------

#-----HEFT-------------------------------------
python3 heft.py change_ratio 2 3 1.5 new_100_1 2 2
python3 heft.py change_ratio 2 3 1.5 new_100_2 2 2
python3 heft.py change_ratio 2 3 1.5 new_100_3 2 2
python3 heft.py change_ratio 2 3 1.5 new_100_4 2 2
python3 heft.py change_ratio 2 3 1.5 new_100_5 2 2
python3 heft.py change_ratio 2 3 1.5 new_100_6 2 2
python3 heft.py change_ratio 2 3 1.5 new_100_7 2 2
python3 heft.py change_ratio 2 3 1.5 new_100_8 2 2

python3 heft.py change_ratio 2 3 3 new_100_1 2 2
python3 heft.py change_ratio 2 3 3 new_100_2 2 2
python3 heft.py change_ratio 2 3 3 new_100_3 2 2
python3 heft.py change_ratio 2 3 3 new_100_4 2 2
python3 heft.py change_ratio 2 3 3 new_100_5 2 2
python3 heft.py change_ratio 2 3 3 new_100_6 2 2
python3 heft.py change_ratio 2 3 3 new_100_7 2 2
python3 heft.py change_ratio 2 3 3 new_100_8 2 2

python3 heft.py change_ratio 2 3 6 new_100_1 2 2
python3 heft.py change_ratio 2 3 6 new_100_2 2 2
python3 heft.py change_ratio 2 3 6 new_100_3 2 2
python3 heft.py change_ratio 2 3 6 new_100_4 2 2
python3 heft.py change_ratio 2 3 6 new_100_5 2 2
python3 heft.py change_ratio 2 3 6 new_100_6 2 2
python3 heft.py change_ratio 2 3 6 new_100_7 2 2
python3 heft.py change_ratio 2 3 6 new_100_8 2 2

python3 heft.py change_ratio 2 3 12 new_100_1 2 2
python3 heft.py change_ratio 2 3 12 new_100_2 2 2
python3 heft.py change_ratio 2 3 12 new_100_3 2 2
python3 heft.py change_ratio 2 3 12 new_100_4 2 2
python3 heft.py change_ratio 2 3 12 new_100_5 2 2
python3 heft.py change_ratio 2 3 12 new_100_6 2 2
python3 heft.py change_ratio 2 3 12 new_100_7 2 2
python3 heft.py change_ratio 2 3 12 new_100_8 2 2

python3 heft.py change_ratio 2 3 24 new_100_1 2 2
python3 heft.py change_ratio 2 3 24 new_100_2 2 2
python3 heft.py change_ratio 2 3 24 new_100_3 2 2
python3 heft.py change_ratio 2 3 24 new_100_4 2 2
python3 heft.py change_ratio 2 3 24 new_100_5 2 2
python3 heft.py change_ratio 2 3 24 new_100_6 2 2
python3 heft.py change_ratio 2 3 24 new_100_7 2 2
python3 heft.py change_ratio 2 3 24 new_100_8 2 2
#-----HEFT-------------------------------------

#-----QLHEFT 2 2 & Propose----------------------------------
python3 proposed.py change_ratio 2 3 1.5 new_100_1 2 2 &
python3 proposed.py change_ratio 2 3 1.5 new_100_2 2 2 &
python3 proposed.py change_ratio 2 3 1.5 new_100_3 2 2 &
python3 proposed.py change_ratio 2 3 1.5 new_100_4 2 2 &
python3 proposed.py change_ratio 2 3 1.5 new_100_5 2 2 &
python3 proposed.py change_ratio 2 3 1.5 new_100_6 2 2 &
python3 proposed.py change_ratio 2 3 1.5 new_100_7 2 2 &
python3 proposed.py change_ratio 2 3 1.5 new_100_8 2 2

python3 proposed.py change_ratio 2 3 3 new_100_1 2 2 &
python3 proposed.py change_ratio 2 3 3 new_100_2 2 2 &
python3 proposed.py change_ratio 2 3 3 new_100_3 2 2 &
python3 proposed.py change_ratio 2 3 3 new_100_4 2 2 &
python3 proposed.py change_ratio 2 3 3 new_100_5 2 2 &
python3 proposed.py change_ratio 2 3 3 new_100_6 2 2 &
python3 proposed.py change_ratio 2 3 3 new_100_7 2 2 &
python3 proposed.py change_ratio 2 3 3 new_100_8 2 2

python3 proposed.py change_ratio 2 3 6 new_100_1 2 2 &
python3 proposed.py change_ratio 2 3 6 new_100_2 2 2 &
python3 proposed.py change_ratio 2 3 6 new_100_3 2 2 &
python3 proposed.py change_ratio 2 3 6 new_100_4 2 2 &
python3 proposed.py change_ratio 2 3 6 new_100_5 2 2 &
python3 proposed.py change_ratio 2 3 6 new_100_6 2 2 &
python3 proposed.py change_ratio 2 3 6 new_100_7 2 2 &
python3 proposed.py change_ratio 2 3 6 new_100_8 2 2

python3 proposed.py change_ratio 2 3 12 new_100_1 2 2 &
python3 proposed.py change_ratio 2 3 12 new_100_2 2 2 &
python3 proposed.py change_ratio 2 3 12 new_100_3 2 2 &
python3 proposed.py change_ratio 2 3 12 new_100_4 2 2 &
python3 proposed.py change_ratio 2 3 12 new_100_5 2 2 &
python3 proposed.py change_ratio 2 3 12 new_100_6 2 2 &
python3 proposed.py change_ratio 2 3 12 new_100_7 2 2 &
python3 proposed.py change_ratio 2 3 12 new_100_8 2 2

python3 proposed.py change_ratio 2 3 24 new_100_1 2 2 &
python3 proposed.py change_ratio 2 3 24 new_100_2 2 2 &
python3 proposed.py change_ratio 2 3 24 new_100_3 2 2 &
python3 proposed.py change_ratio 2 3 24 new_100_4 2 2 &
python3 proposed.py change_ratio 2 3 24 new_100_5 2 2 &
python3 proposed.py change_ratio 2 3 24 new_100_6 2 2 &
python3 proposed.py change_ratio 2 3 24 new_100_7 2 2 &
python3 proposed.py change_ratio 2 3 24 new_100_8 2 2
#-----QLHEFT 2 2 & Propose----------------------------------