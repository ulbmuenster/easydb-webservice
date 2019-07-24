from flask_jwt_extended import fresh_jwt_required


class DataBaseConnector:

    @fresh_jwt_required
    def __init__(self):
        # Connection Logic mit SQLAlchemy hier
        pass
