class System:
    def __init__(self, os_type):
        self.os_type=os_type

class SmartSystem(System):
    def __init__(self, os_type, connectivity):
        super().__init__(os_type)
        self.connectivity=connectivity

class SmartHome(SmartSystem):
    def __init__(self, os_type, connectivity, owner):
        super().__init__(os_type,connectivity)
        self.owner=owner

    def status(self):
        return f'SmartHome of {self.owner} is running {self.os_type} and is currently {self.connectivity}.'

sh1 = SmartHome("Linux", "Online", "Ravi")
print( sh1.status())