from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, redirect
from .forms import CafeSubmissionForm
from .models import CafeSubmission
from coffeeshoplist.models import CoffeeShop
from .decorators import admin_required
from django.shortcuts import get_object_or_404
from django.urls import reverse



@login_required
def cafesubmission(request):
    if request.method == "POST":
        form = CafeSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            cafe_submission = form.save(commit=False)
            cafe_submission.submitted_by = request.user
            cafe_submission.save()
            messages.success(request, 'Thank you for submitting a coffee shop!')
            return redirect('cafesubmission:cafesubmission')
    else:
        form = CafeSubmissionForm()
    return render(request, 'cafesubmission.html', {'form': form})

# admin only view
@admin_required
def draftcafesubmission(request):
    submissions = CafeSubmission.objects.all()
    return render(request, 'draftcafesubmission.html', {'submissions': submissions})

@admin_required
def cafesubmission_approve(request, pk):
    submission = get_object_or_404(CafeSubmission, pk=pk)

    # create new coffee shop instance
    coffee_shop = CoffeeShop()
    coffee_shop.name = submission.name
    coffee_shop.description = submission.description
    coffee_shop.address = submission.address
    coffee_shop.website = submission.website
    coffee_shop.hours = submission.hours
    coffee_shop.phone = submission.phone
    coffee_shop.image = submission.image
    coffee_shop.save()

    # delete the submission
    submission.delete()

    messages.success(request, 'The coffee shop has been approved and added to the list!')
    return redirect('/')

# admin only view
@admin_required
def cafesubmission_delete(request, pk):
    submission = get_object_or_404(CafeSubmission, pk=pk)
    submission.delete()
    messages.success(request, 'The coffee shop submission has been deleted!')
    return redirect('caffesubmisions/draft')


