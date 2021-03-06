from models.community_model import Community


class Delegacy(Community):
    """
    Attributes:
        name (str)
        administrative_number (int)
        voivodeship (Voivodeship)
        county (CountyArea)
        community (Community)
        area_type (str)
    """

    area_type = 'delegatura'
