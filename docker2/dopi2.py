import random
def DoPi(numpts):
    inside = 0.
    for i in range(numpts):
        x = random.random()
        y = random.random()
        if(x*x + y*y < 1. ):
            inside += 1
    pi = inside*4/numpts   
    return pi
import sys
import boto3
from time import sleep
if __name__ == '__main__':
    print(DoPi(100000))
    print(f"Arguments count: {len(sys.argv)}")
    access_key_id = sys.argv[1]
    secret_key = sys.argv[2]
    file_name = sys.argv[3]
    job_name = sys.argv[4]
    sleep(60)
    s3 = boto3.resource( 's3',
        aws_access_key_id=access_key_id,
        aws_secret_access_key=secret_key) 
    s3client = boto3.client( 's3',
        aws_access_key_id=access_key_id,
        aws_secret_access_key=secret_key) 
    found = False
    tries = 0
    while not found:
        for obj in s3.Bucket('dbgbatch-bucket').objects.all():
            key = obj.key
            print(key)
            if key == file_name:
                found = True
        if found == False:    
            tries +=1
            print("sleeping")
            sleep(5)
        if tries > 3: break
    if found:
        obj = s3client.get_object(Bucket='dbgbatch-bucket', Key=file_name)
        s = obj['Body'].read()
        s = s + b' and now stuff added'
        s3.Bucket('dbgbatch-bucket').put_object(Key=job_name+'_second_'+file_name, Body=s)
    else:
       print("failed to find ", file_name) 
