To use, include bin in your $PATH.

# om-repeat

To split up a long job into a recurring small job. Example:

```om-repeat sbatch -t 60 foo.sh```

This job will relaunch every time it stops due to timeout (or preemption), until it completes successfully or throws an error.

NOTE: Requires that all sbatch options are given as command line arguments, rather than in the header of `foo.sh`
