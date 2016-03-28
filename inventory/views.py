# -*- coding: UTF-8 -*- 
# Create your views here.
from django.shortcuts import render_to_response,RequestContext

from django.http import HttpResponse,HttpResponseRedirect

#from django.db import models

from models import Item,InStockBill,Inventory,CType,CVender,CColor,CInStockBill,CInventory,COutStockBill

from forms import ItemForm,InStockBillForm,CTypeForm,CVenderForm,CColorForm,CInStockBillForm,ChangepwdForm,COutStockBillForm

from biz import InventoryBiz,InStockBillBiz,CInventoryBiz,CInStockBillBiz,COutStockBillBiz

from django.db import transaction

import datetime

import time

from django.shortcuts import render_to_response,render,get_object_or_404    
from django.http import HttpResponse, HttpResponseRedirect    
from django.contrib.auth.models import User    
from django.contrib import auth  
from django.contrib import messages  
from django.template.context import RequestContext  
  
from django.forms.formsets import formset_factory  
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage  
  
from bootstrap_toolkit.widgets import BootstrapUneditableInput  
from django.contrib.auth.decorators import login_required  
  
from .forms import LoginForm  


  
def login(request):  
    if request.method == 'GET':  
        form = LoginForm()  
        return render_to_response('login.html', RequestContext(request, {'form': form}))  
    else:  
        form = LoginForm(request.POST)  
        if form.is_valid():  
            username = request.POST.get('username', '')  
            password = request.POST.get('password', '')  
            user = auth.authenticate(username=username, password=password)  
            if user is not None and user.is_active:  
                auth.login(request, user)  
                return render_to_response('index.html', RequestContext(request))  
            else:  
                return render_to_response('login.html', RequestContext(request, {'form': form,'password_is_wrong':True}))  
        else:  
            return render_to_response('login.html', RequestContext(request, {'form': form,}))
           
@login_required(login_url='/login/')   
def logout(request):  
    auth.logout(request)  
    return HttpResponseRedirect("/login/") 
   
@login_required  
def changepwd(request):  
    if request.method == 'GET':  
        form = ChangepwdForm()  
        return render_to_response('changepwd.html', RequestContext(request, {'form': form,}))  
    else:  
        form = ChangepwdForm(request.POST)  
        if form.is_valid():  
            username = request.user.username  
            oldpassword = request.POST.get('oldpassword', '')  
            user = auth.authenticate(username=username, password=oldpassword)  
            if user is not None and user.is_active:  
                newpassword = request.POST.get('newpassword1', '')  
                user.set_password(newpassword)  
                user.save()  
                return render_to_response('index.html', RequestContext(request,{'changepwd_success':True}))  
            else:  
                return render_to_response('changepwd.html', RequestContext(request, {'form': form,'oldpassword_is_wrong':True}))  
        else:  
            return render_to_response('changepwd.html', RequestContext(request, {'form': form,})) 

def success(request):

	return HttpResponse('success')

@login_required(login_url='/login/')	
def index(request):

	return render_to_response('index.html')
	
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

@login_required(login_url='/login/')  
def AddCItemForm(request):

	form1 = CTypeForm({})
	form2 = CVenderForm({})
	form3 = CColorForm({})

	if request.method == 'POST':

		form1 = CTypeForm(request.POST)
		form2 = CVenderForm(request.POST)
		form3 = CColorForm(request.POST)
		success1 = ''
		success2 = ''
		success3 = ''
		inventorys = None
		
		if form1.is_valid():

			cd = form1.cleaned_data

			cType = CType()

			cType.CTypeName = cd['CTypeName']
			
			inventorys = CType.objects.filter(CTypeName__contains=cType.CTypeName)
			
			if (inventorys.count()==0):
				cType.save()
				success1 = '类型添加成功'
			else:
				success1 = '类型已存在！无需再添加！'
					
			form1 = CTypeForm()
			form2 = CVenderForm()
			form3 = CColorForm()

			return render_to_response('CItemAdd.html', {'form1': form1,'form2': form2,'form3': form3,'success1': success1},

			context_instance = RequestContext(request))
			
		if form2.is_valid():

			cd = form2.cleaned_data

			cVender = CVender()

			cVender.CVenderName = cd['CVenderName']

			inventorys = CVender.objects.filter(CVenderName__contains=cVender.CVenderName)
			
			if (inventorys.count()==0):
				cVender.save()
				success2 = '厂家添加成功'
			else:
				success2 = '厂家已存在！无需再添加！'
			
			form1 = CTypeForm()
			form2 = CVenderForm()
			form3 = CColorForm()

			return render_to_response('CItemAdd.html', {'form1': form1,'form2': form2,'form3': form3,'success2': success2},

			context_instance = RequestContext(request))
		
		if form3.is_valid():

			cd = form3.cleaned_data

			cColor = CColor()

			cColor.CColorName = cd['CColorName']

			inventorys = CColor.objects.filter(CColorName__contains=cColor.CColorName)
			
			if (inventorys.count()==0):
				cColor.save()
				success3 = '颜色添加成功'
			else:
				success3 = '颜色已存在！无需再添加！'
			
			form1 = CTypeForm()
			form2 = CVenderForm()
			form3 = CColorForm()
			
			return render_to_response('CItemAdd.html', {'form1': form1,'form2': form2,'form3': form3,'success3': success3},

			context_instance = RequestContext(request))

	else:

		form1 = CTypeForm()
		form2 = CVenderForm()
		form3 = CColorForm()

	return render_to_response('CItemAdd.html', {'form1': form1,'form2': form2,'form3': form3},

			context_instance = RequestContext(request))

@login_required(login_url='/login/') 
def DeleteCItemForm(request):

	form1 = CTypeForm({})
	form2 = CVenderForm({})
	form3 = CColorForm({})

	if request.method == 'POST':

		form1 = CTypeForm(request.POST)
		form2 = CVenderForm(request.POST)
		form3 = CColorForm(request.POST)
		success1 = ''
		success2 = ''
		success3 = ''
		inventorys = None
		
		if form1.is_valid():

			cd = form1.cleaned_data
			
			name = cd['CTypeName']
			
			try:
				cType = CType.objects.get(CTypeName = name)		
				inventorys = CInventory.objects.filter(CType__CTypeName__contains=name)
				if (inventorys.count()==0):				
					cType.delete()
					success1 = '类型删除成功'
				else:
					success1 = '库存中有该类型的数据，无法删除！'
			except:
				success1 = '类型不存在！无需再删除！'
					
			form1 = CTypeForm()
			form2 = CVenderForm()
			form3 = CColorForm()

			return render_to_response('CItemDelete.html', {'form1': form1,'form2': form2,'form3': form3,'success1': success1},

			context_instance = RequestContext(request))
			
		if form2.is_valid():

			cd = form2.cleaned_data

			name = cd['CVenderName']
			
			try:
				cVender = CVender.objects.get(CVenderName = name)
				inventorys = CInventory.objects.filter(CVender__CVenderName__contains=name)
				if (inventorys.count()==0):				
					cVender.delete()
					success2 = '厂家删除成功'
				else:
					success2 = '库存中有该厂家的数据，无法删除！'
			except:
				success2 = '厂家不存在！无需再删除！'
			
			form1 = CTypeForm()
			form2 = CVenderForm()
			form3 = CColorForm()

			return render_to_response('CItemDelete.html', {'form1': form1,'form2': form2,'form3': form3,'success2': success2},

			context_instance = RequestContext(request))
		
		if form3.is_valid():

			cd = form3.cleaned_data

			name = cd['CColorName']
			
			try:	
				cColor = CColor.objects.get(CColorName = name)
				inventorys = CInventory.objects.filter(CColor__CColorName__contains=name)
				if (inventorys.count()==0):				
					cColor.delete()
					success3 = '颜色删除成功'
				else:
					success3 = '库存中有该颜色的数据，无法删除！'
			except:
				success3 = '颜色不存在！无需再删除！'
			
			form1 = CTypeForm()
			form2 = CVenderForm()
			form3 = CColorForm()
			
			return render_to_response('CItemDelete.html', {'form1': form1,'form2': form2,'form3': form3,'success3': success3},

			context_instance = RequestContext(request))

	else:

		form1 = CTypeForm()
		form2 = CVenderForm()
		form3 = CColorForm()

	return render_to_response('CItemDelete.html', {'form1': form1,'form2': form2,'form3': form3},

			context_instance = RequestContext(request))	
	
@login_required(login_url='/login/') 
@transaction.commit_on_success
def	inBillBootstrap(request):
	
	form = CInStockBillForm({})
	
	cinStockBill = CInStockBill()
	
	success = ''

	if request.method == 'POST':

		form = CInStockBillForm(request.POST)

		if form.is_valid():

			cd = form.cleaned_data

			cinStockBill.CInStockBillCode = cd['CInStockBillCode']

			cinStockBill.CInStockDate = cd['CInStockDate']

			cinStockBill.COperator = cd['COperator']

			cinStockBill.CItemCode = cd['CItemCode']
			
			cinStockBill.CType = cd['CType']
			
			cinStockBill.CVender = cd['CVender']
			
			cinStockBill.CColor = cd['CColor']
			
			cinStockBill.CSize_S = cd['CSize_S']
			
			cinStockBill.CSize_M = cd['CSize_M']
			
			cinStockBill.CSize_L = cd['CSize_L']
			
			cinStockBill.CSize_XL = cd['CSize_XL']
			
			cinStockBill.CSize_2XL = cd['CSize_2XL']
			
			cinStockBill.CSize_3XL = cd['CSize_3XL']
			
			cinStockBill.CSize_4XL = cd['CSize_4XL']
			
			billbiz = CInStockBillBiz()
			
			cinStockBill.CAmount = billbiz.getInStockBillAcount(cinStockBill) 
			
			biz = CInventoryBiz()
			
			biz.saveForIn(cinStockBill)
				
			billbiz.save(cinStockBill)
				
			return render_to_response('inStock.html', {'form': form,'success': success,'cinStockBill':cinStockBill},

			context_instance = RequestContext(request))

	else:

		form = CInStockBillForm()

	return render_to_response('inStock.html',{'form':form,'success': success,'cinStockBill':cinStockBill}

		,context_instance = RequestContext(request))
	
@login_required(login_url='/login/') 
@transaction.commit_on_success
def	outBillBootstrap(request):
	
	form = COutStockBillForm({})
	
	outStockBill = COutStockBill()
	
	success = ''

	if request.method == 'POST':

		form = COutStockBillForm(request.POST)

		if form.is_valid():

			cd = form.cleaned_data

			outStockBill.COutStockBillCode = cd['COutStockBillCode']

			outStockBill.COutStockDate = cd['COutStockDate']

			outStockBill.COperator = cd['COperator']

			outStockBill.CItemCode = cd['CItemCode']
			
			outStockBill.CType = cd['CType']
			
			outStockBill.CVender = cd['CVender']
			
			outStockBill.CColor = cd['CColor']
			
			outStockBill.CSize_S = cd['CSize_S']
			
			outStockBill.CSize_M = cd['CSize_M']
			
			outStockBill.CSize_L = cd['CSize_L']
			
			outStockBill.CSize_XL = cd['CSize_XL']
			
			outStockBill.CSize_2XL = cd['CSize_2XL']
			
			outStockBill.CSize_3XL = cd['CSize_3XL']
			
			outStockBill.CSize_4XL = cd['CSize_4XL']
			
			billbiz = COutStockBillBiz()
			
			outStockBill.CAmount = billbiz.getInStockBillAcount(outStockBill) 
			
			biz = CInventoryBiz()
			
			if biz.saveForOut(outStockBill):
			
				billbiz.save(outStockBill)
				success = '出库单添加成功'
			else:
				success = '库存不足，无法出单'
				
			return render_to_response('outStock.html', {'form': form,'success': success,'outStockBill':outStockBill},

			context_instance = RequestContext(request))

	else:

		form = COutStockBillForm()

	return render_to_response('outStock.html',{'form':form,'success': success,'outStockBill':outStockBill}

		,context_instance = RequestContext(request))
	
def is_valid_date(str):
    '''判断是否是一个有效的日期字符串'''
    try:
        time.strptime(str, "%Y-%m-%d")
        return True
    except:
        return False

@login_required(login_url='/login/') 	
def	inventoryQueryBootstrap2(request):
	error=''
	totalAmount = 0
	if 'CItemCode_q' in request.GET:
		cItemCode_q = request.GET['CItemCode_q']
		if len(cItemCode_q) > 20:
			error = '货号长度错误！（<20）'        
		else:
			biz = CInventoryBiz()
			inventorys =biz.getInventoryByItemCode(cItemCode_q)
			for inventory in inventorys:
				totalAmount += inventory.CAmount
			return render_to_response('inventoryQueryBootstrap2.html',
										{'inventorys': inventorys, 'query1': cItemCode_q, 'error': error, 'totalAmount':totalAmount})
			#return render_to_response('inventoryQueryBootstrap.html')
	if 'CVender_q' in request.GET:
		cVender_q = request.GET['CVender_q']
		if len(cVender_q) > 20:
			error = '厂家名称长度错误！（<20）'       
		else: 
			biz = CInventoryBiz()
			inventorys =biz.getInventoryByCVenderName(cVender_q)
			for inventory in inventorys:
				totalAmount += inventory.CAmount
			return render_to_response('inventoryQueryBootstrap2.html',
										{'inventorys': inventorys, 'query2': cVender_q, 'error': error,'totalAmount':totalAmount})
	
	return render_to_response('inventoryQueryBootstrap2.html',{'error': error})

@login_required(login_url='/login/') 
def	inStockBillQueryBootstrap(request):
	error=''
	totalAmount = 0
	if 'Time_q' in request.GET:
		time_q = request.GET['Time_q']
		if  not is_valid_date(time_q):
			error = '时间格式错误！（如：2016-03-27）'         
		else:
			billbiz =  CInStockBillBiz()
			inStockBills =billbiz.getInStockBillByTime(time_q)
			for inStockBill in inStockBills:
				totalAmount += inStockBill.CAmount
			return render_to_response('inStockBillQueryBootstrap.html',
										{'inStockBills': inStockBills, 'query3': time_q, 'error': error,'totalAmount':totalAmount})
	return render_to_response('inStockBillQueryBootstrap.html',{'error': error})

@login_required(login_url='/login/') 
def	outStockBillQueryBootstrap(request):
	error=''
	totalAmount = 0
	if 'Time_q' in request.GET:
		time_q = request.GET['Time_q']
		if  not is_valid_date(time_q):
			error = '时间格式错误！（如：2016-03-27）'         
		else:
			billbiz =  COutStockBillBiz()
			outStockBills =billbiz.getOutStockBillByTime(time_q)
			for outStockBill in outStockBills:
				totalAmount += outStockBill.CAmount
			return render_to_response('outStockBillQueryBootstrap.html',
										{'stockBills': outStockBills, 'query3': time_q, 'error': error,'totalAmount':totalAmount})
	return render_to_response('outStockBillQueryBootstrap.html',{'error': error})

@login_required(login_url='/login/') 
def statisticalAnalysis(request):

	
	return render_to_response('statisticalAnalysis.html')