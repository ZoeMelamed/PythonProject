import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class TestYahooFinance():

    def setup(self):
        print("Test Start")
        options = Options()
        # options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        url = "https://finance.yahoo.com"
        self.driver.get(url)

    def teardown(self):
        # Teardown after each test method
        self.driver.quit()
        print("Test End")

    def test_meta_current_stocks(self):
        time.sleep(3)
        scroll_down_button = self.driver.find_element(By.ID, "scroll-down-btn")
        scroll_down_button.click()
        agree_button = self.driver.find_element(By.NAME, "agree")
        agree_button.click()
        time.sleep(3)

        search_bar = self.driver.find_element(By.ID, "ybar-sbq")
        search_bar.click()
        search_bar.clear()
        search_bar.send_keys("META")
        time.sleep(3)
        search_bar.send_keys(Keys.ENTER)
        meta_stock = self.driver.find_element(By.CSS_SELECTOR, "span[data-testid='qsp-price']")
        meta_stock_text = meta_stock.text
        meta_stock_as_float = float(meta_stock_text)  # use casting to convert string to float
        assert meta_stock_as_float > 200, "meta stock is not above 200"
        print(f"Current meta stock: {meta_stock_as_float}")


    def test_apple_current_stocks(self):
        time.sleep(3)
        scroll_down_button = self.driver.find_element(By.ID, "scroll-down-btn")
        scroll_down_button.click()
        agree_button = self.driver.find_element(By.NAME, "agree")
        agree_button.click()
        time.sleep(3)

        search_bar = self.driver.find_element(By.ID, "ybar-sbq")
        search_bar.click()
        search_bar.clear()
        search_bar.send_keys("AAPL")
        time.sleep(3)
        search_bar.send_keys(Keys.ENTER)
        apple_stock = self.driver.find_element(By.CSS_SELECTOR, "span[data-testid='qsp-price']")
        apple_stock_text = apple_stock.text
        apple_stock_as_float = float(apple_stock_text)  # use casting to convert string to float
        assert apple_stock_as_float > 200, "meta stock is not above 200"
        print(f"Current apple stock price: {apple_stock_as_float}")

    def test_tesla_current_stocks(self):
        time.sleep(3)
        scroll_down_button = self.driver.find_element(By.ID, "scroll-down-btn")
        scroll_down_button.click()
        agree_button = self.driver.find_element(By.NAME, "agree")
        agree_button.click()
        time.sleep(3)

        search_bar = self.driver.find_element(By.ID, "ybar-sbq")
        search_bar.click()
        search_bar.clear()
        search_bar.send_keys("TESLA")
        time.sleep(3)
        search_bar.send_keys(Keys.ENTER)
        tesla_stock = self.driver.find_element(By.CSS_SELECTOR, "span[data-testid='qsp-price']")
        tesla_stock_text = tesla_stock.text
        tesla_stock_as_float = float(tesla_stock_text)  # use casting to convert string to float
        assert tesla_stock_as_float > 200, "tesla stock is not above 200"
        print(f"Current tesla stock:{tesla_stock_as_float}")

    def test_verify_left_menu_button(self):
        # verify "conversations" button in left menu
        time.sleep(3)
        scroll_down_button = self.driver.find_element(By.ID, "scroll-down-btn")
        scroll_down_button.click()
        agree_button = self.driver.find_element(By.NAME, "agree")
        agree_button.click()
        time.sleep(3)

        search_bar = self.driver.find_element(By.ID, "ybar-sbq")
        search_bar.click()
        search_bar.clear()
        search_bar.send_keys("TESLA")
        time.sleep(3)
        search_bar.send_keys(Keys.ENTER)
        conversations = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Conversations")
        conversations_text = conversations.text
        conversations.click()
        time.sleep(3)
        assert conversations_text == 'Conversations', "Conversations button text is not Conversations as defined"
        print("Test end")

    def test_verify_up_menu_button(self):
        # skip cookies menu
        time.sleep(3)
        scroll_down_button = self.driver.find_element(By.ID, "scroll-down-btn")
        scroll_down_button.click()
        agree_button = self.driver.find_element(By.NAME, "agree")
        agree_button.click()
        Yahoo_Finance = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Yahoo Finance")
        Yahoo_Finance_text = Yahoo_Finance.text
        Yahoo_Finance.click()
        time.sleep(3)
        assert Yahoo_Finance_text == 'Yahoo Finance', "Finance button text is not Yahoo Finance as defined"
        print("Test end")
