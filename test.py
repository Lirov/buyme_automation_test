from selenium import webdriver

### Opens the website, pressing on login button and "not sign yet" button
driver = webdriver.Chrome(executable_path="C:\selenium\chromeDriver_selenium\chromedriver.exe")
driver.get("https://buyme.co.il/")
driver.find_element_by_xpath("//*[@id='ember542']/div/header[1]/div[2]/ul/li[5]/a").click()
driver.find_element_by_xpath("//*[@id='auth-modal']/div/span/strong").click()
driver.f