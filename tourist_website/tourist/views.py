from django.shortcuts import render

# Create your views here.
# tourist/views.py
from django.shortcuts import render,redirect, get_object_or_404
from .models import Destination
from datetime import date

def home(request):
    return render(request, 'tourist/home.html')

def destination_detail(request):
    return render(request, 'tourist/destination.html')

def contact(request):
    return render(request, 'tourist/contact.html')

def about(request):
    return render(request, 'tourist/about.html')

def signup(request):
    context = {}
    if request.method == "POST":
        uname = request.POST.get('uname')
        uemail = request.POST.get('uemail')
        upassword = request.POST.get('upassword')
        cpassword = request.POST.get('cpassword')
        if uname == "" or uemail == "" or upassword == "" or cpassword == "":
            context['error'] = "All fields are required"
        elif upassword != cpassword:
            context['error'] = "Passwords did not match"
        else:
            try:
                u = User.objects.create_user(username=uname, email=uemail, password=upassword)
                u.save()
                return redirect('tourist/signup.html')
            except Exception:
                context["error"] = "User already exists"
    return render(request, "tourist/signup.html", context)

def login(request):
    context = {}
    if request.method == "POST":
        nm = request.POST["uname"]
        pw = request.POST["upassword"]  
        if nm == "" or pw == "":
            context['errmsg'] = "Fields cannot be Empty"
            return render(request, "tourist/signup.html", context)
        else:
            user = authenticate(username=nm, password=pw)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                context["errmsg"] = "Invalid Username and password"
                return render(request, "tourist/login.html", context)
    else:
        return render(request, "tourist/login.html")
    

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TravelInfo

def icons_view(request):
    
    # List of cities to show in the dropdown'""
    cities = ["New York", "Los Angeles", "Chicago", "San Francisco", "Houston","India"]
    

    if request.method == 'POST':
        # Get form data
        from_location = request.POST.get('from_location')
        to_location = request.POST.get('to_location')
        travel_date = request.POST.get('travel_date')

        # Save data to the database
        travel_info = TravelInfo(
            from_location=from_location,
            to_location=to_location,
            travel_date=travel_date
        )
        travel_info.save()

        return redirect('/home')  # Redirect after saving

    # Pass the cities list to the template
    context = {
        'cities': cities,
    }
    return render(request, 'tourist/home.html', context)

from .models import Booking

def register_booking(request):
    if request.method == "POST":
        from_location = request.POST.get('from_location')
        to_location = request.POST.get('to_location')
        travel_date = request.POST.get('travel_date')

        # Save data to the Booking model
        booking = Booking(
            from_location=from_location,
            to_location=to_location,
            travel_date=travel_date
        )
        booking.save()

        # Redirect to a success page or home page
        return redirect('/home')

    return HttpResponse("Invalid request.")