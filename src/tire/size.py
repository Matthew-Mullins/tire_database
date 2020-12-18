import sqlite3
'''
Size(
    Tire Type
    Tire Width
    Aspect Ratio
    Construction Type (R, D, F(Runflats))
    Wheel Diameter
    Load Index
    Speed Rating
)
'''
class Size:
    possible_values = {
        'tire_type': [
            'P',
            'LT',
            'ST'
        ],
        'construction_type': [
            'R',
            'ZR'
            'FR',
            'D',
            'FD',
        ],
        'speed_rating': [
            'A1',
            'A2',
            'A3',
            'A4',
            'A5',
            'A6',
            'A7',
            'A8',
            'B',
            'C',
            'D',
            'E',
            'F',
            'G',
            'H',
            'J',
            'K',
            'L',
            'M',
            'N',
            'P',
            'Q',
            'R',
            'S',
            'T',
            'U',
            'H',
            'V',
            'W',
            'Y',
            '(Y)'
        ]
    }

    def __init__(self):
        pass

    def __conform__(self, protocol):
        if protocol is sqlite3.PrepareProtocol:
            pass