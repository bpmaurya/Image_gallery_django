from .models import Imagepost
from django.forms import ModelForm, fields

class Image_form(ModelForm):
    class Meta:
        model = Imagepost
        fields = ['title','head1','chead1','tags','pub_date','image']