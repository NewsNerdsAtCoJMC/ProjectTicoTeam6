from django.forms import ModelForm
from volunteers.models import VolunteerHours

class VolunteerForm(ModelForm):
    class Meta:
        model = VolunteerHours
        fields = ['user', 'date', 'hours']
