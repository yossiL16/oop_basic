from Report import Report

class MissionControl:

    @staticmethod
    def analyze_report( r: Report):

        if r.urgency_level <= 4:
            return "Immediate response required."

        elif r.urgency_level == 3:
            return "High priority. Monitor closely."

        else:
            return "High priority. Monitor closely."


