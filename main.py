from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Setup Chrome options
chrome_Options = Options()
chrome_Options.add_argument("--disable-search-engine-choice-screen")

# Set up the service and driver
service = Service("chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(options=chrome_Options, service=service)

# Open the demo site
driver.get('https://demoqa.com/login')

# Wait for username and password fields, then log in
username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
login_button = driver.find_element(By.ID, 'login')

# Enter credentials and log in
username_field.send_keys('pythonstudent')
password_field.send_keys('PythonStudent123$')
driver.execute_script("arguments[0].click();", login_button)

# Open the form section
element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')))
element.click()

# Navigate to the form area
form_btn = driver.find_element(By.XPATH, '//*[@id="item-0"]')
driver.execute_script("arguments[0].click();", form_btn)

# Fill the form fields
FullName = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.ID, "userName")))
FullName.send_keys("HUba LUBA")

USerEmail = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.ID, "userEmail")))
USerEmail.send_keys("valusageonly@gmail.com")

USerADD = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.ID, "currentAddress")))
USerADD.send_keys("America, England")

USerPerADD = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.ID, "permanentAddress")))
USerPerADD.send_keys("America, England")

# Submit the form
Submit_Btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'submit')))
driver.execute_script("arguments[0].scrollIntoView(true);", Submit_Btn)  # Scroll into view
driver.execute_script("arguments[0].click();", Submit_Btn)  # Click using JS to avoid interception

# Navigate to the download section
download_area = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="item-7"]')))
driver.execute_script("arguments[0].scrollIntoView(true);", download_area)
driver.execute_script("arguments[0].click();", download_area)

# Wait for the download button and click it
download_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'downloadButton')))
driver.execute_script("arguments[0].click();", download_btn)

# Wait for the user to close the window
input("Press enter to close automated window")

# Close the browser
driver.quit()
