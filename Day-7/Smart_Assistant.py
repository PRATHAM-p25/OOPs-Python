class Speaker:
    def speak(self, message):
        return f"Speaking: {message}"

class Scheduler:
    def schedule(self, task, time):
        return f"Scheduled {task} at {time}"

class SmartAssistant(Speaker, Scheduler):
    pass

c1=SmartAssistant()
print(c1.speak("Hello"))
print(c1.schedule("meeting","10:00 AM"))