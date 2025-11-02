from Agent import Agent
from Mission import Mission
from IntelTools import  IntelTools
from Report import Report
from MissionControl import MissionControl

# mission = Mission("YY", "TLV")
# mission.assigned_agent1(Agent("yt", 9))
#
# mission.brief()
#
# agent1 = Agent("unit 8200", 4)
#
# d = IntelTools()
# print(d.encrypt_message("yossi"))
# d.log_transmission("yossi", "i'm in hermon class")

agent =Agent("yossi", 6)

report = Report("dachuf meod", 4)
report.submitted_by1(agent)

MissionControl.analyze_report(report)
IntelTools.log_transmission(agent.code_name, MissionControl.analyze_report(report))