from django.urls import path
from .views import ContactView, SuccessView, UnsubSuccessView, UnsubscribeView, WeeklyAdView


app_name = 'contact_users'

urlpatterns = [
    path('', ContactView.as_view(), name="contact"),
    path('success/', SuccessView.as_view(), name="success"),
    path('unsubscribe/', UnsubscribeView.as_view(), name="unsubscribe"),
    path('weekly_ads/', WeeklyAdView.as_view(), name="weekly_ads"),
    path('unsub_success/', UnsubSuccessView.as_view(), name="unsub_success")
]