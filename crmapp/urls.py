from django.urls import path
from crmapp import views

urlpatterns = [
    path("get/", views.CRLMLEDApi.as_view(), name="crmledapi"),
    path("masslm/", views.MASSLMApi.as_view(), name="crmledapi"),
]