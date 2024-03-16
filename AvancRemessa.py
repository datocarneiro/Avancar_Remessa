import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

while True:
        # Definindo a função para esperar até que um elemento esteja visível
    def esperar_elemento_visivel(driver, locator):
        return WebDriverWait(driver, 20).until(EC.visibility_of_element_located(locator))

    # Configurando o webdriver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    try:
        # Acessando a página de login
        driver.get("https://amplo.eship.com.br/?HOME")

        # Preenchendo as credenciais
        esperar_elemento_visivel(driver, (By.XPATH, '//*[@id="login"]')).send_keys("dashboard3") # seu login
        driver.find_element(By.XPATH, '//*[@id="senha"]').send_keys("12341234") # sua senha
        driver.find_element(By.XPATH, '//*[@id="Entrar"]/span').click()

        # Aguardando o carregamento da página principal
        esperar_elemento_visivel(driver, (By.XPATH, '//*[@id="FormListarRemessas"]/ul/li[2]/div/a[3]/div'))

        # Abrindo visualização para lista de 100
        driver.find_element(By.XPATH, '//*[@id="FormListarRemessas"]/ul/li[2]/div/a[3]/div').click()
        time.sleep(15)

        # Etapa conferidas
        esperar_elemento_visivel(driver, (By.XPATH, '//*[@id="formulario"]/div[1]/div[1]/ul/li/div[1]')).click() # filtro
        esperar_elemento_visivel(driver, (By.XPATH, '//*[@id="formulario"]/div[1]/div[1]/ul/li/div[2]/div/div[1]/div/div[2]/div/fieldset[1]/div/div/div[3]/div[2]/label')).click() # conferido
        esperar_elemento_visivel(driver, (By.XPATH, '//*[@id="formulario"]/div[1]/div[1]/ul/li/div[2]/div/div[1]/div/div[2]/div/fieldset[1]/div/div/div[3]/div[3]/label')).click() # Ag doc

        # Clicar no botão 'Filtrar'
        filtrar_button = esperar_elemento_visivel(driver, (By.XPATH, '//*[@id="cFuncaoListarRemessas_Filtrar"]'))
        filtrar_button.click()
        time.sleep(10)

        # Verificar se o checkbox está presente antes de clicar nele
        checkboxes = driver.find_elements(By.XPATH, '//*[@id="FormListarRemessas"]/table/thead/tr/th[1]/div/label')
        if checkboxes:
            # Selecionar todos os checkboxes
            for checkbox in checkboxes:
                checkbox.click()

            # Clicar no botão 'Avançar'
            avancar_button = esperar_elemento_visivel(driver, (By.XPATH, '//*[@id="cFuncaoListarRemessas_Avançar"]/span'))
            avancar_button.click()

            # Clicar no botão 'Confirmar'
            confirmar_button = esperar_elemento_visivel(driver, (By.XPATH, '//*[@id="cFuncaoListarRemessas_CheckAvancarRemessa_Confirmar"]/span'))
            confirmar_button.click()

            print('IF - fechando navegador , esperando 10 seg e reniciar tarefa ....')
            time.sleep(10)  # Aguardar um tempo antes de recomeçar o loop
            driver.quit()

        else:
            print("Nenhum checkbox encontrado. fechar navegador e reiniciar em 10 seg...")
            driver.quit()
    
    except NoSuchElementException as e:
        print(f"Exceção: {e}")
        pass  # Se ocorrer uma exceção, ignore e continue