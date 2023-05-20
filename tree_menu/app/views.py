from django.shortcuts import render


def index(request, path):
    return render(
        request, 'app/draw_menu.html', {'menu_name': path.split('/')[-1]})
