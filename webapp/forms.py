from django.forms import ModelForm
from webapp.models import Member, Deceased, Contributions


class MemberRegForm(ModelForm):

    class Meta:
        model     = Member
        fields    = ['First_Name', 'Last_Name', 'Cell_Number', 
                    'Surbub', 'admin'
                    ]

class DeceasedForm(ModelForm):
    
    class Meta:
        model = Deceased
        fields = [ 'Name' ]


class ContribForm(ModelForm):
    
    class Meta:
        model = Contributions
        fields = ['Name', 'admin']

