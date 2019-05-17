from selenium import webdriver
import time
import pytest
import allure
import moment
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils

@pytest.mark.usefixtures("test_setup")
class TestLogin():

    # @pytest.fixture(scope="class")
    # def test_setup(self):
    #     global driver
    #     driver = webdriver.Chrome(executable_path='C:/Users/rsharma390/PycharmProjects/SampleProject1/drivers/chromedriver.exe')
    #     driver.implicitly_wait(10)
    #     driver.maximize_window()
    #     yield
    #     driver.close()
    #     driver.quit()
    #     print("Test Completed")

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)
        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_Password(utils.PASSWORD)
        login.click_login()
        # driver.find_element_by_id("txtUsername").send_keys("Admin")
        # driver.find_element_by_id("txtPassword").send_keys("admin123")
        # driver.find_element_by_id("btnLogin").click()

    def test_logout(self):
        try:
            driver = self.driver
            homepage = HomePage(driver)
            homepage.click_welcome()
            homepage.click_logout()
            #driver.find_element_by_id("welcome").click()
            #driver.find_element_by_link_text("Sign off").click()
            x = driver.title
            assert x == "OrangeHRM"

        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            currTime = moment.now().strftime("%H-%M-%S_%m-%d-%Y")
            testName = utils.whoami()
            screenshotName = testName+"_"+ currTime
            allure.attach(self.driver.get_screenshot_as_png(),name=screenshotName,attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/rsharma390/PycharmProjects/SampleProject1/screenshots/" + screenshotName + ".png")
            raise

        except:
            print("Some exception occurred")
            currTime = moment.now().strftime("%H-%M-%S_%m-%d-%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            raise

        else:
            print("No exceptions occurred")

        finally:
            print("This is in finally block")
