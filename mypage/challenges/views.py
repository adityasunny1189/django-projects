from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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
	"dec": "Learn django for 20 mins daily"
}

# Create your views here.
def monthly_challenge_num_wise(request, month):
	months = list(months_and_challenges.keys())
	if month > len(months):
		return HttpResponseNotFound('Invalid Month')
	redirect_month = months[month]
	return HttpResponseRedirect('/challenges/' + redirect_month)

def monthly_challenge(request, month):
	try:
		challenge = months_and_challenges[month]
		return HttpResponse(challenge)
	except KeyError:
		return HttpResponseNotFound('Invalid Month')
