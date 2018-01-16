from django.shortcuts import render
from .models import Verse

# Create your views here.
def verse_list(request):
	verses = Verse.objects.all().order_by('id')
	return render(request, 'memorize/verse_list.html', {'verses': verses})