import boto3
aws_access_key_id = "SECRETKEY"
aws_secret_access_key = "access key"
client = boto3.client('batch',
        aws_access_key_id= aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,  
        region_name="us-west-2")


import random
newid = str(random.randint(0,100))
job1 = 'newpijob'+newid
newid2 = str(random.randint(0,100))
job2 = 'newpijob'+newid2
newid3 = str(random.randint(0,100))
job3 = 'newpijob'+newid3


def start_job(jobName, JobQueue, JobDefinition, command, depends,
    memory = 2048, retries = 2, duration = 120 ):
    response = client.submit_job(
        jobName=jobName,
        jobQueue=JobQueue,
        jobDefinition=JobDefinition,
        containerOverrides={
            #'vcpus': 1,
            'command': command,
            'resourceRequirements': [
                {
                    'value': memory,
                    'type': 'MEMORY'
                },
            ]
        },
        dependsOn=depends,
        retryStrategy={
            'attempts': retries
        },
        timeout={
            'attemptDurationSeconds': duration
        }
    )
    print("job ", jobName, " started")
    return response

job1res = start_job(job1, 'quedemo', 'pi_job:2', 
    ["python","/dopi.py",aws_access_key_id,aws_secret_access_key,"fileXx.txt"],[])
job1id = job1res['jobId']

start_job(job2, 'quedemo', 'pi_job2:1', 
    ["python","/dopi2.py",aws_access_key_id,aws_secret_access_key,"fileXx.txt", job2],
    [{ 'jobId': job1id}])

start_job(job3, 'quedemo', 'pi_job2:1', 
    ["python","/dopi2.py",aws_access_key_id,aws_secret_access_key,"fileXx.txt", job3],
    [{ 'jobId': job1id}])