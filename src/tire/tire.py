from .size import Size
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
Brand
Model
M+S
SNOWFLAKE
ALL-SEASON
Load Range / Ply Rating
Tread Depth
Quantity
Price
Notes
Location
Status(
    Pictures
    Posted
    NFS
)
'''

class Tire():
    brand = ''
    model = ''
    mud_snow = False
    snowflake = False
    all_season = False
    load_range = ''
    tread_depth = 0
    quantity = 0
    price = 0.
    notes = ''
    location = ''
    status = ''
    Size = None

    def __init__(self):
        pass

    def __repr__(self):
        pass