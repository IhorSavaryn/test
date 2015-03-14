#_*_ coding: utf-8 _*_

from django.shortcuts import render
from django.http import HttpResponse

#Students
def students_list(request):
    students = (
    {'id':1,
    'first_name': u'Корост',
    'last_name': u'Андрій',
    'ticket': 2123,
    'image': 'img/1.jpg'},
    {'id':2,
    'first_name': u'Саварин',
    'last_name': u'Сергій',
    'ticket': 2100,
    'image': 'img/2.jpg'},
    {'id':3,
    'first_name': u'Саварин',
    'last_name': u'Ігор',
    'ticket': 1034,
    'image': 'img/3.jpg'},
    )
    return render(request, 'students/students_list.html', 
	{'students': students})
def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')
def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)
def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

#Groups
def groups_list(request):
    return HttpResponse('<h1>Groups Listing</h1>')
def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')
def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)
def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)





