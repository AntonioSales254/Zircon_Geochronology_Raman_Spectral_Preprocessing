# Zircon Raman Spectral Analysis -- Version 7.0

**Advanced Framework for Automated, High‑Precision, Multi‑Method Raman
Processing of Zircon (ZrSiO₄)**

------------------------------------------------------------------------

## 📘 Overview

This repository contains the **Zircon Raman Spectral Analysis System
(v7.0)** --- a fully automated and publication‑ready pipeline for
processing Raman spectra of zircon.\
Designed for academic research, geochronology, metamictization studies,
and material characterization, the system includes:

-   Complete preprocessing workflow\
-   Multi‑method normalization and baseline correction\
-   Automatic peak detection with Gaussian fitting\
-   High‑precision FWHM and R² computation\
-   **7‑region spectral decomposition**\
-   **12‑combination combinatorial analysis**
-   Δ‑metric analysis to quantify normalization effects
-   Regional comparative analysis and scientific reporting

The system was engineered to be **robust, reproducible**, and aligned
with **state‑of‑the‑art Raman spectroscopy research**.

------------------------------------------------------------------------

# 🚀 Features in Detail

## 🔬 1. Preprocessing Capabilities

### **Baseline Correction Methods**

  ------------------------------------------------------------------------
  Method           Description                 When to Use
  ---------------- --------------------------- ---------------------------
  **airPLS**       Asymmetrically penalized    Non‑linear baselines,
                   LS; ideal for               geological samples
                   fluorescence‑rich spectra   

  **Polynomial**   Peak‑excluded polynomial    Smooth or slowly varying
                   regression                  baselines

  **Spline**       Cubic spline with peak      Balanced flexibility and
                   exclusion                   robustness
  ------------------------------------------------------------------------

------------------------------------------------------------------------

### **Normalization Techniques**

  ------------------------------------------------------------------------
  Method           Description                 Application
  ---------------- --------------------------- ---------------------------
  **Min‑Max**      Scales to \[0,1\]           Machine learning, direct
                                               comparisons

  **Area**         Normalization by total area Compensation for
                                               concentration differences

  **Peak**         Divides by tallest peak     Internal standard
                                               normalization

  **Vector (L2)**  Unit‑norm vector            PCA, clustering,
                                               multivariate models

  **None**         Raw spectrum                When absolute intensity
                                               matters
  ------------------------------------------------------------------------

------------------------------------------------------------------------

### **Smoothing**

-   **Savitzky--Golay filter**\
    Configurable window length + polynomial order

------------------------------------------------------------------------

## 📈 2. Peak Processing

### Features:

-   Adaptive prominence and height thresholds\
-   Automatic peak detection (`scipy.signal.find_peaks`)
-   Gaussian curve fitting\
-   Extraction of:
    -   Peak center (cm⁻¹)
    -   Peak height\
    -   Peak area\
    -   **Full Width at Half Maximum (FWHM)**\
    -   Fit quality: **R² (6 decimal places)**

------------------------------------------------------------------------

## 🧭 3. Spectral Region Classification (7 Regions)

Every peak is automatically mapped to one of the zircon vibrational
regions:

  Region       Range (cm⁻¹)   Mode
  ------------ -------------- ---------------------------------------------
  ν₃(SiO₄)     990--1020      Antisymmetric stretch (radiation‑sensitive)
  ν₁(SiO₄)     965--985       Symmetric stretch
  ν₂(SiO₄)     430--450       Bending mode
  External 1   195--210       Lattice mode
  External 2   210--220       Lattice mode
  External 3   220--230       Lattice mode
  External 4   350--365       Lattice mode

This supports **region‑based accuracy, stability, and damage
interpretation**.

------------------------------------------------------------------------

# 📊 4. Combinatorial Analysis (12 Method Combinations)

The software automatically evaluates all combinations of:

### Baseline Methods

-   AirPLS\
-   Polynomial\
-   Spline

### Normalization Methods

-   Min‑Max\
-   Area\
-   Peak\
-   Vector

Total: **3 × 4 = 12 combinations**

For each combination the system generates:

### Per‑Combination Outputs (3 files/combo):

1.  **Scientific_Results...csv** --- All peaks and metrics\
2.  **Scientific_Report...txt** --- Narrative analysis\
3.  **Regional_Analysis...csv** --- Metrics per spectral region

------------------------------------------------------------------------

### Global Outputs (5 files):

-   **Comparative_Summary_All_Combinations.csv**\
-   **Regional_Comparative_Analysis.csv** (84 rows: 12×7 regions)\
-   **Regional_Comparison_Report.txt**\
-   **Scientific_Conclusions_For_Article.txt**\
-   **Combinatorial_Analysis_Scientific_Log.log**

------------------------------------------------------------------------

# 📐 5. Precision Metrics

### Precision Levels:

-   **R²:** 6 decimal places\
-   **FWHM:** 4 decimal places\
-   **Center:** 6 decimals\
-   **Area:** 4 decimals

### Regional Metrics:

-   N peaks\
-   Mean / Std / CV% for FWHM, center, R²\
-   Composite regional score\
-   **Δ‑Metrics** (ΔFWHM, ΔCV) to quantify normalization impact

These metrics are designed for **rigorous scientific interpretation**
and publication‑quality output.

------------------------------------------------------------------------

# 🔥 6. Radiation Damage Analysis

Implements the diagnostic logic established by: - Ginster et al. 2019\
- Zhang et al. 2000\
- Dawson et al. 1971 (vibrational assignments)

Identifies: - Peak broadening\
- Center shifts\
- Loss of symmetry\
- Region‑specific metamictization evidence

Results are annotated in: - Peak datasets\
- Radiation damage summary\
- Scientific reporting

------------------------------------------------------------------------

# 📂 7. Project Directory Structure

    project/
    │── batch_raman_backup_v7.0.py
    │── raman_config.json
    │
    ├── csv_unificados/               # Input CSV spectra
    └── batch_reports/                # All automatic outputs
        ├── Combination_XX_.../
        ├── Comparative_Summary_All_...
        ├── Regional_Comparative_Analysis_...
        ├── Scientific_Conclusions_For_Article_...
        └── Logs

------------------------------------------------------------------------

# ▶️ 8. How to Run the System

## 1. Place input files

Put your Raman spectral files (`*.csv`) inside:

    csv_unificados/

## 2. Run the analysis

``` bash
python batch_raman_backup_v7.0.py
```

## 3. Results

All outputs are generated automatically in:

    batch_reports/

------------------------------------------------------------------------

# 📚 9. Key Scientific References

### Zircon Raman & Metamictization

-   Dawson et al., 1971 -- *Vibrational spectrum of zircon*\
-   Zhang et al., 2000 -- *Annealing of alpha‑decay damage*\
-   Ginster et al., 2019 -- *Radiation‑damage assessment*

### Baseline & Preprocessing

-   Zhang et al., 2010 -- airPLS\
-   Eilers & Boelens, 2005 -- ALS smoothing\
-   Ryabchykov et al., 2022 -- Processing errors to avoid

### Modern Raman & Chemometrics

-   Guo et al., 2021 -- Chemometric review\
-   Ibtehaz et al., 2023 -- Deep learning for Raman\
-   Sun et al., 2025 -- Zircon xenocrysts analysis

------------------------------------------------------------------------

# 👨‍💻 Author

**Antonio Said Webbe Sales**\
PhD Candidate, Materials Science\
Federal University of São Carlos (UFSCar) -- Sorocaba\
Advisor: Prof. Dr. Airton Natanael Coelho Dias

📧 **diasanc@ufscar.br**

------------------------------------------------------------------------

# 🏁 Version

**Version 7.0 --- Enhanced Regional Spectral Analysis (2025)**

------------------------------------------------------------------------

If you use this project in scientific work, please cite the author.
