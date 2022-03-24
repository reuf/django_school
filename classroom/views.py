from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from classroom.models import Teacher
from classroom.forms import ContactForm

# Create your views here.
class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYou(TemplateView):
    template_name = 'classroom/thank_you.html'

class TeacherCreateView(CreateView):
    model = Teacher
    # model_form.html - in this case teacher_form.html
    # it will automatically run .save() after all fields are validated
    fields = "__all__"
    success_url = reverse_lazy('classroom:thank_you')

class TeacherListView(ListView):
    # model_list.html - teacher_list.html
    model = Teacher
    queryset = Teacher.objects.all().order_by('first_name')

    context_object_name = "teacher_list"

class TeacherDetailView(DetailView):
    # RETURN ONLY ONE MODEL ENTRY PK
    # model_detail.html
    model = Teacher
    # PK --> {{teacher}}

class TeacherUpdateView(UpdateView):
    # SHARE model_form.html --- PK
    model = Teacher
    fields = "__all__"
    success_url = reverse_lazy('classroom:list_teacher')

class TeacherDeleteView(DeleteView):
    # Form --> Confirm Delete Button
    # default template name
    # model_confirm_delete.html
    model = Teacher
    success_url = reverse_lazy('classroom:list_teacher')




class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    # URL NOT a template.html
    success_url = reverse_lazy('classroom:thank_you')

    # what to do with a form
    def form_valid(self, form):
        print(form.cleaned_data['name'])
        return super().form_valid(form)

