# References & Analytical Decisions

## Project Cycle 4 — Physical Fighting and Screen Time

**Name: 113370232 周以心**

---

## 1. 資料來源 | Data Source

* **Dataset**: Youth Risk Behavior Surveillance System (YRBS) 2007
* **主辦單位**: Centers for Disease Control and Prevention (CDC)
* **原始檔案**: `YRBS_2007.csv`（共 14,041 筆，103 個變數）
* **官方網站**: [https://www.cdc.gov/yrbs](https://www.cdc.gov/yrbs)
* **官方報告**: CDC. (2008). *Youth Risk Behavior Surveillance — United States, 2007*. MMWR Surveillance Summaries, 57(SS-4). [https://www.cdc.gov/mmwr/preview/mmwrhtml/ss5704a1.htm](https://www.cdc.gov/mmwr/preview/mmwrhtml/ss5704a1.htm)

---

## 2. 變數編碼 | Variable Coding

### Group Variable (A) — `WhatIsYourSex`
根據 YRBS 2007 官方問卷編碼定義：
| 原始編碼 | 官方定義 | 本專題轉換標籤 |
| :---: | :--- | :---: |
| `1.0` | Female（女性） | `Female` |
| `2.0` | Male（男性） | `Male` |

* **來源**: `04_Two_Way_ANOVA.ipynb` 步驟 1 資料清理流程。

### Group Variable (B) — `PhysicalFighting`
根據 YRBS 2007 官方問卷，題目為：*"During the past 12 months, how many times were you in a physical fight?"*
| 原始編碼 | 官方定義次數 | 本專題重編碼群組 (`Fighting_Group`) |
| :---: | :--- | :---: |
| `1` | 0 times | `1_None` |
| `2` | 1 time | `2_Occasional` |
| `3` | 2 to 3 times | `2_Occasional` |
| `4` | 4 to 5 times | `2_Occasional` |
| `5` | 6 to 7 times | `3_Frequent` |
| `6` | 8 to 9 times | `3_Frequent` |
| `7` | 10 to 11 times | `3_Frequent` |
| `8` | 12 or more times | `3_Frequent` |

* **來源**: `01_Question.ipynb` 變數定義與 `02_Descriptive_Statistics.ipynb` 分組說明。

### Response Variables — `TelevisionWatching` & `ComputerUse`
* **TV 題目**: *"On an average school day, how many hours do you watch TV?"*
* **Computer/Game 題目**: *"On an average school day, how many hours do you play video or computer games or use a computer for something that is not school work?"*

本專題將這兩個原始有序代號（1–7）還原映射為實際小時數，藉此加總計算出反應變數 `Total_Screen_Time`：
| 原始編碼 | 官方小時定義 | 本專題映射轉換數值（小時） |
| :---: | :--- | :---: |
| `1` | I do not watch TV / use computer | `0.0` |
| `2` | Less than 1 hour per day | `0.5` |
| `3` | 1 hour per day | `1.0` |
| `4` | 2 hours per day | `2.0` |
| `5` | 3 hours per day | `3.0` |
| `6` | 4 hours per day | `4.0` |
| `7` | 5 or more hours per day | `5.0` |

* **數據還原公式**: `Total_Screen_Time = TV_Hours + Game_Hours`

---

## 3. 分析樣本與排除條件 | Sample & Drop Decisions

* **分組最終有效樣本數 ($n$)**:
  * **1_None**: 8,628 筆
  * **2_Occasional**: 4,133 筆
  * **3_Frequent**: 394 筆
* **排除條件**: 凡是性別欄位、打架欄位、看電視欄位或電腦使用欄位，任一出現缺失值（`NaN`）或填答為「未提供/Unknown」者，基於完整個案分析法（Complete Case Analysis）予以刪除。
* **處理流程（參考 `04_Two_Way_ANOVA.ipynb`）**:
  ```python
  df_selected = df_raw[["WhatIsYourSex", "PhysicalFighting", "TelevisionWatching", "ComputerUse"]].dropna()
  # 過濾掉打架編碼中的不確定/無效代號，並剔除性別缺失
  ```
  * 步驟 A：使用 `df[['WhatIsYourSex', 'PhysicalFighting', 'TelevisionWatching', 'ComputerUse']].dropna()` 篩選核心變數並剔除缺失值。
  * 步驟 B：過濾掉打架編碼中的不確定與無效代號，並確保性別標籤正確對齊。

  ---

## 4. 方法選擇 | Method Selection

### 4a. One-Way ANOVA（單因子變異數分析）
* **適用條件**: 自變數為 3 組以上的類別變數 (`Fighting_Group`)，反應變數為連續變數 (`Total_Screen_Time`)。
* **使用套件**: `statsmodels.formula.api.ols` 搭配 `statsmodels.stats.anova.anova_lm`
* **檢定方向**: Two-sided（雙尾檢定）
* **顯著水準**: $\alpha = 0.05$
* **假設（Hypotheses）**:
  * $H_0: \mu_{\text{None}} = \mu_{\text{Occasional}} = \mu_{\text{Frequent}}$
  * $H_1$: 有至少一組群體之間的每日總螢幕時間平均數不相等。

### 4b. Two-Way ANOVA with Interaction（雙因子變異數分析與交互作用）
* **適用條件**: 同時探討兩個類別自變數（`Fighting_Group` 與 `Sex`）對單一連續反應變數的共同影響與相互干擾。
* **使用套件**: `ols('Total_Screen_Time ~ C(Fighting_Group) * C(Sex)', data=df).fit()`
* **檢定方向**: Two-sided（雙尾檢定）
* **顯著水準**: $\alpha = 0.05$
* **交互作用檢定假設（Hypotheses）**:
  * $H_0$: 打架頻率對螢幕時間的影響，不會因為性別不同而有所改變（兩因素獨立，趨勢線平行）。
  * $H_1$: 打架頻率對螢幕時間的影響，會因為性別不同而有所差異（存在交互作用，趨勢線非平行）。

---

## 5. 考慮的假設與檢定統計前提 | Assumptions Considered

### One-Way & Two-Way ANOVA 假設檢驗說明

| 統計假設項目 | 是否滿足 | 本專題資料處理與應變說明 |
| :--- | :---: | :--- |
| **獨立觀測 (Independence)** | ✅ | YRBS 採用全國性分層抽樣，每位高中生獨立作答，觀測值彼此獨立。 |
| **類別自變數 (Categorical X)** | ✅ | 打架頻率（3組）與性別（2組）皆為標準類別因子。 |
| **連續反應變數 (Continuous Y)** | ⚠️ | 原始資料為有序尺度（1–7），經映射還原為預估小時數作為連續變數的近似（Approximation），此為社會科學常見之處理方式。 |
| **常態性假設 (Normality)** | ✅ | 雖然各組內部的螢幕時間呈現右偏態（如 Violin Plot 所示），但本專案總樣本數遠大於 12,000 筆，根據**中央極限定理 (CLT)**，樣本平均數之抽樣分佈極度趨近常態，ANOVA 檢定對此具備極高韌性。 |
| **等變異數假設 (Homoscedasticity)**| ⚠️ | 由於各組樣本數相差較大（`3_Frequent` 僅 394 筆），本專案採用了 `statsmodels` 內建的 $typ=2$ ANOVA 表格進行穩健估計，並結合事後檢定來謹慎評估。 |

---

## 6. 統計方法參考文獻 | Statistical References

* Diez, D., Çetinkaya-Rundel, M., & Barr, C. (2019). *OpenIntro Statistics* (4th ed.). OpenIntro. [https://www.openintro.org/book/os/](https://www.openintro.org/book/os/)
* Seabold, S., & Perktold, J. (2010). Statsmodels: Econometric and statistical modeling with Python. *Proceedings of the 9th Python in Science Conference*.
* Waskom, M. L. (2021). seaborn: statistical data visualization. *Journal of Open Source Software*, 6(60), 3021. [https://doi.org/10.21105/joss.03021](https://doi.org/10.21105/joss.03021)

---

## 7. 程式碼檔案對照 | Code File Reference

| 專案執行步驟 | 對應實作檔案路徑 | 主要產出與核心目標 |
| :--- | :--- | :--- |
| **1. 研究問題定義** | `notebook/01_Question.ipynb` | 定義研究假說、探討 YRBS 變數結構。 |
| **2. 資料清理與分組** | `notebook/02_Descriptive_Statistics.ipynb` | 處理缺失值、將打架頻率進行三群組編碼。 |
| **3. 單因子推論與視覺化** | `notebook/03_ANOVA_Analysis.ipynb` | 執行 One-Way ANOVA、匯出對齊配色的 Boxplot 與 Violin Plot。 |
| **4. 延伸交互作用探討** | `notebook/04_Two_Way_ANOVA.ipynb` | 導入性別因子、執行 Two-Way ANOVA 並繪製交互作用折線圖。 |
| **5. 統計學術報告** | `notebook/05_interpretation.md` | 撰寫期末論文規格的完整數據分析與統計脈絡解讀。 |
| **6. 專案精華摘要** | `summary/summary.md` | 提供中英文對照的條列式精簡決策摘要。 |