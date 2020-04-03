from django.db import models
from django.utils import timezone

import datetime

class PoliceStationDetail(models.Model):
	station_name = models.CharField(max_length=20,blank=False,null=False)
	address = models.TextField()
	phone_no = models.CharField(unique=True,null=False,max_length=13)

	def __str__(self):
		return self.station_name

class DocumentVerification(models.Model):
	type_of_verification = models.CharField(max_length=20)
	form = models.FileField(blank=False,null=False)
	supporting_document = models.FileField(blank=True,null=True)
	aadhar_no = models.CharField(max_length=20,blank=True,null=True)
	phone_no = models.CharField(max_length=20,blank=True,null=True)
	process_complete = models.BooleanField(default=False)
	verified = models.BooleanField(default=False)
	def __str__(self):
		return self.form.name

# class WitnessDetail(models.Model):
# 	name = models.CharField(max_length=20,blank=False,null=False)
# 	phone_no = models.CharField(unique=True,null=False,max_length=13)
# 	aadhar_no = models.CharField(max_length=16)
# 	address = models.TextField()

# 	def __str__(self):
# 		return self.name

class FIRDetail(models.Model):
	name_of_victim = models.CharField(max_length=20)
	phone_no = models.CharField(max_length=15,blank=True,null=True)
	address = models.CharField(max_length=200,blank=True,null=True)
	aadhar_no = models.CharField(max_length=16,blank=True,null=True)
	description_of_incidence = models.TextField(blank=True,null=True)
	location_of_crime = models.CharField(max_length=50,blank=True,null=True)
	datetime_of_crime = models.DateTimeField(blank=True,null=True)
	witness_name = models.CharField(max_length = 100, null=True,blank=True)
	witness_aadhar = models.CharField(max_length = 100, null=True,blank=True)
	police_station = models.ForeignKey(PoliceStationDetail,on_delete = models.CASCADE, null=True)
	identified_accused = models.TextField(null=True,blank=True)
	type_of_crime = models.CharField(max_length=50)
	datetime_of_FIR = models.DateTimeField(auto_now = True)
	passed_to_CCTNS = models.BooleanField(default = False)
	complete = models.BooleanField(default=False)
	sign = models.FileField(blank=True,null=True)
	document = models.FileField(blank=True,null=True)

	def __str__(self):
		return str(self.datetime_of_FIR)


class OTPVerification(models.Model):
	id_of = models.CharField(max_length=20)
	type_of = models.CharField(max_length=20)
	otp = models.CharField(max_length=4)
	expiry = models.DateTimeField(default=timezone.now,blank=True)

	@property
	def delete_after_minute(self):
		time = self.expiry + datetime.timedelta(minute=1)

		if time < datetime.datetime.now():
			e = OTPVerification.objects.get(pk=self.pk)
			e.delete()
			return True
		else:
			return False 
		



class CyberCrime(models.Model):
	type_of_report = models.CharField(max_length=50)
	#reported_by = models.CharField(max_length=20,blank=True,null=True)
	email = models.EmailField(blank=True,null=True)
	report_anonomous = models.BooleanField(default=False)
	anonomous_info = models.CharField(max_length=200,blank=True,null=True)
	name_of_victim = models.CharField(max_length=20,blank=True,null=True)
	address = models.CharField(max_length=100,blank=True,null=True)
	phone = models.CharField(max_length=12,blank=True,null=True)
	datetime_of_incidence = models.DateTimeField(blank=True,null=True)
	occurence_of_incidence = models.CharField(max_length=200,blank=True,null=True)
	your_knowledge_of_incidence = models.CharField(max_length=100,blank=True,null=True)
	identified_accused = models.CharField(max_length=100,null=True,blank=True)
	description_of_incidence = models.TextField(blank=True,null=True)
	other_info = models.TextField(null=True,blank=True)
	complete = models.BooleanField(default=False)
	passed_to_CC = models.BooleanField(default=False)
	#sign = models.FileField(blank=True,null=True)


