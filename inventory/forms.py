from django import forms

from models import Item,CColor,CVender,CType

from django.contrib.auth.models import User  

from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput, BootstrapUneditableInput  
  
class LoginForm(forms.Form):  
    username = forms.CharField(  
        required=True,  
        label=u"用户名",  
        error_messages={'required': '请输入用户名'},  
        widget=forms.TextInput(  
            attrs={  
                'placeholder':u"用户名",  
            }  
        ),  
    )      
    password = forms.CharField(  
        required=True,  
        label=u"密码",  
        error_messages={'required': u'请输入密码'},  
        widget=forms.PasswordInput(  
            attrs={  
                'placeholder':u"密码",  
            }  
        ),  
    )     
    def clean(self):  
        if not self.is_valid():  
            raise forms.ValidationError(u"用户名和密码为必填项")  
        else:  
            cleaned_data = super(LoginForm, self).clean()

class ChangepwdForm(forms.Form):  
    oldpassword = forms.CharField(  
        required=True,  
        label=u"原密码",  
        error_messages={'required': u'请输入原密码'},  
        widget=forms.PasswordInput(  
            attrs={  
                'placeholder':u"原密码",  
            }  
        ),  
    )   
    newpassword1 = forms.CharField(  
        required=True,  
        label=u"新密码",  
        error_messages={'required': u'请输入新密码'},  
        widget=forms.PasswordInput(  
            attrs={  
                'placeholder':u"新密码",  
            }  
        ),  
    )  
    newpassword2 = forms.CharField(  
        required=True,  
        label=u"确认密码",  
        error_messages={'required': u'请再次输入新密码'},  
        widget=forms.PasswordInput(  
            attrs={  
                'placeholder':u"确认密码",  
            }  
        ),  
     )  
    def clean(self):  
        if not self.is_valid():  
            raise forms.ValidationError(u"所有项都为必填项")  
        elif self.cleaned_data['newpassword1'] <> self.cleaned_data['newpassword2']:  
            raise forms.ValidationError(u"两次输入的新密码不一样")  
        else:  
            cleaned_data = super(ChangepwdForm, self).clean()  
        return cleaned_data 

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
	

	
class CTypeForm(forms.Form):

	CTypeName = forms.CharField(
		
		max_length = 12,
		
		label = u'类型:',
		
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
		
		required = False,
		
		#error_messages={'required': u'必填项'},
		)
	
	CItemCode = forms.CharField(
		
		max_length = 10,
		
		label = u'货号:',
		
		error_messages={'required': u'必填项'},
		)
	
	CType = forms.ModelChoiceField(
		
		label = u'类型:',
		
		queryset = CType.objects.all(),
		
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
	
	CAmount = forms.IntegerField(
		
		label = u'总计:',
		
		required = False,
		)
	
class COutStockBillForm(forms.Form):

	COutStockBillCode = forms.CharField(
		
		max_length = 12,
		
		label = u'出库单编码:',
		
		error_messages={'required': u'必填项'},
		)

	COperator = forms.CharField(
		
		label = u'操作员:',
		
		error_messages={'required': u'必填项'},
		)

	COutStockDate = forms.DateTimeField(
		
		label = u'出库日期:',
		
		required = False,
		
		#error_messages={'required': u'必填项'},
		)
	
	CItemCode = forms.CharField(
		
		max_length = 10,
		
		label = u'货号:',
		
		error_messages={'required': u'必填项'},
		)
	
	CType = forms.ModelChoiceField(
		
		label = u'类型:',
		
		queryset = CType.objects.all(),
		
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
	
	CAmount = forms.IntegerField(
		
		label = u'总计:',
		
		required = False,
		)