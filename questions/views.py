from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    View,
)

from .forms import AnswerForm, QuestionForm
from .models import Answer, Question


class HomeView(ListView):
    model = Question
    template_name = "questions/home.html"
    context_object_name = "questions"
    ordering = ["-date_posted"]
    paginate_by = 10


class QuestionDetailView(DetailView):
    model = Question
    template_name = "questions/question_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["answers"] = self.object.answers.all().order_by("-date_posted")
        context["form"] = AnswerForm()
        return context


class AnswerCreateView(LoginRequiredMixin, CreateView):
    model = Answer
    form_class = AnswerForm
    http_method_names = ["post"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.question = get_object_or_404(Question, pk=self.kwargs["pk"])
        messages.success(self.request, "Your answer has been posted!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("question-detail", kwargs={"pk": self.kwargs["pk"]})


class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    form_class = QuestionForm
    template_name = "questions/ask_question.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Your question has been posted!")
        return super().form_valid(form)


class QuestionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Question
    form_class = QuestionForm
    template_name = "questions/edit_question.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Your question has been updated!")
        return super().form_valid(form)

    def test_func(self):
        question = self.get_object()
        return self.request.user == question.author


class QuestionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Question
    template_name = "questions/delete_question.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        question = self.get_object()
        return self.request.user == question.author

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Your question has been deleted!")
        return super().delete(request, *args, **kwargs)


class AnswerUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Answer
    form_class = AnswerForm
    template_name = "questions/edit_answer.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Your answer has been updated!")
        return super().form_valid(form)

    def test_func(self):
        answer = self.get_object()
        return self.request.user == answer.author


class AnswerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Answer
    template_name = "questions/delete_answer.html"

    def test_func(self):
        answer = self.get_object()
        return self.request.user == answer.author

    def get_success_url(self):
        return reverse("question-detail", kwargs={"pk": self.object.question.pk})

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Your answer has been deleted!")
        return super().delete(request, *args, **kwargs)


class LikeAnswerView(LoginRequiredMixin, View):
    def post(self, request, pk):
        answer = get_object_or_404(Answer, pk=pk)

        if request.user in answer.likes.all():
            answer.likes.remove(request.user)
        else:
            answer.likes.add(request.user)

        return HttpResponseRedirect(reverse("question-detail", args=[answer.question.pk]))
