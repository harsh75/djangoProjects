
# Create your views here.
from django.http import HttpResponse
from .models import Category,SubCategory,List
from django.shortcuts import get_object_or_404, render
def home(request):
	
	q=Category.objects.all()
	return render(request, 'file1/home.html', {'categories':q})

def categorypage(request,cat_text):
    
    q=Category.objects.get(category_text=cat_text)
    
    context={'subcategories': q}
    return render(request, 'file1/categorypage.html',context)
	


def subcategorypage(request,cat_text,subcategory_text):
    q=Category.objects.get(category_text=cat_text)
    
    s=q.subcategory_set.get(subcategory_text=subcategory_text)
    
    return render(request,'file1/subcategorypage.html', {'eachcategories': s} )
    

def details(request,cat_text,subcategory_text,details_text):
    
    return HttpResponse("Hello, world. You're at the file1 details page.")
