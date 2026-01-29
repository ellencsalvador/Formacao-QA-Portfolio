from behave import given, when, then
from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Seu caminho de perfil (está correto)
CAMINHO_PERFIL_EDGE = r"C:\Users\ellen.salvador\AppData\Local\Microsoft\Edge\User Data\Default"

@given("que o WhatsApp Web está logado no navegador Edge")
def step_open_whatsapp(context):
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    options.add_argument(f"user-data-dir={CAMINHO_PERFIL_EDGE}")

    context.driver = Edge(options=options)
    context.driver.get("https://web.whatsapp.com")

    # Seu tempo de 60 segundos (está ótimo)
    print("ℹ️ Abrindo WhatsApp Web... Aguarde 60 segundos.")
    time.sleep(60)
    print("✔️ WhatsApp Web carregado.")


@when('eu enviar uma mensagem para o grupo "{nome_grupo}"')
def step_search_group_and_prepare(context, nome_grupo):
    try:
        print(f"Buscando pelo grupo: {nome_grupo}...")
        
        # =======================================================
        # ✅ LINHA 1 CORRIGIDA: (Trocamos 'div' por '*')
        # =======================================================
        caixa_pesquisa = context.driver.find_element(By.XPATH, "//*[@aria-label='Pesquisar ou começar uma nova conversa']")
        
        caixa_pesquisa.send_keys(nome_grupo)
        time.sleep(3)

        print("Clicando no grupo...")
        grupo = context.driver.find_element(By.XPATH, f"//span[@title='{nome_grupo}']")
        grupo.click()
        time.sleep(3)

    except Exception as e:
        print(f"❌ Erro ao tentar encontrar o grupo: {nome_grupo}")
        print(e)
        context.driver.quit()
        raise AssertionError("Grupo não encontrado. Verifique o nome.")


@then('a mensagem "{mensagem}" deve ser enviada com sucesso')
def step_send_message_and_verify(context, mensagem):
    try:
        print(f"Digitando a mensagem: {mensagem}")
        
        # =======================================================
        # ✅ LINHA 2 CORRIGIDA: (Trocamos 'div' por '*')
        # =======================================================
        caixa_mensagem = context.driver.find_element(By.XPATH, "//*[@aria-label='Digite uma mensagem']")
        
        caixa_mensagem.send_keys(mensagem)
        time.sleep(1)

        caixa_mensagem.send_keys(Keys.RETURN)
        print("✔️ Mensagem enviada!")
        
        time.sleep(5) 

    except Exception as e:
        print("❌ Erro ao tentar enviar a mensagem.")
        print(e)
        raise AssertionError("Não foi possível encontrar a caixa de mensagem.")

    finally:
        print("✅ Desafio concluído. Fechando o navegador.")
        context.driver.quit()