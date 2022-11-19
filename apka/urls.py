from django.urls import path , include
from rest_framework import routers

from .views import ProfileView , ProfileViewSet , UpdateApiView ,  Profilelistview,add_invitation, get_auth_user

router = routers.SimpleRouter()
# router.register(r'profiles/<str:username>' , ProfileViewSet)

# router.register(('update'), UpdateApiView.as_view())

urlpatterns = [
    path('profiles/<username>', ProfileViewSet.as_view({'get':'list'})),
    path('' , include(router.urls) , name = "rest") ,
    path('update/<int:pk>' , UpdateApiView.as_view() , name = 'update') ,
    path('search/<name>/' , Profilelistview.as_view() , name = "search") ,
    path("cr_inv/<int:username_from>/<int:username_to>" , add_invitation, name = "add_invitation"),
    path("<token>" , get_auth_user, name = "get_auth_user"),

]
