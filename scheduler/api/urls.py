from django.urls import path
from .views import CourseView, MyUserView

urlpatterns = [
    path('select-course', CourseView.as_view()),
    path('add-user', MyUserView.as_view())
]
