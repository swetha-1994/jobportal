"""jobportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from appsri import views
from django.conf.urls.static import static
from  django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.foremployer, name='employee'),
    path('sav3',views.employee,name='employe'),
    path('sav6/<int:id>/',views.profiles,name='profile'),
    path('pro/',views.shortresumes,name='proo'),
    path('sav4', views.forjobseker, name='jobseek'),
    path('sav',views.jobseeker,name='jobseker'),
    path('sav5/<int:id>/',views.jobdetails,name='details'),
    path('sav2', views.resume, name='resumee'),
    path('sav1',views.job,name='job'),
    path('save',views.submit,name='save'),
    path('save1',views.submit1,name='save1'),
    path('add/<int:id>',views.fiters,name='filters'),
    path('add1/<int:id>',views.filter,name='job_filter'),
    path('add2/<int:id>',views.infilter,name='ind_filter'),
    path('edit/<int:id>/',views.edit,name='edittes'),
    path('edit5/<int:id>/',views.edit5,name='editrf'),
    path('delete/<int:id>',views.delete,name='deletee'),
    path('register/', views.register, name='regist'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('auth/',include('social_django.urls', namespace='social')),
    path('boo/',views.bookkk,name='book1'),
    path('book/',views.book,name='bookk'),
    path('short1/',views.shortt,name='short'),
    path('short/',views.shortlist,name='shortt1'),
    path('inter1/',views.interjob,name='interest1'),
    path('inter/',views.interest,name='interestt'),



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
