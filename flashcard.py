import time
from storage import load_data
from score_tracking import calculate_score
def main():
    tasks=load_data()
    data=tasks["questions"]
    size=len(data)
    player_answer=[]
    for i in range(size):
        answer=input(f"{data[i]}:").strip()
        time.sleep(2)
        player_answer.append(answer)
    print(f"You have scored:{calculate_score(tasks,player_answer)}/3")
if __name__=="__main__":
    main()
