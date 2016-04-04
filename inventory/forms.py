from django import forms

from models import Color,Vender,Type

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
	
class TypeForm(forms.Form):

	TypeName = forms.CharField(
		
		max_length = 12,
		
		label = u'类型:',
		
		error_messages={'required': u'必填项'},
		)
	
class VenderForm(forms.Form):

	VenderName = forms.CharField(
		
		max_length = 12,
		
		label = u'厂家:',
		
		error_messages={'required': u'必填项'},
		)	
	
class ColorForm(forms.Form):

	ColorName = forms.CharField(
		
		max_length = 12,
		
		label = u'颜色:',
		
		error_messages={'required': u'必填项'},
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
	
	ItemCode = forms.CharField(
		
		max_length = 10,
		
		label = u'货号:',
		
		error_messages={'required': u'必填项'},
		)
	
	Type = forms.ModelChoiceField(
		
		label = u'类型:',
		
		queryset = Type.objects.all(),
		
		error_messages={'required': u'必填项'},
		
		)

	Vender = forms.ModelChoiceField(
		
		label = u'厂家:',
		
		queryset = Vender.objects.all(),
		
		error_messages={'required': u'必填项'},
		
		)

	#Remark = forms.CharField(required=False)
	Color = forms.ModelChoiceField(
		
		label = u'颜色:',
		
		queryset = Color.objects.all(),
		
		error_messages={'required': u'必填项'},
		
		)

	Size_S = forms.IntegerField(
		
		label = u'S:',
		
		required = False,
		)
	
	Size_M = forms.IntegerField(
		
		label = u'M:',
		
		required = False,
		)
	
	Size_L = forms.IntegerField(
		
		label = u'L:',
		
		required = False,
		)
	
	Size_XL = forms.IntegerField(
		
		label = u'XL:',
		
		required = False,
		)
	
	Size_2XL = forms.IntegerField(
		
		label = u'2XL:',
		
		required = False,
		)
	
	Size_3XL = forms.IntegerField(
		
		label = u'3XL:',
		
		required = False,
		)
	
	Size_4XL = forms.IntegerField(
		
		label = u'4XL:',
		
		required = False,
		)

	Size_5XL = forms.IntegerField(
		
		label = u'5XL:',
		
		required = False,
		)

    
    
    
	
	
	
class OutStockBillForm(forms.Form):

	OutStockBillCode = forms.CharField(
		
		max_length = 12,
		
		label = u'出库单编码:',
		
		error_messages={'required': u'必填项'},
		)

	Operator = forms.CharField(
		
		label = u'操作员:',
		
		error_messages={'required': u'必填项'},
		)
	
	ItemCode = forms.CharField(
		
		max_length = 10,
		
		label = u'货号:',
		
		error_messages={'required': u'必填项'},
		)
	
	Type = forms.ModelChoiceField(
		
		label = u'类型:',
		
		queryset = Type.objects.all(),
		
		error_messages={'required': u'必填项'},
		
		)

	Vender = forms.ModelChoiceField(
		
		label = u'厂家:',
		
		queryset = Vender.objects.all(),
		
		error_messages={'required': u'必填项'},
		
		)

	#Remark = forms.CharField(required=False)
	Color = forms.ModelChoiceField(
		
		label = u'颜色:',
		
		queryset = Color.objects.all(),
		
		error_messages={'required': u'必填项'},
		
		)

	Size_S = forms.IntegerField(
		
		label = u'S:',
		
		required = False,
		)
	
	Size_M = forms.IntegerField(
		
		label = u'M:',
		
		required = False,
		)
	
	Size_L = forms.IntegerField(
		
		label = u'L:',
		
		required = False,
		)
	
	Size_XL = forms.IntegerField(
		
		label = u'XL:',
		
		required = False,
		)
	
	Size_2XL = forms.IntegerField(
		
		label = u'2XL:',
		
		required = False,
		)
	
	Size_3XL = forms.IntegerField(
		
		label = u'3XL:',
		
		required = False,
		)
	
	Size_4XL = forms.IntegerField(
		
		label = u'4XL:',
		
		required = False,
		)

	Size_5XL = forms.IntegerField(
		
		label = u'5XL:',
		
		required = False,
		)
    
	
	