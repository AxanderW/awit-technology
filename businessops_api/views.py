from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from businessops_api import serializers
from businessops_api import models

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, updating category objects"""
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.CategorySerializer
    queryset= models.Category.objects.all()
    #permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','description')


class TransCategoryViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, updating category objects"""
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.TransCategorySerializer
    queryset= models.TransCategory.objects.all()
    #permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','description')

class CompanyViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, updating category objects"""
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.CompanySerializer
    queryset= models.Company.objects.all()
    #permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email','city','state','zipcode','country','phone')


class DepartmentViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, updating category objects"""
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.DepartmentSerializer
    queryset= models.Department.objects.all()
    #permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','description')


class EmpDepartmentViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, updating category objects"""
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.EmpDepartmentSerializer
    queryset= models.EmpDepartment.objects.all()
    #permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','description')



class EmployeeViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, updating category objects"""
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.EmployeeSerializer
    queryset= models.Employee.objects.all()
    #permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('fname','lname','email',
                    'city','state','zipcode',
                    'country','phone','title',
                    'status'
                    )


class ProductViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, updating category objects"""
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.ProductSerializer
    queryset= models.Product.objects.all()
    #permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','description','healing_property')



class MaterialViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, updating category objects"""
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.MaterialSerializer
    queryset= models.Material.objects.all()
    #permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','description','supplier')


class RevenueViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, updating category objects"""
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.RevenueSerializer
    queryset= models.Revenue.objects.all()
    #permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title','description')


class ExpenseViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, updating category objects"""
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.ExpenseSerializer
    queryset= models.Expense.objects.all()
    #permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title','description')

    


