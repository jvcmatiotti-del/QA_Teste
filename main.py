from playwright.sync_api import sync_playwright
import time

with sync_playwright() as pw:
    navegador = pw.chromium.launch(headless=False)
    
    pagina = navegador.new_page()
    pagina.goto("https://www.tmb.com.br/")

    link = pagina.get_by_role("link", name="Aluno", exact=True)

    # Aguarda a nova página/popup abrir
    with pagina.context.expect_page() as nova_pagina:
        for link in link.all():
            print(link.inner_text())
            link.click()
    
    # Pega a página aberta
    pagina_login = nova_pagina.value
    pagina_login.wait_for_load_state()
    time.sleep(2)
    
    # Clica no campo de CPF - tenta diferentes seletores 
    try:
        campo_cpf = pagina_login.locator("input[type='text']").first
        campo_cpf.click()
        time.sleep(0.5)
        campo_cpf.type("000.000.000-03", delay=100)
        print("CPF preenchido com sucesso")
    except Exception as e:
        print(f"Erro ao preencher CPF: {e}")
    
    # Clica no campo de senha
    try:
        time.sleep(0.5)
        campo_senha = pagina_login.locator("input[type='password']").first
        campo_senha.click()
        time.sleep(0.5)
        campo_senha.type("password", delay=100)
        print("Senha preenchida com sucesso")
    except Exception as e:
        print(f"Erro ao preencher senha: {e}")