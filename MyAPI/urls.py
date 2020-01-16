from django.views.generic import RedirectView
from django.urls import path, include
from django.conf.urls import url
from . import views
from rest_framework import routers
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = routers.DefaultRouter()
router.register('MyAPI', views.ApprovalsView)
urlpatterns = [
    path('', views.cxcontact, name = 'cxform'),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
    # path('api/', include(router.urls)),
    # path('status/', views.approveReject),
]


urlpatterns += staticfiles_urlpatterns()