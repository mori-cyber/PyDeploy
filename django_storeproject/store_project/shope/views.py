from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, template_name='index.html')
def products(request, product_id: int):
    return  render(request, template_name='product.html')