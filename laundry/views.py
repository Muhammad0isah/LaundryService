from types import FrameType
from django.db.models.expressions import F
from django.shortcuts import render,redirect
from .form import EnquiryForm
from .models import Record


# Create your views here.
def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    enquiry = EnquiryForm()
    if request.method == 'POST':
        enquiry = EnquiryForm(request.POST)
        if enquiry.is_valid():
            enquiry.save()
            return redirect('services')
    context = {'enquiry':enquiry}
    return render(request, 'services.html',context)


def records(request):
    customer_records = Record.objects.all()
    context = {'record': customer_records}
    return render(request, 'record.html', context)


def blog(request):
    return render(request, 'blog.html')


def blog_detail(request):
    return render(request, 'blog_details.html')


def element(request):
    return render(request, 'elements.html')


def contact(request):
    return render(request, 'contact.html')


def delivery(request):
    return render(request, 'delivery.html')
