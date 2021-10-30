from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})

#funkcja post_list ktora pobiera i zwraca wartość wowalaną dzieki innej
#funkcji - render, ktora zlozy w calosc szablon html

