# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import FormView, RedirectView
from django.shortcuts import redirect
from django.contrib.auth import login, logout
from .forms import LoginForm


class LoginView(FormView):
    temnplate_name = ''
    form_class = LoginForm
    success_url = ''

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        

class LogoutView(RedirectView):
    url = ''
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
