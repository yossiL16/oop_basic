from agent import Agent
from mission import Mission

# agent = Agent("yossi", 5)
# misiim = Mission("alon", "tlv",agent)
# print(misiim.brief())


mission = Mission("YY", "TLV")
mission.assigned_agent1(Agent("yt", 9))

mission.brief()