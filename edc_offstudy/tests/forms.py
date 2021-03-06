from django import forms

from ..modelform_mixins import OffstudyModelFormMixin
from ..modelform_mixins import OffstudyCrfModelFormMixin, OffstudyNonCrfModelFormMixin
from .models import SubjectOffstudy, CrfOne, NonCrfOne


class SubjectOffstudyForm(OffstudyModelFormMixin, forms.ModelForm):

    class Meta:
        model = SubjectOffstudy
        fields = '__all__'


class CrfOneForm(OffstudyCrfModelFormMixin, forms.ModelForm):

    class Meta:
        model = CrfOne
        fields = '__all__'


class NonCrfOneForm(OffstudyNonCrfModelFormMixin, forms.ModelForm):

    class Meta:
        model = NonCrfOne
        fields = '__all__'
