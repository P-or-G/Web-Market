from API.lbr import get_status
from imp_control import *


ID_db = 0


def status_check(ID):
    if get_status(ID) == 'usr':
        return True
    return False