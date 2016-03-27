# -*- coding: UTF-8 -*- 
# Create your views here.
from django.shortcuts import render_to_response,RequestContext

from django.http import HttpResponse,HttpResponseRedirect

#from django.db import models

from models import Item,InStockBill,Inventory,CVender,CColor,CInStockBill

from forms import ItemForm,InStockBillForm,CVenderForm,CColorForm,CInStockBillForm

from biz import InventoryBiz,InStockBillBiz,CInventoryBiz,CInStockBillBiz

from django.db import transaction

def success(request):

	return HttpResponse('success')
	
	
def AddItemForm(request):

	form = ItemForm({})

	if request.method == 'POST':

		form = ItemForm(request.POST)

		if form.is_valid():

			cd = form.cleaned_data

			item = Item()

			item.ItemCode = cd['ItemCode']

			item.ItemName = cd['ItemName']
			
			item.Remark = cd['Remark'] 

			item.save()

			return HttpResponseRedirect('/success/')

	else:

		form = ItemForm()

	return render_to_response('ItemAdd.html', {'form': form},

			context_instance = RequestContext(request))

@transaction.commit_on_success			
def AddInStockBillForm(request):

	form = InStockBillForm({})

	if request.method == 'POST':

		form = InStockBillForm(request.POST)

		if form.is_valid():

			cd = form.cleaned_data

			inStockBill = InStockBill()

			inStockBill.InStockBillCode = cd['InStockBillCode']

			inStockBill.InStockDate = cd['InStockDate']

			inStockBill.Amount = cd['Amount']

			inStockBill.Operator = cd['Operator']

			inStockBill.Item = cd['Item']
			
			biz = InventoryBiz()
			
			biz.save(inStockBill)
			
			billbiz = InStockBillBiz()
			
			billbiz.save(inStockBill)

			#inStockBill.save()

			return HttpResponseRedirect('/success/')

	else:

		form = InStockBillForm()

	return render_to_response('InStockAddForm.html',{'form': form}

		,context_instance = RequestContext(request))
		
def UpdatingInventoryIn(inStockBill,inventory):

	if (inventory.InventoryId == None):
	
		inventory.Item = inStockBill.Item
		
		inventory.Amount = 0
		
	inventory.Amount = inventory.Amount + inStockBill.Amount
	
def getInventoryByItemName(request):
    error = False
    inventorysJson = '[]'
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        elif len(q) > 20:
            error = True        
        else:
            biz = InventoryBiz()
            inventorys =biz.getInventoryByItemName(q)    
            inventorysJson=u'[' 

            for inventory in inventorys:
                inventorysJson = inventorysJson + u'{"InventoryId":"' + str( inventory.InventoryId) + u'","ItemName":"' +  inventory.Item.ItemName + u'","Amount":"' + str( inventory.Amount) + u'"}'
            inventorysJson = inventorysJson + u']'


    return HttpResponse(inventorysJson)

def	inventoryQueryBootstrap(request):
	error=False
	if 'q' in request.GET:
		q = request.GET['q']
		if len(q) > 20:
			error = True        
		else:
			biz = InventoryBiz()
			inventorys =biz.getInventoryByItemName(q)
			return render_to_response('inventoryQueryBootstrap.html',
										{'inventorys': inventorys, 'query': q, 'error': error})
			#return render_to_response('inventoryQueryBootstrap.html')
	return render_to_response('inventoryQueryBootstrap.html')

def AddCItemForm(request):

	form1 = CVenderForm({})
	form2 = CColorForm({})

	if request.method == 'POST':

		form1 = CVenderForm(request.POST)
		form2 = CColorForm(request.POST)
		success1 = ''
		success2 = ''

		if form1.is_valid():

			cd = form1.cleaned_data

			cVender = CVender()

			cVender.CVenderName = cd['CVenderName']

			cVender.save()
			
			success1 = '厂家名称添加成功'

			return render_to_response('CItemAdd.html', {'form1': form1,'form2': form2,'success1': success1},

			context_instance = RequestContext(request))
		
		if form2.is_valid():

			cd = form2.cleaned_data

			cColor = CColor()

			cColor.CColorName = cd['CColorName']

			cColor.save()
			
			success2 = '颜色添加成功'

			return render_to_response('CItemAdd.html', {'form1': form1,'form2': form2,'success2': success2},

			context_instance = RequestContext(request))

	else:

		form = CVenderForm()

	return render_to_response('CItemAdd.html', {'form1': form1,'form2': form2},

			context_instance = RequestContext(request))
	
@transaction.commit_on_success
def	rukuBootstrap(request):
	
	form = CInStockBillForm({})
	
	cinStockBill = CInStockBill()
	
	success = ''
	#cVenders = CVender.objects.all()
	
	#cColors = CColor.objects.all()

	if request.method == 'POST':

		form = CInStockBillForm(request.POST)

		if form.is_valid():

			cd = form.cleaned_data

			#cinStockBill = CInStockBill()

			cinStockBill.CInStockBillCode = cd['CInStockBillCode']

			cinStockBill.CInStockDate = cd['CInStockDate']

			cinStockBill.COperator = cd['COperator']

			cinStockBill.CItemCode = cd['CItemCode']
			
			cinStockBill.CVender = cd['CVender']
			
			cinStockBill.CColor = cd['CColor']
			
			cinStockBill.CSize_S = cd['CSize_S']
			
			cinStockBill.CSize_M = cd['CSize_M']
			
			cinStockBill.CSize_L = cd['CSize_L']
			
			cinStockBill.CSize_XL = cd['CSize_XL']
			
			cinStockBill.CSize_2XL = cd['CSize_2XL']
			
			cinStockBill.CSize_3XL = cd['CSize_3XL']
			
			cinStockBill.CSize_4XL = cd['CSize_4XL']
			
			biz = CInventoryBiz()
			
			biz.save(cinStockBill)
			
			billbiz = CInStockBillBiz()
			
			billbiz.save(cinStockBill)
			#cinStockBill.save()
			
			success = '入库单添加成功'
			
			return render_to_response('ruku.html', {'form': form,'success': success,'cinStockBill':cinStockBill},

			context_instance = RequestContext(request))

	else:

		form = CInStockBillForm()

	return render_to_response('ruku.html',{'form':form,'success': success,'cinStockBill':cinStockBill}

		,context_instance = RequestContext(request))
	
def	inventoryQueryBootstrap2(request):
	error=False
	if 'q' in request.GET:
		q = request.GET['q']
		if len(q) > 20:
			error = True        
		else:
			biz = CInventoryBiz()
			inventorys =biz.getInventoryByItemName(q)
			return render_to_response('inventoryQueryBootstrap2.html',
										{'inventorys': inventorys, 'query': q, 'error': error})
			#return render_to_response('inventoryQueryBootstrap.html')
	return render_to_response('inventoryQueryBootstrap2.html')
