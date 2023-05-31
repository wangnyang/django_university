from django.test import TestCase
from university_app import forms
from university.settings import LANGUAGE_CODE
from .attrs import mark_attrs

class MarkFormTests(TestCase):
    
    def test_successful(self):
        forms.AddMarkForm(data=mark_attrs)

    def test_failing(self):
        languages = ('en-EN', 'ru-RU')
        if LANGUAGE_CODE not in languages:
            print('Skipping form failing tests as language is not supported by tests')
            return
        location = random_string()
        form = forms.WeatherForm(data={'location': location})
        errors = [
            f'Выберите корректный вариант. {location} нет среди допустимых значений.',
            f'Select a valid choice. {location} is not one of the available choices.',
        ]
        for error in form.errors['location']:
            self.assertIn(error, errors)        # assertIn - error in errors
