from django.db import models
from django.contrib.auth.models import User
import uuid
import datetime
from django.conf import settings
# Create your models here.

class Product(models.Model):

    product_code = models.CharField(primary_key=True,max_length=20,unique=True)

    class Meta:
        ordering = ['-product_code']

    def get_absolute_url(self):
        return reverse('model-detail-view',args=[str(self.id)])

    def __str__(self):
        return self.product_code

class Order(models.Model):
    '''order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular order')
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    order_date = models.DateField(auto_now_add=True)
    purchaser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    ORDER_STATUS = (
        ('o', 'Open'),
        ('r', 'Released'),
        ('c', 'Closed'),
        ('d', 'Cancelled'),
    )

    status = models.CharField(max_length=1, choices=ORDER_STATUS, blank=True, default='o', help_text='Order status',)

    class Meta:
        ordering = ['-order_date']
        permissions = (("can_mark_released", "Set order as released"),
                       ("can_mark_closed", "Set order as closed"),
                       ("can_mark_cancelled", "Set order as cancelled"),)

    def __str__(self):
        return f'{self.order_id} ({self.order_date})' '''
    DATE_FORMAT = ('%dd-%mm-%yy')
   # id = models.CharField(primary_key=True,default=uuid.uuid4,max_length=30,null=False)
    order_date = models.DateField(verbose_name='DATE', default=datetime.date.today,blank=True,null=True)
    purchaser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,verbose_name='CONTRACTOR')
    po_ref_no = models.CharField(primary_key=True,max_length=30,verbose_name='PO REF No',default='')
    project_name = models.CharField(max_length=50,verbose_name='PROJECT NAME',default='')
    project_site_address = models.CharField(max_length=50,verbose_name='PROJECT SITE ADDRESS',default='')
    contact_person_and_no = models.CharField(max_length=50,verbose_name='PM/CONTACT PERSON Name & HP No',default='')

    UNLOADING_CHOICES = [('A', 'By Site Crane'), ('B', 'By Site Forklift'),
                         ('C', 'By Lorry Crane: Separate arrangement & charges involved')]
    unloading_method = models.CharField(max_length=1,verbose_name='UNLOADING METHOD', choices=UNLOADING_CHOICES,default='')
    #product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,verbose_name='JOE PANEL PRODUCT CODE')
    joe_panel_product_code = models.CharField(verbose_name='JOE PANEL PRODUCT CODE',default='',max_length=30)
    length = models.FloatField(verbose_name='Length (mm)',default=0.0)
    qty = models.IntegerField(verbose_name='QTY',default=0)

    UOM_CHOICES = (('1','PCS'),('2','BAG'),('3','ROLL/BOX'),('4','BOX'),('5','PAIL'),('6','BOTTLE'),('7','UNIT'),('8','CAN'),('9','SET'))
    uom = models.CharField(max_length=1,verbose_name='UOM (Unit of Measurement)',default='',choices=UOM_CHOICES)
    expected_delivery = models.DateField(verbose_name='Expected Delivery',default=datetime.date.today,blank=True,null=True)
    remarks = models.TextField(max_length=200,verbose_name='Remarks',blank=True,null=True)

    ORDER_STATUS = (
        ('o', 'Open'),
        ('r', 'Released'),
        ('c', 'Closed'),
        ('d', 'Cancelled'),
    )

    status = models.BooleanField(verbose_name='Status',default=True)  #true means open, false means closed

    def __str__(self):
        return '{0}: {1}'.format(self.po_ref_no,self.status)


