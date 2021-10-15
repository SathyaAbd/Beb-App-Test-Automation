from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="C:\Driver's\chromedriver.exe")
driver.maximize_window()

driver.get("https://vilvahstore.com/")
print(driver.title)
driver.find_element_by_xpath("//*[@id='shopify-section-header']/div[2]/div[1]/div/div/div[3]/a[1]").click()     #Login
driver.find_element_by_id("CustomerEmail").send_keys("sathya18cbe@gmail.com")    #Username
driver.find_element_by_id("CustomerPassword").send_keys("vilvah@123")   #Password
time.sleep(3)
driver.find_element_by_xpath("//*[@id='form_content']/div[3]/input").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='MainContent']/div[1]/nav/a").click()    #Home

#mouse Hover
hair = driver.find_element_by_xpath("//*[@id='SiteNav']/li[3]/button/span")
oil = driver.find_element_by_xpath("//*[@id='SiteNavLabel-hair']/ul/li[4]/a/span")
action = ActionChains(driver)
action.move_to_element(hair).move_to_element(oil).click().perform()    #Click Hair Oil

#scroll the page
driver.execute_script("window.scrollBy(0,1000)", "")   #Scroll Down
time.sleep(2)

#grow = driver.find_element_by_xpath("//*[@id='Hair_1']/div[6]/div/div[1]/a/div/img[2]")
#action.move_to_element(grow).click().perform()
driver.find_element_by_xpath("//*[@id='Hair_1']/div[6]/div/a/h2[1]").click()    #Click Hair Growth Oil
driver.find_element_by_xpath("//*[@id='product_form_612458987583']/div[3]/div[2]/div[3]/label").click()  #Click 200 ml
time.sleep(3)
driver.find_element_by_xpath("//*[@id='ProductSection-product-template']/div[1]/div[2]/div[1]/div[3]/div[2]/div/button/span[1]").click()   #Click Buy Me
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[4]/div/div[5]/div/div[2]/a").click()    #Click Checkout

#value = driver.find_element_by_xpath("//*[@id='SiteNav']/li[3]/button/span")
#drp = Select(value)
#drp.select_by_visible_text('Hair Oils')
#time.sleep(3)

#print(len(drp.options))

#output = drp.options
#for option in output:
    #print(output.text)
