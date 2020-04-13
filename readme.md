#Projeto BORSO CONTROLO
**Tradução do Nome De Esperanto para Português:** Controla Bolsa :-)
-   **Criador:** Welligton S. de Oliveira
-   **Email:** ws.oliveira@gmail.com
-   **Data:** 31/03/2020
-   **Colaboradores:**

**De onde surgiu a ideia !**
- Para fazer declaração do imposto de renda das ações da Bolsa de valores, você precisa juntar um punhado 
de informação:
    -   Mês da Compra e Venda da Ação;
    -   Valor Pago na compra e Valor na Venda;
    -   O que foi recebido de Dividendos e Juros Sobre Capital por empresa;
    -   Calcular Preço Médio PM=((soma(valor_bruto))/qtd_ação_comprada) por empresa;
    -   Descontar os impostos já pagos, por exemplo:
        -   Emolumentos
        -   Em toda venda a corretora já recolhe 0.005% do valor total, ou seja, se você vai pagar 20% de IR na
         realidade você precisa pagar 19.095%.
        - Taxa de Corretagem;
        - etc;

**Instalação**
-   Requerimento:
    - => Python3.6
-   Instalação:
    - Criar pasta do projeto:
        -   $ mkdir ~/ProjetoBorsoControlo
        -   $ cd ~/ProjetoBorsoControlo
    - Baixar projeto do git:
        -   $ git clone https://github.com/wsoliveira/borsocontrolo.git
    - Crie virtual env e ative:
        -   $ virtualenv -p python3 .vEnv
        -   $ . .vEnv/bin/activate
        
    - Instale os pacotes:
        -   $ pip install -r requirements-dev.txt
       
    - Crie as tabelas do projeto:
        -   $ python manage.py migrate

    - Crie usuário:
        -   $ python manage.py createsuperuser
        
    - Rode a Carga de dados inicial:
        -   $ python manage.py loaddata ./static/fixtures/initial_data.json

    - Rode projeto:        
        -   $ python manage.py runserver        


    
    

**Colaborações:**
- Melhorias nos templates (css, html, forms, etc);
- Tela de cadastro de usuário, usando padrão de usuário do django;
    - https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/
    - Precisa criar form para criação de novos usuários;
- Implantação de um mecanismo de tradução (Português, Inglês), pesquisar em:
    https://docs.djangoproject.com/en/3.0/topics/i18n/translation/
    - Cheguei a fazer alguns testes no sector.html, mas não finalizei;
- Encontrar uma API que retorne cotação da bovespa e atualizar em alguma tabela para ter um relatório de rentabilidade
 do que o usuário contem;
- Talvez criar um mecanismo de alarmes, por exemplo:
    -   Se é vendido mais que R$ 20k no mês de ação você precisa gerar um DARF para pagar IR, esse pode
    ser um alarme interessante.
    -   DayTrade tambem tem que ser gerado DARF;
- Modulo para carregar todas negociacoes no app (negotiations) atráves de import de um arquivo .csv;
- Criação de um dashbord gráfico do relatório "Consolidated":
    - Graficos pizza:
- Revisão/Continuação no testes unitários:
    - Foi criado um teste unitário para 'sector':
        - No '/companies/tests.py'
- Na tela Investiments ou Negotiations criar um relatório/filtro por mês ou range de datas;
    - Essa visão vai ajudar no lançamento do imposto de renda e na geração dos valores para DARF mensal;