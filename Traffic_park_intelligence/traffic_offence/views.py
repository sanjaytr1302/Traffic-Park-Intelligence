from django.shortcuts import render, redirect,get_object_or_404
from .models import UserProfile,Login, RTO, FoundVehicle, Offence, Traffic, TigerVehicle, RegisterTrafficOffence,ViolatorComplaint, FineCollect, NoParking
from django.contrib import messages
from django.db.models import Q


# Create your views here.
def homepage(request):
    if request.method=="POST":
        usr_name=request.POST['username']
        userpassword=request.POST['password']
        role=request.POST['role']
        try:
            if role=="rto":
                check_user=Login.objects.filter(Q(username=usr_name) & Q(password=userpassword)).first()
                if check_user:
                    request.session['user']=usr_name
                    request.session['userid']=check_user.id
                    messages.success(request,"Login Success Welcome," , usr_name)
                    return redirect ('rto_home')
                else:
                    messages.error(request,"Username / Password  is incorrect")
                    return redirect('homepage')
            elif role=="admin":
                check_user=Login.objects.filter(Q(username=usr_name) & Q(password=userpassword)).first()
                if check_user:
                    request.session['user']=usr_name
                    request.session['userid']=check_user.id
                    messages.success(request,"Login Success Welcome," , usr_name)
                    return redirect ('admin_home')
                else:
                    messages.error(request,"Username / Password  is incorrect")
                    return redirect('homepage')
            elif role=="User":
                check_user=Login.objects.filter(Q(username=usr_name) & Q(password=userpassword)).first()
                if check_user:
                    request.session['user']=usr_name
                    request.session['userid']=check_user.id
                    messages.success(request,"Login Success Welcome," , usr_name)
                    return redirect ('user_home')
                else:
                    messages.error(request,"Username / Password  is incorrect")
                    return redirect('homepage')
            elif role=="Traffic_Police":
                check_user=Login.objects.filter(Q(username=usr_name) & Q(password=userpassword)).first()
                if check_user:
                    request.session['user']=usr_name
                    request.session['userid']=check_user.id
                    messages.success(request,"Login Success Welcome," , usr_name)
                    return redirect ('traffic_home')
                else:
                    messages.error(request,"Username / Password  is incorrect")
                    return redirect('homepage')
            elif role=="Tiger_Vehicle":
                check_user=Login.objects.filter(Q(username=usr_name) & Q(password=userpassword)).first()
                if check_user:
                    request.session['user']=usr_name
                    request.session['userid']=check_user.id
                    messages.success(request,"Login Success Welcome," , usr_name)
                    return redirect ('tiger_vehicle')
                else:
                    messages.error(request,"Wrong Password Entered")
                    return redirect('homepage')
            
        except Login.DoesNotExist:
            messages.error(request, 'User not found')
        
    return render(request,'index.html')

from django.db import IntegrityError
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

            if UserProfile.objects.filter(contact_no=request.POST['contactno']).exists():
                messages.error(request, "This contact number is already registered.")
                return redirect('userregister') 
            try:
                user_reg.save()
                login.save()
                messages.success(request, "User Registration Success")
                return redirect('userregister') 
            except IntegrityError as e:
                messages.error(request, "An error occurred while registering. Please try again.")
                return redirect('userregister')

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


    fine_collection=FineCollect.objects.all() 
    v_reg_pol=Traffic.objects.all()
    v_tiger=TigerVehicle.objects.all()
    
    return render(request,'admin_createtraffic_pol.html',{'v_reg_pol':v_reg_pol,'v_tiger':v_tiger,'fine_collection':fine_collection})

from datetime import datetime
from django.utils.timezone import make_aware
from django.db.models.functions import TruncDate
def search_fine_collection(request):
    fine_collection = FineCollect.objects.all()

    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')

    if from_date and to_date:
        from_date = make_aware(datetime.strptime(from_date, "%Y-%m-%d"))
        to_date = make_aware(datetime.strptime(to_date, "%Y-%m-%d"))

        fine_collection = fine_collection.filter(
            collect_date__gte=from_date, 
            collect_date__lte=to_date
        )
        print(fine_collection)
    return render(request, 'print_total_fine_collection.html', {'fine_collection': fine_collection})


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


def user_home(request):
    if 'user' in request.session:
        userid=request.session['userid']
        username=request.session['user']
        if request.method=="POST":
            reg_comp=ViolatorComplaint()
            reg_comp.vehicle_regno=request.POST['vrno']
            reg_comp.violation_date=request.POST['vdate']
            reg_comp.violation_place=request.POST['vplace']
            reg_comp.violation_type=request.POST['vtype']
            reg_comp.violation_time=request.POST['vtime']
            reg_comp.description=request.POST['desc']
            
            reg_comp.pic_traffic_violator=request.FILES['photo']
            reg_comp.save()
            messages.success(request, "Traffic Violator Complaint Raised Successfully")

        user_data=UserProfile.objects.get(username=username)
        
        
        return render(request,'userhome.html',{'user_data':user_data})



    return redirect(user_home)


def userprofile(request):
    if 'user' in request.session:
        userid=request.session['userid']
        username=request.session['user']
        if request.method=="POST":
            id=request.POST['uid']
            user_reg=UserProfile.objects.get(id=id)
            
            user_reg.first_name=request.POST['fname']
            user_reg.last_name=request.POST['lname']
            

            user_reg.address=request.POST['address']
            user_reg.pincode=request.POST['pincode']
            user_reg.city=request.POST['city']
            user_reg.state=request.POST['state']
            user_reg.contact_no=request.POST['contactno']
            user_reg.emailid=request.POST['emailid']
            user_reg.save()
            messages.success(request, "Profile Updated Successfully")
            
        user_data=UserProfile.objects.get(username=username)
        print(user_data)
        return render(request,'userprofile.html',{'user_data':user_data})
    return redirect(user_home)



def view_userposted_complaints(request):
    if 'user' in request.session:
        userid=request.session['userid']
        username=request.session['user']
        
        
        violator_complain=ViolatorComplaint.objects.all()
        print(violator_complain)
        return render(request,'view_userposted_complaints.html',{'violator_complain':violator_complain})
    return redirect(user_home)

from django.http import JsonResponse
def load_subcategories(request):
    """ Fetch subcategories based on selected category """
    category = request.GET.get('category')
    subcategories = Offence.objects.filter(category=category).values('sub_category').distinct()
    
    subcategory_list = list(subcategories)  # Convert to list
    return JsonResponse({"subcategories": subcategory_list})

def load_fine(request):
    """ Fetch fine amount based on selected subcategory """
    sub_category = request.GET.get('sub_category')
    offence = Offence.objects.filter(sub_category=sub_category).first()
    
    fine_amount = offence.fine if offence else 0  # Set default fine to 0 if not found
    return JsonResponse({"fine": fine_amount})



#ML Project Statrs here
import cv2
import easyocr
import numpy as np
import pytesseract

# Load OCR Models
reader = easyocr.Reader(['en'])  
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update if needed

import requests
import numpy as np
from django.conf import settings
import os 
# Function to zoom the image
def zoom_image(img, zoom_factor):
    # Resize the image based on the zoom factor
    height, width = img.shape[:2]
    new_width = int(width * zoom_factor)
    new_height = int(height * zoom_factor)
    zoomed_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
    return zoomed_img

def track_numberplate(request):
    if request.method=="POST":
        #print("Hello")
        #track_image=request.POST['v_img']
        #print(track_image)
        #img = cv2.imread(track_image)
        # Debugging print statements to check paths

        image_path = request.POST['v_img']
        traffic_offence_comp_id = request.POST['traffic_offence_comp_id']

        
        print(f"Image Path: {image_path}")
        
        # Remove the '/media' prefix from the image path
        if image_path.startswith('/media'):
            image_path = image_path[6:]  # Remove '/media' part
        
        # Now combine it with the MEDIA_ROOT to get the full absolute path
        absolute_path = os.path.join(settings.MEDIA_ROOT, image_path.lstrip('/'))
        print(f"Absolute Path: {absolute_path}")
        print('*' * 50)
        print(f"MEDIA_ROOT: {settings.MEDIA_ROOT}")
        print(f"Image Path: {image_path}")
        print(f"Absolute Path: {absolute_path}")
        print('*' * 50)
        

        # Ensure the final path is correct
        if not os.path.exists(absolute_path):
            print("Image file not found at the path.")
            return render(request, 'error_page.html')  # Render an error page or message
        
        # Read the image from the server's absolute path
        img = cv2.imread(absolute_path)

        # Check if the image is loaded correctly
        if img is None:
            print("Error: Image not found!")
            exit()

        # Create a resizable window
        cv2.namedWindow("Select Number Plate", cv2.WINDOW_NORMAL)

        # Let the user manually select the number plate region
        roi = cv2.selectROI("Select Number Plate", img, fromCenter=False, showCrosshair=True)
        cv2.destroyWindow("Select Number Plate")

        # Extract selected region
        x, y, w, h = roi

        if w == 0 or h == 0:
            print("No region selected!")
            exit()

        # Zoom into selected region (scale up)
        zoom_factor = 3  # Increase to 3x for better clarity
        plate_roi = cv2.resize(img[y:y+h, x:x+w], None, fx=zoom_factor, fy=zoom_factor, interpolation=cv2.INTER_CUBIC)

        # Convert to grayscale
        gray_plate = cv2.cvtColor(plate_roi, cv2.COLOR_BGR2GRAY)

        # === Image Preprocessing for Better OCR ===
        gray_plate = cv2.GaussianBlur(gray_plate, (3, 3), 0)  # Reduce noise
        gray_plate = cv2.equalizeHist(gray_plate)  # Improve contrast
        gray_plate = cv2.threshold(gray_plate, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]  # Binarization

        # Morphological operations to refine edges
        kernel = np.ones((2, 2), np.uint8)
        gray_plate = cv2.morphologyEx(gray_plate, cv2.MORPH_CLOSE, kernel)
        gray_plate = cv2.morphologyEx(gray_plate, cv2.MORPH_OPEN, kernel)

        # Sharpen image
        sharpen_kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        gray_plate = cv2.filter2D(gray_plate, -1, sharpen_kernel)

        # Try OCR with EasyOCR
        easyocr_text = reader.readtext(gray_plate)
        plate_easyocr = " ".join([text[1] for text in easyocr_text]) if easyocr_text else "No text detected"

        # Try OCR with Tesseract
        plate_tesseract = pytesseract.image_to_string(gray_plate, config='--psm 8 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

        # Choose the best result
        plate_number = plate_easyocr if len(plate_easyocr) > len(plate_tesseract.strip()) else plate_tesseract.strip()

        # Show detected text
        print("Detected Plate Number:", plate_number)
       
        # Draw rectangle around selected area on original image
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(img, plate_number, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Show the selected & zoomed number plate
        cv2.imshow('Zoomed Plate', plate_roi)
        userinp1=input("is this correct y:yes | n:no")
        if(userinp1 == 'y'):
            cv2.waitKey(0)
            search_owner=RTO.objects.get(vehicle_num=plate_number)
            offences = Offence.objects.values('category').distinct()
            print('*' * 10)
            print(traffic_offence_comp_id)
            search_traffic_offencecomp=ViolatorComplaint.objects.get(id=traffic_offence_comp_id)
            
            
            return render(request, 'viewcompdetail.html', {"search_owner": search_owner,'offences': offences,'search_traffic_offencecomp':search_traffic_offencecomp})
        
        else:
            cv2.waitKey(0)
            userinp=input("Enter the Vehicle number")
            search_owner=RTO.objects.get(vehicle_num=userinp)
            offences = Offence.objects.values('category').distinct()
            search_traffic_offencecomp=ViolatorComplaint.objects.get(id=traffic_offence_comp_id)
            
            
            return render(request, 'viewcompdetail.html', {"search_owner": search_owner,'offences': offences,'search_traffic_offencecomp':search_traffic_offencecomp})
        
        
        

        # Show the original image with detection
        
        cv2.destroyAllWindows()
        #cv2.namedWindow("Detected Plate", cv2.WINDOW_NORMAL)
        return render(request, 'vehicle_check.html', {"plate_number": plate_number})

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return redirect(view_userposted_complaints)


def reject_comp(request,id):
    tr_viola_id=id
    t_vehi=ViolatorComplaint.objects.get(id=tr_viola_id)
    
    t_vehi.delete()
    messages.success(request, "Complaint Rejected Successfully")
    
    return redirect(view_userposted_complaints)



def fetch_police_details(request):
    if request.method=="POST":
            id=request.POST['police_id']
            t_offence=TigerVehicle.objects.get(tigeruser=id)
    
    return render(request,'fetch_police_details.html',{'tp_details':t_offence})
def fetch_station(request):
    if request.method=="POST":
            id=request.POST['police_id']
            t_offence=TigerVehicle.objects.get(tigeruser=id)
    
    return render(request,'fetch_station.html',{'tp_details':t_offence})



def RegisterComp(request, offence_id):
    if 'user' in request.session:
        userid=request.session['userid']
        username=request.session['user']
        if request.method=="POST":
            offence = get_object_or_404(ViolatorComplaint, id=offence_id)

            vownername=request.POST.get("vownername")
            vaadhar1=request.POST.get("vaadhar")
            vRaddress=request.POST.get("vRaddress")
            vRcity=request.POST.get("vRcity")
            vRstate=request.POST.get("vRstate")
            Engine_num=request.POST.get("Engine_num")
            
            
            category = request.POST.get("category")  # Get extra data
            sub_category = request.POST.get("sub_category")
            fine = request.POST.get("fine")
            compid = request.POST.get("compid")
            print(category)
            print(sub_category)
            print(fine)
            

            

            # Copy to ArchivedOffence
            RegisterTrafficOffence.objects.create(
                vehicle_regno=offence.vehicle_regno,
                violation_date=offence.violation_date,
                violation_place=offence.violation_date,
                violation_type=offence.violation_date,
                violation_desc=offence.violation_date,
                violation_pic=offence.pic_traffic_violator,
                vtype=offence.pic_traffic_violator,
                vowner_name = vownername,
                vaadhar=vaadhar1,
                vr_address=vRaddress,
                vr_city=vRcity,
                vr_state=vRstate,
                engine_num=Engine_num,
                
                
                
                comp_vehicle=category,
                com_type=sub_category,
                fine=fine,  # Use fine from the form
                compid=offence.id
                  # Store status as archived_on (if needed)
            )

            offence.delete()  # Delete from Offence table

            messages.success(request, "Traffic Violator Complaint Raised Successfully")

        
        return redirect(view_userposted_complaints)



    return redirect(admin_home)


def traffic_home(request):
    if 'user' in request.session:
        userid=request.session['userid']
        username=request.session['user']
        if request.method=="POST":
            
            v_num=request.POST["Vehicle_num"]
            check_traffic_offence=RegisterTrafficOffence.objects.filter(Q(vehicle_regno=v_num) & Q(fine_status='Unpaid'))
            if(check_traffic_offence):
                try:
                    user_data=Traffic.objects.get(username=username)
                    offences = Offence.objects.values('category').distinct()
                    return render(request,'traffic_home.html',{'user_data':user_data,'check_traffic_offence':check_traffic_offence,'offences':offences,'old_comp':check_traffic_offence,'v_num':v_num})
                except v_num.DoesNotExist:
                    check_traffic_offence = None


            user_data=Traffic.objects.get(username=username)
            offences = Offence.objects.values('category').distinct()
            return render(request,'traffic_home.html',{'user_data':user_data,'check_traffic_offence':'','offences':offences,'old_comp':check_traffic_offence,'v_num':v_num})
        
        user_data=Traffic.objects.get(username=username)
        offences = Offence.objects.values('category').distinct()
        return render(request,'traffic_home.html',{'user_data':user_data,'check_traffic_offence':'','offences':offences})
    
    return redirect(homepage)




def trf_police_collect_fine(request):
    if 'user' in request.session:
        userid=request.session['userid']
        username=request.session['user']
        if request.method=="POST":
            vehicle_Rno=request.POST['Vregno']
            trp_fine=FineCollect(
                vRno=request.POST['Vregno'],
                collected_fine=request.POST['TotalPrice'],
                trafficviolation=request.POST['sub_category'],
                police_id=request.POST['police_id'],
                police_name=request.POST['police_name']
            )
            check_traffic_offence = RegisterTrafficOffence.objects.filter(
                Q(vehicle_regno=vehicle_Rno) & Q(fine_status='Unpaid')
            )

            if check_traffic_offence.exists():  # Check if there is at least one matching record
                check_traffic_offence.update(fine_status='Paid')  # Update fine_status to 'Paid'
                
                print("Payment updated for the first matching offence.")
            else:
                print("No unpaid fines found for this vehicle.")
            trp_fine.save()
            messages.success(request, "Fine Collected")
            return render(request, "receipt.html", {"trp_fine": trp_fine})
        
        return render(traffic_home)
    return redirect(user_home)

from django.core.mail import send_mail
def tiger_vehicle(request):
    if 'user' in request.session:
        userid=request.session['userid']
        username=request.session['user']
        if request.method=="POST":
        
            raise_noparkingcomp=NoParking()
            
            raise_noparkingcomp.vname=request.POST['vname']
            raise_noparkingcomp.vnum=request.POST['vnum']
            raise_noparkingcomp.vaddr=request.POST['vaddr']
            raise_noparkingcomp.vnear_by=request.POST['vnear_by']
            raise_noparkingcomp.v_lift_typ=request.POST['v_lift_typ']
            raise_noparkingcomp.Tiger_id=request.POST['Tiger_id']
            raise_noparkingcomp.save()
            # Send Email Notification
            subject = "No Parking Offence Registered"
            message = f"Dear {raise_noparkingcomp.vname},\n\nYour no parking offence has been registered successfully.\n\nVehicle No: {raise_noparkingcomp.vnum}\nLocation: {raise_noparkingcomp.vaddr}\nNearby: {raise_noparkingcomp.vnear_by}\n\nThank you."
            recipient_email = "recipient@example.com"  # Replace with user email field from form
            sender_email = "your-email@gmail.com"

            try:
                send_mail(subject, message, sender_email, [recipient_email])
                messages.success(request, "No Parking Offence Added Successfully. Email Sent!")
            except Exception as e:
                messages.error(request, f"No Parking Offence Added, but Email Failed! Error: {str(e)}")

            messages.success(request, "No Parking offence Added successfullt")
            
            
        
        user_data=TigerVehicle.objects.get(tigeruser=username)
        return render(request,'tiger_vehicle.html',{'user_data':user_data})
    
    return redirect(homepage)



def find_my_complaints(request):
    if request.method=="POST":    
        v_num=request.POST["Vehicle_num"]
        check_traffic_offence=RegisterTrafficOffence.objects.filter(Q(vehicle_regno=v_num))
        if(check_traffic_offence):
            try:
                return render(request,'find_my_complaints.html',{'check_traffic_offence':check_traffic_offence})
            except check_traffic_offence.DoesNotExist:
                check_traffic_offence = None
                messages.error(request, 'No Complaints Found')
    return render(request,'find_my_complaints.html')


def found_vehicle(request):
    if request.method=="POST":    
        v_num=request.POST["Vehicle_num"]
        v_eng_num=request.POST["eng_num"]
        
        check_found_veh=FoundVehicle.objects.filter(Q(vehicle_num=v_num)  & Q(engine_num=v_eng_num))
        if check_found_veh.exists():  # Check if any records were returned
            return render(request,'found_vehicle.html',{'find_found_veh':check_found_veh})
        else:
            messages.error(request, 'No Details Found') 
    return render(request,'found_vehicle.html')


def no_parking(request):
    if request.method == "POST":
        v_num = request.POST["Vehicle_num"]
        
        # Filter to get all matching records for the vehicle number
        check_np = NoParking.objects.filter(Q(vnum=v_num))
        
        if check_np.exists():  # Check if any records were returned
            return render(request, 'no_parking.html', {'check_nop': check_np})
        else:
            messages.error(request, 'No Details Found')
    
    return render(request, 'no_parking.html')

def logout(request):
    try:
        del request.session['userid']
        del request.session['user']
    except:
        return redirect('homepage')
    messages.info(request,"Logout Success")
    return redirect('homepage')
