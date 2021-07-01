// Copyright 2011 www.mpitutorial.com
//
// An intro MPI hello world program that uses MPI_Init, MPI_Comm_size,
// MPI_Comm_rank, MPI_Finalize, and MPI_Get_processor_name.
//
#include <mpi.h>
#include <stdio.h>
#include <stddef.h>

int main(int argc, char** argv) {
  // Initialize the MPI environment. The two arguments to MPI Init are not
  // currently used by MPI implementations, but are there in case future
  // implementations might need the arguments.
  MPI_Init(NULL, NULL);

  // Get the number of processes
  int world_size;
  MPI_Comm_size(MPI_COMM_WORLD, &world_size);

  // Get the rank of the process
  int world_rank;
  MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

  // Get the name of the processor
  char processor_name[MPI_MAX_PROCESSOR_NAME];
  int name_len;
  MPI_Get_processor_name(processor_name, &name_len);

  // Print off a hello world message
  printf("Hello world from processor %s, rank %d out of %d processors\n",
         processor_name, world_rank, world_size);
int number;
    if (world_rank == 0) {
        number = 11;
        printf("process 0 sending\n");
        MPI_Send(&number, 1, MPI_INT, 1, 10, MPI_COMM_WORLD);
        sleep(5);

    } else if (world_rank < world_size) {
        printf("process %d recieving now\n", world_rank);
        MPI_Status stat;
        MPI_Recv(&number, 1, MPI_INT, world_rank-1, 10, MPI_COMM_WORLD, &stat);
        printf("Process %d received number %d from process %d\n",world_rank,
            number, world_rank-1);
        fflush(stdout);
        number++;
        if (world_rank + 1 < world_size){
            printf("process %d sending\n", world_rank);
            MPI_Send(&number, 1, MPI_INT, world_rank+1, 10, MPI_COMM_WORLD);
        sleep(5);
        }
    }
    int global_sum;
    global_sum = -1;
    MPI_Reduce(&number, &global_sum, 1, MPI_INT, MPI_SUM, 0,
            MPI_COMM_WORLD);
    

  // Finalize the MPI environment. No more MPI calls can be made after this
  MPI_Finalize();
}
