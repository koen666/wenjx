/html/body/div[2]/form/div[11]/div[6]/fieldset/div[1]/div[2]/div[2]/span/a
/html/body/div[2]/form/div[11]/div[6]/fieldset/div[1]/div[2]/div[3]/span/a

/html/body/div[2]/form/div[11]/div[6]/fieldset/div[2]/div[2]/div[2]/span/a
/html/body/div[2]/form/div[11]/div[6]/fieldset/div[4]/div[2]/div[1]/span/a

    /html/body/div[2]/form/div[11]/div[6]/fieldset/div[10]/div[2]/table/tbody/tr[3]/td[2]/a
/html/body/div[2]/form/div[11]/div[6]/fieldset/div[10]/div[2]/table/tbody/tr[3]/td[3]/a
/html/body/div[2]/form/div[11]/div[6]/fieldset/div[10]/div[2]/table/tbody/tr[3]/td[6]/a
/html/body/div[2]/form/div[11]/div[6]/fieldset/div[10]/div[2]/table/tbody/tr[5]/td[2]/a
/html/body/div[2]/form/div[11]/div[6]/fieldset/div[10]/div[2]/table/tbody/tr[7]/td[2]/a

/html/body/div[2]/form/div[11]/div[6]/fieldset/div[11]/ul/li[1]/div[1]/span
/html/body/div[2]/form/div[11]/div[6]/fieldset/div[11]/ul/li[2]/div[1]/span


格式：
/html/body/div[2]/form/div[11]/div[6]/fieldset/div[{题号}]/div[2]/div[{选项号}]/span/a

        for i in range_select:
            fixed_id=[1,2,3,4]
            ans=random.shuffle(fixed_id)
            xpath1=f'/html/body/div[2]/form/div[11]/div[6]/fieldset/div[{i}]/ul/li[{ans[0]}]/div[1]/span'
            xpath2=f'/html/body/div[2]/form/div[11]/div[6]/fieldset/div[{i}]/ul/li[{ans[1]}]/div[1]/span'
            xpath3=f'/html/body/div[2]/form/div[11]/div[6]/fieldset/div[{i}]/ul/li[{ans[3]}]/div[1]/span'
            xpath4=f'/html/body/div[2]/form/div[11]/div[6]/fieldset/div[{i}]/ul/li[{ans[4]}]/div[1]/span'
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath1)))
            a=driver.find_element(By.XPATH,xpath1).click()
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath2)))
            a=driver.find_element(By.XPATH,xpath2).click()
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath3)))
            a=driver.find_element(By.XPATH,xpath3).click()
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath4)))
            a=driver.find_element(By.XPATH,xpath4).click()
