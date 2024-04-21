from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout
from .forms import CustomerRegistrationForm,CustomerProfileForm,AuctionForm,BidForm,ProductForm
from .models import Bid, Customer,auction,Wishlist,Products,Payment,Cart,OrderPlaced, CATEGORY_CHOICES
from django.contrib import messages
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.http import JsonResponse
from django.utils import timezone

# Create your views here.

def landing(request):
    return render(request,'landing.html')

@login_required
def base(request):
    return render(request,'base.html')

@login_required
def home(request):
    Home_dict = {}
    product_obj = Products.objects.all()
    Home_dict['Product'] = product_obj
    return render(request,'home.html', Home_dict)


@login_required
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')  # Redirect to the user's profile page
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to your home or login page


class CustomerRegistrationView(View):
    def get (self,request):
        form = CustomerRegistrationForm()
        totalitem = 0
        wishitem = 0
        # if request.user.is_authenticated:
        #     totalitem = len(Cart.objects.filter(user = request.user))
        #     wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request,'customerregistration.html',locals())
    
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations! User Register Succesfully")
            
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request,'customerregistration.html',locals())
    
@method_decorator(login_required,name='dispatch')      
class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        totalitem = 0
        wishitem = 0
        # if request.user.is_authenticated:
        #     totalitem = len(Cart.objects.filter(user = request.user))
        #     wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request,'profile.html',locals())

    def post(self,request):
        form = CustomerProfileForm(request.POST)
        
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            pincode = form.cleaned_data['pincode']
            
            reg = Customer(user = user , name = name , locality = locality , city = city , mobile = mobile, state = state , pincode = pincode)
            reg.save()
            messages.success(request,"Congratulations! Profile Save Succesfully")
            
        else:
            messages.warning(request,"Invalid Input Data")
            
        return render(request,'profile.html',locals())
@login_required     
def address(request):
    add = Customer.objects.filter(user = request.user)
    totalitem = 0
    wishitem = 0
    # if request.user.is_authenticated:
    #     totalitem = len(Cart.objects.filter(user = request.user))
    #     wishitem = len(Wishlist.objects.filter(user=request.user))
    return render (request,'address.html',locals())

@method_decorator(login_required,name='dispatch')
class updateAddress(View):
    def get(self,request,pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        totalitem = 0
        wishitem = 0
        # if request.user.is_authenticated:
        #     totalitem = len(Cart.objects.filter(user = request.user))
        #     wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request,'updateAddress.html',locals())
    
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.pincode = form.cleaned_data['pincode']
            add.save()
            messages.success(request,"Congratulations ! Profile Updated Succesfully")
        
        else:
            messages.warning("Invalid Input Data")
        # products = Products.objects.get(pk = pk) 
        return redirect("address")
@login_required      
def auction_detail(request, auction_id):
    auction = auction.objects.get(pk=auction_id)
    return render(request, 'auction_detail.html', {'auction': auction})
@login_required   
def browseauctions(request, id):
    auctions = Products.objects.get(pk = id)
    try:
        if request.method == "POST":
            print(request.POST.get('bid_amount'))
            if auctions.place_bid( bid_amount= float(request.POST.get('bid_amount'))):
                Bid.objects.create(bidder = request.user,item = auctions , bid_amount = float(request.POST.get('bid_amount')))
                print('Bid Place Successfully')
                bid_details =  Bid.objects.filter(bidder = request.user, item = auctions).order_by('-timestamp').all()
                return redirect('product_detail', item_id = id)
            else:
                print("Something went wrong")
    except Exception as e:
        print(e)
    return render(request, 'browseauctions.html' , {'auction': auctions})

# def place_bid(request, item_id):
#     product = get_object_or_404(Products, id=item_id)
#     if request.method == 'POST':
#         form = BidForm(request.POST)
#         if form.is_valid():
#             bid_amount = form.cleaned_data['bid_amount']
#             if bid_amount > product.current_price:
#                 product.current_price = bid_amount
#                 product.save()
#                 print(request.user.id)
#                 Bid.objects.create(bidder = request.user.id, item = item_id, bid_amount = bid_amount)
#                 return redirect('product_detail', item_id=item_id)
#             else:
#                 form.add_error('bid_amount', 'Bid amount must be higher than the current price.')
#     else:
        
#         form = BidForm()
#     return render(request, 'place_bid.html', {'form': form, 'product': product})


def place_bid(request, item_id):
    if request.method == "POST":
        product_detail =  get_object_or_404(Products, id = item_id)
        print(product_detail)
    return render(request,'home.html')

def product_detail(request, item_id):
    # Retrieve the product object based on the provided item_id
    product = get_object_or_404(Products, pk=item_id)
    status = 1
    if product.status == "sold":
        status = 0
    elif product.status == "expired":
        status = 3
    elif product.auction_end_time < timezone.now():
        status = 2
    elif product.status == "active" or product.status == "result":
        status = 1
    else:
        status = 0
    bid_details =  Bid.objects.filter(bidder = request.user, item = product).order_by('-timestamp').all()
    return render(request, 'product_detail.html', {'product': product,
                                                    'bid_details': bid_details,
                                                    "status" : status
                                                    }
                )

@method_decorator(login_required,name='dispatch')
class CategoryView(View):
    def get(self,request,val):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user = request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        product = Products.objects.filter(category = val)
        name = Products.objects.filter(category = val).values('name')
        return render(request,"Category.html",{'name': name, 'product': product})

@method_decorator(login_required,name='dispatch')   
class CategoryTitle(View):
    def get(self,request,val):
        product = Products.objects.filter(name = val)
        name = Products.objects.filter(category = product[0].category).values("name")
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user = request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request,"Category.html",{'name': name, 'product': product})
    
@login_required   
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Products.objects.get(id=product_id)
    Cart(user=user,product = product).save()
    return redirect("/cart")

@login_required    
def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
        
    totalamount = amount + 40
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user = request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request,'addtocart.html',locals())

def plus_cart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        print(prod_id)
        c = Cart.objects.get(Q(product = prod_id) & Q(user = request.user))
        c.quantity+=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount+40
        
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
    
def minus_cart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product = prod_id) & Q(user = request.user))
        c.quantity-=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount+40
        
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
    
def remove_cart(request):
        if request.method == "GET":
            prod_id = request.GET['prod_id']
            c = Cart.objects.get(Q(product = prod_id) & Q(user = request.user))
            c.delete()
            user = request.user
            cart = Cart.objects.filter(user=user)
            amount = 0
        
            for p in cart:
                value = p.quantity * p.product.discounted_price
                amount = amount + value
            totalamount = amount+40
        
        data={
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)

def show_wishlist(request):
    user = request.user
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user = request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    product = Wishlist.objects.filter(user=user)
    return render(request,'wishlist.html',locals())
def plus_wishlist(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        product = Products.objects.get(id=prod_id)
        user = request.user
        Wishlist(user=user,product=product).save()
        data={
        'message':'Wishlist Added Successfully',
        }
        return JsonResponse(data)
    
def minus_wishlist(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        product = Products.objects.get(id=prod_id)
        user = request.user
        Wishlist.objects.filter(user=user,product=product).delete()
        data={
            'message':'Wishlist Removed Successfully',
        }
        return JsonResponse(data)

@login_required 
def search(request):
    query = request.GET['search']
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user = request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    product = Products.objects.filter(Q(name__icontains=query))
    return render(request,'search.html',{'Product':product})

@login_required    
def orders(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user = request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    order_placed = OrderPlaced.objects.filter(user = request.user )
    return render(request, 'orders.html',locals())

def addproduct(request):
    addproduct_dict = {}
    addproduct_dict['choices'] = dict(CATEGORY_CHOICES)
    if request.method == "POST":
        form_dict  = request.POST
        file_dict = request.FILES
        print(file_dict)
        add_products = Products.objects.create(
            name = form_dict['ProductName'], 
            description = form_dict['ProductDescription'], 
            image = file_dict['ProductImage'],
            category = form_dict['ProductCategory'], 
            start_price = form_dict['ProductStartPrice'],
            current_price = 0,
            auction_end_time = form_dict['ProductAuctionEnd'],
            seller = request.user )
        if add_products:
            messages.success(request,'Your Product is Upload Successfully')
            return redirect('product_detail', add_products.id)
        else:
            messages.error(request,'Somthing Went Wrong')
            print('unsuccessfully')
    return render(request,'addproduct.html', addproduct_dict)

def add_address(request):
    form = CustomerProfileForm(request.POST)
    if form.is_valid():
        user = request.user
        name = form.cleaned_data['name']
        locality = form.cleaned_data['locality']
        city = form.cleaned_data['city']
        mobile = form.cleaned_data['mobile']
        state = form.cleaned_data['state']
        pincode = form.cleaned_data['pincode']
        reg = Customer(user = user , name = name , locality = locality , city = city , mobile = mobile, state = state , pincode = pincode)
        reg.save()
        messages.success(request,"Congratulations! Profile Save Succesfully")
        return redirect('address')
    else:
        messages.warning(request,"Invalid Input Data")
    return render(request,'add_address.html',{'form':form})

def Winning_Result(request,id=None):
    print("in")
    Winning_Result_Dict = {}
    winning_result = Products.objects.filter(auction_end_time__lt = timezone.now()).exclude(status = "sold").order_by("-auction_end_time")
    for winning in winning_result:
        if winning.status == "active":
            winning.status = "result"
            winning.save()
    higher_bid = Bid.objects.all()
    Winning_Result_Dict["winning_result"] = winning_result
    Winning_Result_Dict["higher_bid"] = higher_bid
    return render(request,"Winning.html",Winning_Result_Dict)

def Winning_Result_Declare(request):
    if request.method == "POST":
        data = request.POST.get('id')
        higher_bid = Bid.objects.all()
        get_obj = Products.objects.get(id= request.POST.get("id"))
        get_obj.status = "sold"
        for higher in higher_bid:
            if higher.item == get_obj and higher.bid_amount == get_obj.current_price:
                get_obj.sold_to = higher.bidder
        get_obj.save()
        return JsonResponse({
            "status": 'success',
            'message': 'Done Successfully'
        })