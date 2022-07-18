import mimetypes
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import render,redirect
from requests import Response


from.import views
import os
from wsgiref.util import FileWrapper
from .models import New_register,students,result,assignment







def home(request):
    return render(request,"fpro.html")

def home2(request):
    return render(request,"Home.html")

def vc(request):
   # if email=="sabiha":
        return render(request,"upload.html")
    #else:
       # return render(request,"Home.html")



def user(request):
    return render(request,"Home2.html")



def table2(request):
    return render(request,"table2.html")


def update(request):
    stname=request.POST['name']
    stbranch=request.POST['type']
    stdct=request.FILES['dct']
    fs=FileSystemStorage()
    filename=fs.save(stdct.name,stdct)
    try:
       if stbranch=='Assignment':
         obj=assignment(Name=stname,Branch=stbranch,Document=filename)
         obj.save()
         return render(request,'table2.html',{'msg':'Record saved successfully'})
       elif stbranch=='Result':
         obj=result(Name=stname,Branch=stbranch,Document=filename)
         obj.save()
         return render(request,'table.html',{'msg':'Record saved successfully'})
       elif stbranch=='Notice':
         obj=result(Name=stname,Branch=stbranch,Document=filename)
         obj.save()
         return render(request,'display.html',{'msg':'Record saved successfully'})
       return render(request,'upload.html',{'msg':'something went wrong'})
    except:
       error_msg="error occured in input"
       return render(request,{'message':error_msg},'upload.html')



def new_user(request):
    email=request.POST['email']
    name=request.POST['name']
    password=request.POST['password']
    obj=New_register(email=email,name=name,password=password)
    obj.save()
    sendmail(request)
    return render(request,"Home.html")



def display_data(request):
    obj=New_register.objects.all()
    return render(request,'data.html',{'mydata':obj})


def delete_dt(request):
    id1=request.GET['rida']
    obj=New_register.objects.get(id=id1)
    obj.delete()
    obj=New_register.objects.all()
    return render(request,"data.html")

def Login_here(request):
    if request.method=="GET":
        return render(request,"Home.html")
    else:
        email=request.POST['email']
        password=request.POST['password']
        obj=New_register.objects.filter(email=email,password=password)
        mydata_length=len(obj)
        if mydata_length>0:
            request.session["email"]=email
            return render(request,"Home.html")
        else:
            return render(request,"Home.html")


def welcome(request):
    if request.session.has_key("myemailid"):
        myem=request.session['myemailid']
        obj=New_register.objects.filter(email=myem)
        for k in obj:
            nms=k.name
            eml=k.email
            return render(request, "Home2.html", {"username":nms, "emailid": eml})
        else:
            return render(request,"Login.html")

def downloadpage(request):
    obj=students.objects.all()
    return render(request,'display.html',{'mydata':obj})

def dwn_file(request):
    file_id=request.GET["shifali"]
    obj=students.objects.get(id=file_id)
    myfilename=obj.Document
    file_path= settings.MEDIA_ROOT + '/' + myfilename
    file_wrapper=FileWrapper(open(file_path,'rb'))
    file_mimetype= mimetypes.guess_type(file_path)
    response=HttpResponse(file_wrapper,content_type=file_mimetype)
    response['X-sendfile']=file_path
    response['content-Length']=os.stat(file_path).st_size
    response['content-Disposition']='attachment; filename=%s' %str(myfilename)
    return response

def down2_file(request):
    file_id=request.GET['aditi']
    obj=assignment.objects.get(id=file_id)
    myfilename=obj.Document
    file_path=settings.MEDIA_ROOT+'/'+myfilename
    file_wrapper=FileWrapper(open(file_path,'rb'))
    file_mimetype=mimetypes.guess_type(file_path)
    response=HttpResponse(file_wrapper,content_type=file_mimetype)
    response['X-sendfile']=file_path
    response['content-length']=os.stat(file_path).st_size
    response['content-Disposition']='attachment; filename=%s'%str(myfilename)
    return response


def down3_file(request):
    file_id=request.GET['aditi2']
    obj=result.objects.get(id=file_id)
    myfilename=obj.Document
    file_path=settings.MEDIA_ROOT+'/'+myfilename
    file_wrapper=FileWrapper(open(file_path,'rb'))
    file_mimetype=mimetypes.guess_type(file_path)
    response=HttpResponse(file_wrapper,content_type=file_mimetype)
    response['X-sendfile']=file_path
    response['content-length']=os.stat(file_path).st_size
    response['content-Disposition']='attachment; filename=%s'%str(myfilename)
    return response



def sendmail(request):
    name=request.POST['email']
    name2=request.POST['name']
    message="Hi "+name2+" thank you for registration!"
    e_from=settings.EMAIL_HOST_USER
    subject="confirmation email"
    send_mail(
        subject,
        message,
        e_from,
        [name],
        fail_silently=False
    )
    return render(request,'Home.html')



#def branch(request):

    #if email in New_register:
        #print('Welcome',)
    #return render(request,'table.html')

def dis_record(request):
    obj=assignment.objects.all()
    return render(request,'table2.html',{"mydata":obj})


def table(request):
    obj=result.objects.all()
    return render(request,'table.html',{"mydata":obj})


