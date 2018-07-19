from django.conf.urls import url, include
from . import views


router = routers.DefaultRouter()




urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),

)

urlpatterns += (
    # urls for patientVisit
    
    url(r'^consecutivenumbers/$', views.consecutivenumber.as_view(), name='consecutivenumbers')

)
