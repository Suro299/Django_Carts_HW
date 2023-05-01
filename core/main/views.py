from django.shortcuts import render, redirect
from .models import Products, Cart
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from users.models import CustomUser as User

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="main/register.html", context={"register_form":form})




def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")



def index(request):
	product_list = Products.objects.all()

	if request.method == "POST":
		prod_id = request.POST.get("id")
  
		my_prod = Products.objects.get(id = prod_id)
  
		user = User.objects.get(username = request.user.username)
		user.cart_prod.add(my_prod)
		user.save()

        # cart_list = Cart.objects.all().select_related('prodcut').values_list('prodcut__name', flat = True)

        # if my_prod.name in cart_list:
        #     cart_prod = Cart.objects.get(prodcut__name = my_prod.name)   
        #     cart_prod.count += 1
        #     cart_prod.price += cart_prod.price          
        #     cart_prod.save()
        # else:
        #     Cart.objects.create(prodcut = my_prod)
        #     prod = Cart.objects.get(prodcut__name = my_prod.name)   
        #     prod.price = my_prod.price
        #     prod.save() 
            
        # return redirect("index")  
	return render(request, "main/index.html", context = {
		"product_list": product_list,
    })
    
    
def cart(request):
    # cart_list = Cart.objects.all()
    # cart_count = sum(list(Cart.objects.all().values_list('count', flat=True)))
    user_carts = User.objects.get(username = request.user.username).cart_prod.all()
    
    return render(request, "main/cart.html", context = {
		"user_carts": user_carts
	})