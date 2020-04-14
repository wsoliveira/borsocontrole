#Projeto BORSO CONTROLO
**Tradução do Nome De Esperanto para Português:** Controla Bolsa :-)
-   **Criador:** Welligton S. de Oliveira
-   **Email:** ws.oliveira@gmail.com
-   **Data:** 31/03/2020
-   **Colaboradores:**
-   **Site Example:** https://borsocontrolo.herokuapp.com/

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
        
    - Existe teste criado para app companies
        - $ python manage.py test        

**Versões:**
    - 13/04/2020 - v1.0.0
    
## Ajuda

Para relatar bugs ou fazer perguntas utilize o [Issues](https://github.com/wsoliveira/borsocontrolo/issues) ou via email ws.oliveira@gmail.com

Como este é um projeto em desenvolvimento, qualquer feedback será bem-vindo.    