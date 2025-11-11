class Vehicle:
    def __init__(self, vehicle_id: str, type: str, plate_number: str):
        self._vehicle_id = vehicle_id
        self._type = type
        self._plate_number = plate_number

    @property
    def plate_number(self):
        return self._plate_number

    def method(self, type):
        pass