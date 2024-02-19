from django.urls import path

from .views import SignUpView, user_list, update_user, delete_user

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('', user_list, name='home'),
    path('update_user/<int:user_id>/', update_user, name='update_user'),
    path('delete_user/<int:user_id>/', delete_user, name='delete_user'),

]