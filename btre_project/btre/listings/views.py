from django.shortcuts import get_object_or_404,render
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from .choices import price_choices,state_choices,bedroom_choices
from .models import Listing
# Create your views here.

def index(request):
    listings = Listing.objects.all().filter(is_published=True)
    
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    
    context = {
        'listings' : paged_listings
    }
    return render(request, 'listings/listings.html',context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing)
    
    context = {
        'listing' : listing
    }
    return render(request, 'listings/listing.html',context)

def search(request):

    context = {
        'state_choices' : state_choices,
        'bedroom_choices' : bedroom_choices,
        'price_choices' : price_choices,
    }
    return render(request, 'listings/search.html',context)