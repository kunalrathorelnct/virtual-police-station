from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import *
from django.http import JsonResponse
from .question_generator import *
from django.views.generic.edit import FormView
from .forms import DocumentVerificationForm

#######################################
from random import randint
from twilio.rest import Client
account_sid = 'AC0796841db5e1a3e7828039babd947f74'
auth_token = '5508f11307c89e657d19e45ef599c91d'
client = Client(account_sid, auth_token)

def message(number):
	otp = randint(1000,9999)
	message = client.messages.create(
                     body="Your OTP is "+str(otp),
                     from_='+18189460631',
                     to='+91'+ number
                 )
	return otp
##########################################
class HomeView(TemplateView):
	template_name = 'index.html'

def OtpView(request):
	if 'request.method'=='POST':
		id_of = request.POST['id']
		otp = request.POST['otp']

		otp_object = OTPVerification.objects.get(id=id_of,type='fir')

		if otp_object==otp:
			fir = FIRDetail.objects.get(id=id_of)
			fir.complete = True
			fir.save()
			try:
				message = client.messages.create(
                     body="Your FIR was successfully registered and your ref No. is "+str(id_of),
                     from_='+18189460631',
                     to='+91'+ fir.phone_no
                 )
			except:
				pass
			return HttpResponse('success')
	return render(request,'otp.html')

class StatusrefView(TemplateView):
	template_name = 'statusref.html'

class CyberHomeView(TemplateView):
	template_name = 'cyber_home.html'

# class CyberCrimeView(FormView):
# 	template_name = 'cyber_report.html'
# 	form_class = DocumentVerificationForm
# 	success_url = '/thanks'

def CyberCrimeView(request):
	if request.method=='POST':
		print(request.POST)
		return JsonResponse({'id':'str(fir.id)'})

	return render(request,'cyber_report.html')

def FIRView(request,pk=None):
	instance = FIRDetail.objects.get(id=pk)
	if request.method=='POST':
		#try:
		instance.sign = request.FILES['sign']
		instance.save()
		#	try:
		otp = message(instance.phone_no)
		verify = OTPVerification(otp=otp,type_of= 'fir',id_of=instance.id)
		verify.save()
		return render(request,'otp.html',{'id':instance.id})
		#	except:
		return HttpResponse('Message not Sent')
		#except:
			#pass

	return render(request,'firview.html',{'instance':instance})

def FIR(request):
	if request.method=='POST':
		print(request.POST)
		data = request.POST
		if 'id' in data:
			fir = FIRDetail.objects.get(id = data['id'])
			try:
				fir.document = request.FILES['document']
				fir.save()
			except:
				pass
			print("")
			return redirect('/firview/'+str(data['id']))	

		fir = FIRDetail()
		fir.name_of_victim = data['name_of_victim']
		try:
			fir.type_of_crime = crime_classifier(data['type_of_crime'])
		except:
			fir.type_of_crime = data['type_of_crime']
		fir.save()

		return JsonResponse({'id':str(fir.id)})
	return render(request,'fir.html')
	



####################### Doc Verify #########################

def DocumentVerificationView(request):
	if request.method=='POST':
		form = DocumentVerificationForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/otp')
	else:
		form = DocumentVerificationForm()
	return render(request,'doc_veri.html',{'form':form})


####################### Status View  ###################
def StatusView(request):
	print(request.GET.get('type'))
	if request.GET.get('type')=='fir':
		instance = FIRDetail.objects.filter(id=request.GET.get('id'))
		if len(instance)>0:
			context = {'instance':instance[0],'flag':0,'type':1}
		else:
			context = {'flag':1}

	elif request.GET.get('type')=='doc':
		instance = DocumentVerification.objects.filter(id=request.GET.get('id'))
		if len(instance)>0:
			context = {'instance':instance[0],'flag':0,'type':0}
		else:
			context = {'flag':1}
	else:
		context = {'flag':1}
	
	return render(request,'status.html',context)

####################################################################