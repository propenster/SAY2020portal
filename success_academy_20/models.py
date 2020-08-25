from django.db import models
from django.contrib.auth.models import User

PARTICIPANT_STATUS = (
    ('', 'Select'),
    ('VSR', 'VISITOR'),
    ('MBR', 'MEMBER'),
    ('WKR', 'WORKER'),
    ('LDR', 'LEADER'),
    ('PSR', 'PASTOR')
)

PARTICIPANT_GENDER = (
    ('', 'Select'),
    ('M', 'MALE'),
    ('FM', 'FEMALE')
)

PARTICIPANT_TITLE = (
    ('', 'Choose'),
    ('MR', 'MR'),
    ('MS', 'MISS'),
    ('MRS', 'MRS')
)

class LGA(models.Model):
    LGA_name = models.CharField(max_length=255)
    LGA_state = models.CharField(max_length=150, default='OYO')
    LGA_created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    LGA_created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['LGA_name']
        verbose_name_plural = 'LGAs'

    def __str__(self):
        return f'{self.LGA_name}' 

class DistrictGroup(models.Model):
    district_group_name = models.CharField(max_length=255)
    district_group_lga = models.ForeignKey(LGA, on_delete=models.CASCADE)
    district_group_created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    district_group_created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['district_group_name']
        verbose_name_plural = 'Group of Districts'

    def __str__(self):
        return f'{self.district_group_name}'

class Cluster(models.Model):
    cluster_name = models.CharField(max_length=255)
    cluster_district_group = models.ForeignKey(DistrictGroup, on_delete=models.CASCADE)
    cluster_LGA = models.ForeignKey(LGA, on_delete=models.CASCADE)
    cluster_created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    cluster_created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['cluster_name']

    def __str__(self):
        return f'{self.cluster_name}'

class District(models.Model):
    district_name = models.CharField(max_length=255)
    district_cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)
    district_group = models.ForeignKey(DistrictGroup, on_delete=models.CASCADE)
    district_created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    district_created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['district_name']

    def __str__(self):
        return f'{self.district_name}'


class Participant(models.Model):
    participant_firstname = models.CharField(max_length=150)
    participant_lastname = models.CharField(max_length=150)
    participant_title = models.CharField(max_length=10, choices=PARTICIPANT_TITLE)
    participant_gender = models.CharField(max_length=10, choices=PARTICIPANT_GENDER)
    participant_phone_number = models.CharField(max_length=11)
    participant_email = models.EmailField()
    participant_home_address_1 = models.CharField(max_length=150)
    participant_home_address_2 = models.CharField(max_length=150, null=True)
    participant_school_name = models.CharField(max_length=255, null=True)
    participant_class = models.CharField(max_length=150, null=True)
    participant_church_denomination = models.CharField(max_length=255)
    participant_group_of_districts = models.ForeignKey(DistrictGroup, on_delete=models.CASCADE)
    participant_district = models.ForeignKey(District, on_delete=models.CASCADE)
    participant_cluster_name = models.ForeignKey(Cluster, on_delete=models.CASCADE)
    participant_membership_status = models.CharField(max_length=255, choices=PARTICIPANT_STATUS)
    participant_prayer_request = models.TextField()
    participant_registration_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-participant_registration_date']

    def __str__(self):
        return f'{self.participant_firstname} {self.participant_lastname}' 
