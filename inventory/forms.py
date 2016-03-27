from django import forms

from models import Item,CColor,CVender

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
	
class CVenderForm(forms.Form):

	CVenderName = forms.CharField(
		
		max_length = 12,
		
		label = u'厂家:',
		
		error_messages={'required': u'必填项'},
		)	
	
class CColorForm(forms.Form):

	CColorName = forms.CharField(
		
		max_length = 12,
		
		label = u'颜色:',
		
		error_messages={'required': u'必填项'},
		)	


class CInStockBillForm(forms.Form):

	CInStockBillCode = forms.CharField(
		
		max_length = 12,
		
		label = u'入库单编码:',
		
		error_messages={'required': u'必填项'},
		)

	COperator = forms.CharField(
		
		label = u'操作员:',
		
		error_messages={'required': u'必填项'},
		)

	CInStockDate = forms.DateTimeField(
		
		label = u'入库日期:',
		
		error_messages={'required': u'必填项'},
		)
	
	CItemCode = forms.CharField(
		
		max_length = 10,
		
		label = u'货号:',
		
		error_messages={'required': u'必填项'},
		)

	CVender = forms.ModelChoiceField(
		
		label = u'厂家:',
		
		queryset = CVender.objects.all(),
		
		error_messages={'required': u'必填项'},
		
		)

	#Remark = forms.CharField(required=False)
	CColor = forms.ModelChoiceField(
		
		label = u'颜色:',
		
		queryset = CColor.objects.all(),
		
		error_messages={'required': u'必填项'},
		
		)

	CSize_S = forms.IntegerField(
		
		label = u'S:',
		
		required = False,
		)
	
	CSize_M = forms.IntegerField(
		
		label = u'M:',
		
		required = False,
		)
	
	CSize_L = forms.IntegerField(
		
		label = u'L:',
		
		required = False,
		)
	
	CSize_XL = forms.IntegerField(
		
		label = u'XL:',
		
		required = False,
		)
	
	CSize_2XL = forms.IntegerField(
		
		label = u'2XL:',
		
		required = False,
		)
	
	CSize_3XL = forms.IntegerField(
		
		label = u'3XL:',
		
		required = False,
		)
	
	CSize_4XL = forms.IntegerField(
		
		label = u'4XL:',
		
		required = False,
		)