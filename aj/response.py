from enum import Enum
class ResponseCode(Enum):
    OK = 0
    ERROR = 1
    FAIL = 2

class Response:
    code:ResponseCode
    data:object
    def obj(self):
        return {'code':self.code.value, 'data':self.data};
