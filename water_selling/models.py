from multiprocessing.dummy import Array
from django.db import models
from datetime import datetime, timedelta

# Create your models here.


class employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    employee_name = models.CharField(max_length=100)
    employee_lastname = models.CharField(max_length=100)
    employee_age = models.IntegerField()
    employee_address = models.CharField(max_length=100)
    employee_contact = models.IntegerField()
    employee_salary = models.IntegerField()

    def __str__(self):
        return self.employee_name


class customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField(max_length=100)
    customer_city = models.CharField(max_length=100)
    customer_address = models.CharField(max_length=100)
    customer_zipcode = models.BigIntegerField()
    customer_contact = models.BigIntegerField()

    def __str__(self):
        return self.customer_name


class product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField()
    product_quantity = models.IntegerField()
    product_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

def one_day_hence():
    return datetime.now()+ timedelta(days=1)


class orders(models.Model):
    order_id = models.BigIntegerField(default=0)
    order_customer_id = models.ForeignKey(customer, on_delete=models.CASCADE)
    order_product_id = models.ForeignKey(product, on_delete=models.CASCADE)
    order_quantity = models.IntegerField(default=0)
    order_date = models.DateTimeField(auto_now_add=True,blank = True)

    

class cart(models.Model):
    cart_customer_id = models.IntegerField()
    cart_product_id = models.IntegerField()
    cart_product_quantity = models.IntegerField()


class container(models.Model):
    container_id = models.IntegerField()
    container_no = models.IntegerField()
    container_quantity = models.IntegerField()
    container_price = models.IntegerField()
    container_on_hand = models.IntegerField()

    def __str__(self):
        return self.container_id


# class payment(models.Model):
#     payment_id = models.IntegerField(primary_key=True)
#     payment_date = models.DateTimeField(auto_now_add=True)
#     payment_customer_id = models.ForeignKey(customer, on_delete=models.CASCADE)
#     payment_total = models.IntegerField()
#     payment_transaction_id = models.IntegerField()

#     def __str__(self):
#         return self.payment_id


class transaction(models.Model):
    transaction_id = models.IntegerField(primary_key=True)
    transaction_date = models.DateTimeField(auto_now_add=True,blank=True)
    transaction_customer_id = models.ForeignKey(customer, on_delete=models.CASCADE)
    transaction_order_id = models.IntegerField()
    transaction_total = models.IntegerField()

    def __str__(self):
        return str(self.transaction_id)

class delivery(models.Model):
    delivery_id = models.IntegerField(primary_key=True)
    delivery_date = models.DateTimeField(default=one_day_hence)
    delivery_customer_id = models.ForeignKey(customer, on_delete=models.CASCADE)
    delivery_order_id = models.IntegerField(default=0)
    delivery_transaction_id = models.ForeignKey(transaction, on_delete=models.CASCADE)
    delivery_city = models.CharField(max_length=100)
    delivery_address = models.CharField(max_length=100)
    delivery_zipcode = models.BigIntegerField(default=0)
    delivery_contact = models.BigIntegerField(default=0)
    delivery_quantity = models.IntegerField(default=0)
    delivery_delivery_man = models.CharField(max_length=20)

    def __str__(self):
        return str(self.delivery_id)
