from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from decouple import config
from .models import bc_sector, bc_company_code, bc_company
from .forms import SectorForm, CompanyForm, CompanyCodeForm
# Create your views here.

@login_required
def sector_list(request):
    name = request.GET.get("search", None)
    page = request.GET.get('page', 1)
    if name:
        tb_values = bc_sector.objects.filter(name__icontains=name)
    else:
        tb_values = bc_sector.objects.all().order_by('name')

    paginator = Paginator(tb_values, config('LIMIT_PAGINATION',default=15,cast=int))
    try:
        tb_values = paginator.page(page)
    except PageNotAnInteger:
        tb_values = paginator.page(1)
    except EmptyPage:
        tb_values = paginator.page(paginator.num_pages)

    return render(request, 'sector.html', {'tb_values': tb_values})

@login_required
def sector_new(request):
    form = SectorForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('sector_list')

    return render(request, 'sector_form.html', {'form': form})

@login_required
def sector_update(request, id):
    tb_values = get_object_or_404(bc_sector, pk=id)
    form = SectorForm(request.POST or None, request.FILES or None, instance=tb_values)
    if form.is_valid():
        form.save()
        return redirect('sector_list')
    return render(request, 'sector_form.html', {'form': form})

@login_required
def sector_delete(request, id):
    tb_values = get_object_or_404(bc_sector, pk=id)
    if request.method == "POST":
        tb_values.is_active=False
        tb_values.save()
        return redirect('sector_list')
    return render(request, 'sector_delete_confirm.html', {'tb_values': tb_values})


@login_required
def company_list(request):
    name = request.GET.get("search", None)
    page = request.GET.get('page', 1)
    if name:
        tb_values = bc_company.objects.filter(name__icontains=name)
    else:
        tb_values = bc_company.objects.all().order_by('name')

    paginator = Paginator(tb_values, config('LIMIT_PAGINATION',default=15,cast=int))
    try:
        tb_values = paginator.page(page)
    except PageNotAnInteger:
        tb_values = paginator.page(1)
    except EmptyPage:
        tb_values = paginator.page(paginator.num_pages)

    return render(request, 'company.html', {'tb_values': tb_values})

@login_required
def company_new(request):
    form = CompanyForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('company_list')

    return render(request, 'company_form.html', {'form': form})

@login_required
def company_update(request, id):
    tb_values = get_object_or_404(bc_company, pk=id)
    form = CompanyForm(request.POST or None, request.FILES or None, instance=tb_values)
    if form.is_valid():
        form.save()
        return redirect('company_list')
    return render(request, 'company_form.html', {'form': form})

@login_required
def company_delete(request, id):
    tb_values = get_object_or_404(bc_company, pk=id)
    if request.method == "POST":
        tb_values.is_active = False
        tb_values.save()
        return redirect('company_list')
    return render(request, 'company_delete_confirm.html', {'tb_values': tb_values})


@login_required
def company_code_list(request):
    name = request.GET.get("search", None)
    page = request.GET.get('page', 1)
    if name:
        tb_values = bc_company_code.objects.filter(name__icontains=name)
    else:
        tb_values = bc_company_code.objects.all().order_by('name')

    paginator = Paginator(tb_values, config('LIMIT_PAGINATION',default=15,cast=int))
    try:
        tb_values = paginator.page(page)
    except PageNotAnInteger:
        tb_values = paginator.page(1)
    except EmptyPage:
        tb_values = paginator.page(paginator.num_pages)

    return render(request, 'company_code.html', {'tb_values': tb_values})

@login_required
def company_code_new(request):
    form = CompanyCodeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('company_code_list')

    return render(request, 'company_code_form.html', {'form': form})

@login_required
def company_code_update(request, id):
    tb_values = get_object_or_404(bc_company_code, pk=id)
    form = CompanyCodeForm(request.POST or None, request.FILES or None, instance=tb_values)
    if form.is_valid():
        form.save()
        return redirect('company_code_list')
    return render(request, 'company_code_form.html', {'form': form})

@login_required
def company_code_delete(request, id):
    tb_values = get_object_or_404(bc_company_code, pk=id)
    if request.method == "POST":
        tb_values.is_active=False
        tb_values.save()
        return redirect('company_code_list')
    return render(request, 'company_code_delete_confirm.html', {'tb_values': tb_values})