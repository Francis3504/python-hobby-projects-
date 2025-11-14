import json,os
File="quiz.json"
def load_data():
    if not os.path.exists(File):
        print("File doesn't exist")
    try:
     with open(File) as f:
      return json.load(f)
    except json.JSONDecodeError as e:
       print("error:",e)
       
