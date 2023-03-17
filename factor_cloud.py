import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FactorClouldTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)
    
    def test_valid_credentials(self):

        '''Logging to the website, using both valid credentials: email and password'''

        self.browser.get("https://dev.factorcloud.com/")

        email= self.browser.find_element(By.ID, ":r2:")
        email.send_keys("jesjar16@gmail.com")

        password= self.browser.find_element(By.ID, ":r3:")
        password.send_keys("FactorCloud_2023")

        self.browser.find_element(By.XPATH,"//button[@type='submit']").click()

        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[2]/main/div/div[2]/div[1]/div[2]/div[1]'))
            )

        assert(self.browser.find_element(By.XPATH, "/html/body/div/div/div[2]/main/div/div[2]/div[1]/div[2]/div[1]"))
    
    def test_unregistered_email(self):

        '''Logging to the website, using an unregistered email address'''

        self.browser.get("https://dev.factorcloud.com/")

        email= self.browser.find_element(By.ID, ":r2:")
        email.send_keys("test@myemail.com")

        password= self.browser.find_element(By.ID, ":r3:")
        password.send_keys("test1234")

        self.browser.find_element(By.XPATH,"//button[@type='submit']").click()
        
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[1]/div/div/div[1]/div[2]/div/div[2]'))
            )

        assert(self.browser.find_element(By.XPATH, "//*[text()='Something Went Wrong']"))

    def test_wrong_password(self):

        '''Logging to the website, using a registered email address, but with the wong password'''

        self.browser.get("https://dev.factorcloud.com/")

        email= self.browser.find_element(By.ID, ":r2:")
        email.send_keys("jesjar16@gmail.com")

        password= self.browser.find_element(By.ID, ":r3:")
        password.send_keys("test1234")

        self.browser.find_element(By.XPATH,"//button[@type='submit']").click()
       
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[1]/div/div/div[1]/div[2]/div/div[2]'))
            )

        assert(self.browser.find_element(By.XPATH, "//*[text()='Server denied access']"))

    def test_empty_credentials(self):

        '''Logging to the website without credentials'''

        self.browser.get("https://dev.factorcloud.com/")

        email= self.browser.find_element(By.ID, ":r2:")
        email.send_keys("")

        password= self.browser.find_element(By.ID, ":r3:")
        password.send_keys("")

        self.browser.find_element(By.XPATH,"//button[@type='submit']").click()
 
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[1]/div/div/div[1]/div[2]/div/div[2]'))
            )

        assert(self.browser.find_element(By.XPATH, "/html/body/div/div/div[1]/div/div/div[1]/div[2]/div/div[2]"))
    
    def test_empty_password(self):

        '''Logging to the website without password'''

        self.browser.get("https://dev.factorcloud.com/")

        email= self.browser.find_element(By.ID, ":r2:")
        email.send_keys("jesjar16@gmail.com")

        password= self.browser.find_element(By.ID, ":r3:")
        password.send_keys("")

        self.browser.find_element(By.XPATH,"//button[@type='submit']").click()
 
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[1]/div/div/div[1]/div[2]/div/div[2]'))
            )

        assert(self.browser.find_element(By.XPATH, "/html/body/div/div/div[1]/div/div/div[1]/div[2]/div/div[2]"))

    def test_empty_email(self):

        '''Logging to the website without email'''

        self.browser.get("https://dev.factorcloud.com/")

        email= self.browser.find_element(By.ID, ":r2:")
        email.send_keys("")

        password= self.browser.find_element(By.ID, ":r3:")
        password.send_keys("FactorCloud_2023")

        self.browser.find_element(By.XPATH,"//button[@type='submit']").click()
 
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[1]/div/div/div[1]/div[2]/div/div[2]'))
            )

        assert(self.browser.find_element(By.XPATH, "/html/body/div/div/div[1]/div/div/div[1]/div[2]/div/div[2]"))

if __name__ == '__main__':
    unittest.main(verbosity=2)