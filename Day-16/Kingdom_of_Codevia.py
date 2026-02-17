class RoyalMessenger:
    def deliver(self, message):
        return f'Delivered: {message}'

class UrgentMessenger(RoyalMessenger):
    def deliver(self, message):
        return f'URGENT: Delivered: {message}'



# Example usage
royal = RoyalMessenger()
urgent = UrgentMessenger()
print(royal.deliver("Your taxes are due."))
print(urgent.deliver("Enemy at the gates!"))