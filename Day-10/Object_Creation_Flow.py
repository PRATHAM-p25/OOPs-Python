class User:

    def __new__(cls, *args, **kwargs):
        print("Object is being created")
        return super().__new__(cls)

    def __init__(self, name):
        print("Object is initialized")
        self.name = name


u1 = User("Aegon")
