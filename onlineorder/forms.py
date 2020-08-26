from django import forms
from onlineorder.models import Product
import datetime
from django.conf import settings
from onlineorder.models import Order

class OrderForm(forms.ModelForm):
    order_date = forms.DateField(label='DATE',initial=datetime.date.today)
    po_ref_no = forms.CharField(label='PO REF No')
    project_name = forms.CharField(label='PROJECT NAME')
    project_site_address = forms.CharField(label='PROJECT SITE ADDRESS')
    contact_person_and_no = forms.CharField(label='CONTACT PERSON AND HP Np',help_text='Siska (1234 5678)')
    UNLOADING_CHOICES = [('A', 'By Site Crane'), ('B', 'By Site Forklift'),
                         ('C', 'By Lorry Crane: Separate arrangement & charges involved')]
    unloading_method = forms.ChoiceField(label='UNLOADING METHOD',widget=forms.RadioSelect,choices=UNLOADING_CHOICES)
    joe_panel_product_code = forms.ModelChoiceField(label='JOE PANEL PRODUCT CODE',queryset=Product.objects.all().order_by('product_code'))
    length = forms.FloatField(label='LENGTH (mm)')
    qty = forms.IntegerField(label='QTY')
    uom = forms.CharField(label='UOM (Unit of Measurement)')
    expected_delivery = forms.DateField(label='EXPECTED DELIVERY')
    remarks = forms.CharField(label='REMARKS')

    class Meta:
        model = Order
        fields = ['order_date','po_ref_no','project_name','project_site_address','contact_person_and_no',
                  'unloading_method','joe_panel_product_code','length','qty','uom','expected_delivery','remarks']

class ProductOrderForm(forms.Form):
    joe_panel_product_code = forms.ModelChoiceField(label='JOE PANEL PRODUCT CODE',queryset=Product.objects.all().order_by('product_code'))
    length = forms.FloatField(label='Length (mm)')
    qty = forms.IntegerField(label='QTY')
    uom = forms.CharField(label='UOM (Unit of Measurement)')
    expected_delivery = forms.DateField(label='Expected Delivery')
    remarks = forms.CharField(label='Remarks',required=False)
    