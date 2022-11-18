from rest_framework import generics, permissions
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin
from .models import *
from .serializers import *
from rest_framework import filters
from rest_framework.decorators import api_view
from django.contrib.auth.models import User


class ProfileView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self , request , *args , **kwargs):
        queryset = self.get_queryset()
        serializer = ProfileSerializer(queryset , many = True)
        return Response(serializer.data)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = "pk"




class UpdateApiView(generics.UpdateAPIView):

    serializer_class = ProfileSerializer
    lookup_field = "pk"
    queryset = Profile.objects.all()
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]




    def get(self , request ,pk=None, *args , **kwargs):
        queryset = [self.get_object()]
        serializer = ProfileSerializer(queryset, many = True )

        return Response(serializer.data)

class Profilelistview(generics.ListAPIView):

    serializer_class = ProfileSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return Profile.objects.filter(name = name)


class ListaProfili(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

@api_view(["POST", "GET"])
def add_invitation(request, username_from, username_to):

    from_som = Profile.objects.filter(pk = username_from).first()
    to_som = Profile.objects.filter(pk = username_to).first()

    if from_som and to_som:
        try:
            if Invitation.objects.filter(from_som=from_som, to_som = to_som) or Invitation.objects.filter(from_som=to_som, to_som = from_som):
                inv = Invitation(from_som = from_som , to_som = to_som , accepted = False)
                serializer = InvitationSer(inv)
                return Response(serializer.data)
            else:
                inv = Invitation(from_som=from_som, to_som = to_som, accepted = False)
                inv.save()
                serializer = InvitationSer(inv)
                print("succesfully created invitation")
                return  Response(serializer.data)
        except ValueError as v:
            print(v)


    else:
        return Response({"We can not create that product": []})



@api_view(["GET"])
def return_prof_id(request, username):
    current_user = User.objects.filter(username = username).first()
    profile = Profile.objects.filter(user = current_user).first()
    if profile:
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    else:
        return Response({"Sorry, something went wrong": []})


