from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

from .models import Review
from .forms import ReviewForm
# Create your views here.

class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review.html' 
    success_url = '/thank-you'

# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, 'reviews/review.html', {
#             'form': form,
#         }) 

#     def post(self, request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/thank-you')
#         else:
#             return render(request, 'reviews/review.html', {
#                 'form': form,
#             })

# def review(request):
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/thank-you')
#     else:
#         form = ReviewForm()
#     return render(request, 'reviews/review.html', {
#         'form': form,
#     })

class ThankyouView(TemplateView):
    template_name = 'reviews/thankyou.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'It Works'
        return context


# class ReviewListView(TemplateView):
#     template_name = 'reviews/review_list.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context['reviews'] = reviews
#         return context


class ReviewListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review
    context_object_name = 'reviews'

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     data = queryset.filter(rating__gt=4)
    #     return data

# class SingleReviewView(TemplateView):
#     template_name = 'reviews/single_review.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs['id']
#         selected_review = Review.objects.get(pk=review_id)
#         context['review'] = selected_review
#         return context

class SingleReviewView(DetailView):
    template_name = 'reviews/single_review.html'
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object 
        request = self.request
        favorite_id = request.session.get('favorite_review')
        context['is_favorite'] = favorite_id == str(loaded_review.id)
        return context

# def thank_you(request):
#     return render(request, 'reviews/thankyou.html')

class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST['review_id']
        request.session['favorite_review'] = review_id
        return HttpResponseRedirect('/reviews/' + review_id)