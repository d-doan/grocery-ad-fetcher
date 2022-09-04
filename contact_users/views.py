from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy

from datetime import date, timedelta
from .forms import Unsubscription, UserPreferences


class ContactView(FormView):
    template_name = 'contact_users/contact.html'
    form_class = UserPreferences
    success_url = reverse_lazy('contact_users:success')

    def form_valid(self, form):
        form.send()
        return super().form_valid(form)
    
class SuccessView(TemplateView):
    template_name = 'contact_users/success.html'

class UnsubscribeView(FormView):
    template_name = 'contact_users/unsubscribe.html'
    form_class = Unsubscription
    success_url = reverse_lazy('contact_users:unsub_success')
    
class UnsubSuccessView(TemplateView):
    template_name = 'contact_users/unsub_success.html'
    
class WeeklyAdView(TemplateView):
    template_name = 'contact_users/weekly_ads.html'
    
    todays_date = date.today()
    date_offset = (todays_date.weekday() -2) % 7
    recent_ad = str(todays_date - timedelta(days=date_offset))
    
    hmartPath = 'contact_users\\Weekly_ads' + '\\' + recent_ad + '\\Hmart.jpg'
    ralphsPath = 'contact_users\\Weekly_ads' + '\\' + recent_ad + '\\Ralphs.pdf'
    
    def get_context_data(self, *args, **kwargs):
        context = super(WeeklyAdView, self).get_context_data(*args,**kwargs)
        context['hmart'] = self.hmartPath
        context['ralphs'] = self.ralphsPath
        return context
    