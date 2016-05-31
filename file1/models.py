from django.db import models

# Create your models here.


class Category(models.Model):
	 category_text=models.CharField(max_length=200)
	 def __str__(self):
	 	return self.category_text
class SubCategory(models.Model):
	 category=models.ForeignKey(Category,on_delete=models.CASCADE)
	 subcategory_text=models.CharField(max_length=200)	
	 def __str__(self):
	 	return self.subcategory_text
        
class List(models.Model):
	 subcategory=models.ForeignKey(SubCategory,on_delete=models.CASCADE)
	 list_text=models.CharField(max_length=200)	
	 def __str__(self):
	 	return self.list_text




