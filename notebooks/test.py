# =====================================================================
# 欄位偵查小程式：幫我們找出電視和電玩的真正欄位名稱
# =====================================================================
import pandas as pd

input_path = "../data/raw/YRBS_2007.csv"

print("正在讀取檔案以列出所有欄位名稱...")
df = pd.read_csv(input_path, nrows=5)  # 只讀5行，速度會極快

# 把所有欄位變成一個清單
all_columns = df.columns.tolist()

print("\n--- 檔案中的欄位名稱前 100 個列表 ---")
# 用迴圈一行一行印出來，方便我們閱讀
for i, col in enumerate(all_columns[:100]):
    print(f"欄位 {i+1}: {col}")