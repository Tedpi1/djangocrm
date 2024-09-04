from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import generic
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm,CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

#CRUD- Create, Retrieve, Update, Delete
# login user
def login_user(request):
    #check wether the user as filled the form
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('leads:lead-list')
        else:
            messages.error(request, "There was an error logging in, please try again")
            return redirect('login')
            # Return an 'invalid login' error message.
    return render(request, "registration/login.html", {})
#logout user
def logout_user(request):
    logout(request)
    return redirect('login')

#signup view
class SignupView(generic.CreateView):
    template_name="registration/register.html"
    form_class=CustomUserCreationForm
    def get_success_url(self):
        return reverse('login')
class landingPageView(generic.TemplateView):
    template_name = "landing_page.html"
class leadListView(LoginRequiredMixin,generic.ListView):
    template_name = "lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"
class LeadDetailView(LoginRequiredMixin,generic.DetailView):
    template_name = "lead_detail.html"
    queryset = Lead.objects.all()

class LeadCreateView(LoginRequiredMixin,generic.CreateView):
    template_name = "lead_create.html"
    form_class = LeadModelForm
    def get_success_url(self):
        return reverse("leads:lead-list")
    def form_valid(self, form):
        send_mail(
            subject="A new lead has been created",
            message="Go to site admin to see new lead",
            from_email="test@test.com",
            recipient_list=["test2@test.com"]
        )
        return super(LeadCreateView, self).form_valid(form)
class LeadUpdateView(LoginRequiredMixin,generic.UpdateView):
    template_name = "lead_update.html"
    form_class = LeadModelForm
    queryset=Lead.objects.all()
    def get_success_url(self):
        return reverse("leads:lead-list")
class LeadDeleteView(LoginRequiredMixin,generic.DeleteView):
    template_name = "lead_delete.html"
    queryset=Lead.objects.all()
    def get_success_url(self):
        return reverse("leads:lead-list")
# def lead_list(request):
#     #return HttpResponse("Hello World")
#     leads=Lead.objects.all()#fetching leads app from our models
#     context={
#         "leads":leads
#     }
#     return render(request, "lead_list.html", context)
# def lead_detail(request, pk):
#     lead=Lead.objects.get(id=pk)
#     context={
#         "lead":lead
#     }
#     return render(request, "lead_detail.html", context)
# def lead_create(request):
#     #print(request.POST)
#     form=LeadModelForm()
#     #check if the request method is POST
#     if request.method=="POST":
#         print('recieving a post request')
#         #form is used to capture record from the user
#         form=LeadModelForm(request.POST)
#         #check the form is valid
#         if form.is_valid():
#             form.save()#easy to use because we specified the model we are using 'Lead'
#             return redirect("/leads")
#     context={
#         "form":form
#     }
#     return render(request, "lead_create.html", context)

# # updating a lead
# def lead_update(request, pk):
#     lead=Lead.objects.get(id=pk)
#     form=LeadModelForm(instance=lead)
#     if request.method=="POST":
#         form=LeadModelForm(request.POST, instance=lead)
#         if form.is_valid():
#             form.save()
#             return redirect("/leads")
#     context={
#         "lead":lead,
#         "form":form
#     }
#     return render(request, "lead_update.html", context)
# def lead_delete(request, pk):
#     lead=Lead.objects.get(id=pk)
#     lead.delete()
#     return redirect("/leads")
# def landing_page(request):
#     return render(request, "landing_page.html")
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
