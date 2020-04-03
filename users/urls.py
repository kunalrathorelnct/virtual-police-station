from users import views
from django.urls import path,include
from rest_framework import routers

app_name = 'FIR_app'

router = routers.DefaultRouter()
router.register(r'FIR', views.FIRViewSet)
router.register(r'docverify', views.DocumentVerificationView)
router.register(r'cybercrime', views.CyberCrimeView)
# router.register(r'witness', views.WitnessDetailView)


urlpatterns = [
    path('', include(router.urls)),
    path('police/',views.PoliceView.as_view(),name='police'),
    path('question/',views.QuestionsView.as_view()),
    path('checkotp/',views.VerifyMobileView.as_view()),
    path('afterverificationfir/',views.AfterFIRVerification.as_view()),
    path('afterverificationdoc/',views.AfterDocMobileVerification.as_view()),
    path('pdfgeneratordoc/',views.PdfGeneratorDocVerification.as_view()),
    
]