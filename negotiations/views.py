from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from decouple import config
from .models import bc_negotiation
from companies.models import bc_company_code
from investiments.models import bc_investiment
from .forms import NegotationForm
from taxes.views import genericCalculates
from administrators.models import bc_admin_type_investiment, bc_admin_type_negotiation
from taxes.models import bc_tax_negotiation
# Create your views here.

@login_required
def negotiation_list(request):
    name = request.GET.get("search", None)
    date_start = request.GET.get("date_start", None)
    date_end = request.GET.get("date_end", None)
    page = request.GET.get('page', 1)

    """
        Fiquei triste com essa quantidade de IF tentei concatenar os filtros, 
        usei funcao Q do Django, usei | (pipe) para conecatenar tambem, nada deu certo, fiquei sem ideias.        
    """
    if name and date_start and date_end:
        tb_values = bc_negotiation.objects.filter(bc_company_code__name__icontains=name,
                                                  date_negotiation__gte=date_start, date_negotiation__lte=date_end,
                                                  bc_user=request.user).order_by('date_negotiation')
    elif name and date_start:
        tb_values = bc_negotiation.objects.filter(bc_company_code__name__icontains=name, date_negotiation__gte=date_start,
                                                  bc_user=request.user).order_by('date_negotiation')
    elif name and date_end:
        tb_values = bc_negotiation.objects.filter(bc_company_code__name__icontains=name, bc_user=request.user,
                                                  date_negotiation__lte=date_end).order_by('date_negotiation')
    elif name:
        tb_values = bc_negotiation.objects.filter(bc_company_code__name__icontains=name,
                                                  bc_user=request.user).order_by('date_negotiation')
    elif date_start and date_end:
        tb_values = bc_negotiation.objects.filter(date_negotiation__gte=date_start, date_negotiation__lte=date_end,
                                                  bc_user=request.user).order_by('date_negotiation')
    elif date_start:
        tb_values = bc_negotiation.objects.filter(date_negotiation__gte=date_start, bc_user=request.user
                                                  ).order_by('date_negotiation')
    elif date_end:
        tb_values = bc_negotiation.objects.filter(date_negotiation__lte=date_end, bc_user=request.user
                                                  ).order_by('date_negotiation')
    else:
        tb_values = bc_negotiation.objects.filter(bc_user=request.user).order_by('date_negotiation')

    paginator = Paginator(tb_values, config('LIMIT_PAGINATION',default=10,cast=int))
    try:
        tb_values = paginator.page(page)
    except PageNotAnInteger:
        tb_values = paginator.page(1)
    except EmptyPage:
        tb_values = paginator.page(paginator.num_pages)

    return render(request, 'negotiation.html', {'tb_values': tb_values})

def calculaNegotiations(id_negotiation):
    tb_negotiation = bc_negotiation.objects.get(id=id_negotiation)
    type_negotiation = tb_negotiation.bc_admin_type_negotiation.name
    type_investiment = tb_negotiation.bc_admin_type_investiment.name
    brokerage_price = float(tb_negotiation.brokerage_price)
    v_gross_total_price = float(tb_negotiation.unit_price) * int(tb_negotiation.amount)  # mutiplicando com qtd comprada
    tax = genericCalculates(type_negotiation, tb_negotiation, v_gross_total_price,
                            type_investiment)  # somando com as taxas

    if type_negotiation.upper() == 'SELL':
        # venda calcula taxas+corretagem e subtrai do valor_liquido
        v_total_net_price = (v_gross_total_price - tax - brokerage_price)
        v_gross_total_price += brokerage_price
        tb_negotiation.gross_total_price = v_gross_total_price
        tb_negotiation.total_net_price = v_total_net_price
        tb_negotiation.average_price = (v_total_net_price / int(tb_negotiation.amount))
    elif type_negotiation.upper() == 'PURCHASE':
        # compra calcula taxas+corretagem e soma no valor_bruto que será o mesmo para valor liquido
        v_gross_total_price += tax
        tb_negotiation.gross_total_price = v_gross_total_price + brokerage_price  # save com add corretagem
        tb_negotiation.total_net_price = v_gross_total_price + brokerage_price  # save com add corretagem
        tb_negotiation.average_price = (v_gross_total_price + brokerage_price) / int(tb_negotiation.amount)

    tb_negotiation.save()
    return True

@login_required
def negotiation_new(request):
    form = NegotationForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        tb_values = bc_negotiation.objects.create(
            bc_admin_type_investiment=bc_admin_type_investiment.objects.get(id=request.POST.get('bc_admin_type_investiment')),
            bc_admin_type_negotiation=bc_admin_type_negotiation.objects.get(id=request.POST.get('bc_admin_type_negotiation')),
            date_negotiation = request.POST.get('date_negotiation'),
            amount = request.POST.get('amount'),
            unit_price = request.POST.get('unit_price'),
            brokerage_price = request.POST.get('brokerage_price'),
            bc_company_code = bc_company_code.objects.get(id=request.POST.get('bc_company_code')),
            bc_user = request.user,
            description = request.POST.get('description','n/d'),
        )
        tb_values.save()
        calculaNegotiations(
            tb_values.id,
        )
        return redirect('negotiation_list')

    return render(request, 'negotiation_form.html', {'form': form})

@login_required
def negotiation_update(request, id):
    tb_values = get_object_or_404(bc_negotiation, pk=id)
    form = NegotationForm(request.POST or None, request.FILES or None, instance=tb_values)
    if form.is_valid():
        tb_tax_negotiation = bc_tax_negotiation.objects.filter(bc_negotiation=tb_values)
        tb_tax_negotiation.delete()
        form.save()
        calculaNegotiations(
            tb_values.id,
        )
        return redirect('negotiation_list')
    return render(request, 'negotiation_form.html', {'form': form})

@login_required
def negotiation_delete(request, id):
    tb_values = get_object_or_404(bc_negotiation, pk=id)
    if request.method == "POST":
        tb_values.delete()
        ###Deletando da tabela investimento esse indice para ser recriado.
        bc_investiment.objects.filter(bc_user=request.user, bc_company_code=tb_values.bc_company_code).delete()
        return redirect('negotiation_list')
    return render(request, 'negotiation_delete_confirm.html', {'tb_values': tb_values})