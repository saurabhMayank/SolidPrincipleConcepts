"""
Problems with this class design structure :-
1. UserProfileImageView is passed with all the info the user it does not need
2. It needs only profile image url because it shows only profile image
3. But it is polluted with all the details of the user which is unnecessary
information for that class

"""

class User:
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

    def load_profile_for(self, user: User):
        """
        functionality to load the Profile
        """
        return user.PROFILE_IMAGE_URL
