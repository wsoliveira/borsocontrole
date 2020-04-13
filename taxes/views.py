from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from decouple import config
from .models import bc_tax, bc_tax_negotiation
from .forms import TaxForm
from administrators.models import bc_admin_type_negotiation
# Create your views here.


def genericCalculates(type_negotiation, id_negotiation, gross_total_price, type_investiment):
    lst_taxes_names = bc_admin_type_negotiation.objects.filter(name=type_negotiation)
    sum_results = 0
    for name in lst_taxes_names:
        try:
            lst_taxs = bc_tax.objects.filter(bc_admin_type_negotiation=name, is_active=True, bc_admin_type_investiment__name=type_investiment)
        except ObjectDoesNotExist:
            lst_taxs = []

        for tax in lst_taxs:
            discounted_price = (float(gross_total_price) * (float(tax.value) / 100))
            bc_tax_negotiation.objects.update_or_create(
                bc_tax=tax,
                bc_negotiation=id_negotiation,
                defaults={
                    'discounted_price':float(discounted_price)
                }
            )
            sum_results += discounted_price

    return float(sum_results)

@login_required
def tax_list(request):
    name = request.GET.get("search", None)
    page = request.GET.get('page', 1)
    if name:
        tb_values = bc_tax.objects.filter(name__icontains=name)
    else:
        tb_values = bc_tax.objects.all()

    paginator = Paginator(tb_values, config('LIMIT_PAGINATION',default=15,cast=int))
    try:
        tb_values = paginator.page(page)
    except PageNotAnInteger:
        tb_values = paginator.page(1)
    except EmptyPage:
        tb_values = paginator.page(paginator.num_pages)

    return render(request, 'tax.html', {'tb_values': tb_values})

@login_required
def tax_new(request):
    form = TaxForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        is_active = False
        if request.POST.get('is_active') == "on":
            is_active = True
        tb_values = bc_tax.objects.create(
            name=request.POST.get('name'),
            value = request.POST.get('value'),
            description = request.POST.get('description'),
            is_active = is_active,
        )
        tb_values.save()
        return redirect('tax_list')

    return render(request, 'tax_form.html', {'form': form})

@login_required
def tax_update(request, id):
    tb_values = get_object_or_404(bc_tax, pk=id)
    form = TaxForm(request.POST or None, request.FILES or None, instance=tb_values)
    if form.is_valid():
        form.save()
        return redirect('tax_list')
    return render(request, 'tax_form.html', {'form': form})

@login_required
def tax_delete(request, id):
    tb_values = get_object_or_404(bc_tax, pk=id)
    if request.method == "POST":
        tb_values.delete()
        return redirect('tax_list')
    return render(request, 'tax_delete_confirm.html', {'tb_values': tb_values})

@login_required
def tax_negotiation_list(request, id_negotiation):
    tb_values = bc_tax_negotiation.objects.filter(bc_negotiation__id=id_negotiation)

    return render(request, 'tax_negotiation.html', {'tb_values': tb_values})