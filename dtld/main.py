__author__ = 'David Dexter'
from DTLD.lib.protocol import Protocol
from DTLD.lib.top_domain import TopDomain
class TopLevelDomain:
    def __init__(self,domain):
        self.domain = domain
    def get_top_level_domain(self):
        check = Protocol(self.domain)
        checkDM = check.check_protocol()
        if checkDM == False:
            print('Invalid Domain')
        else:
            get = TopDomain(self.domain)
            srch = get.extractor()
            if srch == False:
                print ('Could not get domain')
            else:
                #print(srch)
                return srch
