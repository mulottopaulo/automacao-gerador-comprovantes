from fpdf import FPDF
import pandas as pd

base_dados = pd.read_csv('base_dados_funcionarios.csv')
for (indice, funcionario) in base_dados.iterrows():
  # Informações Recebedor -> Da base de dados
  recebedor_nome = funcionario.nome
  recebedor_cpf = funcionario.cpf
  recebedor_salario = funcionario.salario

  # Informações Pagador -> Fixas
  pagador_nome = 'Marcelo e Sara Transportes Ltda'
  pagador_cnpj = '01.336.733/0001-64'

  meio_pagamento = 'depósito bancário'

  # Modelo básico do recibo
  texto_recibo = f'Pelo presente, eu {recebedor_nome}, inscrito no CPF \
  sob nº {recebedor_cpf}, declaro que RECEBI na data de hoje, o valor de \
  R$ {recebedor_salario:.2f} , por meio de {meio_pagamento}, de {pagador_nome} \
  , inscrito no CNPJ sob nº {pagador_cnpj}, referente a criação \
  do gerador de recibos.'

  # Crição do PDF
  pdf = FPDF()
  pdf.add_page()
  
  pdf.set_font('times', '', 14)

  pdf.ln(20)
  
  pdf.multi_cell(180, 10, texto_recibo, align="C")
  pdf.ln(20)

  pdf.cell(180, 10, "Sendo expressão de verdade e sem qualquer coação, firmo o presente.", align="C")
  pdf.ln(40)

  pdf.cell(180, 10, "_______, __ de ______ de ____", align="C")
  pdf.ln(80)

  pdf.cell(180, 10, "________________________________", align="C")
  pdf.ln()
  pdf.cell(180, 10, recebedor_nome, align="C")

  pdf.output(f"recibos/recibo_{recebedor_nome}.pdf")
