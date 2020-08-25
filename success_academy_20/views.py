from django.shortcuts import render
from django.views.generic import CreateView
from .models import Participant

# Create your views here.

def homepage(request):
    template_name = 'success_academy_20/index.html'
    context_object_name = {}
    return render(request, template_name, context_object_name)


class RegisterParticipant(CreateView):
    model = Participant
    template_name = 'success_academy_20/register.html'
    fields = [
                    'participant_firstname',
                    'participant_lastname',
                    'participant_title',
                    'participant_gender',
                    'participant_phone_number',
                    'participant_email',
                    'participant_home_address_1',
                    'participant_home_address_2',
                    'participant_school_name',
                    'participant_class',
                    'participant_church_denomination',
                    'participant_group_of_districts',
                    'participant_district',
                    'participant_cluster_name',
                    'participant_membership_status',
                    'participant_prayer_request']
    
