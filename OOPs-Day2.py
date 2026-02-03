class Instagram:
    def __init__(self, title, description, creator_name, location):
        self.title = title
        self.description = description
        self.creator_name = creator_name
        self.location = location
        self.likes = 0
        self.comments = []

    def display_title(self):
        print("The title of the reel is ", self.title)
    def display_description(self):
        print("The description of the reel is ", self.description)
    def display_creator(self):
        print("The creator of the reel is ", self.creator_name)
    def display_location(self):
        print("The location of the reel is ", self.location)
    def display_likes(self):
        print("The likes of the reel is ", self.likes)
    def display_comments(self):
        if len(self.comments) == 0:
            print("No comments yet")
        else:
            print("The comments are ")
            for comment in self.comments: 
                print("-",comment)
    def liked(self):
        self.likes += 1

    def disliked(self):
        if self.likes > 0:
            self.likes -= 1

    def add_comment(self, comment):
        self.comments.append(comment)

    def remove_last_comment(self):
        if self.comments:
            self.comments.pop()


reel1 = Instagram("dancing", "dancing with friends", "XYZ", "Mysore")

reel1.display_title()
reel1.display_description()
reel1.display_creator()
reel1.display_location()
reel1.liked()
reel1.liked()
reel1.display_likes()
reel1.add_comment("Nice dance")
reel1.add_comment("Awesome")
reel1.display_comments()
reel1.disliked()
reel1.display_likes()


reel2 = Instagram("finance minister conference", "finance minister conference with friends", "ABCD", "Delhi")

reel2.display_title()
reel2.display_description()
reel2.display_creator()
reel2.display_location()
reel2.liked()
reel2.liked()
reel2.liked()
reel2.display_likes()
reel2.add_comment("Informative")
reel2.display_comments()
reel2.disliked()
reel2.display_likes()


print(id(reel1))
print(id(reel2))

reel1.remove_last_comment()
reel1.display_comments()


