import collections
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from decouple import config
from .models import bc_investiment
from .forms import bc_investiment
from negotiations.models import bc_negotiation
from administrators.models import bc_admin_type_investiment


def resumeNegotiations(request):
    dic_relatorio = {}
    lst_types = bc_admin_type_investiment.objects.filter(is_active=True)
    dic_resume = {}
    for type in lst_types:
        tb_negotiations = bc_negotiation.objects.filter(bc_user=request.user, bc_admin_type_investiment=type)
        for tb in tb_negotiations:
            if tb.bc_company_code.name not in dic_resume:
                dic_resume[tb.bc_company_code.name] = {
                    "total_net_price_buying": 0.0,
                    "total_net_price_selling": 0.0,
                    "amount_buying": 0,
                    "amount_selling": 0,
                    "type": tb.bc_admin_type_investiment.name,
                    "company_code": tb.bc_company_code,
                    "profitability": 0
                }
            if tb.bc_admin_type_negotiation.name.upper() == 'PURCHASE':
                dic_resume[tb.bc_company_code.name]['total_net_price_buying'] += float(tb.total_net_price)
                dic_resume[tb.bc_company_code.name]['amount_buying'] += tb.amount
            else:
                dic_resume[tb.bc_company_code.name]['total_net_price_selling'] += float(tb.total_net_price)
                dic_resume[tb.bc_company_code.name]['amount_selling'] += tb.amount

    total = 0 #Variavel criada apenas para o grafico de consolidado
    for company_code_name in dic_resume:
        amount = 1
        if dic_resume[company_code_name]['type'].upper() in ('STOCK'):
            amount = (dic_resume[company_code_name]['amount_buying']-dic_resume[company_code_name]['amount_selling'])
        total_net_price = float(
            dic_resume[company_code_name]['total_net_price_buying']-dic_resume[company_code_name]['total_net_price_selling']
        )
        total += total_net_price

        bc_investiment.objects.update_or_create(
            bc_company_code=dic_resume[company_code_name]['company_code'],
            bc_user=request.user,
            defaults={
                'amount':amount,
                'total_net_price':total_net_price,
                'average_price': float(
                    dic_resume[company_code_name]['total_net_price_buying'] / dic_resume[company_code_name][
                        'amount_buying']
                ),
            }
        )
        if dic_resume[company_code_name]['type'] not in dic_relatorio:
            dic_relatorio[dic_resume[company_code_name]['type']] = {
                'total':round(total_net_price, 2)
            }
        else:
            dic_relatorio[dic_resume[company_code_name]['type']]['total'] += float(total_net_price)

    for key in dic_relatorio:
        consolidated = (dic_relatorio[key]['total']/total)*100
        dic_relatorio[key]['consolidated'] = round(consolidated)

    return dic_relatorio

@login_required
def investiment_list(request):
    dic_relatorio = resumeNegotiations(request)
    name = request.GET.get("search", None)
    page = request.GET.get('page', 1)
    if name:
        tb_values = bc_investiment.objects.filter(bc_company_code__name__icontains=name, bc_user=request.user).order_by("bc_company_code__name")
    else:
        tb_values = bc_investiment.objects.filter(bc_user=request.user).order_by("bc_company_code__name")

    paginator = Paginator(tb_values, config('LIMIT_PAGINATION',default=15,cast=int))
    try:
        tb_values = paginator.page(page)
    except PageNotAnInteger:
        tb_values = paginator.page(1)
    except EmptyPage:
        tb_values = paginator.page(paginator.num_pages)

    return render(request, 'investiment.html', {'tb_values': tb_values, 'tb_consolidated': dic_relatorio})

@login_required
def investiment_delete(request, id):
    tb_values = get_object_or_404(bc_investiment, pk=id)
    if request.method == "POST":
        tb_values.is_active=False
        tb_values.save()
        return redirect('investiment_list')
    return render(request, 'investiment_delete_confirm.html', {'tb_values': tb_values})