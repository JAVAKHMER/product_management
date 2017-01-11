from django.views.generic.base import View
from product_management.forms import CategoryForm, ProductForm
from product_management.models import Category, Product
from django.shortcuts import render, redirect, get_object_or_404
class HomeView(View):
    def get(self,request):
        return render(request,"index.html")
class CategoryView(View):
    def get(self,request):
        categoryForm = CategoryForm()
        return render(request, 'category.html', {'categoryForm': categoryForm})
    def post(self,request):
        categoryForm = CategoryForm(request.POST)
        if categoryForm.is_valid():
            categoryForm.save()
            return redirect('category_list')
        return render(request, 'category.html', {'categoryForm': categoryForm})
class DisplayCategoryView(View):
    def get(self,request):
        if request.GET.get('visible'):
            visible_filter = request.GET.get('visible')
            if 'False' == visible_filter:
                categorys = Category.objects.filter(Visible=False)
            else:
                categorys = Category.objects.filter(Visible=True)
        else:
            categorys = Category.objects.all()
#         categorys = Category.objects.all()
        return render(request, 'list_category.html', {'categorys': categorys})
class UpdateCategoryView(View):
    def get(self,request,id_category):
        category = get_object_or_404(Category, id=id_category)
        categoryForm = CategoryForm(request.POST or None, instance=category)
        return render(request, "update_category.html", {'categoryForm': categoryForm})
                
    def post(self,request,id_category):
        category = get_object_or_404(Category, id=id_category)
        categoryForm = CategoryForm(request.POST or None, instance=category)
        if categoryForm.is_valid():
            categoryForm.save()
            return redirect('category_list')
        return render(request, "update_category.html", {'categoryForm': categoryForm})

class DeleteCategoryView(View):
    def get(self,request,id_category):
        category = Category.objects.get(id=id_category)
        category.delete()
        return redirect('category_list')



class CreateProductView(View):
    def get(self,request):
        productForm = ProductForm()
        return render(request, 'create_product.html', {'productForm': productForm})
    def post(self,request):
        productForm = ProductForm(request.POST)
        if productForm.is_valid():
            productForm.save()
            return redirect('product_list')
        return render(request, 'create_product.html', {'productForm': productForm})

class DisplayProductView(View):
    def get(self,request):
        categorys = Category.objects.all()
        if request.GET.get('submit'):
            title_filter = request.GET.get('title')
            created_filter = request.GET.get('created')
            category_filter = request.GET.get('categorys')
#             if title_filter and created_filter and category_filter:
#                products = Product.objects.filter(title=title_filter,Created=created_filter,category=category_filter)
#             elif  title_filter or created_filter and category_filter:
#                products = Product.objects.filter(Created=created_filter,category=category_filter)
#             elif  title_filter or created_filter and category_filter:
#                products = Product.objects.filter(category=category_filter,Created=created_filter)
            if created_filter and title_filter:
               products = Product.objects.filter(title=title_filter,Created=created_filter,category__Name=category_filter)
            elif title_filter:
                products = Product.objects.filter(title=title_filter,category__Name=category_filter)
            elif created_filter:
                products = Product.objects.filter(Created=created_filter,category__Name=category_filter)
            elif category_filter:
                products = Product.objects.filter(category__Name=category_filter)
            else:
                products = Product.objects.all()
        elif request.GET.get('ascending'):
            products = Product.objects.all().order_by('title')
        elif request.GET.get('descending'):
            products = Product.objects.all().order_by('-title')
        else:
            products = Product.objects.all()
        return render(request,"list_product.html",{'products':products,'categorys':categorys})

class UpdateProductView(View):
    def get(self,request,id_product):
        product = get_object_or_404(Product, id=id_product)
        productForm = ProductForm(request.POST or None, instance=product)
        return render(request, "update_product.html", {'productForm': productForm})
                
    def post(self,request,id_product):
        product = get_object_or_404(Product, id=id_product)
        productForm = ProductForm(request.POST or None, instance=product)
        if productForm.is_valid():
            productForm.save()
            return redirect('product_list')
        return render(request, "update_product.html", {'categoryForm': productForm})


class DeleteProductView(View):
    def get(self,request,id_product):
        product = Product.objects.get(id=id_product)
        product.delete()
        return redirect('product_list')
    
