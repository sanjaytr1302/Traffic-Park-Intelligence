from django.db import models

# Create your models here.
 
class FineCollect(models.Model):
    id = models.AutoField(primary_key=True)
    vRno = models.CharField(max_length=50, unique=True, verbose_name="Vehicle Registration Number")
    collected_fine = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Collected Fine Amount")
    trafficviolation = models.TextField(verbose_name="Traffic Violation Details")
    police_id = models.IntegerField(verbose_name="Police ID")
    police_name = models.CharField(max_length=100, verbose_name="Police Officer Name")
    collect_date = models.DateTimeField(auto_now_add=True, verbose_name="Collection Date")

    class Meta:
        db_table = "fine_collect"
        verbose_name = "Fine Collection"
        verbose_name_plural = "Fine Collections"

    def __str__(self):
        return f"Fine collected from {self.vRno} by {self.police_name} on {self.collect_date.strftime('%Y-%m-%d')}"

class FoundVehicle(models.Model):
    id = models.AutoField(primary_key=True)
    vehicle_name = models.CharField(max_length=255)
    vehicle_num = models.CharField(max_length=50, unique=True)
    engine_num = models.CharField(max_length=100, unique=True)
    vehicle_foundcity = models.CharField(max_length=100)
    vehicle_foundstate = models.CharField(max_length=100)
    vehicle_pic = models.ImageField(upload_to='vehicle_pics/')

    def __str__(self):
        return f"{self.vehicle_name} ({self.vehicle_num})"
    


class NoParking(models.Model):
    id = models.AutoField(primary_key=True)
    vname = models.CharField(max_length=255)
    vnum = models.CharField(max_length=50, unique=True)
    vaddr = models.TextField()
    vnear_by = models.CharField(max_length=255)
    v_lift_typ = models.CharField(max_length=100)
    Tiger_id = models.IntegerField()
    collect_date = models.DateTimeField()

    class Meta:
        db_table = 'no_parking'

    def __str__(self):
        return f"{self.vname} ({self.vnum})"



class Login(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=255)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'login'




class Offence(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ]
    
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255)
    sub_category = models.CharField(max_length=255)
    fine = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    
    def __str__(self):
        return f"{self.category} - {self.sub_category}"



class RegisterTrafficOffence(models.Model):
    id = models.AutoField(primary_key=True)
    vehicle_regno = models.CharField(max_length=20, unique=True)
    violation_date = models.DateField()
    violation_place = models.CharField(max_length=255)
    violation_type = models.CharField(max_length=100)
    violation_desc = models.TextField()
    violation_pic = models.ImageField(upload_to='violation_pics/', null=True, blank=True)
    vtype = models.CharField(max_length=50)
    vowner_name = models.CharField(max_length=100)
    vaadhar = models.CharField(max_length=12, unique=True)
    vr_address = models.TextField()
    vr_city = models.CharField(max_length=100)
    vr_state = models.CharField(max_length=100)
    engine_num = models.CharField(max_length=50, unique=True)
    comp_vehicle = models.BooleanField(default=False)
    com_type = models.CharField(max_length=100, null=True, blank=True)
    fine = models.DecimalField(max_digits=10, decimal_places=2)
    fine_status = models.CharField(max_length=50, choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], default='Unpaid')
    offence_cat = models.CharField(max_length=100)
    offence_subcat = models.CharField(max_length=100)
    fine_total = models.DecimalField(max_digits=10, decimal_places=2)
    compid = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return f"{self.vehicle_regno} - {self.violation_type} ({self.violation_date})"
    



class RTO(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    dob = models.DateField()
    aadhar_card_no = models.CharField(max_length=12, unique=True)
    r_address = models.TextField()
    r_city = models.CharField(max_length=100)
    r_state = models.CharField(max_length=100)
    vehicle_num = models.CharField(max_length=20, unique=True)
    engine_num = models.CharField(max_length=50, unique=True)
    vehicle_type = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return f"{self.name} - {self.vehicle_num}"
    


class TigerVehicle(models.Model):
    id = models.AutoField(primary_key=True)
    tigerPolName = models.CharField(max_length=255)
    tigerStatName = models.CharField(max_length=255)
    stat_address = models.TextField()
    tigeruser = models.CharField(max_length=150, unique=True)
    tigerpass = models.CharField(max_length=150)
    contact_no = models.CharField(max_length=15)

    class Meta:
        db_table = 'tiger_vehicle'

    def __str__(self):
        return f"{self.tigerPolName} - {self.tigerStatName}"
    

class Traffic(models.Model):
    TYPE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
        ('guest', 'Guest'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateField()
    address = models.TextField()
    pincode = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=15, unique=True)
    emailid = models.EmailField(unique=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    username = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ViolatorComplaint(models.Model):
    id = models.AutoField(primary_key=True)
    vehicle_regno = models.CharField(max_length=20, unique=True)
    violation_date = models.DateField()
    violation_place = models.CharField(max_length=255)
    violation_type = models.CharField(max_length=100)
    violation_time = models.TimeField()
    description = models.TextField(blank=True, null=True)
    pic_traffic_violator = models.ImageField(upload_to='violator_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.vehicle_regno} - {self.violation_type} on {self.violation_date}"
