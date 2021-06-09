from selenium import webdriver

firefoxdriver = webdriver.Firefox()


for handle in firefoxdriver.window_handles[0]:
    firefoxdriver.switch_to.window(handle)
    print(firefoxdriver.current_url)



