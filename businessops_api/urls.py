from django.urls import path, include
from rest_framework.routers import DefaultRouter
from businessops_api import views

router = DefaultRouter()
router.register('category',views.CategoryViewSet)
router.register('transcategory',views.TransCategoryViewSet)
router.register('company',views.CompanyViewSet)
router.register('department',views.DepartmentViewSet)
router.register('empdepartment',views.EmpDepartmentViewSet)
router.register('employee',views.EmployeeViewSet)
router.register('product',views.ProductViewSet)
router.register('material',views.MaterialViewSet)
router.register('revenue',views.RevenueViewSet)
router.register('expense',views.ExpenseViewSet)

urlpatterns = [
    path('',include(router.urls))

]