from datetime import datetime

from data.ActiveData import ActiveData
from data.PassiveData import PassiveData
from database.EntityDAO import EntityDAO
import constants


def get_data():
    pd1 = PassiveData(1, 'TV', 'sony', 'a', 112, datetime.now(), datetime.now())
    pd1.ports['usb'] = 5
    pd1.ports['hdmi'] = 1
    pd1.tutorials.append(ActiveData('Gdzie jest pilot?', 'za kanapom'))

    pd2 = PassiveData(2, 'ahjo', 'sony', 'b', 111, datetime.now(), datetime.now())

    pd3 = PassiveData(3, 'router', 'samsung', 'c', 939)
    pd3.ports['usb'] = 2
    pd3.other['temperature'] = 'too damn hot'

    pd4 = PassiveData(4, 'printer')
    pd4.tutorials.append(ActiveData('Drukarka nie dziaa', 'kup nowom'))
    pd4.tutorials.append(ActiveData('Toner sie skońyu', 'użyj soku porzeczkowego'))
    pd4.other['ink'] = 'only red ink'

    return [pd1, pd2, pd3, pd4]


def get_data_from_database():
    pdd = EntityDAO(constants.DATABASE_PATH, constants.DOCUMENTS_PATH)
    return pdd.get_all_data()
