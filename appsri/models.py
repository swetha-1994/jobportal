# from django.db import models
from django.db import models

class Experience(models.Model):
    exp=models.CharField(max_length=5)
    def __str__(self):
        return self.exp
class City(models.Model):
    citys=models.CharField(max_length=30)
    def __str__(self):
        return self.citys
class State(models.Model):
   states=models.CharField(max_length=30)
   def __str__(self):
       return self.states
class Country(models.Model):
   countrys=models.CharField(max_length=30)
   def __str__(self):
       return self.countrys
class Industries(models.Model):
    indus=models.CharField(max_length=30)
    ind=models.ImageField(upload_to='iimg/')
    def __str__(self):
        return self.indus
class Category(models.Model):
    cate=models.CharField(max_length=30)
    catee=models.ImageField(upload_to='cimg/')
    def __str__(self):
        return self.cate
class Jobtype(models.Model):
    jobtype=models.CharField(max_length=30)
    jobtt=models.ImageField(upload_to='jimg/')
    def __str__(self):
        return self.jobtype


class Resume(models.Model):
    user_id = models.CharField(max_length=30)
    userr_id = models.CharField(max_length=30)
    frist=models.CharField(max_length=30)
    second=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.IntegerField()
    designation=models.CharField(max_length=30)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    experience=models.CharField(max_length=30)
    industt=models.ForeignKey(Industries,on_delete=models.CASCADE)
    jobtypeeee=models.ForeignKey(Jobtype,on_delete=models.CASCADE)
    expectpa=models.CharField(max_length=30)
    skill=models.CharField(max_length=30)
    photo=models.FileField(upload_to='file/')
    resumess=models.FileField(upload_to='file/')
    birth=models.DateField()
    address=models.CharField(max_length=30)
    city=models.ForeignKey(City,on_delete=models.CASCADE)
    state=models.ForeignKey(State,on_delete=models.CASCADE)
    country=models.ForeignKey(Country,on_delete=models.CASCADE)
    zipcode=models.IntegerField()
    highest=models.CharField(max_length=30)
    year=models.IntegerField()
    company=models.CharField(max_length=30)
    disg=models.CharField(max_length=30)
    dafrom=models.DateField()
    dato=models.DateField()
    facebook=models.CharField(max_length=30)
    google=models.CharField(max_length=30)
    twiteer=models.CharField(max_length=30)
    linkedin=models.CharField(max_length=30)
    Pinterest=models.CharField(max_length=30)
    instagram=models.CharField(max_length=30)



class Job(models.Model):
    usrejob=models.CharField(max_length=30)
    jobtitle=models.CharField(max_length=30)
    cname=models.CharField(max_length=30)
    cata=models.ForeignKey(Category,on_delete=models.CASCADE)
    position=models.CharField(max_length=30)
    exper=models.ForeignKey(Experience,on_delete=models.CASCADE)
    vacacy=models.IntegerField()
    package=models.CharField(max_length=30)
    logo=models.FileField(upload_to='file/')
    jobtypee=models.ForeignKey(Jobtype,on_delete=models.CASCADE)
    minqul=models.CharField(max_length=30)
    skills=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.IntegerField()
    website=models.CharField(max_length=30)
    adrres=models.CharField(max_length=30)
    city=models.ForeignKey(City,on_delete=models.CASCADE)
    state=models.ForeignKey(State,on_delete=models.CASCADE)
    country=models.ForeignKey(Country,on_delete=models.CASCADE)
    zip=models.IntegerField()
    facebook = models.CharField(max_length=30)
    google = models.CharField(max_length=30)
    twiteer = models.CharField(max_length=30)
    linkedin = models.CharField(max_length=30)
    Pinterest = models.CharField(max_length=30)
    instagram = models.CharField(max_length=30)


class Bookmark(models.Model):
    user=models.IntegerField()
    res=models.IntegerField()

class Shortlist(models.Model):
    listuser=models.IntegerField()
    listres=models.IntegerField()

class Interested(models.Model):
    jobuser=models.IntegerField()
    jobs=models.IntegerField()

