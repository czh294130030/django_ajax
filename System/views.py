from django.shortcuts import render

from System.models import Organization


def index(request):
    # orgList = Organization.objects.all();
    return render(request, "Organization/index.html", locals())
