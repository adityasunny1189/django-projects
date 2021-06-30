from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from .models import UserProfile
from .forms import ProfileForm

# Create your views here.

# def store_files(file):
#     with open(f'temp/{file}', 'wb+') as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)

class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html", {
            'form': form
        })

    def post(self, request):
        submitted_form = ProfileForm(request.POST, request.FILES)
        if submitted_form.is_valid():
            profile = UserProfile(image=request.FILES['user_image'])
            profile.save()
            return HttpResponseRedirect('/profiles')

        else:
            return render(request, "profiles/create_profile.html", {
                'form': submitted_form
            })

class UserProfileView(ListView):
    template_name = 'profiles/user_profile.html'
    model = UserProfile
    context_object_name = 'profiles'
