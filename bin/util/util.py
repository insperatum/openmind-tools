import sys
import os

single_args = ['-H', '-h', '-I', '-O', '-s', '-u', '-V', '-v', '-W']

path = os.path.dirname(os.path.realpath(__file__))
def parse_slurm(args):
	"""
	Parses:
	["om-anything", "sbatch", "--qos=blah", "-O", "-t" "1:23:45", "foo.sh", "-v", "1"]
	Into
	[["--qos=blah", "-O", "-t" "1:23:45"], ["foo.sh", "-v", "1"]]
	"""
	assert(args[0]=="sbatch" or args[0]=="srun")
	cmd=args[0]
	awaiting_value = False
	for idx in range(1, len(args)):
		if args[idx][:2]=='--':
			continue
		elif args[idx][0]=='-':
			if args[idx] not in single_args:
				awaiting_value=True
			continue
		elif awaiting_value:
			awaiting_value=False
			continue
		else:
			break

	return cmd, args[1:idx], args[idx:]

def sbatch_job_id(cmd):
	"""
	run a command beginning with sbatch and get the returned jobid
	"""
	x = os.popen(cmd + " | cut -d' ' -f4").read()[:-1]
	sys.stdout.flush()
	return x
