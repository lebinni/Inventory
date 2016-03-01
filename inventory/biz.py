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
	