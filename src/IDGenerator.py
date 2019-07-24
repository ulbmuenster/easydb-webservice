from flask_jwt_extended import fresh_jwt_required


class IDGenerator():

    @fresh_jwt_required
    def generate(self):
        return 1
