from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('home/',views.home, name = 'home'),
    path('',views.landing,name="landing"),
    path('',views.base,name="base"),
    path('signup/', views.signup, name='signup'),
    path('add-to-cart/',views.add_to_cart, name = 'add-to-cart'),
    path("Category/<slug:val>",views.CategoryView.as_view(), name = 'Category'),
    path("Category-Title/<val>",views.CategoryTitle.as_view(), name = 'Category-Title'),
    path('search/',views.search,name='search'),
    # path('place_bid/<int:item_id>/', views.place_bid, name='place_bid'),
    path('product_detail/<int:item_id>/', views.product_detail, name='product_detail'),
    path('profile/',views.ProfileView.as_view(), name = 'profile'),
    path('updateAddress/<int:pk>',views.updateAddress.as_view(), name = 'updateAddress'),
    path('orders/',views.orders,name = 'orders'),
    path('address/',views.address, name = 'address'),
    path('registration/',views.CustomerRegistrationView.as_view(), name = 'customerregistration'),
    path('login/',auth_view.LoginView.as_view(template_name = 'login.html',authentication_form = LoginForm) , name  = 'login'),
    path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name = 'changepassword.html', form_class = MyPasswordChangeForm, success_url ='/passwordchangedone'), name = 'passwordchange'),
    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name = 'passwordchangedone.html'), name = 'passwordchangedone'),
    path('logout/',auth_view.LogoutView.as_view(next_page = 'login'), name = 'logout'),
    path('password-reset/',auth_view.PasswordResetView.as_view(template_name = 'password_reset.html', form_class = MyPasswordResetForm), name = 'password_reset'),
    path('password-reset/done/',auth_view.PasswordResetDoneView.as_view(template_name = 'password_reset_done.html'), name = 'password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name = 'password_reset_confirm.html', form_class = MySetPasswordForm), name = 'password_reset_confirm'),
    path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(template_name = 'password_reset_complete.html'), name = 'password_reset_complete'),
    path('auction/<int:auction_id>/', views.auction_detail, name='auction_detail'),
    path('browse/<int:id>', views.browseauctions, name='browseauctions'),
    path('add-to-cart/',views.add_to_cart, name = 'add-to-cart'),
    path('cart/',views.show_cart, name = 'showcart'),
    path('pluscart/',views.plus_cart,name='pluscart'),
    path('minuscart/',views.minus_cart,name='minuscart'),
    path('removecart/',views.remove_cart,name='removecart'),
    path('pluswishlist/',views.plus_wishlist,name='pluswishlist'),
    path('minuswishlist/',views.minus_wishlist,name='minuswishlist'),
    path('addproduct/',views.addproduct,name='addproduct'),
    # path('create/', views.create_auction, name='create_auction'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)