from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse

months_and_challenges = {
	"jan": "walk 20 min a day",
	"feb": "learn django for 20 min",
	"mar": "eats fruits daily",
	"apr": "code daily a DSA problem",
	"may": "walk 20 mins a day",
	"jun": "Learn machine learning",
	"jul": "Learn React Native",
	"aug": "Learn Stat and probability",
	"sep": "Learn django for 20 mins",
	"oct": "Learn Machine Learning",
	"nov": "Learn Android Development",
	"dec": None
}

# Create your views here.
def index(request):
	months = list(months_and_challenges.keys())
	return render(request, 'challenges/index.html', {
		"months": months
	})


def monthly_challenge_num_wise(request, month):
	months = list(months_and_challenges.keys())
	if month > len(months):
		raise Http404()
	redirect_month = months[month-1]
	redirect_path = reverse('month-challenge', args=[redirect_month]) # /challenge/<month>
	return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
	try:
		challenge = months_and_challenges[month]
		return render(request, 'challenges/challenges.html', {
				"month_name": month,
				"month_challenge": challenge
			})
	except KeyError:
		raise Http404()
