# from selenium import webdriver
# import pandas as pd
# import time
#
# class_name = input('请输入课程名：')
# df = pd.read_excel('账号.xlsx',names=['username','password'],header=None)
# print(df)
# df['username']=df['username'].astype(str)
# # print(df)
# faillist = []
# l = df.shape[0]
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless') # 隐藏浏览器
# driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)  # 浏览器对象
# p_number = 0
# faile_number = 0
# def get_in_living_room(username,password):
#     global p_number,faile_number
#     try:
#         url = 'http://www.aiquanti.com/loginPage'
#         # chrome_options = webdriver.ChromeOptions()
#         # chrome_options.add_argument('--headless') # 隐藏浏览器
#         # driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)  # 浏览器对象
#
#         # driver.set_window_size(width=1920,height=1080)
#         # driver.get('http://www.baidu.com') # 加载百度页面 和浏览器加载的形式一样 js，css
#         driver.get(url)  # 加载完毕以后，页面的所有东西都在driver中
#         # driver.save_screenshot('test.jpg')
#         user_namebox = driver.find_element_by_xpath('//input[@id="login_account"]')
#         user_passbox = driver.find_element_by_xpath('//input[@id="login_password"]')
#         user_namebox.send_keys(username)
#         user_passbox.send_keys(password)
#         login_button = driver.find_element_by_xpath('//input[@id="login_submit"]')
#         login_button.click()
#
#         time.sleep(2)
#         # print(driver.find_element_by_class_name('bdtn-hide'))
#         # get_in_class = driver.find_elements_by_class_name('state now clear')
#         get_in_class = driver.find_element_by_xpath('//span[text()="'+class_name+'"]')
#         # print(get_in_class)
#         webdriver.ActionChains(driver).move_to_element(get_in_class)
#         # classB = driver.find_element_by_xpath('//span[@class="state now clear"]/button')
#         get_in_class.click()
#         get_in_class.click()
#         get_in_class.click()
#         get_in_class = driver.find_element_by_xpath('//button[text()="进入教室"]')
#         get_in_class.click()
#         time.sleep(2)
#         print(username+'登陆成功')
#         p_number += 1
#         print('当前登录成功%d人'%p_number)
#
#     except:
#         print(username+'登录失败')
#         faillist.append([username, password])
#         faile_number+=1
#         print('当前登录成功%d人' % p_number)
#
#
#
#
# for i in range(l):
#     username = df.iloc[i, :]['username']
#     password = df.iloc[i, :]['password']
#     get_in_living_room(username,password)
#
#
# while True:
#     print('如下账户登录失败：',faillist,'共'+str(len(faillist))+'人')
#     if faillist:
#         for i in faillist:
#             get_in_living_room(i[0], i[1])
#             faillist.remove(i)
#     else:
#         break
#
# while True:
#     time.sleep(1)
























