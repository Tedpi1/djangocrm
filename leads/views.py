from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm

def lead_list(request):
    #return HttpResponse("Hello World")
    leads=Lead.objects.all()#fetching leads app from our models
    context={
        "leads":leads
    }
    return render(request, "lead_list.html", context)
def test(request):
    return render(request, "test.html")
def lead_detail(request, pk):
    lead=Lead.objects.get(id=pk)
    context={
        "lead":lead
    }
    return render(request, "lead_detail.html", context)
def lead_create(request):
    #print(request.POST)
    form=LeadModelForm()
    #check if the request method is POST
    if request.method=="POST":
        print('recieving a post request')
        #form is used to capture record from the user
        form=LeadModelForm(request.POST)
        #check the form is valid
        if form.is_valid():
            form.save()#easy to use because we specified the model we are using 'Lead'
            return redirect("/leads")
    context={
        "form":form
    }
    return render(request, "lead_create.html", context)

# updating a lead
def lead_update(request, pk):
    lead=Lead.objects.get(id=pk)
    form=LeadModelForm(instance=lead)
    if request.method=="POST":
        form=LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context={
        "lead":lead,
        "form":form 
    }
    return render(request, "lead_update.html", context)
def lead_delete(request, pk):
    lead=Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")
def landing_page(request):
    return render(request, "landing_page.html")
# def lead_update(request, pk):
#     lead=Lead.objects.get(id=pk)
#     form=LeadForm()
#     if request.method=="POST":
#         form=LeadForm(request.POST)
#         if form.is_valid():
#             # used to accept user values as input that passes the validation 
#             first_name=form.cleaned_data['first_name']
#             last_name=form.cleaned_data['last_name']
#             age=form.cleaned_data['age']
#             # used to update the leads
#             lead.first_name=first_name
#             lead.last_name=last_name
#             lead.age=age
#             # use to save the values to the database
#             lead.save()
#             # use to redirect use to a specifi page e.g homepage
#             return redirect("/leads")
#     context={
#         "lead":lead,
#         "form":form 
#     }
#     return render(request, 'lead_update.html', context)
# Create your views here.

#     #print(request.POST)
#     form=LeadForm()
#     if request.method=="POST":
#         print('recieving a post request')
#         #form is used to capture record from the user
#         form=LeadForm(request.POST)
#         #check the form is valid
#         if form.is_valid():
#             print("form is valid")
#             print(form.cleaned_data)
#             first_name=form.cleaned_data['first_name']
#             last_name=form.cleaned_data['last_name']
#             age=form.cleaned_data['age']
#             agent= Agent.objects.first()
#             #creating a new lead
#             Lead.objects.create(
#                 first_name=first_name,
#                 last_name=last_name,
#                 age=age,
#                 agent=agent
#             )
#             print("lead created")
#             return redirect("/leads")
#     context={
#         "form":form
#     }
#     return render(request, "lead_create.html", context)
# # Create your views here.
