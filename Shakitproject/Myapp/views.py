# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from .forms import CustomerForm

# แสดงข้อมูลลูกค้าทั้งหมด
def main(request):
    # รับค่าประเภทลูกค้า
    customer_type = request.GET.get('customer_type', '')
    
    # ถ้ามีการเลือกประเภทลูกค้า, ให้กรองข้อมูลจากฐานข้อมูล
    if customer_type:
        customers = Customer.objects.filter(customer_type=customer_type)
    else:
        customers = Customer.objects.all()  # ถ้าไม่เลือกประเภทลูกค้า, ให้แสดงทั้งหมด
    
    return render(request, 'main.html', {'customers': customers, 'customer_type': customer_type})

# เพิ่มข้อมูลลูกค้าใหม่
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')  # กลับไปยังหน้า customer_list หลังบันทึกข้อมูล
    else:
        form = CustomerForm()
    return render(request, 'add_edit_customer.html', {'form': form})

# แก้ไขข้อมูลลูกค้า
def edit_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('main')  # กลับไปยังหน้า customer_list หลังจากแก้ไขข้อมูล
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'add_edit_customer.html', {'form': form})

# ลบข้อมูลลูกค้า
def delete_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    return redirect('main')  # หลังจากลบข้อมูลแล้วไปยังหน้ารายการลูกค้า
