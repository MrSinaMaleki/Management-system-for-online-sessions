from django.urls import path
from online_classes import views


urlpatterns = [
    # path('', views.all_sessions, name="home"),
    path('', views.AllSessions.as_view(), name='all-sessions'),


    # path('detail_session/<int:pk>', views.detail_session, name="detail_session"),
    path('detail_session/<int:pk>', views.SessionDetailView.as_view(), name="detail_session"),

    # path('add_session', views.create_session, name="create_session"),
    path('add_session', views.CreateSession.as_view(), name="create_session"),
    # path('edit_session/<int:pk>', views.edit_session, name="edit_session"),
    path('edit_session/<int:pk>', views.EditSession.as_view(), name="edit_session"),

    # path('delete_session/<int:pk>', views.delete_session, name="delete_session"),
    path('delete_session/<int:pk>', views.DeleteSession.as_view(), name="delete_session"),

]
