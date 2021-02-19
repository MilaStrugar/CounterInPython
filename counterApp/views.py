from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if 'visitcount' in request.session:
        request.session['visitcount'] += 1
    else:
        request.session['visitcount'] = 1
    return render(request, 'index.html')

def reset(request):
    del request.session['visitcount']
    return redirect('/')

def increment(request):
    if 'visitcount' in request.session:
        request.session['visitcount'] += 2
    else:
        request.session['visitcount'] = 2
    return render(request, 'index.html')