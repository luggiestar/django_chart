from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Club
import qrcode
import os
from PIL import Image
from django.conf import settings

# Create your views here.
def index(request):
    return render(request, 'base.html')


class ClubChartView(TemplateView):
    template_name = 'clubs/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs'] = Club.objects.all()
        return context


def generate_qr(request):
    name = "O2 EXPORT GEM COMPANY LTD."
    country = "Tanzania."
    region = "Arusha."
    district = "Sekei, Arusha."
    pocode = "1865."
    road = "Nyerere Road, Arusha."
    plot_number = 15
    tel = "+255 629 000 222"
    whatsapp = "+49 1523 6105811"
    email = "O2exportgems@gmail.com"
    valid = "This qrcode Not valid"
    msg = "We are receiving and  supplying all orders from in and outside Tanzania."
    supply = "We can supply:-\n i). Graphite\n ii). Nickel\n iii). Copper ore\n iv). Gypsum\n v). Iron ore"
    supply_msg = f"{msg}\n{supply}"
    note = f"Note:\n{supply_msg}\n\nAlso We are always at a show at USA:-\n -Denver Show\n -22nd street show\n -Munich show\n -St Marie show"

    link = "https://maps.app.goo.gl/Yw8otxkm1MpJMUax7"
    link_website = "https://o2gemexport.com"
    website = f"Website \n{link_website}"
    location_map = f"Google Map Location Link\n{link}"

    email_link = f"<a href='mailto:{email}'>O2exportgems@gmail.com</a>"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=40,
        border=30
    )

    location1 = f'\nCountry: {country}\nRegion: {region}\nDistrict: {district}\nPostal Code: {pocode}'
    location2 = f'\nRoad: {road}\nPlot Number: {plot_number}'
    data = f'{name} {location1}{location2}\n\nEmail: {email}\nWhatsApp: {tel}\nWhatsApp: {whatsapp}'

    qr.add_data(f'{data}\n\n{note}\n\n{website}\n\n{location_map}')
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="#009eff", back_color='#d1e0e9') #blue
    # qr_img = qr.make_image(fill_color="black", back_color='#d1e0e9')
    # qr_img = qr.make_image(fill_color="black", back_color='white')

    # Define the path to save the QR code PNG file in the static directory
    static_dir = os.path.join(settings.BASE_DIR, 'static')
    qr_code_path = os.path.join(static_dir, 'qrcodes', f'{name}_qrcode.png')

    # Create the 'qrcodes' subdirectory if it doesn't exist
    os.makedirs(os.path.dirname(qr_code_path), exist_ok=True)

    # Save the QR code as a PNG file
    qr_img.save(qr_code_path)

    qr_code_url = os.path.join(settings.STATIC_URL, 'qrcodes', f'{name}_qrcode.png')

    context = {
        'qr_img': qr_code_url,
        'name': name
    }

    return render(request, "qrcode.html", context)