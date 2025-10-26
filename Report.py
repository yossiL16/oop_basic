from Agent import Agent

class Report:

    def __init__(self, summary, urgency_level):
        self.summary = summary
        self.urgency_level = urgency_level
        self.submitted_by = None

    def submitted_by1(self, agent: Agent):
        self.submitted_by = agent