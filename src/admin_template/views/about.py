from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def about_page(request):
    return render(request, "admin_template/about.html")
