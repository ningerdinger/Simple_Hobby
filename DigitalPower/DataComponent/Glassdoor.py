from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
import time
import logging
import writing_to_DB as wDB


class Glassdoor:
    def __init__(self, path: str, pages: int, key):
        self.key = key
        self.url = 'https://www.glassdoor.co.in/Job/netherlands-data-scientist-jobs-SRCH_IL.0,11_IN178_KO12,26.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=&typedLocation=Netherlands&context=Jobs&dropdown=0'
        self.path = path
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(executable_path=path, options=self.options)
        self.driver.get(self.url)
        self.pages_count=1

        while self.pages_count<=pages:
            time.sleep(2)
            logging.info(f"Scraping page{self.pages_count}")
            self.Logic(self.pages_count)
            self.pages_count = self.pages_count + 1

        self.driver.quit()

    def Logic(self, page: int):
        data_set = self.driver.find_element(By.XPATH, '//*[@id="MainCol"]/div[1]/ul')
        data_in_text = str(data_set.text)
        time.sleep(2)
        text_file = open(f"page{page}.txt", "w", encoding="utf-8")
        time.sleep(2)
        n = text_file.write(data_in_text)
        text_file.close()
        path = f'/DigitalPowerCBSData/Bronze/glassdoor'
        wDB.WritingToDB(name=f"page{page}", path=path, key=self.key, file_format='txt')
        time.sleep(2)
        button = self.driver.find_element(By.XPATH, '//*[@id="MainCol"]/div[2]/div/div[1]/button[7]')
        self.driver.execute_script("arguments[0].click();", button)
        time.sleep(2)
