from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import redirect
from chairmanapp.models import * 
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
# def home(request):
#     if "email" in request.session:
#         uid=User.objects.get(email=request.session['email'])
#         if uid.role=="societymember":
#             sid=Societymember.objects.get(user_id=uid)
        
#             context={
#                 'uid' : uid,
                
#                 'sid' : sid,
                
#                 }

            
#             return render(request,"societymemberapp/index.html",context)
#     else:
#          return redirect("login")


def society_profile(request):
    if "email" in request.session:
        uid=User.objects.get(email= request.session['email'])
        sid=Societymember.objects.get(user_id=uid)
        if request.POST:
            firstname= request.POST['firstname']
            lastname=request.POST['lastname']
            sid.firstname=firstname
            sid.lastname=lastname
            sid.save()
            context = {
                        'uid' : uid,
                        'sid' : sid,
                    }
            return render(request,"societymemberapp/profile.html",context)
        else:
            context = {
                        'uid' : uid,
                        'sid' : sid,
                    }
            return render(request,"societymemberapp/profile.html",context)
        
    else:
         return redirect("login")

def society_change_password(request):
    if "email" in request.session:
        uid=User.objects.get(email= request.session['email'])
        sid=Societymember.objects.get(user_id=uid)

        if request.POST:
            currentpassword= request.POST['currentpassword']
            newpassword=request.POST['newpassword']
            
            if uid.password == currentpassword:
               uid.password=newpassword
               uid.save()
               return redirect("logout")

            else:
                pass
            context = {
                        'uid' : uid,
                        'sid' : sid,
                    }
            return render(request,"societymemberapp/profile.html",context)
        else:
            context = {
                    'uid' : uid,
                    'sid' : sid,
                }
            return render(request,"societymemberapp/profile.html",context)
    else:
         return redirect("login")

def society_view_notice(request):
    if "email" in request.session:
        uid=User.objects.get(email= request.session['email'])
        sid=Societymember.objects.get(user_id=uid)
        nall=Notice.objects.all()
        context = {
                            'uid' : uid,
                            'sid' :sid,
                            'nall' : nall
                        }

        return render(request,"societymemberapp/notice-list.html",context)


def society_view_details(request,pk):
    if "email" in request.session:
        print("======>pk:",pk)
        uid=User.objects.get(email= request.session['email'])
        sid=Societymember.objects.get(user_id=uid)
        notice_id=Notice.objects.get(id=pk)
        

        nall=NoticeViewDetails.objects.filter(user_id=uid,notice_id=notice_id)
        if len(nall)==0:
            nid=NoticeViewDetails.objects.create(user_id=uid,notice_id=notice_id)
    


        notice=Notice.objects.filter(id=pk)
        context = {
                            'uid' : uid,
                            'sid' :sid,
                            'notice' : notice
                        }

        return render(request,"societymemberapp/notice-details.html",context)
    
def society_view_event(request):
      if "email" in request.session:
        uid=User.objects.get(email= request.session['email'])
        sid=Societymember.objects.get(user_id=uid)
        eall=Event.objects.all()
        context = {
                            'uid' : uid,
                            'sid' :sid,
                            'eall' : eall
                        }

        return render(request,"societymemberapp/event-list.html",context)


def society_view_event_details(request,pk):
    if "email" in request.session:
        print("======>pk:",pk)
        uid=User.objects.get(email= request.session['email'])
        sid=Societymember.objects.get(user_id=uid)
        event_id=Event.objects.get(id=pk)
        

        eall=EventViewDetails.objects.filter(user_id=uid,event_id=event_id)
        if len(eall)==0:
            eid=EventViewDetails.objects.create(user_id=uid,event_id=event_id)
    


        event=Event.objects.filter(id=pk)
        context = {
                            'uid' : uid,
                            'sid' :sid,
                            'event' : event
                        }

        return render(request,"societymemberapp/event-details.html",context)
    
def add_complaint(request):
    if "email" in request.session:
        uid=User.objects.get(email= request.session['email'])
        sid=Societymember.objects.get(user_id=uid)

        if request.POST:
            mid=Complaint.objects.create(
                user_id=uid,
                title = request.POST['title'],
                description=request.POST['description'],
                
            )
            try:
                if request.FILES['picture']:
                    mid.pic=request.FILES['picture']
                
            except MultiValueDictKeyError:
                pass
            mid.save()
            mall=Complaint.objects.all()
            context = {
                            'uid' : uid,
                            'sid' :sid,
                            'mall' : mall
                        }
            return render(request,"societymemberapp/complaint-list.html",context)
            
        else:
            context = {
                            'uid' : uid,
                            'sid' :sid,
                        }

            return render(request,"societymemberapp/add-complaint.html",context)
    else:
         return redirect('login')

def society_view_complaint(request):
    if "email" in request.session:
        uid=User.objects.get(email= request.session['email'])
        sid=Societymember.objects.get(user_id=uid)
        mall=Complaint.objects.all()
        
        context = {
                            'uid' : uid,
                            'sid' :sid,
                            'mall' : mall
                        }

        return render(request,"societymemberapp/complaint-list.html",context)


def society_complaint_details(request,pk):
    if "email" in request.session:
        print("======>pk:",pk)
        uid=User.objects.get(email= request.session['email'])
        sid=Societymember.objects.get(user_id=uid)
        comp=Complaint.objects.filter(id=pk)
        context = {
                            'uid' : uid,
                            'sid' :sid,
                            'comp' : comp
                        }

        return render(request,"societymemberapp/complaint-details.html",context)
    
def contact_list(request):   
     if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        sid = Societymember.objects.get(user_id = uid)

        sall = Societymember.objects.all()
        context = {
                    'uid' : uid,
                   'sid' :sid,
                    'sall' : sall,
                }
        return render(request,"societymemberapp/contact-list.html",context)
     else:
         return redirect("login")
