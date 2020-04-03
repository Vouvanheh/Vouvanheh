from django.shortcuts import render
from .forms import SubscriberForm


def landing(request):
    name = "Boss"
    current_day = "23.03.2020"
    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()

    return render(request, 'landing/landing.html', locals())
