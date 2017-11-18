from rest_framework import serializers

from . import models




class HelloSerializer(serializers.Serializer):
    """ selrialzes a name field for testing our API"""


    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """ A serializer for our user profile objects"""

    class Meta:
        model= models.UserProfile
        # we are telling django that which model we want to serialize.
        fields = ('id','email','name','password')
        #here we defining fields which we want to serialize of that particular model
        extra_kwargs = {'password':{'write_only':True}}
        # we dont want user to see other people password thats why it is write only.
        # and extra_kwargs means extra keywords . it gives more control over
        # particular field how they get executed.

        def create(self,validated_data):
            """create and return a new user."""
            # we are overwritng the create function as we want to store the
            # password in hash(actually idonnt have exact idea why we are doing this)
            # validated_data is already passed and valid data that we will be using here

            user = models.UserProfile(
            # here we have created an object of userprofile and email and names are
            # thier arguments.
                   email=validated_data['email'],
                   name = validated_data['name']

            )# here we are storing validiated data in email to get serialized
            #same goes for name.(not sure storing data or serializing.)
# ps needs to see it in action to say anything.
            user.set_password(validated_data['password'])
# its again converting password to hash needs to see it in action to comment any further
            user.save()

            return user
class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """ As serializer for profile feed item"""

    class Meta:

        model = models.ProfileFeedItem
        fields = ('id','user_profile','status_text', 'created_on')
        extra_kwargs = {'user_profile':{'read_only':True}}
        # we have set user_profile to read only beacuse it is an key and we dont
        # users to create  other users or delete feed items. as it is an ForeignKey
        # adn it will be Generated automatically and it will connect UserProfile to
        # our ProfileFeedItem .we dont want to edit their or others foreign keys.

        
