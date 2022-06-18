from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages
from django.db.models import Q
from .forms import FeedbackForm
from .models import FeedbackModel



class Home(View):
    def get(self, request):
        form = FeedbackForm()
        
        data = FeedbackModel.objects.all()
        return render(request, 'home.html', {"form":form, 'data':data})
    

    def post(self, request):
        form = FeedbackForm(request.POST)
        
        if form.is_valid():
            user = FeedbackModel.objects.filter(Q(email = form.cleaned_data['email']))
            if user:
                messages.error(request, f'User Already exist with (id : {user.get(name = form.cleaned_data["name"]).id})')
            else:
                form.save()
                id = FeedbackModel.objects.get(email= form.cleaned_data['email']).id
                messages.success(request, f'Successfully Created. (id : {id})')
        return redirect('home')
    

def delete_all(request):
    data = FeedbackModel.objects.all()
    if not data:
        messages.info(request, 'Sorry, There is no accounts to delete.')
    else:
        no_of_accounts = data.count()
        data.delete()
        messages.info(request, f'Deleted {no_of_accounts} accounts')
    return redirect("home")


def delete_data(request, pk):
    try:
        data = FeedbackModel.objects.get(id = pk)
        data.delete() 
        messages.info(request, f'Deleted Successfully. (id : {pk})')
    except:
        messages.error(request, 'User doesnt exit..')
        
    return redirect('home')


class Update(View):
    
    def get(self, request, pk):
        details = FeedbackModel.objects.get(id = pk)
        form = FeedbackForm(instance = details)
        
        return render(request, 'update.html',{"form":form, "pk":pk} )
    
    def post(self, request, pk):
        details = FeedbackModel.objects.get(id = pk)
        form = FeedbackForm(request.POST, instance = details)
        if form.is_valid():
            form.save()
            messages.success(request, f'Update Sucessful (id : {pk})')
        else:
            messages.error(request, 'Invalid Data')
        
        return redirect('home')