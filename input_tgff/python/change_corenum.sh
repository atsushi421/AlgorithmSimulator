#!/usr/bin/bash

#-----remove result---------------------------------------------------------
rm /home/atsushi/evaluation/input_tgff/result/change_corenum/HEFT/*.txt
rm /home/atsushi/evaluation/input_tgff/result/change_corenum/QLHEFT/*.txt
rm /home/atsushi/evaluation/input_tgff/result/change_corenum/Propose/*.txt
#-----remove result---------------------------------------------------------

#-----HEFT-------------------------------------
python3 heft.py change_corenum 2 2 3 new_100_60_1 2 2
python3 heft.py change_corenum 2 2 3 new_100_60_2 2 2
python3 heft.py change_corenum 2 2 3 new_100_60_3 2 2
python3 heft.py change_corenum 2 2 3 new_100_60_4 2 2
python3 heft.py change_corenum 2 2 3 new_100_60_5 2 2
python3 heft.py change_corenum 2 2 3 new_100_60_6 2 2
python3 heft.py change_corenum 2 2 3 new_100_60_7 2 2
python3 heft.py change_corenum 2 2 3 new_100_60_8 2 2

python3 heft.py change_corenum 2 3 3 new_100_60_1 2 2
python3 heft.py change_corenum 2 3 3 new_100_60_2 2 2
python3 heft.py change_corenum 2 3 3 new_100_60_3 2 2
python3 heft.py change_corenum 2 3 3 new_100_60_4 2 2
python3 heft.py change_corenum 2 3 3 new_100_60_5 2 2
python3 heft.py change_corenum 2 3 3 new_100_60_6 2 2
python3 heft.py change_corenum 2 3 3 new_100_60_7 2 2
python3 heft.py change_corenum 2 3 3 new_100_60_8 2 2

python3 heft.py change_corenum 2 4 3 new_100_60_1 2 2
python3 heft.py change_corenum 2 4 3 new_100_60_2 2 2
python3 heft.py change_corenum 2 4 3 new_100_60_3 2 2
python3 heft.py change_corenum 2 4 3 new_100_60_4 2 2
python3 heft.py change_corenum 2 4 3 new_100_60_5 2 2
python3 heft.py change_corenum 2 4 3 new_100_60_6 2 2
python3 heft.py change_corenum 2 4 3 new_100_60_7 2 2
python3 heft.py change_corenum 2 4 3 new_100_60_8 2 2

python3 heft.py change_corenum 2 5 3 new_100_60_1 2 2
python3 heft.py change_corenum 2 5 3 new_100_60_2 2 2
python3 heft.py change_corenum 2 5 3 new_100_60_3 2 2
python3 heft.py change_corenum 2 5 3 new_100_60_4 2 2
python3 heft.py change_corenum 2 5 3 new_100_60_5 2 2
python3 heft.py change_corenum 2 5 3 new_100_60_6 2 2
python3 heft.py change_corenum 2 5 3 new_100_60_7 2 2
python3 heft.py change_corenum 2 5 3 new_100_60_8 2 2
#-----HEFT-------------------------------------

#-----QLHEFT 2 2 & Propose----------------------------------
python3 proposed.py change_corenum 2 2 3 new_100_60_1 2 2 &
python3 proposed.py change_corenum 2 2 3 new_100_60_2 2 2 &
python3 proposed.py change_corenum 2 2 3 new_100_60_3 2 2 &
python3 proposed.py change_corenum 2 2 3 new_100_60_4 2 2 &
python3 proposed.py change_corenum 2 2 3 new_100_60_5 2 2 &
python3 proposed.py change_corenum 2 2 3 new_100_60_6 2 2 &
python3 proposed.py change_corenum 2 2 3 new_100_60_7 2 2 &
python3 proposed.py change_corenum 2 2 3 new_100_60_8 2 2

python3 proposed.py change_corenum 2 3 3 new_100_60_1 2 2 &
python3 proposed.py change_corenum 2 3 3 new_100_60_2 2 2 &
python3 proposed.py change_corenum 2 3 3 new_100_60_3 2 2 &
python3 proposed.py change_corenum 2 3 3 new_100_60_4 2 2 &
python3 proposed.py change_corenum 2 3 3 new_100_60_5 2 2 &
python3 proposed.py change_corenum 2 3 3 new_100_60_6 2 2 &
python3 proposed.py change_corenum 2 3 3 new_100_60_7 2 2 &
python3 proposed.py change_corenum 2 3 3 new_100_60_8 2 2

python3 proposed.py change_corenum 2 4 3 new_100_60_1 2 2 &
python3 proposed.py change_corenum 2 4 3 new_100_60_2 2 2 &
python3 proposed.py change_corenum 2 4 3 new_100_60_3 2 2 &
python3 proposed.py change_corenum 2 4 3 new_100_60_4 2 2 &
python3 proposed.py change_corenum 2 4 3 new_100_60_5 2 2 &
python3 proposed.py change_corenum 2 4 3 new_100_60_6 2 2 &
python3 proposed.py change_corenum 2 4 3 new_100_60_7 2 2 &
python3 proposed.py change_corenum 2 4 3 new_100_60_8 2 2

python3 proposed.py change_corenum 2 5 3 new_100_60_1 2 2 &
python3 proposed.py change_corenum 2 5 3 new_100_60_2 2 2 &
python3 proposed.py change_corenum 2 5 3 new_100_60_3 2 2 &
python3 proposed.py change_corenum 2 5 3 new_100_60_4 2 2 &
python3 proposed.py change_corenum 2 5 3 new_100_60_5 2 2 &
python3 proposed.py change_corenum 2 5 3 new_100_60_6 2 2 &
python3 proposed.py change_corenum 2 5 3 new_100_60_7 2 2 &
python3 proposed.py change_corenum 2 5 3 new_100_60_8 2 2
#-----QLHEFT 2 2 & Propose----------------------------------