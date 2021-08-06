import streamlit as st
import pandas as pd
#import numpy as np

st.set_page_config(page_title = 'FLAI APP - Aplicações de IA/DS', 
				   page_icon = 'iconeflai.png' ,
				   layout = 'wide', 
				   initial_sidebar_state = 'auto')

#dados = pd.read_csv("Planilha - APLICAÇÕES DS - Página1.csv")
dados = pd.read_excel("Planilha - APLICAÇÕES DS.xlsx")
#dados.drop(0, inplace = True) 
  
categorias = dados['CATEGORIA'].unique() 
 
paginas = ['Home', 'Aplicações por Área', 'Submeter Aplicação', 'Relatar um BUG', 'Sobre']

st.image('bannerflai.jpg', use_column_width = 'always')
 
pagina = st.sidebar.selectbox('Navegue por aqui', paginas)


#===============================================================================================================


if pagina == 'Home':
	'''
	#  Coleção FLAI de Aplicações de Inteligência Artificial e Data Science 📘
	'''
	st.image('imagem1.png', use_column_width = 'always')

	'A tecnologia hoje já está presente em praticamente todos os setores existentes. Podemos dizer o mesmo para ciência de dados, e para facilitar sua busca por suas inúmeras aplicações, nós da equipe FLAI desenvolvemos esse web app para que você consiga encontrar com uma maior facilidade alguma aplicação em uma área de seu interesse.'
	
	'Nosso principal objetivo com esse web app é auxiliar a comunidade interessada na área de Ciência de Dados a entender o quão vastos são as oportunidades de emprego.'

	'Vale salientar que além destas aplicações que nós temos aqui, existem mais inúmeras aplicações em inúmeras áreas. Com isso, deixamos em aberto uma ultima aba chamada "Suas Aplicações", no qual VOCÊ, usuário deste web app, poderá compartilhar aplicações das quais você sentiu falta por aqui.'

	st.markdown('---')

	st.markdown('## Neste web app, temos **' + str(len(dados)) + '** aplicações distribuidas em **' + str(len(categorias)) + '** categorias.')
	
	col1, col2, col3, col4 = st.beta_columns(4) 
	
	for i in range(len(categorias)): 
		if i < 5:
		 	col1.subheader(categorias[i])
		elif i < 10:
		 	col2.subheader(categorias[i])
		elif i < 15:
		 	col3.subheader(categorias[i])
		else:
		 	col4.subheader(categorias[i])

	st.markdown('---')

	'''
	E para facilitar a sua navegação, você pode selecionar a área do seu interesse apenas selecionando alguma das áreas na aba a esquerda.
	'''
	g = dados['CATEGORIA'].value_counts().plot(kind = 'barh')
	st.pyplot(g.figure, width = '200')

#============================================================================================

 

if pagina == 'Aplicações por Área':

	st.sidebar.markdown('---')
	categoria = st.sidebar.selectbox('Selecione a área do seu interesse', categorias)


	dados0 = dados[dados['CATEGORIA'] == categoria] 
 

	st.markdown("# Aplicações em {}".format(categoria))
	st.markdown("## {} aplicações".format(str(dados0.shape[0])))
	 

	for i in range(dados0.shape[0]): 
		st.markdown('---')
	 
		col1, col3, col2 = st.beta_columns([10,1,20])
 
		aplic  = dados0.iloc[i, 2]
		imagem = dados0.iloc[i, 5]
		resumo = dados0.iloc[i, 3] 
		links  = dados0.iloc[i, 4]  

		col1.image(imagem, use_column_width = 'always') 

		col2.markdown('# **{}. {}**'.format(i+1, aplic)) 
		col2.markdown(resumo + " **[Referência]({})**".format(links)) 


#============================================================================================

 
	 
if pagina == 'Submeter Aplicação': 

	st.title("Nos ajude com sua sugestão!")

	st.write('Além destas aplicações de Inteligência Artificial, nós da FLAI sabemos que ainda existem muitas outras áreas de atuação das quais as mesmas ainda não adicionameos neste webapp.')

	st.write('Sabendo disso nós deixamos uma aba especialmente para as pessoas que desejarem nos ajudar com áreas de atuação que não foram postas aqui.')

	st.write('Para nos auxiliar a adicionarmos mais áreas de atuação, temos o link abaixo para sua interação (via GOOGLE FORMS)')

	'''
	### [Clique aqui para submeter uma aplicação](https://forms.gle/Z7GEwrsZTYfLqoNJ7)
	'''

	st.write("")

	st.write('Agradecemos pelo seu apoio! 😉')

 


#============================================================================================

 
if pagina == 'Relatar um BUG':
	'''
	### Em Construção
	'''


#============================================================================================


if pagina == 'Sobre':
	'''
	## Versão 0.1.0
	'''

