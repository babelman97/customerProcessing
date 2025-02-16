# Customer Data Processing System

A multi-threaded customer data processing system implemented in Python, designed to simulate customer arrivals, data processing, and record keeping workflows.

## Features

- Simulates random customer arrivals
- Multi-threaded parallel processing
- Real-time status monitoring
- CSV file recording
- Automated processing workflow

## System Architecture

The system consists of four main components, each running in a separate thread:

1. **Customer Generator** (generate_customer)
   - Simulates random customer arrivals
   - Generates unique customer numbers
   - Controls total customer count

2. **Data Processor** (read_card)
   - Processes customer data
   - Records processing timestamps
   - Prepares data for storage

3. **Data Storage** (save_to_file)
   - Writes processed data to CSV file
   - Ensures data is safely stored
   - Tracks saving progress

4. **Status Monitor** (show_status)
   - Displays real-time system status
   - Monitors processing progress
   - Shows queue status

## Technical Features

- Uses Python standard library
- Multi-threaded parallel processing
- Queue management mechanism
- Exception handling
- CSV file operations

## System Requirements

- Python 3.6 or higher
- No additional packages required (standard library only)

## Usage

1. Direct execution:
   ```bash
   python customer_processing.py
   ```

2. Execution process:
   - Automatically generates 5 customer records
   - Displays real-time processing status
   - Automatically saves to customer_log.csv
   - Terminates automatically upon completion

3. Output file:
   - Generates customer_log.csv in execution directory
   - Contains timestamps and customer numbers

## Monitoring and Management

During execution, the program displays:
- Number of customers generated
- Number of customers processed
- Items pending in queue
- File writing status

## Notes

1. Program is designed to process a fixed number of customers (default 5)
2. Customer count can be adjusted via TOTAL_CUSTOMERS variable
3. Program can be interrupted using Ctrl+C
4. CSV file is overwritten on each execution

## Program Structure

```
customer_processing.py
├── generate_customer()  # Customer Generator
├── read_card()         # Data Processor
├── save_to_file()      # Data Storage
├── show_status()       # Status Monitor
└── main()             # Main Program Entry
```

## Contributing

Improvements and bug reports are welcome. You can contribute by:
1. Submitting Issues
2. Suggesting Improvements
3. Submitting Pull Requests

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

# 顧客資料處理系統

這是一個使用 Python 多執行緒實現的顧客資料處理系統，用於模擬顧客到達、資料處理和記錄保存的流程。

## 功能特點

- 模擬顧客隨機到達
- 多執行緒並行處理
- 即時狀態監控
- CSV 檔案記錄
- 自動化處理流程

## 系統架構

系統包含四個主要組件，每個組件運行在獨立的執行緒中：

1. **顧客生成器** (generate_customer)
   - 模擬顧客隨機到達
   - 生成唯一的顧客編號
   - 控制總顧客數量

2. **資料處理器** (read_card)
   - 處理顧客資料
   - 記錄處理時間戳記
   - 準備待保存的資料

3. **資料儲存器** (save_to_file)
   - 將處理後的資料寫入 CSV 檔案
   - 確保資料安全儲存
   - 追踪保存進度

4. **狀態監控器** (show_status)
   - 即時顯示系統狀態
   - 監控處理進度
   - 顯示佇列狀態

## 技術特點

- 使用 Python 標準庫
- 多執行緒並行處理
- 佇列管理機制
- 異常處理機制
- CSV 檔案操作

## 系統需求

- Python 3.6 或更高版本
- 僅使用 Python 標準庫，無需額外安裝套件

## 使用方式

1. 直接執行程式：
   ```bash
   python customer_processing.py
   ```

2. 程式執行過程：
   - 自動生成 5 位顧客資料
   - 即時顯示處理狀態
   - 自動儲存至 customer_log.csv 檔案
   - 完成後自動結束

3. 輸出檔案：
   - 在程式執行目錄生成 customer_log.csv
   - 包含時間戳記和顧客編號

## 監控和管理

程式執行時會顯示：
- 已生成的顧客數量
- 已處理的顧客數量
- 佇列中的待處理項目
- 檔案寫入狀態

## 注意事項

1. 程式設計為處理固定數量的顧客（預設 5 位）
2. 可透過修改 TOTAL_CUSTOMERS 變數調整處理數量
3. 執行過程中可使用 Ctrl+C 中斷程式
4. CSV 檔案會在每次執行時覆寫

## 程式架構

```
customer_processing.py
├── generate_customer()  # 顧客生成器
├── read_card()         # 資料處理器
├── save_to_file()      # 資料儲存器
├── show_status()       # 狀態監控器
└── main()             # 主程式入口
```

## 貢獻指南

歡迎提供改進建議和 Bug 回報。可以通過以下方式貢獻：
1. 提交 Issue
2. 提出改進建議
3. 提交 Pull Request

## 授權協議

本專案採用 MIT 授權協議。詳見 LICENSE 檔案。
