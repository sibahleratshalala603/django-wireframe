from django.shortcuts import render


def track_home(request):
    return render(request, 'track/track_home.html', {
        'title': 'Track Home',
    })


def track_log(request):
    return render(request, 'track/track_log.html', {
        'title': 'Track Log',
    })
