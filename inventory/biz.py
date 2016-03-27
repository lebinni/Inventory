from inventory.models import *

class InventoryBiz(object):		
	def save(self,inStockBill):
		currentInventory = self.getInventoryByItem(inStockBill.Item)	
		self.updatingInventoryIn(inStockBill,currentInventory)
		currentInventory.save()
		
	def getInventoryByItem(self,item):
		if (item != None):
			inventorys = item.inventory_set.all()
			if (inventorys.count()==0):
				currentInventory = Inventory()
			else:
				currentInventory = inventorys[0]
		return currentInventory
		
	def getInventoryByItemName(self,itemName):
		inventorys = None
		if itemName:
			inventorys = Inventory.objects.filter(Item__ItemName__contains=itemName)
		else:
			inventorys = Inventory.objects.all()

		return inventorys
		
	def updatingInventoryIn(self,inStockBill,inventory):
		if (inventory.InventoryId == None):
			inventory.Item = inStockBill.Item
			inventory.Amount = 0
		inventory.Amount = inventory.Amount + inStockBill.Amount
		
class InStockBillBiz(object):		
	def save(self,inStockBill):
		validMsg = ''
		try:
			validMsg = self.validBeforeSave(inStockBill)
			if validMsg != '':
				raise "ValidationException", validMsg
			inStockBill.save()
		except "ValidationException", arg:
			raise "ValidationException", arg
		except Exception, e:
			raise Exception(e)
			
	def validBeforeSave(self, inStockBill):
		validMsg = ''
		if not inStockBill.InStockBillCode:
			validMsg = validMsg + '入库单编号不能为空！'            
		if not inStockBill.InStockDate:
			validMsg = validMsg + '入库单时间不能为空！'
		return validMsg

class CInventoryBiz(object):		
	def save(self,inStockBill):
		currentInventory = self.getInventoryByItem(inStockBill.CItemCode)	
		self.updatingInventoryIn(inStockBill,currentInventory)
		currentInventory.save()
		
	def getInventoryByItem(self,cItemCode):
		if (cItemCode != None):
			inventorys = CInventory.objects.filter(CItemCode__contains=cItemCode)
			if (inventorys.count()==0):
				currentInventory = CInventory()
			else:
				currentInventory = inventorys[0]
		return currentInventory
		
	def getInventoryByItemName(self,cItemCode):
		inventorys = None
		if cItemCode:
			inventorys = CInventory.objects.filter(CItemCode__contains=cItemCode)
		else:
			inventorys = CInventory.objects.all()

		return inventorys
		
	def updatingInventoryIn(self,inStockBill,inventory):
		if (inventory.CInventoryId == None):
			inventory.CVender = inStockBill.CVender
			inventory.CColor = inStockBill.CColor
			inventory.CItemCode = inStockBill.CItemCode
			inventory.CSize_S = 0
			inventory.CSize_M = 0
			inventory.CSize_L = 0
			inventory.CSize_XL = 0
			inventory.CSize_2XL = 0
			inventory.CSize_3XL = 0
			inventory.CSize_4XL = 0
		if (inStockBill.CSize_S == None):
			inStockBill.CSize_S = 0
		if (inStockBill.CSize_M == None):
			inStockBill.CSize_M = 0
		if (inStockBill.CSize_L == None):
			inStockBill.CSize_L = 0
		if (inStockBill.CSize_XL == None):
			inStockBill.CSize_XL = 0
		if (inStockBill.CSize_2XL == None):
			inStockBill.CSize_2XL = 0
		if (inStockBill.CSize_3XL == None):
			inStockBill.CSize_3XL = 0
		if (inStockBill.CSize_4XL == None):
			inStockBill.CSize_4XL = 0
		inventory.CSize_S = inventory.CSize_S + inStockBill.CSize_S
		inventory.CSize_M = inventory.CSize_M + inStockBill.CSize_M
		inventory.CSize_L = inventory.CSize_L + inStockBill.CSize_L
		inventory.CSize_XL = inventory.CSize_XL + inStockBill.CSize_XL
		inventory.CSize_2XL = inventory.CSize_2XL + inStockBill.CSize_2XL
		inventory.CSize_3XL = inventory.CSize_3XL + inStockBill.CSize_3XL
		inventory.CSize_4XL = inventory.CSize_4XL + inStockBill.CSize_4XL
		
class CInStockBillBiz(object):		
	def save(self,inStockBill):
		validMsg = ''
		try:
			validMsg = self.validBeforeSave(inStockBill)
			if validMsg != '':
				raise "ValidationException", validMsg
			inStockBill.save()
		except "ValidationException", arg:
			raise "ValidationException", arg
		except Exception, e:
			raise Exception(e)
			
	def validBeforeSave(self, inStockBill):
		validMsg = ''
		if not inStockBill.CInStockBillCode:
			validMsg = validMsg + '入库单编号不能为空！'            
		if not inStockBill.CInStockDate:
			validMsg = validMsg + '入库单时间不能为空！'
		return validMsg
	