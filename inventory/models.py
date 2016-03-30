from django.db import models

# Create your models here.
class Vender(models.Model):
	VenderId = models.AutoField(primary_key=True)
	VenderName = models.CharField(max_length=10)
	
	def __unicode__(self):  
		return self.VenderName
	class Meta:
		ordering =['VenderName']	
	
class Color(models.Model):
	ColorId = models.AutoField(primary_key=True)
	ColorName = models.CharField(max_length=10)
	
	def __unicode__(self):  
		return self.ColorName	
	class Meta:
		ordering =['ColorName']	

class Type(models.Model):
	TypeId = models.AutoField(primary_key=True)
	TypeName = models.CharField(max_length=10)
	
	def __unicode__(self):  
		return self.TypeName
	class Meta:
		ordering =['TypeName']	
	

class Inventory (models.Model):
	InventoryId = models.AutoField(primary_key=True)
	ItemCode = models.CharField(max_length=50)
	Type = models.ForeignKey(Type, null=False)
	Vender = models.ForeignKey(Vender, null=False)
	Color = models.ForeignKey(Color, null=False)
	Size_S = models.IntegerField(null=True)
	Size_M = models.IntegerField(null=True)
	Size_L = models.IntegerField(null=True)
	Size_XL = models.IntegerField(null=True)
	Size_2XL = models.IntegerField(null=True)
	Size_3XL = models.IntegerField(null=True)
	Size_4XL = models.IntegerField(null=True)
	Amount = models.IntegerField(null=True)
	
	class Meta:
		ordering =['Vender','ItemCode','Color']		

class InStockBill(models.Model):
	InStockBillId = models.AutoField(primary_key=True)
	InStockBillCode = models.CharField(max_length=40)
	InStockDate = models.DateTimeField(null=True, auto_now=True)
	Operator = models.CharField(max_length=40)
	ItemCode = models.CharField(max_length=50)
	Type = models.ForeignKey(Type, null=False)
	Vender = models.ForeignKey(Vender, null=False)
	Color = models.ForeignKey(Color, null=False)
	Size_S = models.IntegerField(null=True)
	Size_M = models.IntegerField(null=True)
	Size_L = models.IntegerField(null=True)
	Size_XL = models.IntegerField(null=True)
	Size_2XL = models.IntegerField(null=True)
	Size_3XL = models.IntegerField(null=True)
	Size_4XL = models.IntegerField(null=True)
	Amount = models.IntegerField(null=True)
	
class OutStockBill(models.Model):
	OutStockBillId = models.AutoField(primary_key=True)
	OutStockBillCode = models.CharField(max_length=40)
	OutStockDate = models.DateTimeField(null=True, auto_now=True)
	Operator = models.CharField(max_length=40)
	ItemCode = models.CharField(max_length=50)
	Type = models.ForeignKey(Type, null=False)
	Vender = models.ForeignKey(Vender, null=False)
	Color = models.ForeignKey(Color, null=False)
	Size_S = models.IntegerField(null=True)
	Size_M = models.IntegerField(null=True)
	Size_L = models.IntegerField(null=True)
	Size_XL = models.IntegerField(null=True)
	Size_2XL = models.IntegerField(null=True)
	Size_3XL = models.IntegerField(null=True)
	Size_4XL = models.IntegerField(null=True)
	Amount = models.IntegerField(null=True)
	