from django.urls import path
from post import views

app_name = 'post'

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('nuevo', views.NuevoUser.as_view(), name='nuevousuario'),
    path('postdetail/<int:pk>', views.PostDetail.as_view(), name='postdetail'),
    path('create', views.CreatePost.as_view(), name='createpost')
]