from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
from main import get_db

BASE_URL = "https://formulario-contato-m8p8.onrender.com/"

@given('que o site do formulario esta acessivel')
def step_open_site(context):
    d = context.driver
    print("\n\nAbrindo página: ", BASE_URL)
    d.get(BASE_URL)
    try:
        WebDriverWait(d, 15).until(EC.presence_of_element_located((By.NAME, "nome")))
        print("Página aberta com sucesso!")
    except TimeoutException:
        print("Timeout esperando campo 'nome'. URL atual: ", d.current_url)
        raise

@when('eu preencho o formulario com nome, email e telefone validos')
def preencher_form(context):
    d = context.driver
    d.find_element(By.NAME, "nome").clear()
    d.find_element(By.NAME, "nome").send_keys("Ellen Salvador")
    d.find_element(By.NAME, "email").clear()
    d.find_element(By.NAME, "email").send_keys("ellenc_salvador@yahoo.com.br")
    d.find_element(By.NAME, "telefone").clear()
    d.find_element(By.NAME, "telefone").send_keys("11979918822")

    try:
        Select(d.find_element(By.NAME, "cidade")).select_by_visible_text("Ilhabela")
    except Exception:
        try:
            el = d.find_element(By.NAME, "cidade")
            el.clear(); el.send_keys("Ilhabela")
        except Exception:
            pass

    try:
        bairro_input = d.find_element(By.NAME, "bairro")
        bairro_input.clear()
        bairro_input.send_keys("Barra Velha")
        WebDriverWait(d, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "autocomplete-list div")))
        itens = d.find_elements(By.CSS_SELECTOR, "autocomplete-list div")
        for item in itens:
            if item.text == "Barra Velha":
                item.click()
                break
    except Exception:
        try:
            Select(d.find_element(By.NAME, "bairro")).select_by_visible_text("Barra Velha")
        except Exception:
            print("Não foi possível selecionar o bairro via autocomplete ou select.")

    try:
        checkboxes = d.find_elements(By.NAME, "escolaridade")
        for cb in checkboxes:
            if cb.get_attribute("value") == "superior":
                if not cb.is_selected():
                    cb.click()
                break
    except Exception:
        pass

    d.find_element(By.NAME, "mensagem").clear()
    d.find_element(By.NAME, "mensagem").send_keys("Gosto muito de aprender com vocês.")
    time.sleep(1)

@when('clico para enviar o formulario')
@then('clico para enviar o formulario')
def clicar_enviar(context):
    d = context.driver
    clicked = False
    try:
        btn = d.find_element(By.CSS_SELECTOR, "button[type='submit'], button.btn-primary")
        btn.click()
        clicked = True
    except NoSuchElementException:
        try:
            d.execute_script("document.querySelector('form').submit();")
            clicked = True
        except Exception:
            pass

    if not clicked:
        raise AssertionError("Não foi possível clicar no botão de envio do formulário.")

    try:
        WebDriverWait(d, 12).until(lambda w: "?ok=1" in w.current_url or "ok=1" in w.current_url)
        print("Formulário enviado com sucesso!")
    except TimeoutException:
        print("Timeout esperando confirmação de envio. URL atual: ", d.current_url)
        raise

@then('vejo a confirmacao de envio do formulario')
def validar_msg(context):
    d = context.driver
    try:
        WebDriverWait(d, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-success, .mensagem-sucesso")))
        print("Mensagem de sucesso encontrada.")
        return
    except TimeoutException:
        print("Timeout esperando mensagem de sucesso. URL atual: ", d.current_url)
        raise AssertionError("Mensagem de sucesso não encontrada após envio do formulário.")