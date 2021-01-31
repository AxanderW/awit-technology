from django.db import models


# Create your models here.
class Category(models.Model):
    """Database model for categories"""
    cat_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,unique=True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name',]
        verbose_name_plural = 'categories'

    def __str__(self):
        """ Return string representation of model"""
        return self.name


class TransCategory(models.Model):
    """Database model for transaction categories"""
    trns_cat_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,unique=True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name',]
        verbose_name_plural = 'transcategories'

    def __str__(self):
        """ Return string representation of model"""
        return self.name

class Company(models.Model):
    """Database model for companies"""
    comp_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,unique=True)
    email = models.EmailField(max_length=255,unique=True)
    address_1 = models.TextField()
    address_2 = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=1024)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=12)
    country = models.CharField(max_length=3,default='usa')
    phone = models.CharField(max_length=12)
    created_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    

    class Meta:
        ordering = ['name',]

    def __str__(self):
        """ Return string representation of model"""
        return self.name


class Department(models.Model):
    """Database model for departments"""
    dept_id = models.AutoField(primary_key=True)
    comp_id = models.ForeignKey(
        Company,
        on_delete = models.CASCADE,
        null=True
    )
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name',]

    def __str__(self):
        """ Return string representation of model"""
        return self.name

class EmpDepartment(models.Model):
    """Database model for departments"""
    emp_dept_id = models.AutoField(primary_key=True)
    comp_id = models.ForeignKey(
        Company,
        on_delete = models.CASCADE,
        null=True
    )
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name',]

    def __str__(self):
        """ Return string representation of model"""
        return self.name



class Person(models.Model):
    """Database model for persons"""
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    dob = models.DateField()
    email = models.EmailField(max_length=255,unique=True)
    address_1 = models.TextField()
    address_2 = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=1024)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=12)
    country = models.CharField(max_length=3,default='usa')
    phone = models.CharField(max_length=12)
    created_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        abstract = True



class Employee(Person):
    """Database model for employees"""
    emp_id = models.AutoField(primary_key=True)
    comp_id = models.ForeignKey(
        Company,
        on_delete = models.CASCADE,
        null=True
    )
    emp_dept_id = models.ForeignKey(
        EmpDepartment,
        on_delete = models.CASCADE,
        null=True,
        blank=True
    )
    title = models.CharField(max_length=100)
    hr_rt = models.DecimalField(max_digits=6,decimal_places=2)
    status = models.CharField(max_length=25)

    class Meta:
        ordering = ['emp_id',]

    def __str__(self):
        """ Return string representation of model"""
        return f'{self.lname},{self.fname}'




class Product(models.Model):
    """Database model for product"""
    prod_id = models.AutoField(primary_key=True)
    cat_id = models.ForeignKey(
        Category,
        on_delete = models.CASCADE,
    )
    dept_id = models.ForeignKey(
        Department,
        on_delete = models.CASCADE,
    )
    name = models.CharField(max_length=100,unique=True)
    price = models.DecimalField(max_digits=10,
                                    decimal_places=2,
                                    default = 0)

    quantity = models.IntegerField(default=1)
    total_cost = models.DecimalField(max_digits=10,
                                    decimal_places=2,
                                    default = 0)

    healing_property = models.TextField(default='none')
    description = models.TextField(default='none')
    image_main = models.ImageField(upload_to='products', null=True, blank=True)
    image_left = models.ImageField(upload_to='products',null=True, blank=True)
    image_right = models.ImageField(upload_to='products',null=True, blank=True)
    image_back = models.ImageField(upload_to='products',null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)
   

    class Meta:
        ordering = ['name',]

    def add_qty(self):
        self.quantity+=1
        return self.quantity

    def subtract_qty(self):
        self.quantity-=1
        return self.quantity


    def get_netprofit(self):
        try:
            return self.price - self.total_cost
        except:
            return None
   

    def __str__(self):
        """ Return string representation of model"""
        return self.name



class Material(models.Model):
    """Database model for materials"""
    mat_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    cat_id = models.ForeignKey(
        Category,
        on_delete = models.CASCADE,
    )
    supplier = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(default='none')
    total_price = models.DecimalField(max_digits=10,
                                    decimal_places=2)
    total_quantity = models.DecimalField(max_digits=10,decimal_places=2)
    unit_measure = models.CharField(max_length=20,default='count')
    created_on = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['name',]

    def get_unitprice(self):
        try:
            return self.total_price/self.total_quantity
        except:
            return None

    def __str__(self):
        """ Return string representation of model"""
        return self.name

class Transaction(models.Model):
    """Database model for transactiona"""
    trns_cat_id = models.ForeignKey(
        TransCategory,
        on_delete = models.CASCADE,
        
    )
    
    date = models.DateTimeField(auto_now_add=True)

    amount = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField(null=True,blank=True)
    

    class Meta:
        abstract = True




class Revenue(Transaction):
    """Database model for revenues"""
    rev_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)

    class Meta:
        ordering = ['rev_id',]

    def __str__(self):
        """ Return string representation of model"""
        return self.title


class Expense(Transaction):
    """Database model for expenses"""
    exp_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)

    class Meta:
        ordering = ['exp_id',]

    def __str__(self):
        """ Return string representation of model"""
        return self.title


        





