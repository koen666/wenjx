import random
import time
import threading
import numpy
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import tkinter as tk

url="https://www.wjx.cn/vm/QHzdwQy.aspx"

class WenjxAuto:
    def __init__(self, url, times):
        self.url = url
        self.times = times
        self.running = True

    def run(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('detach', True)
        option.add_argument("--no-sandbox")
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        option.add_experimental_option('useAutomationExtension', False)
        option.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        option.add_argument("--disable-blink-features=AutomationControlled")
        option.add_argument("--disable-infobars")
        option.add_argument("--disable-dev-shm-usage")
        option.add_argument("--disable-gpu")
        option.add_argument("--no-first-run")
        option.add_argument("--no-default-browser-check")
        option.add_argument("--disable-popup-blocking")
        option.add_argument("--ignore-certificate-errors")
        prefs = {
            "profile.password_manager_enabled": False,
            "credentials_enable_service": False,
            "profile.default_content_setting_values.notifications": 2
        }
        option.add_experimental_option("prefs", prefs)

        service = Service("chromedriver.exe")
        driver = webdriver.Chrome(options=option, service=service)
        
        driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                              {'source': 'Object.defineProperty(navigator,"webdriver",{get:()=>undefined})'})
        
        # 随机偏移窗口位置防止检测
        x_offset = random.randint(0, 100)
        y_offset = random.randint(0, 100)
        driver.set_window_size(400, 600)
        driver.set_window_position(x_offset, y_offset)
        driver.get(self.url)
        time.sleep(5)

        single_select_five=[1,4]
        single_select_two=[2,3]
        multiple_select=[5,6,7,8,9]
        judge_select=[10]


        for i in single_select_five:
            random_int = random.randint(1,5)
            css_selector = f'div#div{i} ul li:nth-child({random_int}) a'
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
            driver.find_element(By.CSS_SELECTOR, css_selector).click()
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
                css_selector = f'div#div{i} ul li:nth-child({random_int}) a'
                try:
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))).click()
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
        try:
            driver.quit()
        except Exception as e:
            print(f"关闭浏览器时发生错误: {str(e)}")


class MainApplication:
    def __init__(self, master):
        self.master = master
        master.title("问卷星自动填写")
        master.geometry("400x250")
        
        # URL输入
        tk.Label(master, text="问卷URL:").grid(row=0, column=0, padx=5, pady=5)
        self.url_entry = tk.Entry(master, width=40)
        self.url_entry.insert(0, "https://www.wjx.cn/vm/QHzdwQy.aspx")
        self.url_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # 份数输入
        tk.Label(master, text="填写份数:").grid(row=1, column=0, padx=5, pady=5)
        self.times_entry = tk.Entry(master)
        self.times_entry.insert(0, "10")
        self.times_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')
        
        # 控制按钮
        self.start_btn = tk.Button(master, text="开始", command=self.start_task)
        self.start_btn.grid(row=2, column=0, padx=5, pady=10)
        
        self.stop_btn = tk.Button(master, text="停止", command=self.stop_task, state=tk.DISABLED)
        self.stop_btn.grid(row=2, column=1, padx=5, pady=10)
        
        # 状态显示
        self.status_label = tk.Label(master, text="准备就绪", relief=tk.SUNKEN, anchor=tk.W)
        self.status_label.grid(row=3, column=0, columnspan=2, sticky="we", padx=5, pady=5)
        
        # 日志框
        self.log_text = tk.Text(master, height=6, width=50)
        self.log_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        
        self.auto_thread = None
    
    def start_task(self):
        url = self.url_entry.get()
        try:
            times = int(self.times_entry.get())
        except ValueError:
            self.update_status("错误：请输入有效的数字份数")
            return
            
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.update_status("运行中...")
        
        self.auto_thread = threading.Thread(
            target=self.run_task,
            args=(url, times),
            daemon=True
        )
        self.auto_thread.start()
    
    def stop_task(self):
        if hasattr(self, 'auto') and self.auto:
            self.auto.running = False
            self.update_status("正在停止...")
            self.stop_btn.config(state=tk.DISABLED)
    
    def run_task(self, url, times):
        self.auto = WenjxAuto(url, times)
        try:
            for i in range(times):
                if not self.auto.running:
                    break
                self.auto.run()
                self.log_text.insert(tk.END, f"第{i+1}份问卷已完成\n")
                self.log_text.see(tk.END)
                self.master.update()
        except Exception as e:
            import traceback
            error_time = time.strftime("%Y-%m-%d %H:%M:%S")
            error_msg = f"[{error_time}] ERROR: {str(e)}\n{traceback.format_exc()}"
            self.log_text.insert(tk.END, error_msg)
            self.log_text.see(tk.END)
        finally:
            self.start_btn.config(state=tk.NORMAL)
            self.stop_btn.config(state=tk.DISABLED)
            self.update_status("已停止" if i < times-1 else "已完成")
    
    def update_status(self, message):
        self.status_label.config(text=message)
        self.master.update()

if __name__ == '__main__':
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()
