from django.urls import path


urlpatterns = [
    path('', BookAPIView.as_view()),
]