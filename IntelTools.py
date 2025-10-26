

class IntelTools:

    def __init__(self):
        pass

    @staticmethod
    def encrypt_message(msg: str):
        return msg[:: -1]

    @staticmethod
    def log_transmission(agent_name: str, message: str):
        print(f"{agent_name} sent encrypted massage: {message}")