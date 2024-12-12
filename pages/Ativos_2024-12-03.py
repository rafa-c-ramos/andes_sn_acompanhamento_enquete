#################### Bibliotecas e Módulos ####################
# Fazer os imports necessários
import pandas as pd
import plotly.express as px
import streamlit as st

#################### Configurações da página do Streamlit ####################
st.set_page_config(page_title='Relatório de 03/12/2024', layout='wide', page_icon='📊')

#################### Título da página do Streamlit ####################
st.markdown('# Relatório de Respostas - 03/12/2024')

#################### Leitura e Tratamento dos Dados ####################
# Ler os dados originais
grafico_ativos_totais_df = pd.read_csv('grafico_ativos_totais_03_12.csv')

# Filtrar as respostas completas
grafico_ativos_completas_df = pd.read_csv('grafico_ativos_completas_03_12.csv')

# Filtrar as respostas incompletas
grafico_ativos_incompletas_df = pd.read_csv('grafico_ativos_incompletas_03_12.csv')

#################### Layout do Streamlit ####################        
# Criar e nomear as tabs (abas) 
tab_1, tab_2, tab_3, tab_4 = st.tabs(['Métricas', 'Respostas Totais', 'Respostas Completas', 'Respostas Incompletas'])

# Preencher a tab 1 (Relatório Geral)
with tab_1:
        # Criar as métricas gerais
        with st.container():
                st.title('Métricas Gerais')
                col_1, col_2, col_3, col_4 = st.columns(4, gap='large')
                
                # Criar a métrica de restaurantes registrados
                with col_1:
                        col_1.metric('Respostas Totais:', 3248)
                        
                # Criar a métrica de países registrados
                with col_2:
                        col_1.metric('Respostas Completas:', 2068)
                        
                # Criar a métrica de cidades registrados
                with col_3:
                        col_1.metric('Respostas Incompletas:', 1180)
                        
                # Criar a métrica do total de avaliações feitas
                with col_4:
                        col_1.metric('Instituições de Ensino Citadas:', 138)
                        
        # Criar as métricas semenais
        with st.container():
                st.title('Crescimento Semanal (26/11/2024 a 03/12/2024)')
                col_1, col_2, col_3, col_4 = st.columns(4, gap='large')
                
                # Criar a métrica de restaurantes registrados
                with col_1:
                        col_1.metric('Respostas Totais:', 409)
                        
                # Criar a métrica de países registrados
                with col_2:
                        col_1.metric('Respostas Completas:', 258)
                        
                # Criar a métrica de cidades registrados
                with col_3:
                        col_1.metric('Respostas Incompletas:', 151)
                        
                # Criar a métrica do total de avaliações feitas
                with col_4:
                        col_1.metric('Instituições de Ensino Citadas:', 3)
                        
# Preencher a tab 2 (Respostas Totais)
with tab_2:
    # Fazer o gráfico de barras 
    fig = px.bar(grafico_ativos_totais_df, x='uf_instituicao', y='contagem', color='instituicao',
                labels = {'uf_instituicao':'UF', 'contagem':'Respostas totais',
                        'instituicao':'Instituição de ensino'},
                title='Respostas Totais por UF e Instituição de Ensino (03/12/2024) - Servidores e Aposentados em Atividade')
    fig.update_yaxes(tick0=0, dtick=20)
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

    # Mostrar a tabela de respostas
    st.title('Tabela de Respostas Totais')
    tabela_ativos_totais_df = pd.read_csv('tabela_ativos_totais_03_12.csv')
    tabela_ativos_totais_df.drop(columns=tabela_ativos_totais_df.columns[0], axis=1, inplace=True)
    st.dataframe(tabela_ativos_totais_df, use_container_width=True)
    
# Preencher a tab 3 (Respostas Completas)
with tab_3:
    # Fazer o gráfico de barras 
    fig = px.bar(grafico_ativos_completas_df, x='uf_instituicao', y='contagem', color='instituicao',
                labels = {'uf_instituicao':'UF', 'contagem':'Respostas completas',
                        'instituicao':'Instituição de ensino'},
                title='Respostas Completas por UF e Instituição de Ensino (03/12/2024) - Servidores e Aposentados em Atividade')
    fig.update_yaxes(tick0=0, dtick=20)
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
    
    # Mostrar a tabela de respostas
    st.title('Tabela de Respostas Completas')
    tabela_ativos_completas_df = pd.read_csv('tabela_ativos_completas_03_12.csv')
    tabela_ativos_completas_df.drop(columns=tabela_ativos_completas_df.columns[0], axis=1, inplace=True)
    st.dataframe(tabela_ativos_completas_df, use_container_width=True) 
    
# Preencher a tab 4 (Respostas Incompletas)
with tab_4:
    # Fazer o gráfico de barras 
    fig = px.bar(grafico_ativos_incompletas_df, x='uf_instituicao', y='contagem', color='instituicao',
                labels = {'uf_instituicao':'UF', 'contagem':'Respostas incompletas',
                        'instituicao':'Instituição de ensino'},
                title='Respostas Incompletas por UF e Instituição de Ensino (03/12/2024) - Servidores e Aposentados em Atividade')
    fig.update_yaxes(tick0=0, dtick=20)
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
    
    # Mostrar a tabela de respostas
    st.title('Tabela de Respostas Incompletas')
    tabela_ativos_incompletas_df = pd.read_csv('tabela_ativos_incompletas_03_12.csv')
    tabela_ativos_incompletas_df.drop(columns=tabela_ativos_incompletas_df.columns[0], axis=1, inplace=True)
    st.dataframe(tabela_ativos_incompletas_df, use_container_width=True) 