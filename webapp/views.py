from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Member, Contributions, Deceased
from .forms import MemberRegForm, DeceasedForm, ContribForm
from django.contrib.auth.decorators import login_required


def home(request):
    
    context = {
        'members' :  Member.objects.all(), 
        # 'memberCount'    : Member.objects.count()          
     }
    return render(request, 'webapp/home.html', context)

def about(request):
    return  render(request, 'webapp/about.html')    


def contributions(request):
    context = {
           'payments': Contributions.objects.all(),
           'paidMembers': Contributions.objects.count()
       }
    return render(request, 'webapp/contributions.html', context) 


@login_required
def registration(request):
    if request.method == 'POST':
        global member
       
        form = MemberRegForm(request.POST)
        if form.is_valid():             
                  
            form.save()
            member = form.cleaned_data.get('member')
            messages.success(request, f'NEW MEMBER  REGISTERED SUCCESSIFULY. YOU CAN NOW ACCEPT THEIR CONTRIBUTION ')
            return redirect('payments')
    else:
        form = MemberRegForm() 
        
    return render(request, 'webapp/registration.html', {'form': form})

@login_required
def deceased(request):
    if request.method == 'POST':
        global form
        form = DeceasedForm(request.POST)
        if form .is_valid():
            form.save()
            
            return redirect('home')
    else:        
        form = DeceasedForm()

    return render(request, 'webapp/deceased.html', {'form': form})

    
@login_required
def payments(request):
    if request.method == 'POST':
        
        form = ContribForm(request.POST)
        if form.is_valid():
            form.save()
                    
            return redirect('contributions')
    else:        
        form = ContribForm()
    return render(request, 'webapp/payments.html', {'form':form})



