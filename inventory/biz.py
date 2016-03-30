from inventory.models import *

class InventoryBiz(object):		
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
		if (inStockBill.ItemCode != None):
			inventorys = Inventory.objects.filter(ItemCode__exact=inStockBill.ItemCode)
			if (inventorys.count()==0):
				currentInventory = Inventory()
			else:
				inventorys1 = inventorys.filter(Vender__exact=inStockBill.Vender)
				if (inventorys1.count()==0):
					currentInventory = CInventory()
				else:
					inventorys2 = inventorys1.filter(Color__exact=inStockBill.Color)
					if (inventorys2.count()==0):
						currentInventory = Inventory()
					else:
						currentInventory = inventorys2[0]
		return currentInventory
		
	def getInventoryByItemCode(self,itemCode):
		inventorys = None
		if itemCode:
			inventorys = Inventory.objects.filter(ItemCode__contains=itemCode)
		else:
			inventorys = Inventory.objects.all()

		return inventorys
	
	def getInventoryByCVenderName(self,venderName):
		inventorys = None
		if venderName:
			inventorys = Inventory.objects.filter(Vender__VenderName__contains=venderName)
		else:
			inventorys = Inventory.objects.all()

		return inventorys
		
	def updatingInventoryIn(self,inStockBill,inventory):
		if (inventory.InventoryId == None):
			inventory.Type = inStockBill.Type
			inventory.Vender = inStockBill.Vender
			inventory.Color = inStockBill.Color
			inventory.ItemCode = inStockBill.ItemCode
			inventory.Size_S = 0
			inventory.Size_M = 0
			inventory.Size_L = 0
			inventory.Size_XL = 0
			inventory.Size_2XL = 0
			inventory.Size_3XL = 0
			inventory.Size_4XL = 0
			inventory.Amount = 0
		if (inStockBill.Size_S == None):
			inStockBill.Size_S = 0
		if (inStockBill.Size_M == None):
			inStockBill.Size_M = 0
		if (inStockBill.Size_L == None):
			inStockBill.Size_L = 0
		if (inStockBill.Size_XL == None):
			inStockBill.Size_XL = 0
		if (inStockBill.Size_2XL == None):
			inStockBill.Size_2XL = 0
		if (inStockBill.Size_3XL == None):
			inStockBill.Size_3XL = 0
		if (inStockBill.Size_4XL == None):
			inStockBill.Size_4XL = 0
		if (inStockBill.Amount == None):
			inStockBill.Amount = 0
		inventory.Size_S = inventory.Size_S + inStockBill.Size_S
		inventory.Size_M = inventory.Size_M + inStockBill.Size_M
		inventory.Size_L = inventory.Size_L + inStockBill.Size_L
		inventory.Size_XL = inventory.Size_XL + inStockBill.Size_XL
		inventory.Size_2XL = inventory.Size_2XL + inStockBill.Size_2XL
		inventory.Size_3XL = inventory.Size_3XL + inStockBill.Size_3XL
		inventory.Size_4XL = inventory.Size_4XL + inStockBill.Size_4XL
		inventory.Amount = inventory.Amount + inStockBill.Amount
		
	def updatingInventoryOut(self,outStockBill,inventory):
		if (inventory.InventoryId == None):
			inventory.Type = outStockBill.CType
			inventory.Vender = outStockBill.CVender
			inventory.Color = outStockBill.CColor
			inventory.ItemCode = outStockBill.CItemCode
			inventory.Size_S = 0
			inventory.Size_M = 0
			inventory.Size_L = 0
			inventory.Size_XL = 0
			inventory.Size_2XL = 0
			inventory.Size_3XL = 0
			inventory.Size_4XL = 0
			inventory.Amount = 0
		if (outStockBill.Size_S == None):
			outStockBill.Size_S = 0
		if (outStockBill.Size_M == None):
			outStockBill.Size_M = 0
		if (outStockBill.Size_L == None):
			outStockBill.Size_L = 0
		if (outStockBill.Size_XL == None):
			outStockBill.Size_XL = 0
		if (outStockBill.Size_2XL == None):
			outStockBill.Size_2XL = 0
		if (outStockBill.Size_3XL == None):
			outStockBill.Size_3XL = 0
		if (outStockBill.Size_4XL == None):
			outStockBill.Size_4XL = 0
		if (outStockBill.Amount == None):
			outStockBill.Amount = 0
		if (inventory.Size_S >= outStockBill.Size_S):
			inventory.Size_S = inventory.Size_S - outStockBill.Size_S
		else:
			return False
		
		if (inventory.Size_M >= outStockBill.Size_M):
			inventory.Size_M = inventory.Size_M - outStockBill.Size_M
		else:
			return False
		
		if (inventory.Size_L >= outStockBill.Size_L):
			inventory.Size_L = inventory.Size_L - outStockBill.Size_L
		else:
			return False
		
		if (inventory.Size_XL >= outStockBill.Size_XL):
			inventory.Size_XL = inventory.Size_XL - outStockBill.Size_XL
		else:
			return False
		
		if (inventory.Size_2XL >= outStockBill.Size_2XL):
			inventory.Size_2XL = inventory.Size_2XL - outStockBill.Size_2XL
		else:
			return False
		
		if (inventory.Size_3XL >= outStockBill.Size_3XL):
			inventory.Size_3XL = inventory.Size_3XL - outStockBill.Size_3XL
		else:
			return False
		
		if (inventory.Size_4XL >= outStockBill.Size_4XL):
			inventory.Size_4XL = inventory.Size_4XL - outStockBill.Size_4XL
		else:
			return False
		if (inventory.Amount >= outStockBill.Amount):
			inventory.Amount = inventory.Amount - outStockBill.Amount
		else:
			return False
		
		return True
	
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
		#if not inStockBill.InStockDate:
		#	validMsg = validMsg + '入库单时间不能为空！'
		return validMsg
	
	def getInStockBillByTime(self,currentTime):
		inStockBills = None
		if currentTime:
			inStockBills = InStockBill.objects.filter(InStockDate__contains=currentTime)

		return inStockBills
	
	def getInStockBillAcount(self,inStockBill):
		if (inStockBill.Size_S == None):
			inStockBill.Size_S = 0
		if (inStockBill.Size_M == None):
			inStockBill.Size_M = 0
		if (inStockBill.Size_L == None):
			inStockBill.Size_L = 0
		if (inStockBill.Size_XL == None):
			inStockBill.Size_XL = 0
		if (inStockBill.Size_2XL == None):
			inStockBill.Size_2XL = 0
		if (inStockBill.Size_3XL == None):
			inStockBill.Size_3XL = 0
		if (inStockBill.Size_4XL == None):
			inStockBill.Size_4XL = 0
			
		totalAmount =  inStockBill.Size_S + inStockBill.Size_M + inStockBill.Size_L + inStockBill.Size_XL + inStockBill.Size_2XL + inStockBill.Size_3XL + inStockBill.Size_4XL
		
		return totalAmount

class OutStockBillBiz(object):		
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
		if not outStockBill.OutStockBillCode:
			validMsg = validMsg + '出库单编号不能为空！'            
		#if not outStockBill.OutStockDate:
		#	validMsg = validMsg + '入库单时间不能为空！'
		return validMsg
	
	def getOutStockBillByTime(self,currentTime):
		outStockBills = None
		if currentTime:
			outStockBills = OutStockBill.objects.filter(OutStockDate__contains=currentTime)

		return outStockBills
	
	def getInStockBillAcount(self,outStockBill):
		if (outStockBill.Size_S == None):
			outStockBill.Size_S = 0
		if (outStockBill.Size_M == None):
			outStockBill.Size_M = 0
		if (outStockBill.Size_L == None):
			outStockBill.Size_L = 0
		if (outStockBill.Size_XL == None):
			outStockBill.Size_XL = 0
		if (outStockBill.Size_2XL == None):
			outStockBill.Size_2XL = 0
		if (outStockBill.Size_3XL == None):
			outStockBill.Size_3XL = 0
		if (outStockBill.Size_4XL == None):
			outStockBill.Size_4XL = 0
			
		totalAmount =  outStockBill.Size_S + outStockBill.Size_M + outStockBill.Size_L + outStockBill.Size_XL + outStockBill.Size_2XL + outStockBill.Size_3XL + outStockBill.Size_4XL
		
		return totalAmount