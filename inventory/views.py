# -*- coding: UTF-8 -*- 
# Create your views here.
from django.shortcuts import render_to_response,RequestContext

from django.http import HttpResponse,HttpResponseRedirect

#from django.db import models

from models import Type,Vender,Color,InStockBill,Inventory,OutStockBill

from forms import TypeForm,VenderForm,ColorForm,InStockBillForm,ChangepwdForm,OutStockBillForm

from biz import InventoryBiz,InStockBillBiz,OutStockBillBiz

from django.db import transaction

import datetime,time,sys 

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
sys.path.append("..")
import db2xls


def charts(request):
    exchange = {'2001-01-31': 1.064, '2002-01-31': 1.1305,
                '2003-01-31': 0.9417, '2004-01-31': 0.7937,
                '2005-01-31': 0.7609, '2006-01-31': 0.827,
                '2007-01-31': 0.7692, '2008-01-31': 0.6801,
                '2009-01-31': 0.7491, '2010-01-31': 0.7002,
                '2011-01-31': 0.7489, '2012-01-31': 0.7755,
                '2013-01-31': 0.7531,
                }

    browser_stats = [['Chrome', 52.9], ['Firefox', 27.7], ['Opera', 1.6],
                     ['Internet Explorer', 12.6], ['Safari', 4], ['baidu', 4]]

    temperature = [{u'data': {  '2012-00-01 00:00:00 -0700': 7,
                                '2012-01-01 00:00:00 -0700': 6.9,
                                '2012-02-01 00:00:00 -0700': 9.5,
                                '2012-03-01 00:00:00 -0700': 14.5,
                                '2012-04-01 00:00:00 -0700': 18.2,
                                '2012-05-01 00:00:00 -0700': 21.5,
                                '2012-06-01 00:00:00 -0700': 25.2,
                                '2012-07-01 00:00:00 -0700': 26.5,
                                '2012-08-01 00:00:00 -0700': 23.3,
                                '2012-09-01 00:00:00 -0700': 18.3,
                                '2012-10-01 00:00:00 -0700': 13.9,
                                '2012-11-01 00:00:00 -0700': 9.6},
                    u'name': u'Tokyo'},
                    {u'data': { '2012-00-01 00:00:00 -0700': -0.2,
                                '2012-01-01 00:00:00 -0700': 0.8,
                                '2012-02-01 00:00:00 -0700': 5.7,
                                '2012-03-01 00:00:00 -0700': 11.3,
                                '2012-04-01 00:00:00 -0700': 17,
                                '2012-05-01 00:00:00 -0700': 22,
                                '2012-06-01 00:00:00 -0700': 24.8,
                                '2012-07-01 00:00:00 -0700': 24.1,
                                '2012-08-01 00:00:00 -0700': 20.1,
                                '2012-09-01 00:00:00 -0700': 14.1,
                                '2012-10-01 00:00:00 -0700': 8.6,
                                '2012-11-01 00:00:00 -0700': 2.5},
                    u'name': u'New York'},
                    {u'data': { '2012-00-01 00:00:00 -0700': -0.9,
                                '2012-01-01 00:00:00 -0700': 0.6,
                                '2012-02-01 00:00:00 -0700': 3.5,
                                '2012-03-01 00:00:00 -0700': 8.4,
                                '2012-04-01 00:00:00 -0700': 13.5,
                                '2012-05-01 00:00:00 -0700': 17,
                                '2012-06-01 00:00:00 -0700': 18.6,
                                '2012-07-01 00:00:00 -0700': 17.9,
                                '2012-08-01 00:00:00 -0700': 14.3,
                                '2012-09-01 00:00:00 -0700': 9,
                                '2012-10-01 00:00:00 -0700': 3.9,
                                '2012-11-01 00:00:00 -0700': 1},
                    u'name': u'Berlin'},
                    {u'data': { '2012-00-01 00:00:00 -0700': 3.9,
                                '2012-01-01 00:00:00 -0700': 4.2,
                                '2012-02-01 00:00:00 -0700': 5.7,
                                '2012-03-01 00:00:00 -0700': 8.5,
                                '2012-04-01 00:00:00 -0700': 11.9,
                                '2012-05-01 00:00:00 -0700': 15.2,
                                '2012-06-01 00:00:00 -0700': 17,
                                '2012-07-01 00:00:00 -0700': 16.6,
                                '2012-08-01 00:00:00 -0700': 14.2,
                                '2012-09-01 00:00:00 -0700': 10.3,
                                '2012-10-01 00:00:00 -0700': 6.6,
                                '2012-11-01 00:00:00 -0700': 4.8},
                    u'name': u'London'}]

    sizes = [['X-Small', 5], ['Small', 27], ['Medium', 10],
             ['Large', 14], ['X-Large', 10]]

    areas = {'2013-07-27 07:08:00 UTC': 4, '2013-07-27 07:09:00 UTC': 3,
             '2013-07-27 07:10:00 UTC': 2, '2013-07-27 07:04:00 UTC': 2,
             '2013-07-27 07:02:00 UTC': 3, '2013-07-27 07:00:00 UTC': 2,
             '2013-07-27 07:06:00 UTC': 1, '2013-07-27 07:01:00 UTC': 5,
             '2013-07-27 07:05:00 UTC': 5, '2013-07-27 07:03:00 UTC': 3,
             '2013-07-27 07:07:00 UTC': 3}

    return render(request, 'charts.html', locals())
  
def login(request):  
    db2xls.db2xls()
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
def about(request):

    return render_to_response('about.html')

@login_required(login_url='/login/')	
def index(request):
	db2xls.db2xls()
	return render_to_response('index.html')
	
@login_required(login_url='/login/')  
def addItem(request):

	form1 = TypeForm({})
	form2 = VenderForm({})
	form3 = ColorForm({})

	if request.method == 'POST':

		form1 = TypeForm(request.POST)
		form2 = VenderForm(request.POST)
		form3 = ColorForm(request.POST)
		success1 = ''
		success2 = ''
		success3 = ''
		inventorys = None
		
		if form1.is_valid():

			cd = form1.cleaned_data

			type = Type()

			type.TypeName = cd['TypeName']
			
			inventorys = Type.objects.filter(TypeName__contains=type.TypeName)
			
			if (inventorys.count()==0):
				type.save()
				success1 = '类型添加成功'
			else:
				success1 = '类型已存在！无需再添加！'
					
			form1 = TypeForm()
			form2 = VenderForm()
			form3 = ColorForm()

			return render_to_response('itemAdd.html', {'form1': form1,'form2': form2,'form3': form3,'success1': success1},

			context_instance = RequestContext(request))
			
		if form2.is_valid():

			cd = form2.cleaned_data

			vender = Vender()

			vender.VenderName = cd['VenderName']

			inventorys = Vender.objects.filter(VenderName__contains=vender.VenderName)
			
			if (inventorys.count()==0):
				vender.save()
				success2 = '厂家添加成功'
			else:
				success2 = '厂家已存在！无需再添加！'
			
			form1 = TypeForm()
			form2 = VenderForm()
			form3 = ColorForm()

			return render_to_response('itemAdd.html', {'form1': form1,'form2': form2,'form3': form3,'success2': success2},

			context_instance = RequestContext(request))
		
		if form3.is_valid():

			cd = form3.cleaned_data

			color = Color()

			color.ColorName = cd['ColorName']

			inventorys = Color.objects.filter(ColorName__contains=color.ColorName)
			
			if (inventorys.count()==0):
				color.save()
				success3 = '颜色添加成功'
			else:
				success3 = '颜色已存在！无需再添加！'
			
			form1 = TypeForm()
			form2 = VenderForm()
			form3 = ColorForm()
			
			return render_to_response('itemAdd.html', {'form1': form1,'form2': form2,'form3': form3,'success3': success3},

			context_instance = RequestContext(request))

	else:

		form1 = TypeForm()
		form2 = VenderForm()
		form3 = ColorForm()

	return render_to_response('itemAdd.html', {'form1': form1,'form2': form2,'form3': form3},

			context_instance = RequestContext(request))	
	
@login_required(login_url='/login/') 
def deleteItem(request):

	form1 = TypeForm({})
	form2 = VenderForm({})
	form3 = ColorForm({})

	if request.method == 'POST':

		form1 = TypeForm(request.POST)
		form2 = VenderForm(request.POST)
		form3 = ColorForm(request.POST)
		success1 = ''
		success2 = ''
		success3 = ''
		inventorys = None
		
		if form1.is_valid():

			cd = form1.cleaned_data
			
			name = cd['TypeName']
			
			try:
				type = Type.objects.get(TypeName = name)		
				inventorys = Inventory.objects.filter(Type__TypeName__contains=name)
				if (inventorys.count()==0):				
					type.delete()
					success1 = '类型删除成功'
				else:
					success1 = '库存中有该类型的数据，无法删除！'
			except:
				success1 = '类型不存在！无需再删除！'
					
			form1 = TypeForm()
			form2 = VenderForm()
			form3 = ColorForm()

			return render_to_response('itemDelete.html', {'form1': form1,'form2': form2,'form3': form3,'success1': success1},

			context_instance = RequestContext(request))
			
		if form2.is_valid():

			cd = form2.cleaned_data

			name = cd['VenderName']
			
			try:
				vender = Vender.objects.get(VenderName = name)
				inventorys = Inventory.objects.filter(Vender__VenderName__contains=name)
				if (inventorys.count()==0):				
					vender.delete()
					success2 = '厂家删除成功'
				else:
					success2 = '库存中有该厂家的数据，无法删除！'
			except:
				success2 = '厂家不存在！无需再删除！'
			
			form1 = TypeForm()
			form2 = VenderForm()
			form3 = ColorForm()

			return render_to_response('itemDelete.html', {'form1': form1,'form2': form2,'form3': form3,'success2': success2},

			context_instance = RequestContext(request))
		
		if form3.is_valid():

			cd = form3.cleaned_data

			name = cd['ColorName']
			
			try:	
				color = Color.objects.get(ColorName = name)
				inventorys = Inventory.objects.filter(Color__ColorName__contains=name)
				if (inventorys.count()==0):				
					color.delete()
					success3 = '颜色删除成功'
				else:
					success3 = '库存中有该颜色的数据，无法删除！'
			except:
				success3 = '颜色不存在！无需再删除！'
			
			form1 = TypeForm()
			form2 = VenderForm()
			form3 = ColorForm()
			
			return render_to_response('itemDelete.html', {'form1': form1,'form2': form2,'form3': form3,'success3': success3},

			context_instance = RequestContext(request))

	else:

		form1 = TypeForm()
		form2 = VenderForm()
		form3 = ColorForm()

	return render_to_response('itemDelete.html', {'form1': form1,'form2': form2,'form3': form3},

			context_instance = RequestContext(request))	
	
@login_required(login_url='/login/') 
@transaction.commit_on_success
def	inBillBootstrap(request):
	
	form = InStockBillForm({})
	
	inStockBill = InStockBill()
	
	success = ''

	if request.method == 'POST':

		form = InStockBillForm(request.POST)

		if form.is_valid():

			cd = form.cleaned_data

			inStockBill.InStockBillCode = cd['InStockBillCode']

			inStockBill.Operator = cd['Operator']

			inStockBill.ItemCode = cd['ItemCode']
			
			inStockBill.Type = cd['Type']
			
			inStockBill.Vender = cd['Vender']
			
			inStockBill.Color = cd['Color']
			
			inStockBill.Size_S = cd['Size_S']
			
			inStockBill.Size_M = cd['Size_M']
			
			inStockBill.Size_L = cd['Size_L']
			
			inStockBill.Size_XL = cd['Size_XL']
			
			inStockBill.Size_2XL = cd['Size_2XL']
			
			inStockBill.Size_3XL = cd['Size_3XL']
			
			inStockBill.Size_4XL = cd['Size_4XL']
            
			inStockBill.Size_5XL = cd['Size_5XL']
			
			billbiz = InStockBillBiz()
			
			inStockBill.Amount = billbiz.getInStockBillAcount(inStockBill) 
			
			biz = InventoryBiz()
			
			biz.saveForIn(inStockBill)
				
			billbiz.save(inStockBill)
            
			success = '入库单添加成功'
				
			return render_to_response('inStock.html', {'form': form,'success': success,'inStockBill':inStockBill},

			context_instance = RequestContext(request))

	else:

		form = InStockBillForm()

	return render_to_response('inStock.html',{'form':form,'success': success,'inStockBill':inStockBill}

		,context_instance = RequestContext(request))
	
@login_required(login_url='/login/') 
@transaction.commit_on_success
def	outBillBootstrap(request):
	
	form = OutStockBillForm({})
	
	outStockBill = OutStockBill()
	
	success = ''

	if request.method == 'POST':

		form = OutStockBillForm(request.POST)

		if form.is_valid():

			cd = form.cleaned_data

			outStockBill.OutStockBillCode = cd['OutStockBillCode']

			outStockBill.Operator = cd['Operator']

			outStockBill.ItemCode = cd['ItemCode']
			
			outStockBill.Type = cd['Type']
			
			outStockBill.Vender = cd['Vender']
			
			outStockBill.Color = cd['Color']
			
			outStockBill.Size_S = cd['Size_S']
			
			outStockBill.Size_M = cd['Size_M']
			
			outStockBill.Size_L = cd['Size_L']
			
			outStockBill.Size_XL = cd['Size_XL']
			
			outStockBill.Size_2XL = cd['Size_2XL']
			
			outStockBill.Size_3XL = cd['Size_3XL']
			
			outStockBill.Size_4XL = cd['Size_4XL']
            
			outStockBill.Size_5XL = cd['Size_5XL']
			
			billbiz = OutStockBillBiz()
			
			outStockBill.Amount = billbiz.getInStockBillAcount(outStockBill) 
			
			biz = InventoryBiz()
			
			if biz.saveForOut(outStockBill):
			
				billbiz.save(outStockBill)
				success = '出库单添加成功'
			else:
				success = '库存不足，无法出单'
				
			return render_to_response('outStock.html', {'form': form,'success': success,'outStockBill':outStockBill},

			context_instance = RequestContext(request))

	else:

		form = OutStockBillForm()

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
def	inventoryQueryBootstrap(request):
	error=''
	totalAmount = 0
	showContext = ''
	if 'ItemCode_q' in request.GET:
		itemCode_q = request.GET['ItemCode_q']
		if len(itemCode_q) > 20:
			error = '货号长度错误！（<20）'        
		else:
			biz = InventoryBiz()
			inventorys =biz.getInventoryByItemCode(itemCode_q)
			for inventory in inventorys:
				totalAmount += inventory.Amount
			showContext = '查询结果共计 %d 件' %totalAmount
			return render_to_response('inventoryQueryBootstrap.html',
										{'inventorys': inventorys, 'query1': itemCode_q, 'error': error, 'showContext':showContext})
			
	if 'Vender_q' in request.GET:
		vender_q = request.GET['Vender_q']
		if len(vender_q) > 20:
			error = '厂家名称长度错误！（<20）'       
		else: 
			biz = InventoryBiz()
			inventorys =biz.getInventoryByCVenderName(vender_q)
			for inventory in inventorys:
				totalAmount += inventory.Amount
			showContext = '查询结果共计 %d 件' %totalAmount
			return render_to_response('inventoryQueryBootstrap.html',
										{'inventorys': inventorys, 'query2': vender_q, 'error': error,'showContext':showContext})
	
	if request.method == "GET":
		if request.GET.has_key('find0Amount0'): 
			biz = InventoryBiz()
			inventorys =biz.find0Inventory()
			totalAmount =inventorys.count()
			showContext = '查询结果共计 %d 条' %totalAmount
			return render_to_response('inventoryQueryBootstrap.html',{'inventorys': inventorys, 'error': error,'showContext':showContext})
		elif request.GET.has_key('find0Amount1'): 
			biz = InventoryBiz()
			inventorys = biz.find0InventoryForItemCode()
			totalAmount =inventorys.count()
			showContext = '查询结果共计 %d 条' %totalAmount
			return render_to_response('inventoryQueryBootstrap.html',{'inventorys': inventorys, 'error': error,'showContext':showContext})
		elif request.GET.has_key('delete0Amount0'): 
			biz = InventoryBiz()
			inventorys =biz.find0Inventory()
			totalAmount =inventorys.count()
			if inventorys.count()>0:
				for inv in inventorys:
					inv.delete()
			showContext = '删除记录共计 %d 条' %totalAmount
			return render_to_response('inventoryQueryBootstrap.html',{'inventorys': inventorys, 'error': error,'showContext':showContext})	
		elif request.GET.has_key('delete0Amount1'): 
			biz = InventoryBiz()
			inventorys = biz.find0InventoryForItemCode()
			totalAmount =inventorys.count()
			if inventorys.count()>0:
				for inv in inventorys:
					inv.delete()
			showContext = '删除记录共计 %d 条' %totalAmount
			return render_to_response('inventoryQueryBootstrap.html',{'inventorys': inventorys, 'error': error,'showContext':showContext})
		
                		
	return render_to_response('inventoryQueryBootstrap.html',{'error': error,'showContext':showContext})

@login_required(login_url='/login/') 
def	inStockBillQueryBootstrap(request):
	error=''
	totalAmount = 0
	if 'Time_q' in request.GET:
		time_q = request.GET['Time_q']
		if  not is_valid_date(time_q):
			error = '时间格式错误！（如：2016-03-27）'         
		else:
			billbiz =  InStockBillBiz()
			inStockBills =billbiz.getInStockBillByTime(time_q)
			for inStockBill in inStockBills:
				totalAmount += inStockBill.Amount
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
			billbiz =  OutStockBillBiz()
			outStockBills =billbiz.getOutStockBillByTime(time_q)
			for outStockBill in outStockBills:
				totalAmount += outStockBill.Amount
			return render_to_response('outStockBillQueryBootstrap.html',
										{'outStockBills': outStockBills, 'query3': time_q, 'error': error,'totalAmount':totalAmount})
	return render_to_response('outStockBillQueryBootstrap.html',{'error': error})

@login_required(login_url='/login/') 
def statisticalAnalysis(request):
	
	return render_to_response('statisticalAnalysis.html')