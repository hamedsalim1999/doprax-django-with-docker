from django.views.generic import ListView,DetailView,View
from .models import Product,Category,Order,OrderItem,Coupon
from django.shortcuts import render,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
# Create your views here.
class Allproduct(ListView):
    queryset = Product.objects.available()
    template_name = 'shop/shop.html'
    context_object_name = 'shop'
    paginate_by = 25
    
class ProductList(DetailView):
    queryset = Product.objects.available()
    template_name = 'shop/produce.html'
    context_object_name = 'shop'
    slug_url_kwarg ='slug'

class CategoryList(ListView):
    paginate_by = 5
    template_name = 'shop/shop.html'
    context_object_name = 'product_category'
    model = Product
    def get_queryset(self):
        self.category = get_object_or_404(Category,slug = self.kwargs['slug'])
        product = Product.objects.filter(category = self.category)
        return product
    def get_context_data(self, **kwargs):
        context = super(CategoryList,self).get_context_data(**kwargs)
        context["category"] = self.category
        return context

@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        product=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0] 
        # check if the order item is in the order
        if order.items.filter(product=item).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("shop:order-summary")
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("shop:order-summary")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("shop:order-summary")

@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(product=item).exists():
            order_item = OrderItem.objects.filter(
                product=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from your cart.")
            return redirect("shop:order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect('shop:order-summary')
    else:
        messages.info(request, "You do not have an active order")
        return redirect("shop:product", slug=slug)

@login_required
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)

    order_qs = Order.objects.filter(
        user=request.user
    )

    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order

        if order.items.filter(product=item).exists():
            order_item = OrderItem.objects.filter(
                product=item,

            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, "This item quantity was updated.")
            return redirect("shop:order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("shop:order-summary")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("shop:order-summary", slug=slug)

def get_coupon(request, code):
    try:
        coupon = Coupon.objects.get(code=code)
        return coupon
    except ObjectDoesNotExist:
        messages.info(request, "This coupon does not exist")
        return redirect("shop:checkout")

class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'shop/test.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("/")
