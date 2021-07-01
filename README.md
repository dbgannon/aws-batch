# aws-batch
This is the repo for the aws-batch and aws MPI example.   There are two docker files.  docker contains the dopi.py function and docker2 contains dopisecond.py.  These are used in the startbatchjob_workflowfake.py.   this is "fake" because it does not contain aws credentials.  

for the MPI program there is the aws_batchcconfig.config file.  you will need to modify the networking.   the MPI C program mpi_hello_world.c and the script for submitting it from the head node is submmit_mpi.sh

