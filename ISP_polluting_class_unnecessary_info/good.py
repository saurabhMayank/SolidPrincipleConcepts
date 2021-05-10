from abc import ABC, abstractmethod

"""
How the problem of bad.py was solved?
1. Earlier UserProfileImageView class was polluted with a lot of info that it 
actually didn't really need.
2. So by defining an abstract class UserProfileViewDetails and defining only the method 
that is needed by UserProfileImageView needs.
3. The abstract is inherited in User class. 
4. class UserProfileImageView now depends on the abstract class UserProfileViewDetails rather
than the whole User class therefore getting only the info it needs.
Will get only the info it needs because of the abstract class dependency.
5. It is no longer polluted by the excess of info.

"""

class UserProfileViewDetails(ABC):
    """
     Abstract class defining methods related to user profile viewing
    """
    PROFILE_IMAGE_URL: str


class User(UserProfileViewDetails):
    """
    Contains the Details of the User
    """
    FIRST_NAME: str
    LAST_NAME: str
    PROFILE_IMAGE_URL: str
    BIO: str
    DOB: str

    def __init__(self, first_name: str, last_name: str, 
                profile_image_url: str, bio:str,dob: str):
        self.FIRST_NAME = first_name
        self.LAST_NAME = last_name
        self.PROFILE_IMAGE_URL = profile_image_url
        self.BIO = bio
        self.DOB = dob

class UserProfileImageView():
    """
     Class which takes care of user profile image view functionality
    """

    def load_profile_for(self, user: UserProfileViewDetails):
        """
        functionality to load the Profile
        """
        return user.PROFILE_IMAGE_URL

first_name = "XY"
last_name = "Z"
profile_image_url = "http://xyz.com"
bio = "I am a coder"
dob = "15081996"
user = User(first_name,last_name,profile_image_url, bio, dob)
user_image_profile = UserProfileImageView()
print("--------------user profile url------------")
print(user_image_profile.load_profile_for(user))

