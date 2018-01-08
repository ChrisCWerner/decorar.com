from django.shortcuts import render

# Create your views here.
def verse_list(request):
    return render(request, 'memorize/verse_list.html')