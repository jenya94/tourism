from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, HTML, Hidden, BaseInput
from crispy_forms.bootstrap import Field
from sightseeing.models import Sightseeing


class EditSightseeingForm(forms.ModelForm):
    class Meta:
        model = Sightseeing
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EditSightseeingForm, self).__init__(*args, **kwargs)
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
                Field('eatery_type'),
                Submit('submit', 'Add hotel', css_class='col-lg-offset-2'),
                HTML("<style>.asteriskField {display: none;}</style>")
            )
        )


class AddSightseeingForm(forms.ModelForm):
    class Meta:
        model = Sightseeing
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AddSightseeingForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.field_class = 'col-lg-8'
        self.helper.label_class = 'col-lg-2'
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Fieldset(
                'Form',
                Hidden('owner', '{{ user.id }}'),
                HTML("""<div id="div_id_date" class="form-group">
                  <label for="id_date" class="control-label col-lg-2 requiredField">Date</label>
                  <div class="col-lg-8">
                      <input type="date" name="date" class="form-control" required id="id_date"> 
                    </div> 
                </div>
                """),
                Field('photo'),
                Field('place', placeholder='Place'),
                Submit('submit', 'Add hotel', css_class='col-lg-offset-2'),
                HTML("<style>.asteriskField {display: none;}</style>")
            )
        )

