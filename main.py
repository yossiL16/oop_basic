from Agent import Agent
from Mission import Mission
from IntelTools import  IntelTools
from Report import Report
from MissionControl import MissionControl

mission = Mission("YY", "TLV")
mission.assigned_agent1(Agent("yt", 9))

mission.brief()

agent1 = Agent("unit 8200", 4)
