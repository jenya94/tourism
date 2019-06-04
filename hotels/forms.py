from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, HTML, Hidden, BaseInput
from crispy_forms.bootstrap import Field
from .models import Hotel


class EditHotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EditHotelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.field_class = 'col-lg-8'
        self.helper.label_class = 'col-lg-2'
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Fieldset(
                'Form',
                Hidden('owner', '{{ user.id }}'),
                Field('name',  placeholder='Bes qala'),
                Field('address', placeholder='Nokis qalasi Avto vokzal'),
                Field('phone_number', placeholder='+9989********'),
                Field('email',  placeholder='example@mail.ru'),
                Submit('submit', 'Add hotel', css_class='col-lg-offset-2'),
                HTML("<style>.asteriskField {display: none;}</style>")
            )
        )


class AddHotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AddHotelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.field_class = 'col-lg-8'
        self.helper.label_class = 'col-lg-2'
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Fieldset(
                'Form',
                Hidden('owner', '{{ user.id }}'),
                Field('name', placeholder='Bes qala'),
                Field('address', placeholder='Nokis qalasi Avto vokzal'),
                Field('phone_number', placeholder='+9989********'),
                Field('email', placeholder='example@mail.ru'),
                Field('photo'),
                Field('price'),
                Field('currency'),
                Submit('submit', 'Add hotel', css_class='col-lg-offset-2'),
                HTML("<style>.asteriskField {display: none;}</style>")
            )
        )


