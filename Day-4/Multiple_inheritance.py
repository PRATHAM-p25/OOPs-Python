class Camera:
    def __init__(self, camera_quality):
        self.camera_quality = camera_quality

    def display_camera_details(self):
        print("Camera Quality:", self.camera_quality)


class MusicPlayer:
    def __init__(self, sound_quality):
        self.sound_quality = sound_quality

    def display_music_details(self):
        print("Sound Quality:", self.sound_quality)


class SmartPhone(Camera, MusicPlayer):
    def __init__(self, brand, camera_quality, sound_quality):
        self.brand = brand
        Camera.__init__(self, camera_quality)
        MusicPlayer.__init__(self, sound_quality)

    def display_smartphone_details(self):
        print("Brand:", self.brand)


phone = SmartPhone("Samsung", "108MP", "Dolby Atmos")

phone.display_smartphone_details()
phone.display_camera_details()
phone.display_music_details()