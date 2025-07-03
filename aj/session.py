from datetime import datetime 
import uuid


class SessionManager:
    active = []
    def add_session(self,_uuid):
        now = datetime.now()
        session = [item for item in self.active if (now - item[2]).days < 2] 


        suid = str(uuid.uuid4())
        self.active.append((_uuid,suid,datetime.now()))

        session = [item for item in session if (now - item[2]).days < 2]
        print('HEHE',suid)
        return suid

         
    def get_uuid_from (self,suid):
        for session in self.active:
            if session[1] == suid:
                return session[0]
        return None
