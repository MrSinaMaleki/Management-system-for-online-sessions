from django import forms
from online_classes.models import Session


class SessionForm(forms.ModelForm):
    # start_date = forms.TimeField(widget=forms.SplitDateTimeField())
    # end_time = forms.TimeField(widget=forms.SelectDateWidget())

    # end_time = forms.DateField(label='Release year', required=False, widget=forms.SelectDateWidget)

    class Meta:
        model = Session
        fields = '__all__'
        # end_time = forms.TimeField(
        #     widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        #     label='Select Time',
        # )

