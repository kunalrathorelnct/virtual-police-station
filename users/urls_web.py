from django.urls import path
from . import views_web

app_name = 'FIR'

urlpatterns = [
	path('',views_web.HomeView.as_view(),name='homepage'),
	path('fir',views_web.FIR,name='fir_page'),
	path('firview/<int:pk>/',views_web.FIRView,name='fir_page'),
	path('otp',views_web.OtpView,name = 'otp'),
	path('statusref',views_web.StatusrefView.as_view(),name = 'statusref'),
	path('status',views_web.StatusView,name = 'status'),
	path('docverify',views_web.DocumentVerificationView,name = 'docverify'),
	path('cybercrimehome',views_web.CyberHomeView.as_view(),name = 'cyberhome'),
	path('cyberreport',views_web.CyberCrimeView,name = 'cyberreport'),


]