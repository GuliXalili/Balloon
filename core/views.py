from django.shortcuts import render

def olma(request):
    return render(request, 'olma.html')

def sabzi(request):
    return render(request, 'sabzi.html')

def gulkaram(request):
    return render(request, 'gulkaram.html')
