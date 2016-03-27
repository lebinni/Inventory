from django.db import models

# Create your models here.

class Item(models.Model):
	ItemId = models.AutoField(primary_key=True)
	ItemCode = models.CharField(max_length=50)
	ItemName = models.CharField(max_length=50)
	Remark = models.CharField(max_length=200)

	def __unicode__(self):  
		return self.ItemName




class Inventory (models.Model):
	InventoryId = models.AutoField(primary_key=True)
	Item = models.ForeignKey(Item, null=False)
	Amount = models.IntegerField(null=True)


class InStockBill(models.Model):
	InStockBillId = models.AutoField(primary_key=True)
	InStockBillCode = models.CharField(max_length=40)
	InStockDate = models.DateTimeField(null=True, auto_now=True)
	Operator = models.CharField(max_length=40)
	Item = models.ForeignKey(Item, null=False)
	Amount = models.IntegerField(null=True)
	
class CVender(models.Model):
	CVenderId = models.AutoField(primary_key=True)
	CVenderName = models.CharField(max_length=10)
	
	def __unicode__(self):  
		return self.CVenderName
	
class CColor(models.Model):
	CColorId = models.AutoField(primary_key=True)
	CColorName = models.CharField(max_length=10)
	
	def __unicode__(self):  
		return self.CColorName	
	
class Meta:
	ordering =['ItemCode']
	ordering =['CVenderName']
	ordering =['CColorName']

class CInventory (models.Model):
	CInventoryId = models.AutoField(primary_key=True)
	CItemCode = models.CharField(max_length=50)
	CVender = models.ForeignKey(CVender, null=False)
	CColor = models.ForeignKey(CColor, null=False)
	CSize_S = models.IntegerField(null=True)
	CSize_M = models.IntegerField(null=True)
	CSize_L = models.IntegerField(null=True)
	CSize_XL = models.IntegerField(null=True)
	CSize_2XL = models.IntegerField(null=True)
	CSize_3XL = models.IntegerField(null=True)
	CSize_4XL = models.IntegerField(null=True)

class CInStockBill(models.Model):
	CInStockBillId = models.AutoField(primary_key=True)
	CInStockBillCode = models.CharField(max_length=40)
	CInStockDate = models.DateTimeField(null=True, auto_now=True)
	COperator = models.CharField(max_length=40)
	CItemCode = models.CharField(max_length=50)
	CVender = models.ForeignKey(CVender, null=False)
	CColor = models.ForeignKey(CColor, null=False)
	CSize_S = models.IntegerField(null=True)
	CSize_M = models.IntegerField(null=True)
	CSize_L = models.IntegerField(null=True)
	CSize_XL = models.IntegerField(null=True)
	CSize_2XL = models.IntegerField(null=True)
	CSize_3XL = models.IntegerField(null=True)
	CSize_4XL = models.IntegerField(null=True)