from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def home_page(request):
    return render(
        request,
        "admin_template/home.html",
        context={
            "avatar_url": request.user.avatar_url,
        },
    )
