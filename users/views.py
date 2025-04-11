from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from .forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm


class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get("username")
        messages.success(self.request, f"Account created for {username}! You can now log in.")
        return response

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return super().dispatch(request, *args, **kwargs)


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "users/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_questions"] = self.request.user.question_set.all().order_by("-date_posted")
        context["user_answers"] = self.request.user.answer_set.all().order_by("-date_posted")
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "users/profile_update.html"
    success_url = reverse_lazy("profile")

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["profile_form"] = ProfileUpdateForm(
                self.request.POST, self.request.FILES, instance=self.request.user.profile
            )
        else:
            context["profile_form"] = ProfileUpdateForm(instance=self.request.user.profile)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        profile_form = context["profile_form"]

        if profile_form.is_valid():
            profile_form.save()
            messages.success(self.request, "Your profile has been updated!")
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))
