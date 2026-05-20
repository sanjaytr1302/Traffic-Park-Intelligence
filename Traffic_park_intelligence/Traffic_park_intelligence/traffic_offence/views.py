from django.shortcuts import render, redirect
from .models import UserProfile,Login, RTO, FoundVehicle, Offence, Traffic, TigerVehicle
from django.contrib import messages
from django.db.models import Q


# Create your views here.
def homepage(request):
    if request.method=="POST":
        usr_name=request.POST['username']
        userpassword=request.POST['password']
        role=request.POST['role'] 
        if role=="rto":
            check_user=Login.objects.filter(Q(username=usr_name) & Q(password=userpassword)).first()
            if check_user.password==userpassword:
                request.session['user']=usr_name
                request.session['userid']=check_user.id
                messages.success(request,"Login Success Welcome," , usr_name)
                return redirect ('rto_home')
            else:
                messages.info(request,"Wrong Password Entered")
                return redirect('homepage')
        elif role=="admin":
            check_user=Login.objects.filter(Q(username=usr_name) & Q(password=userpassword)).first()
            if check_user.password==userpassword:
                request.session['user']=usr_name
                request.session['userid']=check_user.id
                messages.success(request,"Login Success Welcome," , usr_name)
                return redirect ('admin_home')
            else:
                messages.info(request,"Wrong Password Entered")
                return redirect('homepage')
    return render(request,'index.html')


def userregister(request):
    if request.method=="POST":
            user_reg=UserProfile()
            user_reg.first_name=request.POST['fname']
            user_reg.last_name=request.POST['lname']
            user_reg.dob=request.POST['bdate']
            user_reg.address=request.POST['address']
            user_reg.city=request.POST['city']
            user_reg.state=request.POST['state']
            user_reg.pincode=request.POST['pincode']
            user_reg.contact_no=request.POST['contactno']
            user_reg.emailid=request.POST['emailid']
            user_reg.profile_photo=request.FILES['image']
            user_reg.username=request.POST['loginname']
           
            login=Login()
            login.username=request.POST['loginname']
            login.password=request.POST['password']
            login.type='User'
            user_reg.save()

            login.save()
            messages.success(request, "User Registration Success")
    return render(request,'userregister.html')

def rto_home(request):
    if request.method=="POST":
            rto_reg=RTO()
            rto_reg.name=request.POST['name']
            rto_reg.dob=request.POST['dob']
            rto_reg.aadhar_card_no=request.POST['Aadhar_card_no']
            rto_reg.r_address=request.POST['address']
            rto_reg.r_city=request.POST['city']
            rto_reg.r_state=request.POST['state']
            rto_reg.vehicle_num=request.POST['vhnum']
            rto_reg.engine_num=request.POST['engnum']
            rto_reg.vehicle_type=request.POST['vno']
            rto_reg.email=request.POST['email']
            rto_reg.save()
            messages.success(request, "Vehicle Registered Successfully")
    return render(request,'rto_home.html')

def rto_view_reg_veh(request):
    view_rto_reg=RTO.objects.all()
    return render(request,'rto_view_reg_veh.html',{'view_rto_reg':view_rto_reg})



def admin_home(request):
    if request.method=="POST":
            f_v=FoundVehicle()
            f_v.vehicle_name=request.POST['vname']
            f_v.vehicle_num=request.POST['vnum']
            f_v.engine_num=request.POST['enum']
            f_v.vehicle_foundcity=request.POST['vcity']
            f_v.vehicle_foundstate=request.POST['vstate']
            f_v.vehicle_pic=request.FILES['photo']
            f_v.save()
            messages.success(request, "Vehicle Uploaded under Found Vehicle List Successfully")
    v_foundVehicle=FoundVehicle.objects.all()
    return render(request,'admin_home.html',{'v_foundVehicle':v_foundVehicle})



def admin_addfine(request):
    if request.method=="POST":
        t_offence=Offence()
        t_offence.category=request.POST['vtype']
        t_offence.sub_category=request.POST['Traffic_violation']
        t_offence.fine=request.POST['fine']
        t_offence.save()
        messages.success(request, "Traffic Offence Fine Added Successfully")
    v_Offence=Offence.objects.all()
    return render(request,'admin_addfine.html',{'v_Offence':v_Offence})

def admin_createtraffic_pol(request):
    if request.method == 'POST':
        # Check if form 1 is submitted
        if 'create_trafi_pol' in request.POST:
             cr_trf_pol=Traffic()
             cr_trf_pol.name=request.POST['name']
             cr_trf_pol.username=request.POST['user']
             cr_trf_pol.password=request.POST['pass']
             cr_trf_pol.type='Traffic_Police'
             login=Login()
             login.username=request.POST['user']
             login.password=request.POST['pass']
             login.type='Traffic_Police'
             login.save()
             cr_trf_pol.save()
             messages.success(request, "Traffic Police Added Successfully")
        elif 'create_tiger_v' in request.POST:
             cr_tigr=TigerVehicle()
             cr_tigr.tigerPolName=request.POST['tigerPolName']
             cr_tigr.tigerStatName=request.POST['tigerStatName']
             cr_tigr.stat_address=request.POST['stat_address']
             cr_tigr.tigeruser=request.POST['tigeruser']
             cr_tigr.tigerpass=request.POST['tigerpass']
             cr_tigr.contact_no=request.POST['contact_no']
             login=Login()
             login.username=request.POST['tigeruser']
             login.password=request.POST['tigerpass']
             login.type='Tiger_Vehicle'
             login.save()
             cr_tigr.save()
             
             messages.success(request, "Tiger Vehicle Added Successfully")


             
    v_reg_pol=Traffic.objects.all()
    v_tiger=TigerVehicle.objects.all()
    
    return render(request,'admin_createtraffic_pol.html',{'v_reg_pol':v_reg_pol,'v_tiger':v_tiger})



def delete_police(request,id):
    tr_id=id
    t_offence=Traffic.objects.get(id=tr_id)
    t_user=t_offence.username
    t_log=Login.objects.get(username=t_user)
    t_offence.delete()
    t_log.delete()
    
    messages.success(request, "Traffic Police Data Deleted Successfully")
    
    return redirect(admin_createtraffic_pol)

def delete_tigr(request,id):
    tr_id=id
    t_vehi=TigerVehicle.objects.get(id=tr_id)
    t_user=t_vehi.username
    t_log=Login.objects.get(username=t_user)
    t_vehi.delete()
    t_log.delete()
    messages.success(request, "Tiger Vehicle Data Deleted Successfully")
    
    return redirect(admin_createtraffic_pol)






def logout(request):
    try:
        del request.session['userid']
        del request.session['user']
    except:
        return redirect('homepage')
    messages.info(request,"Logout Success")
    return redirect('homepage')
