from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

CATEGORY_CHOICES = {
    ('AW','ArtWork'),
    ('JW','Jewelry and Watches'),
    ('VC','Vehicles'),
    ('RE','RealEstate'),
    ('FA','Fashion and Accesories'),
    ('VRB','Vintage and Rare Books'),
    ('C','Collectibles'),
    ('W','Fine Wine and Spirits'),
    ('E','Electronics'),
}

STATUS_CHOICES = {
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancelled','Cancelled'),
    ('Pending','Pending'),
}

STATE_CHOICES = {
      ('Andhra Pradesh' , 'Andhra Pradesh'),
      ('Arunachal Pradesh' , 'Arunachal Pradesh'),
      ('Assam' , 'Assam'),
      ('Bihar' , 'Bihar'),
      ('Chhattisgarh' , 'Chhattisgarh'),
      ('Goa' , 'Goa'),
      ('Gujarat' , 'Gujrat'),
      ('Haryana' , 'Haryana'),
      ('Himachal Pradesh' , 'Himachal Pradesh'),
      ('Jharkhand' , 'Jharkhand'),
      ('Karnataka' , 'Karnataka'),
      ('Kerala' , 'Kerla'),
      ('Madhya Pradesh' , 'Madhya Pradesh'),
      ('Maharashtra' , 'Maharashtra'),
      ('Manipur' , 'Manipur'),
      ('Meghalaya' , 'Meghalaya'),
      ('Mizoram' , 'Mizoram'),
      ('Nagaland' , 'Nagaland'),
      ('Odisha' , 'Odisha'),
      ('Punjab' , 'Punjab'),
      ('Rajasthan' , 'Rajasthan'),
      ('Sikkim' , 'Sikkim'),
      ('Tamil Nadu' , 'Tamil Nadu'),
      ('Telangana' , 'Telangana'),
      ('Tripura' , 'Tripura'),
      ('Uttar Pradesh' , 'Uttar Pradesh'),
      ('Uttarakhand' , 'Uttarakhand'),
      ('West Bengal' , 'West Bengal'),
      ('Andaman and Nicobar Islands' , 'Andaman and Nicobar Islands'),
      ('Chandigarh' , 'Chandigarh'),
      ('Dadra and Nagar Haveli and Daman and Diu' , 'Dadra and Nagar Haveli and Daman and Diu'),
      ('Jammu and Kashmir' , 'Jammu and Kashmir'),
      ('Ladakh' , 'Ladakh'),
      ('Lakshadweep' , 'Lakshadweep'),
     ('Puducherry' , 'Puducherry'),
}

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields as needed for your auction system
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.user.username


class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='item_images/')
    category = models.CharField(choices= CATEGORY_CHOICES, max_length=3)
    start_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    auction_end_time = models.DateTimeField(default=None, null=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('sold', 'Sold'),
        ('expired', 'Expired'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def is_active(self):
        return self.status == 'active'

    def is_sold(self):
        return self.status == 'sold'

    def is_expired(self):
        return self.status == 'expired'

    def place_bid(self, bid_amount):
        if self.is_active():
            if bid_amount > self.current_price:
                self.current_price = bid_amount
                self.save()
                return True
            else:
                return False
        else:
            return False


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.CharField(max_length=12)
    pincode = models.IntegerField()
    state = models.CharField(choices= STATE_CHOICES, max_length=100)
    
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    

    
class Bid(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Products, on_delete=models.CASCADE)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bid for {self.item.name} by {self.bidder.username} of ${self.bid_amount}"
    
class auction(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField(max_length=100)
    description = models.TextField(default='')
    image = models.ImageField(upload_to='item_images/')
    start_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Manually define a default value for 'start_price'
    end_date = models.DateTimeField()
    is_featured = models.BooleanField(default=False)
    item = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.product
    
class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.recipient.username} - {self.timestamp}"

    class Meta:
        ordering = ['-timestamp']
        
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(default=timezone.now)  # Manually defining default value

    def __str__(self):
        return f"Payment #{self.id} - {self.user.username} - ${self.amount} - {self.payment_date}"
    
    
class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE) 
    
class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')
    payment =  models.ForeignKey(Payment,on_delete=models.CASCADE,default="")
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    