from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from onlineorder.models import Order,Product
from onlineorder.forms import OrderForm, ProductOrderForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.conf import settings

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL,request.path))
    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits + 1
    
    context = {
        'num_visits': num_visits,
    }
    return render(request,'index.html',context=context)

def all_products(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL,request.path))
    return render(request,'onlineorder/all_products.html')

def all_accessories(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL,request.path))
    return render(request,'onlineorder/all_accessories.html')

def solid_panel(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL,request.path))
    return render(request,'onlineorder/solid_panel.html')

class OrderedProductsByUserListView(LoginRequiredMixin,generic.ListView):
    model = Order
    template_name = 'onlineorder/order_list_purchased_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return Order.objects.filter(purchaser=self.request.user).filter(status__exact='True').order_by('order_date')

def purchase_order_form(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL,request.path))
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            #next = request.GET.get('next',reverse('my-orders'))
            return HttpResponseRedirect(reverse('my-orders'))
            #return HttpResponseRedirect(next)
    context = {
        'form': form,
    }
    return render(request,'onlineorder/order_form.html',context)

def product_order_form(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL,request.path))
    form = ProductOrderForm()
    if request.method == 'POST':
        form = ProductOrderForm(request.POST)
        if form.is_valid():
           # form.save()
            return HttpResponseRedirect(reverse('purchase-order-form'))
    context = {
        'form': form,
    }
    return render(request,'onlineorder/product_order_form.html',context)

class ProductCreate(LoginRequiredMixin,CreateView):
    model = Product
    fields = '__all__'
    
class ProductUpdate(LoginRequiredMixin,UpdateView):
    model = Product
    fields = '__all__'

class ProductDelete(LoginRequiredMixin,DeleteView):
    model = Product
    success_url = reverse_lazy('products')

class OrderCreate(LoginRequiredMixin,CreateView):
    model = Order
    fields = '__all__'

class OrderUpdate(LoginRequiredMixin,UpdateView):
    model = Order
    fields = '__all__'

class OrderDelete(LoginRequiredMixin,DeleteView):
    model = Order
    fields = reverse_lazy('orders')

