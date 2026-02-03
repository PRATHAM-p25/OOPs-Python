# For the Given code add the comments, Creator_name, Location and their display methods . 
# Note comments should be a list of strings. 

# Add a delete method to delete the last comments when ever that method is 
# called with respective object.

# Class and object


class Instagram:
    def __init__(self,title, description,creator_name,location):    
        self.title = title
        self.description = description
        self.likes = 0
        self.creator_name = creator_name 
        self.location = location
        self.comments = [] 
    def display_title(self):
        print("The title of the reel is ",self.title)
    def display_description(self):
        print("The description of the reel is ",self.description)
    def display_likes(self):
        print("The likes of the reel is ",self.likes)
    def liked(self):
        self.likes += 1
    def disliked(self):
        if self.likes > 0:
            self.likes-=1 
    def display_creator_name(self):
        print("The creator name is ",self.creator_name) 
    def display_location(self):
        print("The location is ",self.location)
    def display_comment(self):
        if len(self.comments) == 0:
            print("No comments yet")
        else:
            print("The comments are ")
            for comment in self.comments: 
                print("-",comment)
    def add_comments(self,comment):
        self.comments.append(comment)
    def delete_last_comment(self):
        temp_comment=self.comments.pop()
        print("The last comment is deleted ",temp_comment)


        


reel1=Instagram("dancing","dancing with friends","John","New York")
# comment=[]

reel1.add_comments("comment1")
reel1.display_comment()
reel1.delete_last_comment()
reel1.display_comment()




# reel2=Instagram("finance minister conference","finance minister conference with friends","Jane","London") 
# reel1.display_title()
# reel1.display_description()
# reel1.display_creator_name()
# reel1.display_location()
# reel1.display_comment()
