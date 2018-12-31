import os
import logging

from pyvirtualdisplay import Display
from selenium import webdriver

logging.getLogger().setLevel(logging.INFO)

BASE_URL = 'http://www.google.com/'


def scraping_title():
    Display_var = Display(visible=0, size=(800, 600))
    Display_var.start()
    logging.info('Virtual display inicializado..')

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')

    chrome_options.add_experimental_option('prefs', {
        'download.default_directory': os.getcwd(),
        'download.prompt_for_download': False,
    })
    logging.info('Chrome Options setado..')

    driver = webdriver.Chrome(chrome_options=chrome_options)
    logging.info('Chrome inicializado..')

    driver.get(BASE_URL)
    logging.info('Acessando %s ..', BASE_URL)

    logging.info('Titulo: %s', driver.title)

    driver.quit()
    Display_var.stop()



if __name__ == '__main__':
    scraping_title()
