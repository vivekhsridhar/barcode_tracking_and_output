## Resources limits: about of wall time that you allow (after this time has passed, the job will stop)
#PBS -l walltime=120:00:00
#PBS -l nodes=1:ppn=12
###PBS -l cput = 02:00:00
#PBS -S /bin/bash
### Name of the job on the queue
#PBS -n ${0}

### Output files
#PBS -e $HOME/multinodes/log_e1.txt
#PBS -o $HOME/multinodes/log_o1.txt

module load devel/python/3.5.1
module load cs/opencv/3.3.1-python-3.5-mkl-2018

#echo "Log Location should be: [ $LOG_LOCATION ]file"
python3 $HOME/multinodes/tracking.py
