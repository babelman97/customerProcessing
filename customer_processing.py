import threading
import time
import random
import queue
import csv
from datetime import datetime

# 全域變數定義
in_queue = queue.Queue()        # 存放新進顧客的佇列
temp_queue = queue.Queue()      # 存放待寫入檔案的顧客資料佇列
is_running = True              # 控制程式運行狀態的標誌
saving = False                 # 控制檔案寫入狀態的標誌
TOTAL_CUSTOMERS = 5            # 設定要處理的總顧客數
customers_generated = 0        # 追踪已生成的顧客數量
customers_processed = 0        # 追踪已處理的顧客數量

def generate_customer():
    """模擬顧客到達的生成器函數
    
    此函數會在隨機時間間隔內生成指定數量的顧客編號，並將其放入輸入佇列。
    - 使用 random.randint 生成 1-2 秒的隨機間隔
    - 生成 6 位數的隨機顧客編號
    - 當達到 TOTAL_CUSTOMERS 數量後停止生成
    """
    global is_running, customers_generated
    
    while is_running and customers_generated < TOTAL_CUSTOMERS:
        try:
            time.sleep(random.randint(1, 2))  # 模擬顧客到達的隨機時間間隔
            customer_no = random.randint(100000, 999999)  # 生成 6 位數顧客編號
            print(f"New Customer {customers_generated + 1}/{TOTAL_CUSTOMERS}: {customer_no}")
            in_queue.put(customer_no)  # 將顧客編號放入佇列
            customers_generated += 1
        except Exception as e:
            print(f"Error in generate_customer: {e}")
    
    print(f"Customer generation completed. Generated {customers_generated} customers.")
    is_running = False  # 設定結束標記

def read_card():
    """處理顧客資料的函數
    
    此函數從輸入佇列讀取顧客編號，模擬讀卡過程：
    - 從輸入佇列獲取顧客編號
    - 記錄處理時間戳記
    - 將處理後的資料放入暫存佇列等待寫入檔案
    - 追踪處理進度
    """
    global customers_processed
    
    while is_running or not in_queue.empty():
        try:
            if not in_queue.empty():
                customer_no = in_queue.get()  # 從佇列取出顧客編號
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 記錄處理時間
                print(f"Processing Customer {customers_processed + 1}/{TOTAL_CUSTOMERS}: {customer_no} at {timestamp}")
                
                temp_queue.put([timestamp, customer_no])  # 將處理後的資料放入暫存佇列
                customers_processed += 1
                in_queue.task_done()
                
                if customers_processed >= TOTAL_CUSTOMERS:
                    break
                    
            time.sleep(0.5)  # 模擬處理時間
        except Exception as e:
            print(f"Error in read_card: {e}")
    
    print("Card reading completed")

def save_to_file():
    """將處理後的資料寫入 CSV 檔案
    
    此函數負責：
    - 創建/覆寫 CSV 檔案
    - 寫入標題列
    - 從暫存佇列讀取資料並寫入檔案
    - 追踪寫入進度
    - 確保資料即時寫入磁碟
    """
    global saving
    records_saved = 0
    
    try:
        saving = True
        with open('customer_log.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Timestamp', 'Customer Number'])  # 寫入標題列
            
            while records_saved < TOTAL_CUSTOMERS:
                if not temp_queue.empty():
                    data = temp_queue.get()  # 從暫存佇列取出資料
                    writer.writerow(data)    # 寫入 CSV
                    f.flush()                # 確保資料立即寫入磁碟
                    records_saved += 1
                    print(f"Saving record {records_saved}/{TOTAL_CUSTOMERS}")
                    temp_queue.task_done()
                    
                    if records_saved >= TOTAL_CUSTOMERS:
                        break
                        
                time.sleep(0.5)
                
    except Exception as e:
        print(f"Error in save_to_file: {e}")
    finally:
        saving = False
    
    print(f"Data saving completed. Saved {records_saved} records.")

def show_status():
    """顯示系統當前狀態的監控函數
    
    定期顯示：
    - 已生成的顧客數量
    - 已處理的顧客數量
    - 佇列中等待處理的顧客數
    - 等待寫入的記錄數
    - 檔案寫入狀態
    """
    while is_running or customers_processed < TOTAL_CUSTOMERS:
        try:
            print("\nSystem Status:")
            print(f"Customers generated: {customers_generated}/{TOTAL_CUSTOMERS}")
            print(f"Customers processed: {customers_processed}/{TOTAL_CUSTOMERS}")
            print(f"Customers in queue: {in_queue.qsize()}")
            print(f"Records to save: {temp_queue.qsize()}")
            print(f"Saving status: {'Active' if saving else 'Inactive'}")
            time.sleep(2)  # 每 2 秒更新一次狀態
            
            if not is_running and customers_processed >= TOTAL_CUSTOMERS:
                break
                
        except Exception as e:
            print(f"Error in show_status: {e}")
    
    print("Status monitoring completed")

def main():
    """主程式入口點
    
    負責：
    - 創建並啟動所有工作執行緒
    - 等待所有執行緒完成
    - 顯示最終處理統計
    - 處理程式中斷
    """
    try:
        # 創建所有工作執行緒
        threads = [
            threading.Thread(target=generate_customer),
            threading.Thread(target=read_card),
            threading.Thread(target=save_to_file),
            threading.Thread(target=show_status)
        ]
        
        # 啟動所有執行緒
        for thread in threads:
            thread.start()
        
        # 等待所有執行緒完成
        for thread in threads:
            thread.join()
            
        print(f"\nProgram completed successfully:")
        print(f"Total customers generated: {customers_generated}")
        print(f"Total customers processed: {customers_processed}")
        
    except KeyboardInterrupt:
        print("\nProgram interrupted by user")
        global is_running
        is_running = False
    except Exception as e:
        print(f"Error in main: {e}")

if __name__ == "__main__":
    main()
