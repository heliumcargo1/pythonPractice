import time
waitTime = 1
maxTries = 5
attempts = 0

while attempts <maxTries:
    print("attempts",attempts,"wait time = ",waitTime)
    time.sleep(waitTime)
    waitTime*=2
    attempts += 1
