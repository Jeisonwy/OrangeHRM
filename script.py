import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar el navegador
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

try:
    # Inicio de sesión
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    wait = WebDriverWait(driver, 10)

    username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    username.send_keys("Admin")
    password.send_keys("admin123")
    login_button.click()

    # Navegar a Recruitment
    recruitment_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Recruitment']")))
    recruitment_tab.click()

    # Add Candidate
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/addCandidate")

    # Llenar los campos
    first_name_field = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
    first_name_field.send_keys("USUARIO 1")
    last_name_field = driver.find_element(By.NAME, "lastName")
    last_name_field.send_keys("APELLIDO")
    email_field = driver.find_element(By.XPATH, "//input[@placeholder='Type here']")
    email_field.send_keys("jeisongg02@gmail.com")

    # Esperar y hacer clic en el botón "Save"
    save_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(@class, 'oxd-button--secondary')]")
    ))
    driver.execute_script("arguments[0].scrollIntoView(true);", save_button)
    save_button.click()
    time.sleep(3)

except Exception as e:
    print(f"Error en el flujo: {e}")

finally:
    driver.quit()
