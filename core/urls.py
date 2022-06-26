from django.urls import path

from core.views import UserView, NewsLetterView

app_name='core'
urlpatterns = [
    path('users/', UserView.as_view()),
    path('newsletter/', NewsLetterView.as_view()),
]
