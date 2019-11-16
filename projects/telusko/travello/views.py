from django.shortcuts import render
from . models import Destination
# Create your views here.

def index(request):
	dest1 = Destination()
	dest1.name = 'Mumbai'
	dest1.desc = 'The City that never sleeps'
	dest1.img = 'muma.webp'
	dest1.price = 700
	dest1.offer = False

	dest2 = Destination()
	dest2.name = 'Kolkata'
	dest2.desc = 'City of joy'
	dest2.img = 'Victoria.jpg'
	dest2.price = 550
	dest2.offer = True

	dest3 = Destination()
	dest3.name = 'Hyderabad'
	dest3.desc = 'First Biryani, Then Sherwani'
	dest3.img = 'hyder.jpg'
	dest3.price = 650
	dest3.offer = False


	dests = [dest1, dest2, dest3]

	return render(request,"index.html",{'dests':dests})