from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
# def home(request):
#     return render(request,'base.html')
from .models import *
from .forms import PlaceForm

def list(request):
    query = request.GET.get('name')  # รับคำค้นหาจากช่องกรอกคำค้น
    show_emp = Place.objects.all()

    if query:
        show_emp = Place.objects.filter(name__icontains=query)

    context = {'Placedata': show_emp}
    return render(request, 'list.html', context)

def manage(request):
    show_emp = Place.objects.all()
    context = {'Placedata':show_emp}
    return render(request,'show.html',context)

def add(request):
    if request.method == "POST":
        try:
            table = Place()
            table.name = request.POST['name']
            table.location = request.POST['location']
            table.description = request.POST['description']
            table.opening_hours = request.POST['opening_hours']
            table.closing_hours = request.POST['closing_hours']
            table.image = request.FILES['image']
            table.save()
            messages.success(request, 'เพิ่มข้อมูลสำเร็จ!')
            return redirect('/manage')
        except Exception as e:
            print(e)  # ให้แสดง error ใน console เพื่อดูว่ามีปัญหาอะไร
            messages.error(request, 'เพิ่มข้อมูลไม่สำเร็จ! กรุณาตรวจสอบข้อมูล')
    return render(request, 'add.html')

def edit(request, pk):
    place = get_object_or_404(Place, place_id=pk)

    if request.method == "POST":
        form = PlaceForm(request.POST, request.FILES, instance=place)
        if form.is_valid():
            form.save()
            messages.success(request, 'แก้ไขข้อมูลสำเร็จ!')
            return redirect('/manage')
    else:
        form = PlaceForm(instance=place)

    context = {"form": form, "place_data": place}
    return render(request, 'edit.html', context)

def delete_place(request,pk):
    table = Place.objects.get(place_id=pk)
    table.delete()
    messages.success(request, 'ลบข้อมูลสำเร็จ!')
    return redirect('/manage')

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pswd']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'เข้าสู่ระบบสำเร็จ!')
            return redirect('/')
        else:
            messages.error(request, 'เข้าสู่ระบบผิดพลาด. โปรดตรวจสอบข้อมูลของคุณอีกครั้ง.')
            pass
    return render(request, 'login.html')

def logout_view(request):
        logout(request)
        return render(request, 'login.html')

