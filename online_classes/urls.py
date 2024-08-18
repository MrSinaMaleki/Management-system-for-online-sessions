from django.urls import path
from online_classes import views


urlpatterns = [
    path('', views.all_sessions, name="home"),
    path('/<str:name>', views.all_sessions, name="home"),
    path('add_session', views.create_session, name="create_session"),
    path('edit_session/<int:pk>', views.edit_session, name="edit_session"),
    path('detail_session/<int:pk>', views.detail_session, name="detail_session"),

]
