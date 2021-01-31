from rest_framework import serializers
from businessops_api import models

class CategorySerializer(serializers.ModelSerializer):
    """Serializes a category object"""
    class Meta:
        model = models.Category
        fields = '__all__'

class TransCategorySerializer(serializers.ModelSerializer):
    """Serializes a transaction category object"""
    class Meta:
        model = models.TransCategory
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    """Serializes a company object"""
    class Meta:
        model = models.Company
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    """Serializes a Department object"""
    class Meta:
        model = models.Department
        fields = '__all__'

class EmpDepartmentSerializer(serializers.ModelSerializer):
    """Serializes a Employee Department object"""
    class Meta:
        model = models.EmpDepartment
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    """Serializes a Employee object"""
    class Meta:
        model = models.Employee
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
    """Serializes a Product object"""
    class Meta:
        model = models.Product
        fields = '__all__'



class MaterialSerializer(serializers.ModelSerializer):
    """Serializes a Product object"""
    class Meta:
        model = models.Material
        fields = '__all__'


class RevenueSerializer(serializers.ModelSerializer):
    """Serializes a Product object"""
    class Meta:
        model = models.Revenue
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    """Serializes a Product object"""
    class Meta:
        model = models.Expense
        fields = '__all__'