from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.template import Template
from ..forms import render_form, save_form
from django.views.generic import UpdateView
from django.utils.decorators import method_decorator
from authentication.forms import StudentForm
from django.urls import reverse
from datetime import datetime
from django.http import HttpResponse

from ..models import *


@login_required()
def student_home(request):
    student = request.user.student
    forms = ApplicationForm.objects.exclude(questions__answers__response__owner=student)
    responses = student.responses.all()

    return render(request, 'broker/student/home.html',
                  context={'user': request.user, 'forms': forms, 'responses': responses})


@login_required()
def application(request, id):
    form = ApplicationForm.objects.get(id=id)

    if request.method == "GET":
        form_template = Template(render_form(form, editable=True))
        form_html = form_template.render(RequestContext(request))

        return render(request, 'broker/student/application.html', context={'form': form_html})
    else:
        if datetime.now().date() <= form.deadline:
            response = ApplicationResponse(application=form, owner=request.user.student, state='p')
            response.save()
            save_form(form, request.POST, response)

            return redirect('application_success')
        else:
            return redirect('application_failed')


def application_success(request):
    return render(request, 'broker/student/success.html', {'message': 'Your Application Successfully Submited.'})

def application_failed(request):
    return render(request, 'broker/student/failed.html', {'message': "You can't submit this Application cause deadline date!"})


@login_required()
def view_student_profile(request):
    student = request.user.student
    return render(request, 'broker/student/view_student_profile.html', context={'student': student})


@method_decorator([login_required], name='dispatch')
class update_student_profile(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'broker/student/update_profile.html'

    def get_success_url(self):
        return reverse('student_home')

    def get_object(self, queryset=None):
        return self.request.user.student


@login_required()
def view_student(request, pk):
    student = Student.objects.get(student_id=pk)
    return render(request, 'broker/student/view_student_profile.html', context={'student': student})


@login_required()
def student_response_delete(request, id):
    student = request.user.student
    response = student.responses.get(id=id)
    response.delete()
    return render(request, 'broker/student/success.html', {'message': "Your Response was successfully canceled !"})
