from django.shortcuts import render, redirect
from .models import Products, Cart


def index(request):
    product_list = Products.objects.all()
    cart_count = sum(list(Cart.objects.all().values_list('count', flat=True)))
    

    if request.method == "POST":
        prod_id = request.POST.get("id")
        my_prod = Products.objects.get(id = prod_id)

        cart_list = Cart.objects.all().select_related('prodcut').values_list('prodcut__name', flat = True)


        if my_prod.name in cart_list:
        
            cart_prod = Cart.objects.get(prodcut__name = my_prod.name)   
            cart_prod.count += 1
            cart_prod.price += cart_prod.price          
            cart_prod.save()
        
        else:
            Cart.objects.create(prodcut = my_prod)
            prod = cart_prod = Cart.objects.get(prodcut__name = my_prod.name)   
            prod.price = my_prod.price
            prod.save() 
            
        return redirect("index")  
            
    return render(request, "main/index.html", context = {
        "product_list": product_list,
        "cart_count": cart_count
    })
    
    
def cart(request):
    cart_list = Cart.objects.all()
    cart_count = sum(list(Cart.objects.all().values_list('count', flat=True)))
    
    return render(request, "main/cart.html", context = {
        "cart_list": cart_list,
        "cart_count": cart_count
    })
    