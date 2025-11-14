import time
def calculate_score(data,part):
    answers=data["answers"] 
    score=0
    for i in range(len(answers)):
        if answers[i]==part[i]:
            score+=1
    print("calculating score....")
    time.sleep(3)
    return score