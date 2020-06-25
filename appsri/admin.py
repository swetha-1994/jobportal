from django.contrib import admin
from .models import Resume,Experience,City,State,Country,Industries,Jobtype,Category,Bookmark,Shortlist,Interested
from .models import Job
admin.site.register(Resume)
admin.site.register(Job)
admin.site.register(Experience)
admin.site.register(City)
admin.site.register(State)
admin.site.register(Country)
admin.site.register(Industries)
admin.site.register(Jobtype)
admin.site.register(Category)
admin.site.register(Bookmark)
admin.site.register(Shortlist)
admin.site.register(Interested)