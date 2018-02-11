from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import os

class Carousel():
    def test_carousel(self):
        _baseURL = "https://www.amazon.com/stream/ref=nav_upnav_LargeImage_C_Gateway?asCursor=WyIxLjgiLCJ0czEiLCIxNTE3NDI1OTIwMDAwIiwiIiwiUzAwMDU6MDpudWxsIiwiUzAwMDU6MjoxIiwiUzAwMDU6MDotMSIsIiIsIiIsIjAiLCJzdWIyIiwiMTUxNzQzNTUwNzAxMiIsImhmMS1zYXZlcyIsIjE1MTc0Mjk3MDAwMDAiLCJ2MSIsIjE1MTc0MzQ3ODU1MjciLCJ2MSIsIjE1MDEwMTYzNDk2NTgiLCJ2MSIsIjE1MTc0MjYwMjEyMzAiXQ%3D%3D&asCacheIndex=0&asYOffset=-348.1000061035156"
        _carousel = "//div[@id='anonCarousel1']//img"
        _arrow = "//a[@class='a-carousel-goto-nextpage']/span"
        _selected_items = "//li[@class='a-carousel-card aux-theme-tab aux-theme-tab-selected']//span[@class='aux-theme-tab-text']"

        chromeDriverLocation = "/Users/sergiiskarshevskyi/Documents/workspace_Python/SeleniumProject/lib/chromedriver"
        os.environ["webreiver.chrome.driver"] = chromeDriverLocation
        driver = webdriver.Chrome(chromeDriverLocation)
        driver.implicitly_wait(10)
        driver.get(_baseURL)


        carousel_list = driver.find_elements(By.XPATH, _carousel)
        length_of_carousel = len(carousel_list)
        print("length of carousel items is: " +str(length_of_carousel))

        for element in range(length_of_carousel):
            if not carousel_list[element].is_displayed():
                arrow = driver.find_element(By.XPATH, _arrow)
                arrow.click()
                time.sleep(2)

            carousel_list[element].click()
            carousel_list = driver.find_elements(By.XPATH, _carousel)
            time.sleep(2)

            selected_items = driver.find_element(By.XPATH, _selected_items).text
            if selected_items != carousel_list[element]:
                print("Item %s selected !!!" %(selected_items))
            else:
                print("element not found")
        print("Finish carousel loop")
        driver.quit()


FF = Carousel()
FF.test_carousel()
