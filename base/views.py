from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from base import models
from base.models import contact

# Home Page


# Contact Form View
def contact_view(request):
    if request.method == "POST":
        # Get form data from POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('content')
        number = request.POST.get('number')

        print(name, email, number, content)  # For debugging

        # Name validation
        if not (1 < len(name) < 30):
            messages.error(request, 'Length of name should be greater than 2 and less than 30 characters.')
            return render(request, 'home.html')

        # Email validation
        if not (1 < len(email) < 30) or '@' not in email:
            messages.error(request, 'Invalid email. Please try again.')
            return render(request, 'home.html')

        # Number validation
        if not (number.isdigit() and len(number) == 10):
            messages.error(request, 'Invalid phone number. Please enter a 10-digit number.')
            return render(request, 'home.html')

        # Save to database
        ins = contact(name=name, email=email, content=content, number=number)
        ins.save()

        # Success message
        messages.success(request, 'Thank you for contacting me! Your message has been saved.')
        print('Data has been saved to the database')

    return render(request, 'home.html')
