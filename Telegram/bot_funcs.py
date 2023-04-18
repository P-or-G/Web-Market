from API.lbr import get_status
from imp_control import *


def status_check(ID):
    if get_status(ID) == 'usr':
        return False
    return True