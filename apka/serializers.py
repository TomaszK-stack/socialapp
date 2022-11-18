from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Profile , Friendship , Invitation


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile

        fields = [
            'id',
            'name' ,
            'surname' ,
            'username' ,

        ]


# class UserSer(ModelSerializer):
#     class Meta:
#         model = User
#         fields =
#         [
#             'id'
#         ]


class InvitationSer(ModelSerializer):
    class Meta:
        model = Invitation
        fields = [
            'from_som' ,
            'to_som' ,
            'accepted' ,

        ]
