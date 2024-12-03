from django import forms
from .models import ContactModel, NearByPlace, ClientReview, Gallery, Folder, Booking, RoomPrice



# Contact us
class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'

# NearByPlaceForm
class NearByPlaceForm(forms.ModelForm):
    class Meta:
        model = NearByPlace
        fields = '__all__'

# Clien Review
class ClientReviewForm(forms.ModelForm):
    class Meta:
        model = ClientReview
        fields = '__all__'

# Gallery
class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'

# Folder
class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = '__all__'


# Booking
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'  # You can choose specific fields if you don't need all fields
        
        # Define the custom widgets for arrival_date and departure_date
        widgets = {
            'arrival_date': forms.DateInput(
                format='%A %d %B %Y',  # Full date format including weekday
                attrs={'placeholder': 'Thursday 14 November 2024'}  # Optional: placeholder in the input field
            ),
            'departure_date': forms.DateInput(
                format='%A %d %B %Y',  # Same date format for departure
                attrs={'placeholder': 'Thursday 14 November 2024'}
            ),
        }
        
    # Ensuring that the form can handle the custom date format on submission
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the allowed input formats for both arrival_date and departure_date fields
        self.fields['arrival_date'].input_formats = ['%A %d %B %Y']
        self.fields['departure_date'].input_formats = ['%A %d %B %Y']



