import sys
from django.utils.timezone import now
try:
    from django.db import models
except Exception:
    print("There was an error loading django modules. Do you have django installed?")
    sys.exit()

from django.conf import settings
import uuid


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=20, default='car_make')
    description = models.CharField(max_length=1000)

    def __str__(self):
        return "Make: " + self.name + "," + \
             "Description: " + self.description


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car model object
class CarModel(models.Model):
    model_name = models.CharField(null=False, max_length=20)
    dealer_id = models.IntegerField(default=0)
    SEDAN = 'sedan'
    SUV = 'suv'
    WAGON = 'wagon'
    TYPE_CHOICES = [
        (SEDAN, 'Sedan'), 
        (SUV, 'SUV'), 
        (WAGON, 'WAGON')
    ]
    model_type = models.CharField(null=False, max_length=20, choices=TYPE_CHOICES, default=WAGON)
    year = models.DateField(null=True)
    make = models.ForeignKey(CarMake, null=False, on_delete=models.CASCADE)
    #make = models.ManyToManyField(CarMake)

    def __str__(self):
        return "Model: " + self.model_name + "," + \
            "Type: " + self.model_type + "," + \
                "Year: " + self.year




# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
