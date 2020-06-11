from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')


capitals = {
    'Rome': 'Italy',
    'Oslo': 'Norway',
    'Seoul': 'South Korea',
    'Washington': 'United States',
    'Madrid': 'Spain',
    'Copenhagen': 'Denmark',
    'Stockholm': 'Sweden'
}

targets = driver.find_elements_by_class_name('dragableBoxRight')

for i in range(0,8):
    try:
        source = driver.find_element_by_xpath('//*[@id="box%s"]' % (i + 1) )
        print('%s' % i, source.text)
        
        for j in range(0,8):
            if (targets[j].text) == capitals.get(source.text):
                print(' > dest: ', targets[j].text)
                actions = ActionChains(driver)
                actions.drag_and_drop(source, targets[j]).perform()
                break

    except:
        continue



