from rest_framework import viewsets
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .question_generator import *
from .summarizer import generate_summary # Text Summarizer
##### For PDF Generation###########
from drf_pdf.response import PDFFileResponse
from drf_pdf.renderer import PDFRenderer
from .utils import render_to_pdf
######For Messaging########
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


#############Editable###########################

class QuestionsView(APIView):
	def get(self,request):
		parameters = request.query_params
		type_of_crime = FIRDetail.objects.get(id=int(parameters['id'])).type_of_crime
		words = list(type_of_crime.split())
		type_of_crime = words[0]
		for i in words[1:]:
			type_of_crime+='_'+i
		print('static/crime/'+str(type_of_crime)+'.txt')
		with open('static/crime/'+str(type_of_crime).lower()+'.txt') as f:
		 	ques = f.readlines()
		response = [] 
		for i in ques:
			response.append(i)
		print(response)

		try:
			if parameters['type']=='list':
				return Response({'questions':response},status=status.HTTP_201_CREATED)
		except:
			pass
		return Response({'question1':response[0],'question2':response[1],'question3':response[2]},status=status.HTTP_201_CREATED)
		

#######################Working#####################
#############Police Station Locator#########

class PoliceView(APIView):

	def get(self,request):
		points = {
					"Anand Nagar" :[23.252035,77.485608],
					"Piplani" : [23.232207,77.472003],
					"Govindpura" : [23.231437,77.454365],
					"Bilkeriya" : [23.255571,77.571361],
					"Awadhpuri" : [23.220783,77.486502],
					"Ayodhya Nagar" : [23.277755,77.464968],
					"Ashoka Garden" : [23.266669,77.442625],
				}
		def find_nearest(coord):
			x, y = coord
			dist = lambda key: (x - points[key][0]) ** 2 + (y - points[key][1]) ** 2
			return min(points, key=dist)

		parameters = request.query_params
		ans = find_nearest((float(parameters['lat']),float(parameters['long'])))
		response = PoliceStationDetail.objects.filter(station_name=ans)
		return Response(response.values('phone_no','station_name')[0],status = status.HTTP_201_CREATED)

########################## FIR ###############

class FIRViewSet(viewsets.ModelViewSet):
	queryset = FIRDetail.objects.all()
	serializer_class = FIRDetailSerializer
	# http_method_names = ['get','post','put']

	def perform_create(self, serializer):
		print(serializer.validated_data)
		if serializer.is_valid():
			try:
				pass
				#serializer.validated_data['type_of_crime'] = crime_classifier(serializer.validated_data['type_of_crime']) 
				#print("stop")
			except:
				pass

			serializer.save()
	def create(self,request):
		super().create(request)
		id_of_fir = FIRDetail.objects.last().id
		return Response({'status':True,'id':id_of_fir},status=status.HTTP_201_CREATED)
	def partial_update(self,request,*args,**kwargs):
		# instance = self.get_object()
		# try:
		# 	instance.description_of_incidence = generate_summary(request.data.get('description_of_incidence'))
		# except:
		# 	pass
		# instance.location_of_crime = request.data.get('location_of_crime')
		# instance.witness_name = request.data.get('witness_name')
		# instance.witness_aadhar = request.data.get('witness_aadhar')
		# instance.identified_accused = request.data.get('identified_accused')
		# instance.save()
		print(request.data)
		super().partial_update(request)
		print("something")
		instance = self.get_object()
		if instance.phone_no and instance.sign:
			try:
				otp = message(instance.phone_no)
				verify = OTPVerification(otp=otp,type_of= 'fir',id_of=instance.id)
				verify.save()
			except:
				return Response({'message':'Number Not registered'}, status=status.HTTP_400_BAD_REQUEST)
			return Response({'otp':str(otp)},status = status.HTTP_201_CREATED)
		# serializer = self.get_serializer(instance)
		# if serializer.is_valid():
		# 	self.perform_create(serializer)
		return Response({'status':True},status=status.HTTP_201_CREATED)


############################ Document Verification##############
class DocumentVerificationView(viewsets.ModelViewSet):
	parser_class = (FileUploadParser,)
	queryset = DocumentVerification.objects.all()
	serializer_class = DocumentVerificationSerializer
	http_method_names = ['get','post','put']

	def update(self,request,pk=None,*args,**kwargs):
		instance = self.get_object()
		instance.supporting_document = request.data.get('supporting_document')
		instance.phone_no = request.data.get('phone_no')
		instance.aadhar_no = request.data.get('aadhar_no')
		instance.process_complete = True
		instance.save()

		try:
			print(request.data.get('phone_no'))
			otp = message(request.data.get('phone_no'))
			verify = OTPVerification(otp=otp,type_of= 'doc',id_of=instance.id)
			print("no Error yet")
			verify.save()
		except:
			return Response({'message':'Number Not registered'}, status=status.HTTP_400_BAD_REQUEST)

		return Response({'id':str(instance.id)},status=status.HTTP_201_CREATED)
	def get(self,request,pk=None,*args,**kwargs):
		return Response(self.queryset.filter( pk=pk))

	def post(self,request,*args,**kwargs):
		file_serializer = DocumentVerificationSerializer(data=request.data)

		if file_serializer.is_valid():
			file_serializer.save()
			return Response(file_serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

############# Verify Mobile No.#############
class VerifyMobileView(APIView):
	# def get(self,request):
	# 	parameters = request.query_params
	# 	number = str(parameters['phone'])
	# 	try:
	# 		otp = message(number)
	# 	except:
	# 		return Response({'message':'Number Not registered'}, status=status.HTTP_400_BAD_REQUEST)
	# 	print(otp)
	# 	return Response({'otp':str(otp)},status = status.HTTP_201_CREATED)

	def post(self,request):
		id_of = int(request.data.get('id'))
		otp = str(request.data.get('otp'))
		type_of = request.data.get('type')

		instance = OTPVerification.objects.filter(id_of=id_of,type_of=type_of).last()
		print(instance.otp)
		if instance.otp==otp:
			if instance.type_of=='fir':
				objec = FIRDetail.objects.get(id=id_of)
				objec.complete = True

				message = client.messages.create(
                     body="Dear sir/mam, Your FIR was registered successfully. Your reference No. is fir@"+str(id_of) + ".",
                     from_='+18189460631',
                     to='+91'+ objec.phone_no
                 )

				objec.save()
			else:
				objec = DocumentVerification.objects.get(id=id_of)
				objec.process_complete = True
				message = client.messages.create(
                     body="Dear sir/mam, Your Verification was submitted successfully. Your reference No. is doc@"+str(id_of) + ".",
                     from_='+18189460631',
                     to='+91'+ objec.phone_no
                 )
				objec.save()
			return Response({'result':'success'},status = status.HTTP_201_CREATED)	

		return Response({'result':'Invalid'},status = status.HTTP_400_BAD_REQUEST)


################### After Verification #########################

class AfterFIRVerification(APIView):
	renderer_classes = (PDFRenderer,)
	def get(self,request):
		parameters = request.query_params
		id_of_fir = int(parameters['id'])
		fir = FIRDetail.objects.get(id=id_of_fir)
		context = {'instance':fir}
		pdf = render_to_pdf('fir_pdf.html',context)
		fir.complete = True
		fir.save()
		headers = {
            'Content-Disposition': 'filename="FIR.pdf"',
            }
		# if not pdf:
		# 	return Response({'error': 'Not found'},status=status.HTTP_404_NOT_FOUND)
		# return PDFFileResponse(
  #           pdf=pdf,
  #           file_name='FIR_'+str(id_of_fir),
  #           status=status.HTTP_200_OK
  #       )
		return Response(pdf,headers=headers,status=status.HTTP_200_OK)

######################################################

class AfterDocMobileVerification(APIView):
	def get(self,request):
		parameters = request.query_params
		id_of_doc = int(parameters['id'])
		doc = DocumentVerification.objects.get(id=id_of_doc)
		doc.process_complete = True
		doc.save()

		return Response({'message':'Process Complete','id':str(id_of_doc)},status=status.HTTP_200_OK)
####################################################################
class PdfGeneratorDocVerification(APIView):
	renderer_classes = (PDFRenderer,)
	def get(self,request):
		parameters = request.query_params
		id_of_doc = int(parameters['id'])
		doc = DocumentVerification.objects.get(id=id_of_doc)
		if doc.verified:
			context = {'instance':doc}
			pdf = render_to_pdf('index.html',context)
			headers = {
            'Content-Disposition': 'filename="verified.pdf"',
            }
			return Response(pdf,headers=headers,status=status.HTTP_200_OK)
		else:
			return Response({'message':'Not Verfied yet'}, status=status.HTTP_400_BAD_REQUEST)

############################### Cyber Crime ########################

class CyberCrimeView(viewsets.ModelViewSet):
	queryset = CyberCrime.objects.all()
	serializer_class = CyberCrimeSerializer

	