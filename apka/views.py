from django.shortcuts import render
from rest_framework import generics
from .serializers import ProfileSerializer
from .models import Profile
from rest_framework.response import Response


class ProfileView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ProfileSerializer(queryset, many=True)
        return Response(serializer.data)


