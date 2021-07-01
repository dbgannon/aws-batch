import random
from time import sleep
def DoPi(numpts):
    inside = 0.
    for i in range(numpts):
        x = random.random()
        y = random.random()
        if(x*x + y*y < 1. ):
            inside += 1
    pi = inside*4/numpts   
    return pi
print(DoPi(100000))
import sys
import boto3

if __name__ == '__main__':
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")
    access_key_id = sys.argv[1]
    secret_key = sys.argv[2]
    file_name = sys.argv[3]
    sleep(120)
    s3 = boto3.resource( 's3',
        aws_access_key_id=access_key_id,
        aws_secret_access_key=secret_key) 
    s3.Bucket('dbgbatch-bucket').put_object(Key=file_name, Body='hello thered')
    
