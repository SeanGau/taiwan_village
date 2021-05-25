# DEMO
https://village.collective.tw

# 系統需求
* postgresql+postgis
* python3.7↑

# 使用說明
1. 
    ```bash
    pip install -r requirement.txt
    ```
2. 至 https://data.gov.tw/dataset/7438 下載圖資後轉為 geojson 格式
3. 執行 geojson2pgsql.py 將村里界圖匯入至postgresql
    ```bash
    python geojson2pgsql.py
    ```
4. 建立 config.py (可參考 config_example.py )
5. 
    ```bash
    python app.py
    ```
6. 前往 localhost:5000