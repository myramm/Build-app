init -10 python:
    class MailBoxManager(object):
        def __init__(self, name, unlocked_mails=[]):
            self.name = name
            self.current_mail = None
            self._next_mail = None
            self._available_mails = {"m_pizza_pamphlet": False,
                                     "m_newspaper": False,
                                     "m_erik_package": False,
                                     "m_dad_letter": False,
                                     "m_magazine": False,
                                     "m_orcette_package": False,
                                     "m_bank_statement": False}
            self.unlock_mail(*unlocked_mails)
        
        def __eq__(self, other):
            if self.current_mail is None:
                return False
            elif isinstance(other, unicode) or isinstance(other, str):
                return self.current_mail.lower() == other.lower()
            else:
                return False
        
        def __bool__(self):
            return self.current_mail is not None
        
        def __nonzero__(self):
            return self.__bool__()
        
        def unlock_mail(self, *mails):
            for mail in mails:
                self._available_mails[mail] = True
        
        def lock_mail(self, *mails):
            for mail in mails:
                self._available_mails[mail] = False
        
        @property
        def available_mails(self):
            return [k for k, v in self._available_mails.items() if v]
        
        @property
        def get(self):
            return self.current_mail if self.current_mail is not None else False
        
        def randomize(self):
            if self._next_mail:
                self.current_mail = self._next_mail
            elif not random.randint(0, 4):
                self.current_mail = random.choice(self.available_mails)
            else:
                self.current_mail = None
        
        @classmethod
        def randomize_all(cls):
            for mailbox in game.mail.values():
                mailbox.randomize()
        
        def set(self, mail):
            
            
            if mail not in self._available_mails:
                raise RuntimeError('Invalid mail: {}'.format(mail))
            if self._next_mail:
                return False
            self._next_mail = mail
            return True
        
        def reset(self):
            self._next_mail = None
        
        def take(self):
            self.reset()
            self.current_mail = None
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
