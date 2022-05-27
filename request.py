from enum import IntEnum


class Request:
    class Type(IntEnum):
        ERROR = 0
        MSG = 1
        LOGIN = 2
        REG = 3

    def __init__(self):
        self.type = Request.Type.MSG
        self.data = ""

    def __str__(self):
        return f"{self.type} {self.data}"

    def get_data(self):
        match self.type:
            case Request.Type.ERROR:
                return {"code": self.data}
            case Request.Type.MSG:
                spt = self.data.split(" ")
                return {"target_user": spt[0], "msg": spt[1]}
            case Request.Type.LOGIN:
                spt = self.data.split(" ")
                return {"user": spt[0], "psw": spt[1]}
            case Request.Type.REG:
                spt = self.data.split(" ")
                return {"user": spt[0], "psw": spt[1]}

    @staticmethod
    def msg(target_user: str, msg: str):
        packet = Request()
        packet.type = Request.Type.MSG
        packet.data = f"{target_user} {msg}"

    @staticmethod
    def login(user: str, password: str):
        packet = Request()
        packet.type = Request.Type.LOGIN
        packet.data = f"{user} {password}"

    @staticmethod
    def reg(user: str, password: str):
        packet = Request()
        packet.type = Request.Type.REG
        packet.data = f"{user} {password}"

    @staticmethod
    def error(code: int):
        packet = Request()
        packet.type = Request.Type.LOGIN
        packet.data = f"{code}"

    @staticmethod
    def from_string(s: str):
        if len(s) == 0 or not s[0].isnumeric() and s[0] in Request.Type:
            return None
        packet = Request()
        packet.type = s[0]
        packet.data = s.split(" ")[1]
