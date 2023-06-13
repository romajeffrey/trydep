from django.shortcuts import render


def home(request):
    # print 'jeffrey'
    return render(request, 'home.html')
