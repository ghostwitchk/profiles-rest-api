from rest_framework import permissions



class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    # what we are trying to do is that we dont want any other user to edit or delete
    # other objects or profile.so we are defining permissions so that he can only view
    # other profiles but not able to edit or delete them.he woould be able to edit
    # his own profile.
    # we want user to edit or delete his own profile and able to only view other's
    # profiles.

    def has_object_permission(self,request,view,obj):
        """check user is trying to edit own profile only"""
        # it is an function that is predefined in permissions class .it just
        # returns true or false whether the user will get permission to do what
        # he wants to do or not.
        # there is a list of methods that are being known as 'SAFE_METHODS'
        # SAFE_METHODS are the list of HTTP methods that are being regarded as
        # safe by Django not destructive. means methods that can only view the other
        # objects or profiles  but not able to edit them.so HHTP GET is a SAFE_METHODS.

        if request.method in permissions.SAFE_METHODS :
            return True
        # if there is a safe method in if statement then only it will run and return true .
        # it is checking that the method that is there in request whether it lies
        # in SAFE_METHODS or not.if not then this 'if 'statement wont get executed
        # if the method in rquest lies in SAFE_METHODS then it will allow that
        # method to get executed.
        # once this 'if' statement gets executed then system wont go any further in
        # this 'has_object_permission' function ( as a function can only
        #return once and returning is the end of a function).it will allow user what he wants
        # to do. but if the 'if' statement doesnt get executed then it will go further
        # in this 'has_object_permission' function and will check the next condition

        return obj.id == request.user.id
    # here it is comparing the id's of the user object and the object he is trying
    # to edit is same or not.if its same then it will return true and if isnt
    # his request wont get accepted
    # here obj.id is the id of the object that user is trying to edit
    # here request.user.id is the id of the user who is trying to edit objects
    # this 'return obj.id==request.user_set.id' will get executed if the above
    # 'if statement' wont get executed.that means that the user was trying to use destructive
    # methods . he cannot use destructive methods on other objects or profiles
    # he can only use destructive methods on his profile .so that is why we are
    # checking after the rejection of the 'if statement' that the user is trying
    # to use destructive on his profile or not. as it got cleared that he is trying
    # to use destructive methods as the 'if statement' didnt execute.if 'if statement'
    # got executed then the system wont reach til 'return obj.id==request.user.id'
    # he cannot use destructive methods on other profiles

class PostOwnStatus(permissions.BasePermission):
    """allows users to update their own status."""
    # this permissions is for feed api .
    # and for more info read above descriptions.

    def has_object_permission(self,request,view,obj):
        """checks the user is trying to update their own status."""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
# dont know why we are using foriegn key to get user's id this time.
