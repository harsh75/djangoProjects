from django.conf.urls import url
from . import views



urlpatterns = [
    # ex: /file1/
    url(r'^$', views.home, name='home'),
    # ex: /file1/education/
    url(r'^(?P<cat_text>\w+)/$', views.categorypage, name='categories'),
    # ex: /file1/education/enginnering/
    url(r'^(?P<cat_text>\w+)/(?P<subcategory_text>\w+)/$', views.subcategorypage, name='subcategories'),
    # ex: /file1/education/enginnering/rv college/
    url(r'^(?P<cat_text>\w+)/(?P<subcategory_text>\w+)/(?P<details_text>(?s).*)/$', views.details, name='details'),
]