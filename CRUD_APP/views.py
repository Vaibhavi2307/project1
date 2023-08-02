from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm
from django.views import View
import logging 

logger=logging.getLogger('django')


class Employee_view(View):
    def get(self,request):
        template_name='CRUD_APP/employee.html'
        form=EmployeeForm()
        context={'form':form}
        return render(request,template_name,context)
    
    def post(self,request):
        template_name='CRUD_APP/employee.html'
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info("new record is added")
            return redirect('show_url')
        context={'form':form}
        return render(request,template_name,context)
    
class Show_view(View):
    def get(self,request):
        template_name='CRUD_APP/show.html'
        employee=Employee.objects.all()
        logger.info("All records are fetch")
        logger.error("records are fetch")
        context={'employee':employee}
        return render(request,template_name,context)
    
class Update_view(View):
    def get(self,request,pk):
        template_name='CRUD_APP/employee.html'
        obj=Employee.objects.get(eid=pk)
        form=EmployeeForm(instance=obj)
        context={'form':form}
        return render(request,template_name,context)
    
    def post(self,request,pk):
        template_name='CRUD_APP/employee.html'
        obj=Employee.objects.get(eid=pk)
        form=EmployeeForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            logger.info("record is updated")
            return redirect('show_url')
        context={'form':form}
        return render(request,template_name,context)
    
class Delete_view(View):
    def get(self,request,pk):
        template_name='CRUD_APP/confirm.html'
        obj=Employee.objects.get(eid=pk)
        context={}
        return render(request,template_name,context)
    
    def post(self,request,pk):
        template_name='CRUD_APP/confirm.html'
        obj=Employee.objects.get(eid=pk)
        obj.delete()
        logger.info("record is deleted")
        return redirect('show_url')
    

    

