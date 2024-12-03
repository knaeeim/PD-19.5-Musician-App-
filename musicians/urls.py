from django.urls import path, include
from .views import *

urlpatterns = [
    path('', show_musician, name='home'),
    # path('add_musician/', add_musician, name='add_mus'),
    path('add_musician/', AddMusicianView.as_view(), name='add_mus'),
    # path('add_album/', add_album, name='add_album'),
    path('add_album/', AddAlbumView.as_view(), name='add_album'),
    # path('user_registration/', reistration, name='registation'),
    path('user_registration/', RegistrationView.as_view(), name='registation'),
    # path('login/', userLogin, name='login'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', user_logout, name='logout'),
    # path('edit_album/<int:id>', edit_album, name='edit_album'),
    path('edit_album/<int:id>', EditAlbumView.as_view(), name='edit_album'),
    # path('edit_musician/<int:id>', edit_musician, name='edit_musician'),
    path('edit_musician/<int:id>', EditMusicianView.as_view(), name='edit_musician'),
    # path('delete_album/<int:id>', delete_album, name='del_album'),
    path('delete_album/<int:id>', DeleteAlbumView.as_view(), name='del_album'),
    # path('edit_user/', user_data, name='edit_user'),
    path('edit_user/', EditProfileView.as_view(), name='edit_user'),
    # path('edit_password/', password_change, name='edit_password'),
    path('edit_password/', PasswordChangeView.as_view(), name='edit_password'),
]
