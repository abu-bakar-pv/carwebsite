from django.shortcuts import render ,redirect , get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)

from .  import models
from buggy_app.models import Booking , Car
from django.forms import ModelForm
from django.views.generic.edit import FormView


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ('booking_name','rental_price','book_car','customer_name',)




class IndexView(TemplateView):

    template_name = 'buggy_app/index.html'




'''
class BookingListView(ListView):

    model = models.Booking


class BookingDetailView(DetailView):
    context_object_name = 'booking_details'
    model = models.Booking
    template_name = 'buggy_app/booking_detail.html'


class BookingCreateView(CreateView):
    fields = ("customer_name","book_car","booking_end_date","rental_price","is_approved")
    model = models.Booking


class BookingUpdateView(UpdateView):
    fields = ("customer_name","book_car","booking_end_date","rental_price","is_approved")
    model = models.Booking
'''

class CarListView(ListView):
    context_object_name = 'cars'
    model = models.Car

class CarDetailView(DetailView):
    context_object_name = 'car_details'
    model = models.Car
    template_name = 'buggy_app/car_detail.html'



#amir bhai stackoverflow p yh code btaya tha paste kiya hua kch ni
class BookingView(FormView):
    template_name = 'buggy_app/booking.html'
    form_class = BookingForm

    def get_context_data(self, **kwargs):
        try:
            kwargs['car'] = Car.objects.get(id=self.request.GET.get('car', ''))
        except (Car.DoesNotExist, ValueError):
            kwargs['car'] = None
        return super(BookingView, self).get_context_data(**kwargs)






'''
def booking_create(request,pk):
    book_car = get_object_or_404(Car, pk=pk)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():

            booking = form.save(commit=False)
            booking.book_car = book_car
            booking.save()
            return redirect('car_detail', pk=book_car.pk)
    else:
        form = BookingForm()
    return render(request, 'buggy_app/booking_form.html', {'form': form})
'''
