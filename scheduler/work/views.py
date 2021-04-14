from django.shortcuts import render,redirect
from django.http.request import HttpRequest
from django.http import HttpResponse
from .models import Work


# Create your views here.



def work_table(request):
    context = {
        'work_table': Work.objects.all()
    }
    return render(request, 'work/work_table.html', context)



def insert_table(request:HttpRequest):

    work = Work(content = request.POST['content'])
    work.save()
    return redirect('/work/table/')


def delete_table(request, work_id):
    work_to_delete = Work.objects.get(id = work_id)
    work_to_delete.delete()
    return redirect('/work/table/')