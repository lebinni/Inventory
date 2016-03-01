from django import forms

from models import Item

class ItemForm(forms.Form):

	ItemCode = forms.CharField(
		
		max_length = 10,
		
		label = u'物料编码:',
		
		error_messages={'required': u'必填项'},
		)

	ItemName = forms.CharField(
		
		label = u'物料名称:',
		
		error_messages={'required': u'必填项'},
		
		)

	#Remark = forms.CharField(required=False)
	Remark = forms.CharField(
		
		widget = forms.Textarea,
		
		required = False,
		
		label = u'备注:',
		
		)
		
class InStockBillForm(forms.Form):

	InStockBillCode = forms.CharField(
		
		max_length = 12,
		
		label = u'入库单编码:',
		
		error_messages={'required': u'必填项'},
		)

	Operator = forms.CharField(
		
		label = u'操作员:',
		
		error_messages={'required': u'必填项'},
		)

	InStockDate = forms.DateTimeField(
		
		label = u'入库日期:',
		
		error_messages={'required': u'必填项'},
		)

	Amount = forms.IntegerField(
		
		label = u'入库数量:',
		
		error_messages={'required': u'必填项'},
		)

	Item = forms.ModelChoiceField(
		
		label = u'物料:',
	
		queryset = Item.objects.all(),
		
		error_messages={'required': u'必填项'},

		)