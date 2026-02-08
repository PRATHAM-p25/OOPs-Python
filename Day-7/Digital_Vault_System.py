class Vault:
    def __init__(self, password):
        self.__password = password
        self.__is_locked = True

    def unlock(self, password):
        if password == self.__password:
            self.__is_locked = False

    def lock(self):
        self.__is_locked = True

    def is_opened(self):
        return not self.__is_locked
    
v1 = Vault("1234")
v1.unlock("0000")
print( v1.is_opened())