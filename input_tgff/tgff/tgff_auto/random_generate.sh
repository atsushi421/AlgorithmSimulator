#!/usr/bin/bash

rm generate_log.txt

for ((i=0 ; i<200 ; i++))
do
python3 change_option.py
./tgff3_1.exe test
rm test.vcg
mv test.eps random_${i}.eps
mv random_${i}.eps ./random_dag/
mv test.tgff random_${i}.tgff
mv random_${i}.tgff ./random_dag/
done

python3 change_dag_name.py