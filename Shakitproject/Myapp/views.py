# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from .forms import CustomerForm

# แสดงข้อมูลลูกค้าทั้งหมด
def main(request):
    # เริ่มต้นด้วยการดึงข้อมูลลูกค้าทั้งหมด
    customers = Customer.objects.all()
    
    # ตรวจสอบการกรองตามประเภทลูกค้า
    customer_type_filter = request.GET.get('customer_type')
    if customer_type_filter and customer_type_filter != '-- ทั้งหมด --':
        customers = customers.filter(customer_type=customer_type_filter)
    
    # ตรวจสอบการกรองตามอำเภอ
    district_filter = request.GET.get('district')
    if district_filter and district_filter != '-- อำเภอ --':
        customers = customers.filter(address__district=district_filter)
    
    return render(request, 'main.html', {
        'customers': customers,
        'selected_customer_type': customer_type_filter or '-- ทั้งหมด --',
        'selected_district': district_filter or '-- อำเภอ --'
    })

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

# ดูรายละเอียดบิล
def bill(request):
    customers = Customer.objects.all()
    return render(request,'bill.html', {'customers': customers})

