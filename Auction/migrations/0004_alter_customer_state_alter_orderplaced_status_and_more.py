<<<<<<< HEAD
# Generated by Django 5.0.4 on 2024-04-21 06:24
=======
# Generated by Django 5.0.4 on 2024-04-21 06:44
>>>>>>> 4a8151cafd3d029479903ad5c4d084ad9b94cbaa

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auction', '0003_alter_customer_state_alter_orderplaced_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
<<<<<<< HEAD
            field=models.CharField(choices=[('Tamil Nadu', 'Tamil Nadu'), ('Goa', 'Goa'), ('Punjab', 'Punjab'), ('Tripura', 'Tripura'), ('Chandigarh', 'Chandigarh'), ('Ladakh', 'Ladakh'), ('Uttarakhand', 'Uttarakhand'), ('Mizoram', 'Mizoram'), ('Bihar', 'Bihar'), ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'), ('Manipur', 'Manipur'), ('Haryana', 'Haryana'), ('Chhattisgarh', 'Chhattisgarh'), ('Odisha', 'Odisha'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Jammu and Kashmir', 'Jammu and Kashmir'), ('Rajasthan', 'Rajasthan'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Assam', 'Assam'), ('Jharkhand', 'Jharkhand'), ('West Bengal', 'West Bengal'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Maharashtra', 'Maharashtra'), ('Nagaland', 'Nagaland'), ('Sikkim', 'Sikkim'), ('Gujarat', 'Gujrat'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Lakshadweep', 'Lakshadweep'), ('Karnataka', 'Karnataka'), ('Meghalaya', 'Meghalaya'), ('Kerala', 'Kerla'), ('Telangana', 'Telangana'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'), ('Puducherry', 'Puducherry')], max_length=100),
=======
            field=models.CharField(choices=[('Nagaland', 'Nagaland'), ('Bihar', 'Bihar'), ('Meghalaya', 'Meghalaya'), ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'), ('Jharkhand', 'Jharkhand'), ('Sikkim', 'Sikkim'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Goa', 'Goa'), ('Rajasthan', 'Rajasthan'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Telangana', 'Telangana'), ('Jammu and Kashmir', 'Jammu and Kashmir'), ('Haryana', 'Haryana'), ('Karnataka', 'Karnataka'), ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'), ('Uttarakhand', 'Uttarakhand'), ('Tamil Nadu', 'Tamil Nadu'), ('Lakshadweep', 'Lakshadweep'), ('Maharashtra', 'Maharashtra'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Gujarat', 'Gujrat'), ('Kerala', 'Kerla'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Puducherry', 'Puducherry'), ('Mizoram', 'Mizoram'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Manipur', 'Manipur'), ('West Bengal', 'West Bengal'), ('Tripura', 'Tripura'), ('Ladakh', 'Ladakh'), ('Assam', 'Assam'), ('Chhattisgarh', 'Chhattisgarh'), ('Chandigarh', 'Chandigarh'), ('Madhya Pradesh', 'Madhya Pradesh')], max_length=100),
>>>>>>> 4a8151cafd3d029479903ad5c4d084ad9b94cbaa
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
<<<<<<< HEAD
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled'), ('Pending', 'Pending')], default='Pending', max_length=50),
=======
            field=models.CharField(choices=[('Packed', 'Packed'), ('Delivered', 'Delivered'), ('Accepted', 'Accepted'), ('Pending', 'Pending'), ('Cancelled', 'Cancelled'), ('On The Way', 'On The Way')], default='Pending', max_length=50),
>>>>>>> 4a8151cafd3d029479903ad5c4d084ad9b94cbaa
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
<<<<<<< HEAD
            field=models.CharField(choices=[('E', 'Electronics'), ('AW', 'ArtWork'), ('W', 'Fine Wine and Spirits'), ('VC', 'Vehicles'), ('VRB', 'Vintage and Rare Books'), ('RE', 'RealEstate'), ('C', 'Collectibles'), ('FA', 'Fashion and Accesories'), ('JW', 'Jewelry and Watches')], max_length=3),
=======
            field=models.CharField(choices=[('VRB', 'Vintage and Rare Books'), ('FA', 'Fashion and Accesories'), ('VC', 'Vehicles'), ('C', 'Collectibles'), ('W', 'Fine Wine and Spirits'), ('AW', 'ArtWork'), ('RE', 'RealEstate'), ('E', 'Electronics'), ('JW', 'Jewelry and Watches')], max_length=3),
>>>>>>> 4a8151cafd3d029479903ad5c4d084ad9b94cbaa
        ),
    ]
