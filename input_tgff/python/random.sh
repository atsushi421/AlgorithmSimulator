#!/usr/bin/bash

#-----remove result---------------------------------------------------------
rm /home/atsushi/evaluation/input_tgff/result/random/HEFT/*.txt
rm /home/atsushi/evaluation/input_tgff/result/random/QLHEFT/*.txt
rm /home/atsushi/evaluation/input_tgff/result/random/Propose/*.txt
#-----remove result---------------------------------------------------------

#-----HEFT-------------------------------------
python3 heft.py random 3 3 3 100_0 2 2 &
python3 heft.py random 3 3 3 100_1 2 2 &
python3 heft.py random 3 3 3 100_2 2 2 &
python3 heft.py random 3 3 3 100_3 2 2 &
python3 heft.py random 3 3 3 100_4 2 2 &
python3 heft.py random 3 3 3 100_5 2 2 &
python3 heft.py random 3 3 3 100_6 2 2 &
python3 heft.py random 3 3 3 100_7 2 2 &

python3 heft.py random 3 3 3 100_8 2 2 &
python3 heft.py random 3 3 3 100_9 2 2 &
python3 heft.py random 3 3 3 100_10 2 2 &
python3 heft.py random 3 3 3 100_11 2 2 &
python3 heft.py random 3 3 3 100_12 2 2 &
python3 heft.py random 3 3 3 100_13 2 2 &
python3 heft.py random 3 3 3 100_14 2 2 &
python3 heft.py random 3 3 3 100_15 2 2 &

python3 heft.py random 3 3 3 100_16 2 2 &
python3 heft.py random 3 3 3 100_17 2 2 &
python3 heft.py random 3 3 3 100_18 2 2 &
python3 heft.py random 3 3 3 100_19 2 2 &
python3 heft.py random 3 3 3 100_20 2 2 &
python3 heft.py random 3 3 3 100_21 2 2 &
python3 heft.py random 3 3 3 100_22 2 2 &
python3 heft.py random 3 3 3 100_23 2 2 &

python3 heft.py random 3 3 3 100_24 2 2 &
python3 heft.py random 3 3 3 100_25 2 2 &
python3 heft.py random 3 3 3 100_26 2 2 &
python3 heft.py random 3 3 3 100_27 2 2 &
python3 heft.py random 3 3 3 100_28 2 2 &
python3 heft.py random 3 3 3 100_29 2 2 &
python3 heft.py random 3 3 3 100_30 2 2 &
python3 heft.py random 3 3 3 100_31 2 2 &

python3 heft.py random 3 3 3 100_32 2 2 &
python3 heft.py random 3 3 3 100_33 2 2 &
python3 heft.py random 3 3 3 100_34 2 2 &
python3 heft.py random 3 3 3 100_35 2 2 &
python3 heft.py random 3 3 3 100_36 2 2 &
python3 heft.py random 3 3 3 100_37 2 2 &
python3 heft.py random 3 3 3 100_38 2 2 &
python3 heft.py random 3 3 3 100_39 2 2 &
#-----HEFT-------------------------------------

#-----QLHEFT 2 2 & & Propose----------------------------------
python3 proposed.py random 3 3 3 100_0 2 2 &
python3 proposed.py random 3 3 3 100_1 2 2 &
python3 proposed.py random 3 3 3 100_2 2 2 &
python3 proposed.py random 3 3 3 100_3 2 2 &
python3 proposed.py random 3 3 3 100_4 2 2 &
python3 proposed.py random 3 3 3 100_5 2 2 &
python3 proposed.py random 3 3 3 100_6 2 2 &
python3 proposed.py random 3 3 3 100_7 2 2

python3 proposed.py random 3 3 3 100_8 2 2 &
python3 proposed.py random 3 3 3 100_9 2 2 &
python3 proposed.py random 3 3 3 100_10 2 2 &
python3 proposed.py random 3 3 3 100_11 2 2 &
python3 proposed.py random 3 3 3 100_12 2 2 &
python3 proposed.py random 3 3 3 100_13 2 2 &
python3 proposed.py random 3 3 3 100_14 2 2 &
python3 proposed.py random 3 3 3 100_15 2 2

python3 proposed.py random 3 3 3 100_16 2 2 &
python3 proposed.py random 3 3 3 100_17 2 2 &
python3 proposed.py random 3 3 3 100_18 2 2 &
python3 proposed.py random 3 3 3 100_19 2 2 &
python3 proposed.py random 3 3 3 100_20 2 2 &
python3 proposed.py random 3 3 3 100_21 2 2 &
python3 proposed.py random 3 3 3 100_22 2 2 &
python3 proposed.py random 3 3 3 100_23 2 2

python3 proposed.py random 3 3 3 100_24 2 2 &
python3 proposed.py random 3 3 3 100_25 2 2 &
python3 proposed.py random 3 3 3 100_26 2 2 &
python3 proposed.py random 3 3 3 100_27 2 2 &
python3 proposed.py random 3 3 3 100_28 2 2 &
python3 proposed.py random 3 3 3 100_29 2 2 &
python3 proposed.py random 3 3 3 100_30 2 2 &
python3 proposed.py random 3 3 3 100_31 2 2

python3 proposed.py random 3 3 3 100_32 2 2 &
python3 proposed.py random 3 3 3 100_33 2 2 &
python3 proposed.py random 3 3 3 100_34 2 2 &
python3 proposed.py random 3 3 3 100_35 2 2 &
python3 proposed.py random 3 3 3 100_36 2 2 &
python3 proposed.py random 3 3 3 100_37 2 2 &
python3 proposed.py random 3 3 3 100_38 2 2 &
python3 proposed.py random 3 3 3 100_39 2 2
#-----QLHEFT 2 2 & & Propose----------------------------------