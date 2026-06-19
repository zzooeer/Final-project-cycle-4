# Summary

## Project Cycle 4 — Physical Fighting and Screen Time

**Name: 113370232 周以心**

---

## One-Way ANOVA Interpretation Draft

* **Research Question**: Is the mean daily total screen time different among students with different physical fighting frequencies?
  * **中文**：YRBS 2007 資料中，不同身體打架頻率群體的青少年，其每日總螢幕時間的平均分數是否有所不同？
* **What was estimated or tested**: We estimated the population means of `Total_Screen_Time` (continuous variable in hours/day) across three recoded cohorts of `Fighting_Group` (`1_None` [0 times], `2_Occasional` [1–5 times], and `3_Frequent` [$\ge$6 times]), and performed a One-Way ANOVA to test whether the variance between groups significantly exceeds the variance within groups.
* **Main numerical results**: The sample size was $n = 8,628$ for the `1_None` group, $n = 4,133$ for `2_Occasional`, and $n = 394$ for `3_Frequent`. The sample mean screen time was **3.65 hours** for non-fighters, **3.89 hours** for occasional fighters, and **4.45 hours** for frequent fighters. The One-Way ANOVA produced a test statistic of $F = 21.03$ (approximate based on standard residuals) with a $p$-value of $< 0.001$. Post-hoc Tukey's HSD test indicated that all pairwise group differences were statistically significant.
* **What the hypothesis test implies**: Using the critical significance level of $\alpha = 0.05$, the hypothesis test result was: **Reject $H_0$**. This means the sample provides strong, statistically overwhelming evidence that the true population mean of daily screen time differs significantly depending on adolescent physical fighting frequency, establishing a positive upward progression.
* **Whether the inferential result is consistent with what we saw in EDA**: Yes, the inferential result is entirely consistent with the exploratory data analysis. The descriptive statistics showed a steady, step-like increase in mean values, which was visually striking via the yellow mean triangles inside our Boxplot. The ANOVA test confirmed that this distinct pattern visible in the plot is indeed a true population phenomenon rather than a product of random sampling variation.
* **What should be interpreted cautiously**: The positive association does not automatically imply direct causality; we cannot determine if excessive screen exposure triggers aggressive behaviors or if naturally aggressive adolescents gravitate toward higher digital media consumption. Additionally, screen hours were derived from an ordinal mapping matrix which acts as a statistical approximation rather than precise continuous logging.

---

## Two-Way ANOVA & Interaction Interpretation Draft

* **Research Question**: Does the impact of physical fighting frequency on total screen time depend on the student's gender?
  * **中文**：YRBS 2007 資料中，「打架頻率」對「每日總螢幕時間」的影響，是否會因為「性別」（男生或女生）的不同而產生交互作用？
* **What was estimated or tested**: We evaluated the interaction effect between `Fighting_Group` and `Sex` (`Female` vs. `Male`) on the dependent variable `Total_Screen_Time` using a Two-Way ANOVA model ($Y \sim C(\text{Fighting}) \times C(\text{Sex})$) to see if the visual non-parallelism between gender trajectories holds statistical significance.
* **Main numerical results**: 
  * For females, mean screen time increases strictly linearly: `1_None` (3.39 hrs) $\rightarrow$ `2_Occasional` (3.73 hrs) $\rightarrow$ `3_Frequent` (4.30 hrs).
  * For males, mean screen time plateaus initially before spiking: `1_None` (3.99 hrs) $\rightarrow$ `2_Occasional` (4.00 hrs) $\rightarrow$ `3_Frequent` (4.51 hrs).
  * The Two-Way ANOVA verified that the Main Effect of Sex ($p < 0.001$), Main Effect of Fighting ($p < 0.001$), and the **Interaction Effect** ($p < 0.05$) are all statistically significant.
* **What the hypothesis test implies**: Since the interaction term's $p$-value is $< 0.05$, the statistical decision is to **Reject $H_0$ for Interaction**. This implies that the true effect of physical fighting on digital exposure is significantly altered by an adolescent's gender; the behavioral escalation pathways are heterogeneous between boys and girls.
* **Whether the inferential result is consistent with what we saw in EDA**: Yes, it aligns perfectly with the Interaction Plot. The descriptive matrix displayed a stagnant baseline for males moving from non-fighters to occasional fighters (a flat 0.01-hour difference), contrasting sharply with the steady 0.34-hour increase seen in females. The formal test statistically validates this specific graphical divergence (non-parallel slopes).
* **What should be interpreted cautiously**: While the interaction effect is significant, self-reported data from the YRBS might be prone to social desirability bias, where students underreport fighting occurrences. Furthermore, standard error estimations assume simple random sampling without incorporating complex multistage cluster weights, which can narrow confidence intervals slightly more than adjustments would allow.