import streamlit as st

st.set_page_config(
    page_title='Dashboard',
    page_icon=':bar_chart:',
    layout='wide'
)
st.sidebar.image('Logo.png')
st.sidebar.title('Menu')

menu = st.sidebar.selectbox(' ', ['Selecionar', 'Login', 'Processo produtivo', 'Dashboard'])

# Opção Login
if menu == 'Login':
    st.title('Login')

    user_name = st.text_input('Usuário')
    password = st.text_input('Password', type='password')

    usuario = st.selectbox('Selecionar usuário', ['Selecionar', 'Usuário 1', 'Usuário 2', 'Usuário 3', 'Usuário 4', 'Usuário 5'])

    st.checkbox('Login')























# Opcão Processo Produtivo
elif menu == 'Processo produtivo':
    st.title('Processo produtivo')

# Opção Dashboard
elif menu == 'Dashboard':
    st.title('Dashboard')
