
import subprocess
subprocess.run(["python", "Runnables/Initial.py"]) #To create National-Winning Stats
subprocess.run(["python", "Runnables/drop_down.py"]) #To create State Seat Winning stats
subprocess.run(["python", "Runnables/next_scene.py"]) #To create per state, Constituency winning of each party, and the margin
print("Scraping done... begining preprocessing")
subprocess.run(["python", "Runnables/merge.py"]) #To create merged list of all 543 constituency and associated details
subprocess.run(["python", "Runnables/leading.py"]) #To create state wise list of leading parties(Maximum seats per state
subprocess.run(["python", "Runnables/State_competition.py"]) #To create comparison between Top 2 parties of each state
