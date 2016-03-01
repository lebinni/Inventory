# -*- coding: UTF-8 -*- 
# Create your views here.
from django.shortcuts import render_to_response,RequestContext

from django.http import HttpResponse,HttpResponseRedirect

#from django.db import models

from models import Item,InStockBill,Inventory

from forms import ItemForm,InStockBillForm

from biz import InventoryBiz,InStockBillBiz

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
	return render_to_response('inventoryQueryBootstrap.html')