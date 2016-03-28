from django.conf.urls import patterns, include, url

from django.views.generic import TemplateView

from inventory import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    
	url(r'^$', views.login, name="home"),
    
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
	
	# url(r'^admin/', include(admin.site.urls)),
    
    url(r'^index/$',  views.index),
    
    url(r'^login/$',  views.login), 
    
    url(r'^logout/$',  views.logout),
    
    url(r'^changepwd/$',  views.changepwd),  

	url(r'^success/$', views.success),
	
	url(r'^AddItem/$', views.AddItemForm),
    
    url(r'^AddCItem/$', views.AddCItemForm),
    
    url(r'^DeleteCItem/$', views.DeleteCItemForm),
	
	url(r'^AddInStockBill/$', views.AddInStockBillForm),
	
	url(r'^inventoryQueryBootstrap/$',views.inventoryQueryBootstrap2),
    
    url(r'^inStockBillQueryBootstrap/$',views.inStockBillQueryBootstrap),
    
    url(r'^outStockBillQueryBootstrap/$',views.outStockBillQueryBootstrap),
    
    url(r'^inBillBootstrap/$',views.inBillBootstrap),
    
    url(r'^outBillBootstrap/$',views.outBillBootstrap),
    
    url(r'^statisticalAnalysis/$',views.statisticalAnalysis),

)
