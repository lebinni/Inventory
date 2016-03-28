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
	def saveForIn(self,inStockBill):
		currentInventory = self.getInventoryByItem(inStockBill)	
		self.updatingInventoryIn(inStockBill,currentInventory)
		currentInventory.save()
		
	def saveForOut(self,outStockBill):
		currentInventory = self.getInventoryByItem(outStockBill)	
		if self.updatingInventoryOut(outStockBill,currentInventory):			
			currentInventory.save()
			return True
		else:
			return False
		
	def getInventoryByItem(self,inStockBill):
		if (inStockBill.CItemCode != None):
			inventorys = CInventory.objects.filter(CItemCode__exact=inStockBill.CItemCode)
			if (inventorys.count()==0):
				currentInventory = CInventory()
			else:
				inventorys1 = inventorys.filter(CVender__exact=inStockBill.CVender)
				if (inventorys1.count()==0):
					currentInventory = CInventory()
				else:
					inventorys2 = inventorys1.filter(CColor__exact=inStockBill.CColor)
					if (inventorys2.count()==0):
						currentInventory = CInventory()
					else:
						currentInventory = inventorys2[0]
		return currentInventory
		
	def getInventoryByItemCode(self,cItemCode):
		inventorys = None
		if cItemCode:
			inventorys = CInventory.objects.filter(CItemCode__contains=cItemCode)
		else:
			inventorys = CInventory.objects.all()

		return inventorys
	
	def getInventoryByCVenderName(self,cVenderName):
		inventorys = None
		if cVenderName:
			inventorys = CInventory.objects.filter(CVender__CVenderName__contains=cVenderName)
		else:
			inventorys = CInventory.objects.all()

		return inventorys
		
	def updatingInventoryIn(self,inStockBill,inventory):
		if (inventory.CInventoryId == None):
			inventory.CType = inStockBill.CType
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
			inventory.CAmount = 0
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
		if (inStockBill.CAmount == None):
			inStockBill.CAmount = 0
		inventory.CSize_S = inventory.CSize_S + inStockBill.CSize_S
		inventory.CSize_M = inventory.CSize_M + inStockBill.CSize_M
		inventory.CSize_L = inventory.CSize_L + inStockBill.CSize_L
		inventory.CSize_XL = inventory.CSize_XL + inStockBill.CSize_XL
		inventory.CSize_2XL = inventory.CSize_2XL + inStockBill.CSize_2XL
		inventory.CSize_3XL = inventory.CSize_3XL + inStockBill.CSize_3XL
		inventory.CSize_4XL = inventory.CSize_4XL + inStockBill.CSize_4XL
		inventory.CAmount = inventory.CAmount + inStockBill.CAmount
		
	def updatingInventoryOut(self,outStockBill,inventory):
		if (inventory.CInventoryId == None):
			inventory.CType = outStockBill.CType
			inventory.CVender = outStockBill.CVender
			inventory.CColor = outStockBill.CColor
			inventory.CItemCode = outStockBill.CItemCode
			inventory.CSize_S = 0
			inventory.CSize_M = 0
			inventory.CSize_L = 0
			inventory.CSize_XL = 0
			inventory.CSize_2XL = 0
			inventory.CSize_3XL = 0
			inventory.CSize_4XL = 0
			inventory.CAmount = 0
		if (outStockBill.CSize_S == None):
			outStockBill.CSize_S = 0
		if (outStockBill.CSize_M == None):
			outStockBill.CSize_M = 0
		if (outStockBill.CSize_L == None):
			outStockBill.CSize_L = 0
		if (outStockBill.CSize_XL == None):
			outStockBill.CSize_XL = 0
		if (outStockBill.CSize_2XL == None):
			outStockBill.CSize_2XL = 0
		if (outStockBill.CSize_3XL == None):
			outStockBill.CSize_3XL = 0
		if (outStockBill.CSize_4XL == None):
			outStockBill.CSize_4XL = 0
		if (outStockBill.CAmount == None):
			outStockBill.CAmount = 0
		if (inventory.CSize_S >= outStockBill.CSize_S):
			inventory.CSize_S = inventory.CSize_S - outStockBill.CSize_S
		else:
			return False
		
		if (inventory.CSize_M >= outStockBill.CSize_M):
			inventory.CSize_M = inventory.CSize_M - outStockBill.CSize_M
		else:
			return False
		
		if (inventory.CSize_L >= outStockBill.CSize_L):
			inventory.CSize_L = inventory.CSize_L - outStockBill.CSize_L
		else:
			return False
		
		if (inventory.CSize_XL >= outStockBill.CSize_XL):
			inventory.CSize_XL = inventory.CSize_XL - outStockBill.CSize_XL
		else:
			return False
		
		if (inventory.CSize_2XL >= outStockBill.CSize_2XL):
			inventory.CSize_2XL = inventory.CSize_2XL - outStockBill.CSize_2XL
		else:
			return False
		
		if (inventory.CSize_3XL >= outStockBill.CSize_3XL):
			inventory.CSize_3XL = inventory.CSize_3XL - outStockBill.CSize_3XL
		else:
			return False
		
		if (inventory.CSize_4XL >= outStockBill.CSize_4XL):
			inventory.CSize_4XL = inventory.CSize_4XL - outStockBill.CSize_4XL
		else:
			return False
		if (inventory.CAmount >= outStockBill.CAmount):
			inventory.CAmount = inventory.CAmount - outStockBill.CAmount
		else:
			return False
		
		return True
	
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
		#if not inStockBill.CInStockDate:
		#	validMsg = validMsg + '入库单时间不能为空！'
		return validMsg
	
	def getInStockBillByTime(self,currentTime):
		inStockBills = None
		if currentTime:
			inStockBills = CInStockBill.objects.filter(CInStockDate__contains=currentTime)

		return inStockBills
	
	def getInStockBillAcount(self,inStockBill):
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
			
		totalAmount =  inStockBill.CSize_S + inStockBill.CSize_M + inStockBill.CSize_L + inStockBill.CSize_XL + inStockBill.CSize_2XL + inStockBill.CSize_3XL + inStockBill.CSize_4XL
		
		return totalAmount

class COutStockBillBiz(object):		
	def save(self,outStockBill):
		validMsg = ''
		try:
			validMsg = self.validBeforeSave(outStockBill)
			if validMsg != '':
				raise "ValidationException", validMsg
			outStockBill.save()
		except "ValidationException", arg:
			raise "ValidationException", arg
		except Exception, e:
			raise Exception(e)
			
	def validBeforeSave(self, outStockBill):
		validMsg = ''
		if not outStockBill.COutStockBillCode:
			validMsg = validMsg + '出库单编号不能为空！'            
		#if not outStockBill.COutStockDate:
		#	validMsg = validMsg + '入库单时间不能为空！'
		return validMsg
	
	def getOutStockBillByTime(self,currentTime):
		outStockBills = None
		if currentTime:
			outStockBills = COutStockBill.objects.filter(COutStockDate__contains=currentTime)

		return outStockBills
	
	def getInStockBillAcount(self,outStockBill):
		if (outStockBill.CSize_S == None):
			outStockBill.CSize_S = 0
		if (outStockBill.CSize_M == None):
			outStockBill.CSize_M = 0
		if (outStockBill.CSize_L == None):
			outStockBill.CSize_L = 0
		if (outStockBill.CSize_XL == None):
			outStockBill.CSize_XL = 0
		if (outStockBill.CSize_2XL == None):
			outStockBill.CSize_2XL = 0
		if (outStockBill.CSize_3XL == None):
			outStockBill.CSize_3XL = 0
		if (outStockBill.CSize_4XL == None):
			outStockBill.CSize_4XL = 0
			
		totalAmount =  outStockBill.CSize_S + outStockBill.CSize_M + outStockBill.CSize_L + outStockBill.CSize_XL + outStockBill.CSize_2XL + outStockBill.CSize_3XL + outStockBill.CSize_4XL
		
		return totalAmount