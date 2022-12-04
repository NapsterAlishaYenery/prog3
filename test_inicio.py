from datetime import datetime
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def test_busqueda():
    driver = webdriver.Chrome()
    driver.get("https://www.pokemon.com/el/pokedex/")
    driver.maximize_window()
    driver.find_element(By.XPATH, '//*[@id="searchInput"]').send_keys('Pikachu')
    driver.find_element(By.XPATH, '//*[@id="search"]').click()
    time.sleep(3)
    pokemon = driver.find_element(By.XPATH, '/html/body/div[4]/section[5]/ul/li/div/h5').text
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot(f"./img/busqueda/img{now}")
    assert pokemon == 'Pikachu'

def test_infoPokemon():
    driver = webdriver.Chrome()
    driver.get("https://www.pokemon.com/el/pokedex/")
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[4]/section[5]/ul/li[1]').click()
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot(f"./img/infopokemon/img{now}")
    assert driver.current_url == 'https://www.pokemon.com/el/pokedex/bulbasaur'

def test_descripcionpokemon():
    driver = webdriver.Chrome()
    driver.get("https://www.pokemon.com/el/pokedex/bulbasaur")
    driver.maximize_window()
    time.sleep(5)
    info = driver.find_element(By.XPATH, '/html/body/div[4]/section[3]/div[2]/div/div[1]/p[2]').text
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot(f"./img/descripcion/img{now}")
    assert len(info) != 0

def test_aplicacionbtn():
    driver = webdriver.Chrome()
    driver.get("https://www.pokemon.com/el")
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
    driver.find_element(By.XPATH, '//li[@class="watch"]/a').click()
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot(f"./img/aplicacionbtn/img{now}")
    assert driver.current_url == 'https://www.pokemon.com/el/app/'

def test_noticias():
    driver = webdriver.Chrome()
    driver.get("https://www.pokemon.com/el")
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
    driver.find_element(By.XPATH, '/html/body/nav/div[2]/ul/li[7]/a').click()
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot(f"./img/noticias/img{now}")
    assert driver.current_url == 'https://www.pokemon.com/el/noticias-pokemon'