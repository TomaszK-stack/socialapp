from django.urls import path , include
from rest_framework import routers

from .views import ProfileView , ProfileViewSet , UpdateApiView , ListaProfili , Profilelistview,add_invitation, get_auth_user

router = routers.SimpleRouter()
router.register('edit' , ProfileViewSet)
router.register('lista' , ListaProfili)
# router.register(('update'), UpdateApiView.as_view())

urlpatterns = [
    path('profiles' , ProfileView.as_view() , name = 'Profile_view') ,
    path('' , include(router.urls) , name = "rest") ,
    path('update/<int:pk>' , UpdateApiView.as_view() , name = 'update') ,
    path('search/<name>' , Profilelistview.as_view() , name = "search") ,
    path("cr_inv/<int:username_from>/<int:username_to>" , add_invitation, name = "add_invitation"),
    path("<token>" , get_auth_user, name = "get_auth_user"),

]
