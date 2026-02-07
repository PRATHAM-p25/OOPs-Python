class InstagramAccount:
    def __init__(self, account_name, password):
        self.account_name = account_name

        self._private_reels = []

        self.__archived_reels = []

        self.__password = password

    def add_private_reel(self, reel_name):
        self._private_reels.append(reel_name)

    def display_private_reels(self, is_follower):
        if is_follower:
            print("Private Reels:", self._private_reels)
        else:
            print("Access Denied! Only followers can view private reels")

    def add_archived_reel(self, reel_name):
        self.__archived_reels.append(reel_name)

    def display_archived_reels(self, password):
        if password == self.__password:
            print("Archived Reels:", self.__archived_reels)
        else:
            print("Access Denied! Only account holder can view archived reels")

    def get_archived_reels(self, password):
        if password == self.__password:
            return self.__archived_reels
        else:
            return "Access Denied!"

    def set_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password updated successfully")
        else:
            print("Incorrect old password")

account = InstagramAccount("Duncan", "1234")

account.add_private_reel("Friends trip reel")
account.add_private_reel("Birthday celebration reel")

account.add_archived_reel("Old dance reel")
account.add_archived_reel("College memories reel")

print("\n--- Private Reels ---")
account.display_private_reels(is_follower=True)
account.display_private_reels(is_follower=False)

print("\n--- Archived Reels ---")
account.display_archived_reels("1234")    
account.display_archived_reels("wrong")    

print("\n--- Getter Method ---")
print(account.get_archived_reels("1234"))
print(account.get_archived_reels("wrong"))

print("\n--- Updating Password ---")
account.set_password("1234", "newpass")

print("\n--- Archived Reels After Password Update ---")
account.display_archived_reels("newpass")
