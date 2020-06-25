from django.shortcuts import render,redirect
from appsri.models import Resume,Job, Experience, City, State, Country, Category, Industries, Jobtype, Bookmark ,Shortlist,Interested
from django.contrib.auth.models import User
from  django.contrib import messages
from django.contrib import auth
from django.contrib.auth import authenticate,logout as auth_logout
def employee(request):
    browse=Resume.objects.all()
    skill=request.POST.get('skills')
    cityes=request.POST.get('citys')
    expern=request.POST.get('expern')
    if skill:
        browse=browse.filter(skill=skill)
    if   cityes:
        browse=browse.filter(city=cityes)
    if  expern:
        browse=browse.filter(experience=expern)
    return render(request, 'browse_employer.html', {'brow': browse})

def jobseeker(request):
    browsejob=Job.objects.all()
    skill = request.POST.get('skills')
    jobtitle = request.POST.get('jobtitle')
    expern = request.POST.get('expern')
    if skill:
        browsejob = browsejob.filter(skills=skill)
    if jobtitle:
        browsejob = browsejob.filter(jobtitle=jobtitle)
    if expern:
        browsejob = browsejob.filter(exper=expern)
    return render(request,'browse_jobseeker.html',{'browjob':browsejob})
def job(request):
    expernce = Experience.objects.all()
    cityss1 = City.objects.all()
    statess1 = State.objects.all()
    countryss1 = Country.objects.all()
    catatt= Category.objects.all()
    jobb= Jobtype.objects.all()
    return render(request,'create_job.html',{'key':expernce,'key1':cityss1,'key2':statess1,'key3':countryss1,'key4':catatt,'key5':jobb})
def resume(request):
    exper=Experience.objects.all()
    cityss=City.objects.all()
    statess=State.objects.all()
    countryss=Country.objects.all()
    catatt = Category.objects.all()
    jobb = Jobtype.objects.all()
    indus= Industries.objects.all()
    return render(request,'create_resume.html',{'key':exper,'key1':cityss,'key2':statess,'key3':countryss,'key4':catatt,'key5':jobb,'key6':indus})
def foremployer(request):

    cityss=City.objects.all()
    exper = Experience.objects.all()
    indus = Industries.objects.all()
    return render(request,'for_employer.html',{'key':exper,'key1':cityss,'key6':indus})
def forjobseker(request):
    expernce = Experience.objects.all()
    catatt = Category.objects.all()
    jobb = Jobtype.objects.all()
    return render(request,'for_jobseeker.html',{'key':expernce,'key4':catatt,'key5':jobb})
def jobdetails(request,id):
    jobdetail=Job.objects.get(id=id)

    try:
        interested = Interested.objects.get(jobs=id)
    except Interested.DoesNotExist:
        interested = None
    usere = User.objects.get(id=request.user.id)
    return render(request,'job_detail.html',{'details':jobdetail,'userrr':usere,'interested':interested})
def profiles(request,id):
    pro=Resume.objects.get(id=id)
    try:
        book = Bookmark.objects.get(res=id)
    except Bookmark.DoesNotExist:
        book = None
    user=User.objects.get(id=request.user.id)
    return render(request,'profile.html',{'prof':pro,'userr':user,'book':book})
def shortresumes(request,id):
    pro=Resume.objects.get(id=id)
    try:
        shortlist = Shortlist.objects.get(listres=id)
    except Shortlist.DoesNotExist:
        shortlist = None
    user=User.objects.get(id=request.user.id)
    return render(request,'profile.html',{'proff':pro,'userrr':user,'shortlist':shortlist})
def fiters(request,id):
    cattta=Category.objects.get(id=id)
    cattta1=Job.objects.filter(cata=cattta)
    return render(request,'browse_jobseeker.html',{'browjob':cattta1})
def filter(request,id):
    jobbb = Jobtype.objects.get(id=id)
    jobbb1 = Job.objects.filter(jobtypee=jobbb)
    return render(request, 'browse_jobseeker.html', {'browjob': jobbb1})
def infilter(request,id):
    induss=Industries.objects.get(id=id)
    induss1=Resume.objects.filter(industt=induss)
    return render(request, 'browse_employer.html', {'brow': induss1})
def submit(request):
    user_id = request.POST.get('user_id')
    userr_id = request.POST.get('userr_id')
    lucky1=request.POST.get('ed')
    frist=request.POST.get('fristname')
    second=request.POST.get('lastname')
    email=request.POST.get('email')
    phone=request.POST.get('phone')
    designation=request.POST.get('designation')
    category=request.POST.get('category')
    cateee=Category.objects.get(id=category)
    experience=request.POST.get('experience')
    expern=Experience.objects.get(id=experience)
    jobtype=request.POST.get('jobtype')
    jobbb=Jobtype.objects.get(id=jobtype)
    expectpa=request.POST.get('expectpackage')
    skill=request.POST.get('skills')
    photo=request.FILES.get('photo')
    resumess=request.FILES.get('resumes')
    birth=request.POST.get('birth')
    address=request.POST.get('address')
    city=request.POST.get('city')
    city1=City.objects.get(id=city)
    state=request.POST.get('state')
    state1=State.objects.get(id=state)
    country=request.POST.get('country')
    country1=Country.objects.get(id=country)
    zipcode=request.POST.get('zipcode')
    highest=request.POST.get('highest')
    year=request.POST.get('yop')
    company=request.POST.get('company')
    disg=request.POST.get('desig')
    dafrom=request.POST.get('dafrom')
    dato=request.POST.get('dato')
    facebook=request.POST.get('face')
    google=request.POST.get('google')
    twiteer=request.POST.get('twitter')
    linkedin=request.POST.get('linkedin')
    Pinterest=request.POST.get('pinterest')
    instagram=request.POST.get('instagram')
    indu=request.POST.get("indus")
    indust=Industries.objects.get(id=indu)
    if lucky1 == '':
         edittt=Resume(user_id=user_id,userr_id=userr_id, frist=frist,second=second,email=email,phone=phone,designation=designation,category=cateee,experience=expern,industt=indust,jobtypeeee=jobbb,
             expectpa=expectpa,skill=skill,photo=photo,resumess=resumess,birth=birth,address=address,city=city1,state=state1,country=country1,zipcode=zipcode,
             highest=highest,year=year,company=company,disg=disg,dafrom=dafrom,dato=dato,facebook=facebook,google=google,
             twiteer=twiteer,linkedin=linkedin,Pinterest=Pinterest,instagram=instagram)
         edittt.save()
         return render(request,'create_resume.html')
    else:
        resume=Resume.objects.filter(id=lucky1).update(user_id=user_id,userr_id=userr_id,frist=frist,second=second,email=email,phone=phone,designation=designation,category=cateee,industt=indust,experience=expern,jobtypeeee=jobbb,
             expectpa=expectpa,skill=skill,photo=photo,resumess=resumess,birth=birth,address=address,city=city1,state=state1,country=country1,zipcode=zipcode,
             highest=highest,year=year,company=company,disg=disg,dafrom=dafrom,dato=dato,facebook=facebook,google=google,
             twiteer=twiteer,linkedin=linkedin,Pinterest=Pinterest,instagram=instagram)
        return render(request,'create_resume.html',{'edittt':resume})

def submit1(request):
    lucky=request.POST.get('fd')
    usrejob=request.POST.get('userrr_id')
    print(id)
    jobtitle=request.POST.get('jobtitle')
    cname=request.POST.get('companyname')
    catae=request.POST.get('category')
    catata=Category.objects.get(id=catae)
    position=request.POST.get('position')
    exper=request.POST.get('experience')
    exper1=Experience.objects.get(id=exper)
    vacacy=request.POST.get('vacancy')
    package=request.POST.get('package')
    logo=request.FILES.get('logo')
    jobtype=request.POST.get('jobtype')
    jobbb=Jobtype.objects.get(id=jobtype)
    minqul=request.POST.get('qulification')
    skills=request.POST.get('skills')
    email=request.POST.get('email')
    phone=request.POST.get('phoneno')
    website=request.POST.get('website')
    adrres=request.POST.get('address')
    city=request.POST.get('city')
    city2=City.objects.get(id=city)
    state=request.POST.get('state')
    state2=State.objects.get(id=state)
    country=request.POST.get('country')
    country2=Country.objects.get(id=country)
    zip=request.POST.get('zip')
    facebook=request.POST.get('facebook')
    google=request.POST.get('google')
    twiteer=request.POST.get('twitter')
    linkedin=request.POST.get('linkedin')
    pinterest=request.POST.get('pinterest')
    instagram=request.POST.get('instagram')
    if lucky == '':
       edit2=Job(usrejob=usrejob,jobtitle=jobtitle,cname=cname,cata=catata,position=position,exper=exper1,vacacy=vacacy,package=package,logo=logo,jobtypee=jobbb,
               minqul=minqul,skills=skills,email=email,phone=phone,website=website,adrres=adrres,city=city2,state=state2,country=country2,zip=zip,
               facebook=facebook,google=google,twiteer=twiteer,linkedin=linkedin,Pinterest=pinterest,instagram=instagram)
       edit2.save()
       return render(request,'create_job.html')
    else:
        portal=Job.objects.filter(id=lucky).update(usrejob=usrejob,jobtitle=jobtitle,cname=cname,cata=catata,position=position,exper=exper1,vacacy=vacacy,package=package,logo=logo,jobtypee=jobbb,
               minqul=minqul,skills=skills,email=email,phone=phone,website=website,adrres=adrres,city=city2,state=state2,country=country2,zip=zip,
               facebook=facebook,google=google,twiteer=twiteer,linkedin=linkedin,Pinterest=pinterest,instagram=instagram)
        return render(request,'create_job.html',{'edit2':portal})
def edit(request,id):
    editt=Resume.objects.get(id=id)
    expere = Experience.objects.all()
    citysss = City.objects.all()
    statesss = State.objects.all()
    countrysss = Country.objects.all()
    return render(request,'create_resume.html',{'edittt':editt, 'key':expere,'key1':citysss,'key2':statesss,'key3':countrysss})
def edit5(request,id):
    edit1=Job.objects.get(id=id)
    expere = Experience.objects.all()
    citysss = City.objects.all()
    statesss = State.objects.all()
    countrysss = Country.objects.all()
    return render(request,'create_job.html',{'edit2':edit1,'key':expere,'key1':citysss,'key2':statesss,'key3':countrysss})
def delete(request,id):
    lava=Resume.objects.get(id=id)
    lava.delete()
    return redirect(forjobseker)
def register(request):
     if request.method == 'POST':
         fristname=request.POST.get("firstname")
         secondname=request.POST.get("lastname")
         email=request.POST.get("email")
         password=request.POST.get("password1")
         password1=request.POST.get("password2")
         if password==password1:
             if User.objects.filter(email=email).exists():
                 messages.error(request, 'email already exists')
                 return redirect(foremployer)
             else:
                 user=User.objects.create_user(username=email,first_name=fristname,last_name=secondname,email=email,password=password)
                 mylog = authenticate(username=email,password=password)
                 auth.login(request, user,backend='django.contrib.auth.backends.ModelBackend')
                 messages.success(request, 'from successfully completed')
                 return redirect(foremployer)
         else:
             messages.error(request, 'passwords not matching')
             return redirect(foremployer)
     else:
         return render(request, 'for_employer.html')
def login(request):
   if request.method == 'POST':
       uname=request.POST.get('user')
       raw_password=request.POST.get('password')
       user_check=authenticate(username=uname,password=raw_password)
       if user_check is not None:
           auth.login(request,user_check)
           messages.success(request, 'successfully login')
           return redirect(foremployer)
       else:
           messages.error(request, "Username or password error")
           return redirect(foremployer)
   else:
      return redirect(login)
def logout(request):
   auth_logout(request)
   return redirect(foremployer)
def bookkk(request):
     mark = Bookmark.objects.filter(user=request.user.id)
     browse = Resume.objects.filter(id__in=mark)
     return render(request,'browse_employer.html', {'brow': browse})

def book(request):
    userid=request.POST.get('user')
    resumeid=request.POST.get('resume')
    avv=Bookmark(user=userid,res=resumeid)
    avv.save()
    return redirect(employee)

def shortt(request):
    shor = Shortlist.objects.filter(listuser=request.user.id)
    browse = Resume.objects.filter(id__in=shor)
    return render(request, 'browse_employer.html', {'brow': browse})

def shortlist(request):
    user1=request.POST.get('userlist')
    resume1=request.POST.get('resumelist')
    short=Shortlist(listuser=user1,listres=resume1)
    short.save()
    return redirect(employee)

def interjob(request):
    interr = Interested.objects.filter(jobuser=request.user.id)
    browsejob = Job.objects.filter(id__in=interr)
    return render(request, 'browse_jobseeker.html', {'browjob': browsejob})


def interest(request):
    user=request.POST.get('user5')
    jobb=request.POST.get('job')
    interjob=Interested(jobuser=user,jobs=jobb)
    interjob.save()
    return redirect(jobseeker)