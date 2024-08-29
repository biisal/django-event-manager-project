from django import forms
from .models import Event
from django_quill.widgets import QuillWidget

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'location','event_date', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'bg-transparent block w-full p-2 border border-gray-300 rounded mt-1 mb-4' , 'placeholder': 'Enter Event Name'}),
            'location': forms.TextInput(attrs={'class': 'bg-transparent block w-full p-2 border border-gray-300 rounded mt-1 mb-4 text-white' , 'placeholder': 'Enter Event Location'}),
            'event_date': forms.DateInput(attrs={'class': 'bg-transparent block w-full p-2 border border-gray-300 rounded mt-1 mb-4 text-white' , 'placeholder': 'Enter Event Date: YYYY-MM-DD'}),
            'description': QuillWidget(attrs={
                'class': 'custom-quill-editor text-white block w-full h-[400px] p-2 border border-gray-300 rounded mt-1 row-span-2 resize-none'}),
        }
