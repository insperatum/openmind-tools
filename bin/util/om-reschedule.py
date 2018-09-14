#!/bin/bash
""":"
python $0 $@
exit
":"""

import os
import sys
import util

job_id = os.environ['SLURM_JOBID']
cmd, arg, post = util.parse_slurm(sys.argv[1:])
assert(cmd=="sbatch")
arg = [x for x in arg if x[:13]!="--dependency="]

#print("SLURM_JOB_NAME:", os.environ['SLURM_JOB_NAME'])
print(' '.join(['sbatch'] + arg + ['--dependency=singleton'] + ["om-run", util.path + "/om-reschedule.py"] + [cmd] + arg + post))

next_job_id = util.sbatch_job_id(' '.join(['sbatch'] + arg + ['--dependency=singleton'] + ["om-run", util.path + "/om-reschedule.py"] + [cmd] + arg + post))
os.system(' '.join(post))
os.system("scancel " + next_job_id)
