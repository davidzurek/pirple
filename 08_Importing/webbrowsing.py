from selenium import webdriver

browser1 = webdriver.Chrome("./chromedriver")
browser1.get("https://www.pirple.com/")

course_python_is_easy = browser1.find_element_by_xpath(
    "/html/body/main/section[3]/div/article/ul/li[1]/div[2]/a")
course_python_is_easy.click()

browser1.get_screenshot_as_file(
    "./python_curriculum.png")

browser2 = webdriver.Chrome("/Users/davidzurek/Downloads/chromedriver")
browser2.get("https://www.pirple.com/")

contact_us = browser2.find_element_by_link_text("Contact Us")
contact_us.click()

facebook_group = browser2.find_element_by_link_text(
    "https://facebook.com/groups/1282717078530848/")
facebook_group.click()
