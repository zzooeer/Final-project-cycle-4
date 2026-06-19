# Project Cycle 4: Physical Fighting and Screen Time

* **Repository**: 
* **Presentation Video**: *(請在此處貼上你們這次 Cycle 4 的雲端影片連結)*

---

## Student Information

* **Member Name**: 113370232 周以心

---

## Dataset Used

* `YRBS_2007.csv` (Youth Risk Behavior Surveillance System 2007, CDC)

---

## Selected Variables

* **Group Variable (A)**: `WhatIsYourSex` (Recoded: `Female`, `Male`)
* **Group Variable (B)**: `PhysicalFighting` (Recoded into `Fighting_Group`: `1_None`, `2_Occasional`, `3_Frequent`)
* **Response Variable**: `Total_Screen_Time` (Derived continuous variable: `TelevisionWatching` + `ComputerUse` hours)

---

## Benchmark Values

### One-Way ANOVA Summary (Fighting Group)
* **Sample Size ($n$)**: `1_None`: 8,628 | `2_Occasional`: 4,133 | `3_Frequent`: 394
* **Mean Screen Time (Hours/Day)**: 
  * `1_None`: 3.65 hrs
  * `2_Occasional`: 3.89 hrs
  * `3_Frequent`: 4.45 hrs

### Two-Way ANOVA Summary (Sex × Fighting Interaction)
* **Female Mean Progression**: `1_None` (3.39) $\rightarrow$ `2_Occasional` (3.73) $\rightarrow$ `3_Frequent` (4.30)
* **Male Mean Progression**: `1_None` (3.99) $\rightarrow$ `2_Occasional` (4.00) $\rightarrow$ `3_Frequent` (4.51)

---

## Short Project Questions

1. **One-Way ANOVA**: Is there a significant difference in the average daily total screen time among students with different physical fighting frequencies?
2. **Two-Way ANOVA**: Does the impact of physical fighting frequency on total screen time significantly depend on the student's gender (Interaction Effect)?

---

## Project Workflow

1. **Data Prep**: Loaded `YRBS_2007.csv`, handled missing values (`NaN`), and mapped categorical labels.
2. **Feature Engineering**: Converted ordinal screen codes to quantitative hours and combined them into `Total_Screen_Time`.
3. **One-Way Analysis**: 
   * Segmented data by `Fighting_Group` and computed subgroup metrics.
   * Conducted formal One-Way ANOVA and post-hoc Tukey's HSD test.
   * Generated synchronized-color **Boxplot** and **Violin Plot**.
4. **Two-Way Analysis**: 
   * Introduced `Sex` as the second factor to evaluate full factorial effects ($X_1 \times X_2$).
   * Conducted Two-Way ANOVA to isolate Main Effects and the Interaction Effect.
   * Generated **Interaction Plot** to visualize gender trajectory divergence.

---

## Short Final Conclusions

### One-Way ANOVA
Based on the YRBS 2007 data, daily screen time scales strictly upward with physical fighting frequencies (3.65 to 4.45 hours). The One-Way ANOVA yielded $p < 0.001$, strongly rejecting $H_0$. Post-hoc tests confirmed all pairwise differences are significant, proving that increased conflict involvement tracks with substantially higher digital screen exposure.

### Two-Way ANOVA & Interaction
The Two-Way ANOVA confirmed that the main effects of Sex ($p < 0.001$), Fighting ($p < 0.001$), and their **Interaction Effect** ($p < 0.05$) are all statistically significant. This tells us that behavioral escalation pathways are heterogeneous: for females, screen time increases strictly linearly with fighting, whereas males maintain a stagnant baseline from non-fighters to occasional fighters before experiencing an intense spike in the frequent fighting cohort.

---

## Project Files

* `notebook/01_Question.ipynb`
* `notebook/02_Descriptive_Statistics.ipynb`
* `notebook/03_ANOVA_Analysis.ipynb`
* `notebook/04_Two_Way_ANOVA.ipynb`
* `notebook/05_interpretation.md`
* `summary/summary.md`
* `references/references.md`
* `outputs/figures/screen_time_anova_boxplot.png`
* `outputs/figures/screen_time_anova_violinplot.png`
* `outputs/figures/screen_time_interaction_plot.png`
* `outputs/tables/anova_one_way_results.csv`
* `outputs/tables/anova_two_way_results.csv`
* `outputs/tables/screen_time_by_sex_and_fighting.csv`