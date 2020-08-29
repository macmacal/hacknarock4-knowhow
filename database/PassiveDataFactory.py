from datetime import datetime
from data.PassiveData import PassiveData


def get_passive_data():
    pd1 = PassiveData(1, 'TV', 'sony', 'a', 112, datetime.now(), datetime.now())
    pd1.ports['usb'] = 5
    pd1.ports['hdmi'] = 1

    pd2 = PassiveData(2, 'ahjo', 'sony', 'b', 111, datetime.now(), datetime.now())

    pd3 = PassiveData(3, 'router', 'samsung', 'c', 939)
    pd3.ports['usb'] = 2
    pd3.other['temperature'] = 'too damn hot'

    pd4 = PassiveData(4, 'printer')
    pd4.other['ink'] = 'only red ink'

    return [pd1, pd2, pd3, pd4]
