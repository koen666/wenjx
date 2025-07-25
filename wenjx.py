import random
import time
import threading
import numpy
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

url="https://www.wjx.cn/vm/QHzdwQy.aspx"

class Wenjx:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def run(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('detach', True)
        option.add_argument("--no-sandbox")
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        option.add_experimental_option('useAutomationExtension', False)
        option.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        option.add_argument("--disable-blink-features=AutomationControlled")

        service = Service("chromedriver.exe")
        driver = webdriver.Chrome(options=option, service=service)
        
        driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                              {'source': 'Object.defineProperty(navigator,"webdriver",{get:()=>undefined})'})
        
        driver.set_window_position(self.x, self.y)
        driver.set_window_size(400, 600)
        driver.get(url)
        time.sleep(5)

        single_select_five=[1,4]
        single_select_two=[2,3]
        multiple_select=[5,6,7,8,9]
        judge_select=[10]


        for i in single_select_five:
            random_int = random.randint(1,5)
            xpath = f'/html/body/div[2]/form/div[11]/div[6]/fieldset/div[{i}]/div[2]/div[{random_int}]/span/a'
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath)))
            a = driver.find_element(By.XPATH, xpath).click()
            time.sleep(0.3)

        for i in single_select_two:
            random_int = random.randint(1,2)
            xpath = f'/html/body/div[2]/form/div[11]/div[6]/fieldset/div[{i}]/div[2]/div[{random_int}]/span/a'
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath)))
            a = driver.find_element(By.XPATH, xpath).click()
            time.sleep(0.3)

        for i in multiple_select:
            # 首先生成1-5的选项范围
            options = list(range(1, 6))
            
            # 随机决定要选多少个选项(1-5个)
            ans_num = numpy.random.choice(a=numpy.arange(1,6), p=[0.15,0.15,0.2,0.3,0.2])
            
            # 从所有选项中随机选择ans_num个不重复的选项
            selected_options = numpy.random.choice(options, size=ans_num, replace=False, p=[0.15,0.2,0.2,0.25,0.2])
            
            # 点击选中的选项
            for random_int in selected_options:
                xpath = f'/html/body/div[2]/form/div[11]/div[6]/fieldset/div[{i}]/div[2]/div[{random_int}]/span/a'
                try:
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
                    time.sleep(0.1)  # 稍微增加间隔确保点击生效
                except Exception as e:
                    print(f"点击选项{random_int}失败: {str(e)}")
                    continue
            
            time.sleep(0.3)

        for i in judge_select:
            ans1=numpy.random.choice(a=numpy.arange(2,7),p=[0.1,0.1,0.2,0.3,0.3])
            ans2=numpy.random.choice(a=numpy.arange(2,7),p=[0.1,0.1,0.2,0.3,0.3])
            ans3=numpy.random.choice(a=numpy.arange(2,7),p=[0.1,0.1,0.2,0.3,0.3])
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, f'/html/body/div[2]/form/div[11]/div[6]/fieldset/div[10]/div[2]/table/tbody/tr[3]/td[{ans1}]/a')))
            a=driver.find_element(By.XPATH,f'/html/body/div[2]/form/div[11]/div[6]/fieldset/div[10]/div[2]/table/tbody/tr[3]/td[{ans1}]/a').click()
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, f'/html/body/div[2]/form/div[11]/div[6]/fieldset/div[10]/div[2]/table/tbody/tr[5]/td[{ans2}]/a')))
            a=driver.find_element(By.XPATH,f'/html/body/div[2]/form/div[11]/div[6]/fieldset/div[10]/div[2]/table/tbody/tr[5]/td[{ans2}]/a').click()
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, f'/html/body/div[2]/form/div[11]/div[6]/fieldset/div[10]/div[2]/table/tbody/tr[7]/td[{ans3}]/a')))
            a=driver.find_element(By.XPATH,f'/html/body/div[2]/form/div[11]/div[6]/fieldset/div[10]/div[2]/table/tbody/tr[7]/td[{ans3}]/a').click()
            time.sleep(0.1)

        
        submit=driver.find_element(By.XPATH,'/html/body/div[2]/form/div[11]/div[12]/div[3]/div/div')
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/form/div[11]/div[12]/div[3]/div/div')))
        submit.click()
        time.sleep(2)
        handles = driver.window_handles
        driver.switch_to.window(handles[0])
        driver.close()

if __name__ == '__main__':
    s = Wenjx(0, 0)
    for i in range(400):
        s.run()