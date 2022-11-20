# from cgi import print_form
from multiprocessing.connection import wait
from re import A
from selenium import webdriver
import undetected_chromedriver as uc
import time
from selenium_stealth import stealth
from selenium.webdriver.common.keys import Keys
# from helium import *
from selenium.common.exceptions import NoSuchElementException        
import msvcrt as m

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.action_chains import ActionChains


driver = uc.Chrome(use_subprocess=True)
def check_exists(xpath):
    try:
        driver.find_element(By.CSS_SELECTOR,xpath)
    except NoSuchElementException:
        return False
    return True
def wait():
    m.getch()
def login(email, password):
     driver.get("https://accounts.google.com/ServiceLogin")
     myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'identifier'))).send_keys(email)
     myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button'))).click()
     print("bạn đang đăng nhập đúng tài khoản?")
     print("1.đúng tài khoản")
     print("2.sai tài khoản")
     val = input("Enter your value: ")
     val = int(val)
     if(val !=1):
          return
     myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'Passwd'))).send_keys(password)
     myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button'))).click()
     time.sleep(3)
     driver.get("https://drive.google.com/drive/my-drive")
     print("Hoàn Thành Kiểm Thử Mời Nhấn Enter để Tiếp Tục...")
     wait()        
def addFolder(x):
     driver.get("https://drive.google.com/drive/my-drive")
     myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[aria-label='Drive của tôi']")))
     driver.find_element(By.XPATH,"/html/body/div[3]/div/div[5]/div[1]/div/div/div/div[2]/div/div[1]/div/div/div[1]/div/div[2]").click()
     time.sleep(1.5)
     myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, 'h-v-pc'))).click()
     myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME,"LUNIy"))).send_keys(Keys.CONTROL, 'a')
     myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME,"LUNIy"))).send_keys(x)
     time.sleep(4)
     myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME,"LUNIy"))).send_keys(Keys.RETURN)
     time.sleep(4)
     driver.get("https://drive.google.com/drive/my-drive")
     myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[aria-label='Drive của tôi']")))
     if(check_exists("[aria-label='"+x+" Thư mục Google Drive']")):
            print("Được Thông Qua!!!")
     else:
            print("Thất Bại!!!")
     print("Hoàn Thành Kiểm Thử Mời Nhấn Enter để Tiếp Tục...")
     wait()

def removeFolder(x):
     driver.get("https://drive.google.com/drive/my-drive")
     myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[aria-label='Drive của tôi']")))
     if(check_exists("[aria-label='"+x+" Thư mục Google Drive']")):
            action = ActionChains(driver)
            # myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '[aria-label="Thư Mục Test case Thư mục Google Drive"]'))).click()
            action.context_click(driver.find_element(By.CSS_SELECTOR,"[aria-label='"+x+" Thư mục Google Drive']")).perform()
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME,"h-w"))).send_keys(Keys.RETURN)
            print("chờ đợi quá trình xóa...")
            time.sleep(5)
            driver.get("https://drive.google.com/drive/my-drive")
            myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[aria-label='Drive của tôi']")))
            if(check_exists("[aria-label='"+x+" Thư mục Google Drive']")):
                        print("Thất Bại!!!")
            else:
                        print("Được Thông Qua!!!")
     else:
            print("Folder Không Tồn Tại ~ Thất Bại !!!")
     driver.get("https://drive.google.com/drive/my-drive") 
     myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[aria-label='Drive của tôi']")))
     print("Hoàn Thành Kiểm Thử Mời Nhấn Enter để Tiếp Tục...")
     wait()
def removeFile(x):
     driver.get("https://drive.google.com/drive/my-drive")
     myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[aria-label='Drive của tôi']")))
     if(check_exists("[aria-label='"+x+"']")):
            action = ActionChains(driver)
            # myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '[aria-label="Thư Mục Test case Thư mục Google Drive"]'))).click()
            action.context_click(driver.find_element(By.CSS_SELECTOR,"[aria-label='"+x+"']")).perform()
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME,"h-w"))).send_keys(Keys.RETURN)
            print("chờ đợi quá trình xóa...")
            time.sleep(5)
            driver.get("https://drive.google.com/drive/my-drive")
            myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[aria-label='Drive của tôi']")))
            if(check_exists("[aria-label='"+x+"']")):
                        print("Thất Bại!!!")
            else:
                        print("Được Thông Qua!!!")
     else:
            print("File Không Tồn Tại ~ Thất Bại !!!")
     driver.get("https://drive.google.com/drive/my-drive") 
     myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[aria-label='Drive của tôi']")))
     print("Hoàn Thành Kiểm Thử Mời Nhấn Enter để Tiếp Tục...")
     wait()
def dowloadFolder(x):
      driver.get("https://drive.google.com/drive/my-drive")
      action = ActionChains(driver)
      myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[aria-label='Drive của tôi']")))
      if(check_exists("[aria-label='"+x+" Thư mục Google Drive']")):
            action = ActionChains(driver)
            action.context_click(driver.find_element(By.CSS_SELECTOR,"[aria-label='"+x+" Thư mục Google Drive']")).perform()
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME,"h-w"))).send_keys(Keys.RETURN)
            print("Chờ Đợi Quá Trình Nén file để Tải~")
            time.sleep(7)
      else:
            print("Đối Tượng truyền vào Không Có trong danh Sách, Vui Lòng Kiểm Tra Lại!!!")
      print("Hoàn Thành Kiểm Thử Mời Nhấn Enter để Tiếp Tục...")
      wait()
def dowloadOject(x):
      driver.get("https://drive.google.com/drive/my-drive")
      action = ActionChains(driver)
      myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[aria-label='Drive của tôi']")))
      if(check_exists("[aria-label='"+x+" Thư mục Google Drive']")):
            action = ActionChains(driver)
            action.context_click(driver.find_element(By.CSS_SELECTOR,"[aria-label='"+x+" Thư mục Google Drive']")).perform()
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME,"h-w"))).send_keys(Keys.RETURN)
            print("Chờ Đợi Quá Trình Nén file để Tải~")
            time.sleep(7)
      else:
            print("Đối Tượng truyền vào Không Có trong danh Sách, Vui Lòng Kiểm Tra Lại!!!")
      print("Hoàn Thành Kiểm Thử Mời Nhấn Enter để Tiếp Tục...")
      wait()
def dowloadFile(x):
      driver.get("https://drive.google.com/drive/my-drive")
      action = ActionChains(driver)
      myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[aria-label='Drive của tôi']")))
      if(check_exists("[aria-label='"+x+"']")):
            action = ActionChains(driver)
            action.context_click(driver.find_element(By.CSS_SELECTOR,"[aria-label='"+x+"']")).perform()
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME,"h-w"))).send_keys(Keys.RETURN)
            print("Chờ Đợi Quá Trình Nén file để Tải~")
            time.sleep(7)
      else:
            print("Đối Tượng truyền vào Không Có trong danh Sách, Vui Lòng Kiểm Tra Lại!!!")
      print("Hoàn Thành Kiểm Thử Mời Nhấn Enter để Tiếp Tục...")
      wait()


     #========================================================
def editFolder(x,x1):
     driver.get("https://drive.google.com/drive/my-drive")
     myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[aria-label='Drive của tôi']")))
     if(check_exists("[aria-label='"+x+" Thư mục Google Drive']")):
            action = ActionChains(driver)
            # myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '[aria-label="Thư Mục Test case Thư mục Google Drive"]'))).click()
            action.context_click(driver.find_element(By.CSS_SELECTOR,"[aria-label='"+x+" Thư mục Google Drive']")).perform()
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME,"h-w"))).send_keys(Keys.RETURN)
            myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME,"lb-k-Kk"))).send_keys(Keys.CONTROL, 'a')
            myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME,"lb-k-Kk"))).send_keys(x1)
            myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME,"lb-k-Kk"))).send_keys(Keys.RETURN)
            print("chờ Đợi Tạo Folder~")
            time.sleep(5)
     else:
            print("Folder Không Tồn Tại ~ Thất Bại !!!")
     driver.get("https://drive.google.com/drive/my-drive") 
     time.sleep(5)
     print("Hoàn Thành Kiểm Thử Mời Nhấn Enter để Tiếp Tục...")
     wait()
def editFile(x,x1):
     driver.get("https://drive.google.com/drive/my-drive")
     myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[aria-label='Drive của tôi']")))
     if(check_exists("[aria-label='"+x+"']")):
            action = ActionChains(driver)
            # myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '[aria-label="Thư Mục Test case Thư mục Google Drive"]'))).click()
            action.context_click(driver.find_element(By.CSS_SELECTOR,"[aria-label='"+x+"']")).perform()
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
            time.sleep(0.6)
            myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME,"h-w"))).send_keys(Keys.RETURN)
            myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME,"lb-k-Kk"))).send_keys(Keys.CONTROL, 'a')
            myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME,"lb-k-Kk"))).send_keys(x1)
            myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME,"lb-k-Kk"))).send_keys(Keys.RETURN)
            print("chờ Đợi Tạo File~")
            time.sleep(5)
     else:
            print("Folder Không Tồn Tại ~ Thất Bại !!!")
     driver.get("https://drive.google.com/drive/my-drive") 
     myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[aria-label='Drive của tôi']")))
     print("Hoàn Thành Kiểm Thử Mời Nhấn Enter để Tiếp Tục...")
     wait()
#============================================================
def chossen_Folder(x):
      if(check_exists("[aria-label='"+x+" Thư mục Google Drive']")):
            myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[aria-label='"+x+" Thư mục Google Drive']")))
            action = ActionChains(driver).key_down(Keys.CONTROL).click(myElem).key_up(Keys.CONTROL).perform()
def chossen_File(x):
      if(check_exists("[aria-label='"+x+"']")):
            myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[aria-label='"+x+"']")))
            action = ActionChains(driver).key_down(Keys.CONTROL).click(myElem).key_up(Keys.CONTROL).perform()
def chossen_Dowload(x,i):
      time.sleep(2)
      if(i==2):
            if(check_exists("[aria-label='"+x+"']")):
                  myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[aria-label='"+x+"']")))
                  action = ActionChains(driver).key_down(Keys.CONTROL).context_click(myElem).key_up(Keys.CONTROL).perform()
                  time.sleep(0.6)
                  driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
                  time.sleep(0.6)
                  driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
                  time.sleep(0.6)
                  driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
                  time.sleep(0.6)
                  driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
                  time.sleep(0.6)
                  driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
                  time.sleep(0.6)
                  driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
                  time.sleep(0.6)
                  myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME,"h-w"))).send_keys(Keys.RETURN)
                  print("Chờ Đợi Quá Trình Nén file để Tải~")
                  time.sleep(7)
                  print("Hoàn Tất Kiểm Thử Nhấn Enter Để tiếp tục!!!")
                  wait()
                  return
      else:
            if(check_exists("[aria-label='"+x+" Thư mục Google Drive']")):
                  myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[aria-label='"+x+" Thư mục Google Drive']")))
                  action = ActionChains(driver).key_down(Keys.CONTROL).context_click(myElem).key_up(Keys.CONTROL).perform()
                  time.sleep(0.6)
                  driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
                  time.sleep(0.6)
                  driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
                  time.sleep(0.6)
                  driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
                  time.sleep(0.6)
                  driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
                  time.sleep(0.6)
                  driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
                  time.sleep(0.6)
                  driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
                  time.sleep(0.6)
                  myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME,"h-w"))).send_keys(Keys.RETURN)
                  print("Chờ Đợi Quá Trình Nén file để Tải~")
                  time.sleep(7)
                  print("Hoàn Tất Kiểm Thử Nhấn Enter Để tiếp tục!!!")
                  wait()
                  return
def chossen_Delete(x,i):
      time.sleep(2)
      if(i==2):
            if(check_exists("[aria-label='"+x+"']")):
                  myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[aria-label='"+x+"']")))
                  action = ActionChains(driver).key_down(Keys.CONTROL).context_click(myElem).key_up(Keys.CONTROL).perform()
                  time.sleep(0.6)
                  driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
                  time.sleep(0.6)
                  driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
                  time.sleep(0.6)
                  driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
                  time.sleep(0.6)
                  driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
                  time.sleep(0.6)
                  driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
                  time.sleep(0.6)
                  driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
                  time.sleep(0.6)
                  driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
                  time.sleep(0.6)
                  myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME,"h-w"))).send_keys(Keys.RETURN)
                  print("Chờ Đợi Quá Trình Nén file để Tải~")
                  time.sleep(7)
                  print("Hoàn Tất Kiểm Thử Nhấn Enter Để tiếp tục!!!")
                  wait()
                  return
      else:
            if(check_exists("[aria-label='"+x+" Thư mục Google Drive']")):
                  myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[aria-label='"+x+" Thư mục Google Drive']")))
                  action = ActionChains(driver).key_down(Keys.CONTROL).context_click(myElem).key_up(Keys.CONTROL).perform()
                  time.sleep(0.6)
                  driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
                  time.sleep(0.6)
                  driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
                  time.sleep(0.6)
                  driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
                  time.sleep(0.6)
                  driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
                  time.sleep(0.6)
                  driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
                  time.sleep(0.6)
                  driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
                  time.sleep(0.6)
                  driver.find_element(By.CLASS_NAME,"h-w").send_keys(Keys.DOWN)
                  time.sleep(0.6)
                  myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME,"h-w"))).send_keys(Keys.RETURN)
                  print("Chờ Đợi Quá Trình Nén file để Tải~")
                  time.sleep(7)
                  print("Hoàn Tất Kiểm Thử Nhấn Enter Để tiếp tục!!!")
                  wait()
                  return
#============================================================
def timKiem(x):
      dem = 0
      driver.get("https://drive.google.com/drive/my-drive")
      myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[aria-label='Tìm trong Drive']"))).send_keys(x)
      myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[aria-label='Tìm trong Drive']"))).send_keys(Keys.RETURN)
      time.sleep(6)
      print(check_exists(".Q5txwe"))
      if (check_exists(".Q5txwe")):
            list = WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.CLASS_NAME,"Q5txwe")))
            for i in list:
                  if x in i.get_attribute("aria-label"):
                        dem= dem + 1
            print("Số Lượng Bộ Lọc Hợp Lệ ",dem," trên ",len(list)," Kết quả")
            if((dem/len(list))*100 > 70):
                  print("testcase được thông qua")
            else:
                  print("testcase thất bại")
            print("Hoàn Thành Kiểm Thử Mời Nhấn Enter để Tiếp Tục...")
            wait()
            return
      print("Không Tìm Thấy trong danh sach, Kiểm tra lại")
      print("Hoàn Thành Kiểm Thử Mời Nhấn Enter để Tiếp Tục...")
      wait()
def Ds2():                                                  #menu các thao tác kiểm thử
    print("")
    print("============================================================")
    print("Danh Sách Thao Tác Kiểm Thử Đăng Nhập:")
    print("1.TC1 Kiểm Thử Đăng Nhập Tài Khoản Đúng Mật Khẩu Đúng:")
    print("2.TC2 Kiểm Thử Đăng Nhập sai:")
    print("3.TC3 Kiểm Thử Đăng Nhập Tài Khoản Đúng Nhưng Mật Khẩu Sai:")
    print("4.TC4 Kiểm Thử Đăng Nhập Tài Khoản để trống:")
    print("5.TC5 Kiểm Thử Đăng Nhập Tài Khoản để Đúng Mật Khẩu Để trống:")
    print("5.Nhập Tay Để Đăng Nhập:")
    print("phím Bất Kì Để Thoát Danh Sach")
    val = input("Enter your value: ")
    val = int(val)
    if(val == 1):
          taikhoan = "kidcher1416"                         #tài khoan sai
          matkhau = "thonglovechou123"                      #Mật Khẩu đúng
          login(taikhoan, matkhau)
    elif(val == 2):
          taikhoan = "kidcher1416sai"                         #tài khoản sai
          matkhau = "thonglovechou123"                     #Mật Khẩu Đúng
          login(taikhoan, matkhau)
    elif(val == 3):
          taikhoan = "kidcher1416"                         #tài khoản đúng
          matkhau = "thonglovechou123sai"                   #Mật Khẩu sai
          login(taikhoan, matkhau)
    elif(val == 4):
          taikhoan = ""                                     #tài khoản trống
          matkhau = "thonglovechou123"                   #Mật Khẩu đúng
          login(taikhoan, matkhau)
    elif(val == 5):
          taikhoan = "kidcher1416"                                      #tài khoản đúng
          matkhau = ""                                                  #Mật Khẩu trống
          login(taikhoan, matkhau)
    elif(val == 6):
            val1 = input("Nhập Tài Khoản: ")
            val2 = input("Nhập Mật Khẩu: ")
            login(val1, val2)
    else:
          return
def Ds3():                                                  #menu các thao tác kiểm thử
    print("")
    print("============================================================")
    print("Danh Sách Thao Tác Kiểm Thử Upload:")
    print("1.kiểm thử Tạo Folder trong root")
    print("2.kiểm thử Xóa Một gì Đó trong root")
    print("3.kiểm thử Tải Một gì đó trong root")
    print("4.kiểm thử Đổi tên Một gì đó trong root")
    print("phím Bất Kì Để Thoát Danh Sach")
    val = input("Enter your value: ")
    val = int(val)
    if(val == 1):
                  Ds4()
    elif(val == 2):
                  print("1. Xóa Folder chỉ định")
                  print("2. Xóa tệp chỉ định")
                  print("3. Xóa hỗn hợp nhiều tệp, file chỉ định")
                  val = input("Enter your value: ")
                  val = int(val)
                  if(val == 1):
                        Ds5(val)
                  if(val == 2):
                        Ds5(val)
                  if(val == 3):
                        n = input("Vui Lòng Nhập số lượng File/Folder bạn muốn Xóa: ")
                        n = int(n)
                        a=[]
                        b=[]
                        for i in range(n):
                              print("quá trình Xóa file/folder thứ ",(i+1))
                              print("1. Xóa Folder chỉ định")
                              print("2. Xóa tệp chỉ định")
                              a.append(input('lua chon của bạn: '))
                              a[i] = int(a[i])
                              b.append(input("Vui Lòng Nhập Tên Fordel/file thứ %d "% (i+1)))
                        driver.get("https://drive.google.com/drive/my-drive")
                        for i in range(n):
                              if(a[i]==1):
                                    chossen_Folder(b[i])
                              if(a[i]==2):
                                    chossen_File(b[i])
                              if(i == (n-1)):
                                    chossen_Delete(b[i],a[i])
                                    return
    elif(val == 3):            
            print("1. Dowload Folder chỉ định")
            print("2. Dowload tệp chỉ định")
            print("3. Dowload hỗn hợp nhiều tệp, file chỉ định")
            val = input("Enter your value: ")
            val = int(val)
            if(val ==1):
                  Ds6(val)
            if(val ==2):
                  Ds6(val)
            if(val ==3):
                  n = input("Vui Lòng Nhập số lượng File/Folder bạn muốn Tai: ")
                  n = int(n)
                  a=[]
                  b=[]
                  for i in range(n):
                        print("quá trình tải file/folder thứ ",(i+1))
                        print("1. Dowload Folder chỉ định")
                        print("2. Dowload tệp chỉ định")
                        a.append(input('lua chon của bạn: '))
                        a[i] = int(a[i])
                        b.append(input("Vui Lòng Nhập Tên Fordel/file thứ %d "% (i+1)))
                  driver.get("https://drive.google.com/drive/my-drive")
                  for i in range(n):
                        if(a[i]==1):
                              chossen_Folder(b[i])
                        if(a[i]==2):
                              chossen_File(b[i])
                        if(i == (n-1)):
                              chossen_Dowload(b[i],a[i])
                              return
                  return
            else:
                  return
    elif(val==4):
            print("1. Sửa Tên Folder chỉ định")
            print("2. Sửa Tên tệp chỉ định")
            val = input("Enter your value: ")
            val = int(val)
            if(val ==1):
                  val = input("Vui Lòng Nhập Tên Fordel bạn muốn Đổi Tên: ")
                  val1 =input("Vui Lòng Nhập Tên Fordel cuối cùng bạn muốn Đổi Tên: ")
                  editFolder(val, val1)
            if(val ==2):
                  val = input("Vui Lòng Nhập Tên File bạn muốn Đổi Tên: ")
                  val1 =input("Vui Lòng Nhập Tên File cuối cùng bạn muốn Đổi Tên: ")
                  editFile(val, val1)          
    else:
          return
def Ds4():
      print("==============kiểm thử Tạo Folder trong root============")
      print("1.TC1 Tên Folder được tạo chứa kí tự đặc biệt:")
      print("2.TC2 Tên Folder để trống:")
      print("3.TC3 Tên Folder được tạo chứa kí tự in hoa:")
      print("4.TC4 Tên Folder được tạo chứa trên 20 kí tự:")
      print("5.TC5 Tên Folder được tạo trùng với folder đã tồn tại:")
      print("6. Taoj Folder Bang Tay:")
      val = input("Enter your value: ")
      val = int(val)
      if(val == 1):
            addFolder("thu muc test @")
      if(val == 2):
            addFolder("")
      if(val == 3):
            addFolder("Thu muc test")
      if(val == 4):
            addFolder("thu muc test co thu muc test co thu muc test co thu muc test co thu muc test co thu muc test co thu muc test co thu muc test co thu muc test co thu muc test co thu muc test co thu muc test co")
      if(val == 5):
            addFolder("Thư mục test exist")
      if(val == 6):
            val = input("Nhập tên folder sẽ được tạo: ")
            addFolder(val)
def Ds5(x):
      print("==============kiểm thử Xóa Một gì Đó trong root")
      print("1. TC1 Tên Folder/file xóa có tồn tại trong hệ thống: ")
      print("2. TC2 Tên Folder/file xóa là giá trị rỗng: ")
      print("3. TC3 Tên Folder/file xóa không tồn tại trong hệ thống: ")
      print("4. Nhập Tay Tên Folder Xóa: ")
      val = input("Nhập lựa chọn: ")
      val = int(val)
      if(val == 1):
            if(x == 1):
                  removeFolder("Thư mục Test Xóa")
            if(x==2):
                  removeFile("File Test Xóa")
      if(val == 2):
            if(x == 1):
                  removeFolder("")
            if(x==2):
                  removeFile("")
      if(val == 3):
            if(x == 1):
                  removeFolder("Thư Mục Test Xóa Không Có")
            if(x==2):
                  removeFile("File Test Xóa Không Có")
      if(val == 4):
            val = input("Nhập tên: ")
            if(x == 1):
                  removeFolder(val)
            if(x==2):
                  removeFile(val)
def Ds6(x):
      print("======kiểm thử Tải Một gì đó trong root======")
      print("1. TC1 Tên Folder/file để Tải có trong hệ thống:")
      print("2. TC2 Tên Folder/file để Tải rỗng:")
      print("3. TC3 Tên Folder/file để Tải không có trong hệ thống:")
      print("4. Nhập Tay Tên Folder/file để Tải:")
      val = input("Nhập lựa chọn: ")
      val = int(val)
      if(val == 1):
            if(x == 1):
                  dowloadFolder("thumucDeTai")
            if(x==2):
                  dowloadFile("fileDeTai")
      if(val == 2):
            if(x == 1):
                  dowloadFolder("")
            if(x==2):
                  dowloadFile("")
      if(val == 3):
                  dowloadFile("point.jpg")
      
def Ds1():                                                  #menu Tổng
    print("")
    print("============================================================")
    print("Danh Sách Thao Tác Demo:")
    print("1.Kiểm Thử Đăng Nhập:")
    print("2.Kiểm Thử đối Tượng Folder,File:")
    print("3.Kiểm Thử Tìm Kiếm")
    print("4.Đăng Xuất Tài Khoản Google:")
    print("phím Bất Kì Để Thoát Danh Sach")
    val = input("Enter your value: ")
    val = int(val)
    if(val == 1):
          Ds2()
    elif(val == 2):
          Ds3()
    elif(val == 4):
          driver.delete_all_cookies()
          driver.get("https://accounts.google.com/ServiceLogin")
    elif(val == 3):
          driver.get("https://drive.google.com/drive/my-drive")
          val = input("Mời Bạn Nhập Từ Khóa Tìm Kiếm: ")
          timKiem(val)
    else:
        global checker
        checker = True
        print("Thoát!!")
checker = False
while(checker != True):
    Ds1()