from homepage import SauceAutomation
import pytest

url ="https://www.saucedemo.com/"
automation = SauceAutomation(url)

#test case for verifiying the title
def test_title():
    expected_title = "Swag Labs"
    assert automation.fetch_title() == expected_title
    print("SUCESS: Title verified successfully")

#test case for verifying the url
def test_url():
    expected_url = "https://www.saucedemo.com/"
    assert automation.fetch_url() == expected_url
    print("SUCCESS: Url verified successfully")

#test case for extracting the page content
def test_page_content():
    file = open("Webpage_task_9.txt",'a')
    file.write(automation.fetch_page_content())
    file.close()
    print("SUCCESS: Page content extracted successfully")
