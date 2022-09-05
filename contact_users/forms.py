from django import forms
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from datetime import date, timedelta

class UserPreferences(forms.Form):
    
    ralphs = forms.BooleanField(required=False)
    hmart = forms.BooleanField(required=False)
    email = forms.EmailField(required=True)    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('ralphs', css_class='form-group col-md-6 mb-0'),
                Column('hmart', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'email',
            Submit('submit', 'Submit')
        )    
    
    def get_info(self):
        cleaned_data = super().clean()
        
        user_ralphs = cleaned_data.get('ralphs')
        user_hmart = cleaned_data.get('hmart')
        user_email = cleaned_data.get('email')
        
        return user_ralphs, user_hmart, user_email
        
    
    def send(self):
        ralphs, hmart, user_email = self.get_info()
        
        subject = str(date.today()) + " Grocery Stores Weekly Ads"
        msg = """Here are copies of this week's grocery ads.\n 
        If you would like to change which stores are being delivered to you please visit ______.com.\n 
        Similarly, if you want to unsubscribe from these emails visit ____unsubscribe.com"""
        
        todays_date = date.today()
        date_offset = (todays_date.weekday()-2) % 7
        last_wednesday = str(todays_date - timedelta(days=date_offset))

        
        pref_email = EmailMessage(subject, msg, settings.EMAIL_HOST_USER, [user_email])
        
        if hmart:
            pref_email.attach_file('contact_users\\static\\contact_users\\Weekly_ads\\' + last_wednesday + '\\Hmart.jpg')
        if ralphs:
            pref_email.attach_file('contact_users\\static\\contact_users\\Weekly_ads\\' + last_wednesday + '\\Ralphs.pdf')
            
        pref_email.send()

class Unsubscription(forms.Form):
    
    email = forms.EmailField(required=True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'email',
            Submit('submit','Submit')
        )
    
    def get_info(self):
        clean_email = super().clean()
        return clean_email.get('email')
        
    
        
