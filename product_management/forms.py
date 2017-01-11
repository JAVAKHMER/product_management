from django.forms.models import ModelForm
from product_management.models import Category, Product
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    