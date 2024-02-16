from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

class MenuImage(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='menu_images/')

class MenuReview(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])

class Order(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)
    order_date = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.menu_item.price * self.quantity

class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name