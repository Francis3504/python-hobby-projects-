from base import load_data,save_points
import time
def find_winner(computer,player):
    winner={  ("rock","scissors"):{"scores":(1,0) ,"player":"lost"},
              ("scissors","rock"):{"scores":(0,1),"player":"won"},
              ("rock","paper"):{"scores":(0,1),"player":"won"},
              ("paper","rock"):{"scores":(1,0),"player":"lost"},
              ("scissors","paper"):{"scores":(1,0),"player":"lost"},
              ("paper","scissors"):{"scores":(0,1),"player":"won"}}
    
    answers=(computer,player)
    stats=winner.get(answers,{"scores":(0.5,0.5),"player":"It's a draw"})
    print("......")
    time.sleep(1)
    status=stats["player"]
    print(f"You've {status}") if status in ["won","lost"] else print(f"{status}")
    score=stats["scores"]
    save_points([{"computer":score[0],"player":score[1]}])

def dispay_points():
    points=load_data()
    size=len([float(c["computer"].strip()) for c in points])
    computer=sum([float(c["computer"].strip()) for c in points ])
    player=sum([float(p["player"].strip()) for p in points])
    print(f"Out of {size} rounds ")
    return computer,player