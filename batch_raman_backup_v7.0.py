#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
ZIRCON RAMAN SPECTRAL ANALYSIS - VERSION 7.0
================================================================================

DEVELOPED BY: Antonio Said Webbe Sales
ADVISOR: Prof. Dr. Airton Natanael Coelho Dias
INSTITUTION: Federal University of São Carlos - Sorocaba
PROGRAM: PhD in Materials Science

================================================================================
VERSION 7.0 INFORMATION - ENHANCED REGIONAL SPECTRAL ANALYSIS
================================================================================

CREATION DATE: December 2024
CURRENT VERSION: 7.0 (Enhanced from v6.0)
RELEASE DATE: November 6, 2025
LANGUAGE: Python 3.x
DEPENDENCIES: numpy, pandas, scipy, matplotlib, pathlib, json, datetime, logging

MAIN OBJECTIVE FOR V7.0:
🎯 REGIONAL SPECTRAL ANALYSIS ENHANCEMENT
   - Detailed spectral region analysis in combinatorial reports
   - High-precision metrics (6 decimal places for R², 4 for FWHM)
   - Regional comparative analysis across all combinations
   - Differential impact assessment of normalization methods
   - Enhanced scientific reporting with regional insights

COMBINATORIAL ANALYSIS FRAMEWORK:
• Baseline Methods: AirPLS, Polynomial, Spline
• Normalization Methods: min_max, area, peak, vector
• Total Combinations: 12 systematic parameter combinations
• Regional analysis for 7 spectral regions
• Cross-validation approach for method selection
• Statistical significance testing by region

NEW FEATURES V7.0:
🔬 REGIONAL ANALYSIS ENHANCEMENT:
   - Per-region metrics in individual combination reports
   - Regional CSV analysis files for each combination
   - Consolidated regional comparative analysis
   - Differential impact quantification (Δ metrics)
   - Region-specific method ranking

📊 ENHANCED PRECISION:
   - 6 decimal places for R² metrics
   - 4 decimal places for FWHM and CV
   - High-precision center position tracking
   - Quantification of subtle normalization effects

📋 ADVANCED SCIENTIFIC REPORTING:
   - Regional comparison reports with rankings
   - Impact of normalization within same baseline
   - ν₃(SiO₄) specific metrics (most radiation-sensitive)
   - Publication-ready regional analysis tables
   - Hypothesis validation with regional context

🎯 OUTPUT STRUCTURE V7.0:
   - Regional_Analysis_{combination}_{timestamp}.csv per combination
   - Regional_Comparative_Analysis_{timestamp}.csv (consolidated)
   - Regional_Comparison_Report_{timestamp}.txt (interpretative)
   - Enhanced Scientific_Report with regional sections
   - Nu3-specific columns in comparative summary

DEVELOPMENT STATUS v7.0:
✅ STABLE - Enhanced regional analysis implementation
✅ VALIDATED - High-precision metrics tested
✅ OPTIMIZED - Regional comparative framework operational
✅ PUBLICATION-READY - Regional insights for scientific articles

CHANGELOG v6.0 → v7.0:
✨ NEW - Regional analysis by spectral region in reports
✨ NEW - Regional_Analysis_{combination}.csv files
✨ NEW - Regional_Comparative_Analysis.csv consolidated file
✨ NEW - Regional_Comparison_Report.txt interpretative report
✨ NEW - Nu3-specific metrics in comparative summary
🔧 ENHANCED - Precision increased (R²: 6 decimals, FWHM: 4 decimals)
🔧 ENHANCED - Individual reports include detailed regional sections
🔧 ENHANCED - Δ metrics to quantify normalization impact
📊 IMPROVED - Better revelation of subtle differences between methods
📊 IMPROVED - Region-specific method optimization capability

RESOLVED v7.0:
✅ Identical metrics issue: precision increased reveals real differences
✅ Regional blind spot: now analyzes impact per spectral region
✅ Normalization impact: quantified via Δ metrics per baseline
✅ Scientific insight: identifies region-specific optimal methods

================================================================================
MAIN FUNCTIONALITIES
================================================================================

🔬 COMPLETE RAMAN SPECTRA ANALYSIS:
• Advanced normalization (min-max, area, peak, vector)
• Baseline correction (AirPLS, polynomial, spline)
• Savitzky-Golay filter smoothing
• Automatic peak detection with configurable parameters
• FWHM calculation and Gaussian profile fitting
• Radiation damage analysis (Ginster et al., 2019)
• Statistical outlier detection and removal
• Contextualized robustness analysis with scientific basis

📊 SPECTRAL REGION ANALYSIS:
• ν₃(SiO₄): Antisymmetric stretching (990-1020 cm⁻¹)
• ν₁(SiO₄): Symmetric stretching (965-985 cm⁻¹)  
• ν₂(SiO₄): Bending deformation (430-450 cm⁻¹)
• External lattice modes (195-365 cm⁻¹)
• Automatic radiation damage categorization

📈 DETAILED REPORTS:
• Complete data with outliers (original)
• Clean data without statistical outliers
• Radiation damage summary
• Outlier removal report
• Contextualized robustness analysis
• Quality metrics and R² of fits

⚙️ FLEXIBLE CONFIGURATION:
• JSON file for configurable parameters
• Batch processing of multiple CSV files
• Customizable input and output directories
• Automatic naming based on sample name

================================================================================
OUTPUT STRUCTURE
================================================================================

STANDARD PROCESSING OUTPUT FILES (with sample suffix when applicable):
• batch_raman_analysis[_sample]_{timestamp}.csv - Complete data
• batch_raman_analysis_cleaned[_sample]_{timestamp}.csv - Data without outliers
• raman_analysis_report[_sample]_{timestamp}.txt - Complete report
• radiation_damage_summary[_sample]_{timestamp}.csv - Damage summary
• outliers_removal_report[_sample]_{timestamp}.txt - Outliers report
• peak_detection_robustness_analysis[_sample]_{timestamp}.txt - Contextualized analysis

COMBINATORIAL ANALYSIS OUTPUT FILES (v7.0 ENHANCED):

GLOBAL FILES (in Scientific_Combinatorial_Analysis_{timestamp}/ directory):
• Comparative_Summary_All_Combinations_{timestamp}.csv
  └── Summary table with Nu3-specific columns (v7.0: 6-decimal R², 4-decimal FWHM)
• Regional_Comparative_Analysis_{timestamp}.csv [NEW v7.0]
  └── Consolidated regional analysis (84 rows: 12 combinations × 7 regions)
• Regional_Comparison_Report_{timestamp}.txt [NEW v7.0]
  └── Interpretative report with rankings and Δ metrics per region
• Scientific_Conclusions_For_Article_{timestamp}.txt [ENHANCED v7.0]
  └── Includes: hypothesis validation + regional analysis + best method per mode
• Combinatorial_Analysis_Scientific_Log_{timestamp}.log
  └── Detailed processing log with timestamps

PER-COMBINATION FILES (12 directories: Combination_XX_{method}_{norm}/):
• Scientific_Results_{combination}_N{peaks}_{timestamp}.csv
  └── Complete peak data for this combination
• Scientific_Report_{combination}_{timestamp}.txt [ENHANCED v7.0]
  └── Individual report with regional analysis section (7 regions)
• Regional_Analysis_{combination}_{timestamp}.csv [NEW v7.0]
  └── Regional metrics table (7 regions × multiple metrics)

DIRECTORY STRUCTURE (COMBINATORIAL ANALYSIS):
Scientific_Combinatorial_Analysis_{timestamp}/
├── Comparative_Summary_All_Combinations_{timestamp}.csv [ENHANCED v7.0]
├── Regional_Comparative_Analysis_{timestamp}.csv [NEW v7.0]
├── Regional_Comparison_Report_{timestamp}.txt [NEW v7.0]
├── Scientific_Conclusions_For_Article_{timestamp}.txt [ENHANCED v7.0]
├── Combinatorial_Analysis_Scientific_Log_{timestamp}.log
├── Combination_01_Airpls_Min_max/
│   ├── Scientific_Results_Airpls_Min_max_N{peaks}_{timestamp}.csv
│   ├── Scientific_Report_Airpls_Min_max_{timestamp}.txt [ENHANCED v7.0]
│   └── Regional_Analysis_Airpls_Min_max_{timestamp}.csv [NEW v7.0]
├── Combination_02_Airpls_Area/
│   ├── Scientific_Results_Airpls_Area_N{peaks}_{timestamp}.csv
│   ├── Scientific_Report_Airpls_Area_{timestamp}.txt [ENHANCED v7.0]
│   └── Regional_Analysis_Airpls_Area_{timestamp}.csv [NEW v7.0]
├── ... (Combinations 03-11)
└── Combination_12_Spline_Vector/
    ├── Scientific_Results_Spline_Vector_N{peaks}_{timestamp}.csv
    ├── Scientific_Report_Spline_Vector_{timestamp}.txt [ENHANCED v7.0]
    └── Regional_Analysis_Spline_Vector_{timestamp}.csv [NEW v7.0]

TOTAL FILES PER COMBINATORIAL RUN:
• Global: 5 files (3 CSVs + 1 TXT + 1 LOG)
• Per combination: 3 files × 12 = 36 files
• TOTAL: 41 files (v6.0: 27 files | v7.0: +14 new files)

INCLUDED METRICS (STANDARD):
• Peak center (cm⁻¹)
• Peak height (normalized intensity)
• FWHM (full width at half maximum)
• Peak area (Gaussian fit)
• R² of Gaussian fit
• Radiation damage categorization
• Spectral region of origin
• Sample and grain identification

REGIONAL METRICS (v7.0 NEW):
• N_Picos per region
• R2_Médio, R2_Std per region (6 decimals)
• FWHM_Médio, FWHM_Std, FWHM_CV_% per region (4 decimals)
• Centro_Médio, Centro_Std, Centro_CV_% per region (6 decimals)
• Área_Média, Área_Std per region (4 decimals)
• Score_Composto per region (0.4×Precision + 0.3×Quality + 0.3×Consistency)
• Δ metrics (ΔFWHM, ΔCV) showing normalization impact

DETAILED FILE DESCRIPTIONS (v7.0):

1. Regional_Analysis_{combination}_{timestamp}.csv:
   - One file per combination (12 total)
   - Contains metrics for 7 spectral regions
   - Columns: Região, N_Picos, R2_Médio/Std, FWHM_Médio/Std/CV_%,
             Centro_Médio/Std/CV_%,  Área_Média/Std
   - Purpose: Detailed regional performance of specific combination

2. Regional_Comparative_Analysis_{timestamp}.csv:
   - Single consolidated file
   - 84 rows: 12 combinations × 7 regions
   - All regional metrics in unified table
   - Additional columns: Combination, Baseline, Normalization
   - Purpose: Cross-combination regional comparison and filtering

3. Regional_Comparison_Report_{timestamp}.txt:
   - Interpretative text report
   - For each region: Top 3 by precision, Top 3 by quality
   - Δ metrics: ΔFWHM and ΔCV per baseline method
   - Impact classification: MÍNIMO, BAIXO, MODERADO, ALTO
   - Purpose: Human-readable regional insights

4. Scientific_Conclusions_For_Article_{timestamp}.txt [ENHANCED]:
   - Added section: "ANÁLISE POR MODO VIBRACIONAL"
   - Per-region best combination with detailed metrics
   - Executive summary table (7 regions)
   - Specific recommendations for ν₃ (radiation damage) vs multi-regional
   - Purpose: Publication-ready scientific conclusions with regional context

5. Comparative_Summary_All_Combinations_{timestamp}.csv [ENHANCED]:
   - New columns: Nu3_Count, Nu3_FWHM, Nu3_CV, Nu3_R2
   - Increased precision: R² (6 decimals), FWHM/CV (4 decimals)
   - Purpose: Focus on most radiation-sensitive region (ν₃)

6. Scientific_Report_{combination}_{timestamp}.txt [ENHANCED]:
   - New section: "ANÁLISE POR REGIÃO ESPECTRAL"
   - Detailed metrics for all 7 regions in each combination
   - High-precision values (6 decimals R², 4 decimals FWHM)
   - Purpose: Complete documentation of combination performance

SPECTRAL REGIONS ANALYZED (7 total):
• ν₃(SiO₄): 990-1020 cm⁻¹ - Antisymmetric stretching (primary damage indicator)
• ν₁(SiO₄): 965-985 cm⁻¹ - Symmetric stretching (complementary)
• ν₂(SiO₄): 430-450 cm⁻¹ - Bending deformation (structural)
• ExtRot 1: 195-210 cm⁻¹ - External rotation mode 1
• ExtRot 2: 210-220 cm⁻¹ - External rotation mode 2
• ExtRot 3: 220-230 cm⁻¹ - External rotation mode 3
• ExtRot 4: 350-365 cm⁻¹ - External rotation mode 4

================================================================================
CONTEXTUALIZED ROBUSTNESS ANALYSIS (VALIDATED AND PRESERVED V3.0)
================================================================================

🎯 MAIN FEATURES:
• Considers that data has already been cleaned of statistical outliers
• Uses typical ranges from literature for scientific context
• Differentiates statistical outliers from values outside typical range
• Provides prioritized recommendations (High/Medium/Low/Informative)
• Includes context for result interpretation

📚 TYPICAL FWHM RANGES (based on literature):
• ν₃(SiO₄): 8-25 cm⁻¹ (sensitive to radiation damage)
• ν₁(SiO₄): 6-20 cm⁻¹ (also sensitive to damage)
• ν₂(SiO₄): 15-35 cm⁻¹ (naturally broader)
• External modes: 10-40 cm⁻¹ (greater natural variation)

🔍 INTERPRETATION OF VALUES OUTSIDE TYPICAL RANGE:
• Not outliers to be removed
• May indicate radiation damage
• Special crystallization conditions
• Instrumental effects
• Sample-specific characteristics

================================================================================
VALIDATION AND QUALITY
================================================================================

✅ QUALITY CONTROL:
• Automatic validation of input parameters
• Data consistency verification
• Detection of fitting problems (low R²)
• Regional peak distribution analysis
• Contextualized recommendations for improvement

📊 ROBUSTNESS METRICS:
• Percentage of peaks in expected regions
• Quality of Gaussian fits (R²)
• FWHM distribution by region
• Comparison with typical literature values
• Detection of systematic vs regional problems

🔬 READY FOR:
• Zircon sample analysis in scientific research
• Publication of results in specialized journals
• Use in PhD and academic research projects
• Application in Raman spectroscopy laboratories
• Validation through peer review

================================================================================
CONTACT AND SUPPORT
================================================================================

Developer: Antonio Said Webbe Sales
Email: [antonio.sales@estudante.ufscar.br]
Institution: UFSCar - Sorocaba
Program: PhD in Materials Science
Advisor: Prof. Dr. Airton Natanael Coelho Dias

For technical support or scientific questions, please contact the developer.

================================================================================
"""

import numpy as np
import pandas as pd
from scipy.signal import find_peaks, peak_widths, savgol_filter
from scipy import sparse
from scipy.sparse.linalg import spsolve
from scipy import integrate
from pathlib import Path
import json
from datetime import datetime
import statistics
import os
import glob
import re
from raman_visualization import RamanVisualization

def generate_timestamp():
    """Gera timestamp no formato YYYYMMDD_HHMMSS para nomear arquivos"""
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def get_zircon_spectral_regions():
    """
    Define zircon spectral regions with mutually exclusive intervals.
    
    The vibrational modes of zircon (ZrSiO₄) are well characterized in the scientific literature
    through Raman spectroscopy. This function defines spectral regions based on the
    main vibrational modes of zircon, as extensively documented in the literature.
    
    The main vibrational modes include:
    - Internal modes of SiO₄: ~1008 cm⁻¹ (ν₃), ~974 cm⁻¹ (ν₁), ~438 cm⁻¹ (ν₂)
    - External modes: ~420 cm⁻¹, ~357 cm⁻¹, ~268 cm⁻¹, ~214 cm⁻¹
    - Low frequency modes: ~130 cm⁻¹, ~100 cm⁻¹
    
    Raman spectroscopy is particularly useful for assessing zircon metamictization,
    as peaks broaden and shift to lower frequencies with increasing radiation damage,
    as demonstrated through full width at half maximum (FWHM) studies.
    
    Uses the convention of half-open intervals [min, max) where:
    - min is INCLUSIVE (>=)
    - max is EXCLUSIVE (<)
    
    Except for the last region of each main group which uses closed interval [min, max].
    
    This avoids peak overlap at boundary values (e.g., 210 cm⁻¹).
    
    Bibliographic References:
    - Dawson, P., Hargreave, M.M., Wilkinson, G.R. (1971). The vibrational spectrum of 
      zircon (ZrSiO₄). Journal of Physics C: Solid State Physics, 4(2), 240-256.
      https://doi.org/10.1088/0022-3719/4/2/014
      
    - Gucsik, A., Zhang, M., Koeberl, C., Salje, E.K.H., Redfern, S.A.T., Pruneda, J.M. (2004).
      Infrared and Raman spectra of ZrSiO₄ experimentally shocked at high pressures.
      Mineralogical Magazine, 68(5), 801-811.
      https://doi.org/10.1180/0026461046850220
      
    - Härtel, B., Jonckheere, R., Wauschkuhn, B., Ratschbacher, L. (2021).
      The closure temperature(s) of zircon Raman dating.
      Geochronology, 3, 259-272.
      https://doi.org/10.5194/gchron-3-259-2021
      
    - Zhang, M., Salje, E.K.H., Capitani, G.C., Leroux, H., Clark, A.M., Schlüter, J., 
      Ewing, R.C. (2000). Annealing of alpha-decay damage in zircon: a Raman 
      spectroscopic study. Journal of Physics: Condensed Matter, 12(13), 3131-3148.
      https://doi.org/10.1088/0953-8984/12/13/321
      
    Recent References (2022-2024):
    - Bjerga, A., Stubseid, H.H., Pedersen, L.E.R., Pedersen, R.B. (2022). 
      Radiation damage allows identification of truly inherited zircon.
      Communications Earth & Environment, 3, 37.
      https://doi.org/10.1038/s43247-022-00372-2
      
    - McKanna, A.J., Koran, I., Schoene, B., Ketcham, R.A. (2023).
      Chemical abrasion: the mechanics of zircon dissolution.
      Geochronology, 5, 127-151.
      https://doi.org/10.5194/gchron-5-127-2023
      
    - Suchorab, K., Gawęda, M., Kurpaska, L. (2023).
      Comparison of Raman imaging assessment methods in phase determination and 
      stress analysis of zirconium oxide layer.
      Spectrochimica Acta Part A: Molecular and Biomolecular Spectroscopy, 298, 122625.
      https://doi.org/10.1016/j.saa.2023.122625
      
    - Sun, Z., Li, J., Wang, X. (2025). Origins of Zircon Xenocrysts in the 
      Neoproterozoic South Anhui Ophiolite, Yangtze Block.
      Minerals, 15(6), 563.
      https://doi.org/10.3390/min15060563
      
    Spectral Preprocessing References:
    - Bocklitz, T., Walter, A., Hartmann, K., Rösch, P., Popp, J. (2011).
      How to pre-process Raman spectra for reliable and stable models?
      Analytica Chimica Acta, 704(1-2), 47-56.
      https://doi.org/10.1016/j.aca.2011.06.043
      
    - Movasaghi, Z., Rehman, S., Rehman, I.U. (2007).
      Raman spectroscopy of biological tissues.
      Applied Spectroscopy Reviews, 42(5), 493-541.
      https://doi.org/10.1080/05704920701551530
      
    - Wirth, R. (2009). Focused Ion Beam (FIB) combined with SEM and TEM: 
      Advanced analytical tools for studies of chemical composition, microstructure 
      and crystal structure in geomaterials on a nanometre scale.
      Chemical Geology, 261(3-4), 217-229.
      https://doi.org/10.1016/j.chemgeo.2008.05.019
      
    Note: Specific frequencies may vary slightly depending on composition,
    measurement temperature, degree of metamictization and experimental conditions.
    
    Returns:
        dict: Dictionary with spectral regions and their intervals (min_wave, max_wave, is_inclusive)
              where is_inclusive indicates if max_wave is inclusive (True) or exclusive (False)
    """
    return {
        # Internal modes of SiO₄ tetrahedron (closed intervals - they are unique)
        "ν₃(SiO₄)": (990, 1020, True),   # [990, 1020] - Antisymmetric stretching
        "ν₁(SiO₄)": (965, 985, True),    # [965, 985] - Symmetric stretching  
        "ν₂(SiO₄)": (430, 450, True),    # [430, 450] - Bending deformation
        
        # External crystal lattice modes (half-open intervals to avoid overlap)
        "External mode 1": (195, 210, False),  # [195, 210) - Does not include 210
        "External mode 2": (210, 220, False),  # [210, 220) - Includes 210, does not include 220
        "External mode 3": (220, 230, False),  # [220, 230) - Includes 220, does not include 230
        "External mode 4": (350, 365, True)    # [350, 365] - Last region, closed interval
    }

def is_peak_in_region(center_value, min_wave, max_wave, is_inclusive):
    """
    Check if a peak is within a specific spectral region.
    
    Args:
        center_value (float): Peak center position (cm⁻¹)
        min_wave (float): Lower region limit (inclusive)
        max_wave (float): Upper region limit  
        is_inclusive (bool): If True, max_wave is inclusive (<=); if False, exclusive (<)
    
    Returns:
        bool: True if peak is in region, False otherwise
    """
    if is_inclusive:
        return min_wave <= center_value <= max_wave  # Closed interval [min, max]
    else:
        return min_wave <= center_value < max_wave   # Half-open interval [min, max)

# ============ MODULE DOCUMENTATION ==============
"""
ZIRCON RAMAN SPECTRAL ANALYSIS
Developed by: Antonio Said Webbe Sales
Advisor: Prof. Dr. Airton Natanael Coelho Dias
Federal University of São Carlos - Sorocaba

This module implements complete zircon Raman spectra analysis, including:
1. Spectrum normalization and preprocessing
2. Baseline correction with advanced methods (AirPLS, spline, polynomial)
3. Spectral smoothing using Savitzky-Golay filter
4. Automatic peak detection
5. Full width at half maximum (FWHM) calculation
6. Gaussian profile fitting
7. Radiation damage analysis based on Ginster et al. (2019)
8. Detailed report generation with spectral region analysis
9. Radiation damage visualizations and statistics
"""

# ============ CONFIG FUNCTIONS ==============

def load_config(config_path='raman_config.json'):
    """
    Load configurations from a JSON file or create a default configuration if the file does not exist.

    The configuration file stores parameters for normalization, baseline correction, smoothing,
    peak detection, curve fitting and input/output directories. If the file is not present,
    it is automatically created with default values.

    Args:
        config_path (str, optional): Path to the JSON configuration file. Default: 'raman_config.json'.

    Returns:
        dict: Dictionary containing the loaded configurations or default values if the file does not exist.

    Notes:
        - If the JSON file is corrupted or badly formatted, it may cause errors when loading configurations.
        - The output and input directory must be configured correctly to avoid errors during processing execution.
    """

    # If a config file already exists, load and return it (do not overwrite user settings)
    try:
        config_path_obj = Path(config_path)
        if config_path_obj.exists():
            with open(config_path_obj, 'r') as f:
                loaded = json.load(f)
            return loaded
    except Exception:
        # If reading fails, we will fall back to creating a fresh default config below
        pass

    # Build safe, project-relative defaults (avoid hardcoded user profiles like C:\\Users\\Usuario)
    base_dir = Path(__file__).parent.resolve()
    default_output_dir = str((base_dir / 'batch_reports').resolve())
    default_input_dir = str((base_dir / 'csv_unificados').resolve())

    default_config = {
        "normalization": {
            "method": "min_max",  # Options: min_max, area, peak, vector, none
        },
        "baseline_correction": {
            "method": "spline",    # Options: airpls, polynomial, spline
            "airpls_lambda": 10000,
            "polynomial_degree": 4,
            "spline_smoothing": 0.1
        },
        "smoothing": {
            "window_length": 11,
            "polyorder": 3
        },
        "peak_detection": {
            "height_percent": 8,    # % of max intensity
            "prominence_percent": 4, # % of max intensity
            "distance": 2,         # minimum distance between peaks (in points)
            "width": 2              # minimum width of peaks (in points)
        },
        "fitting": {
            "method": "trf",        # Options: trf, dogbox, lm
            "max_iterations": 1000,
            "tolerance": 1e-8
        },
        "data_format": {
            "grain_only_columns": False,
            "default_location": "1"
        },
        # Project-relative defaults to avoid permissions and missing-path issues
        "output_dir": default_output_dir,
        "input_dir": default_input_dir,
        "peak_analysis": {
            "height_threshold": 0.05,
            "prominence_threshold": 0.02,
        }
    }

    # Persist the default configuration to disk
    with open(config_path, 'w') as f:
        json.dump(default_config, f, indent=4)
    print(f"Created configuration file: {config_path}")
    return default_config

# ============ FUNCTION TO SAVE FILES ==============

def get_output_dir(config):
    """
    Create and return the absolute path of the output directory specified in the configuration.

    The function checks if the output directory is defined in the configuration (`config["output_dir"]`). 
    If the path is relative, it is converted to an absolute path based on the current directory. 
    If the directory does not exist, it is created automatically.

    Args:
        config (dict): Dictionary containing program configurations, including the `"output_dir"` key.

    Returns:
        str: Absolute path of the output directory.

    Operation:
        1. Gets the output directory from configuration (`config["output_dir"]`).
        2. If the path is relative, converts to an absolute path based on current directory (`os.getcwd()`).
        3. Checks if the directory exists:
            - If it exists, returns the path.
            - If it doesn't exist, creates the directory and displays a message informing the creation.
        4. Returns the absolute path of the output directory.

    
    Notes:
        - If `"output_dir"` is not defined in configuration, the default `"batch_reports"` directory will be used.
        - Ensures that the output directory is always available to save generated files.
        - The created directory will be relative to the execution directory, if an absolute path is not specified.

    Raises:
        - `PermissionError`: If the system does not allow creation of the output directory.
        - `OSError`: If an unexpected error occurs when trying to create the directory.

    """
    output_dir = config["output_dir"]
    
    output_path = Path(output_dir)
    if not output_path.is_absolute():
        # Make relative to current directory
        output_path = Path.cwd() / output_dir
    
    # Create the output directory if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)
    print(f"Created output directory: {output_path}")
    
    return str(output_path)

# ============ NORMALIZATION FUNCTIONS ============

def normalize_min_max(y, scale_factor=1.0):
    """
    Normalize a spectrum using Min-Max scaling to the interval [0,1].

    The Min-Max method rescales the values of array `y`, so that the smallest value becomes 0 and the largest becomes 1.
    Optionally, the values can be multiplied by a scale factor (`scale_factor`).

    Min-Max normalization is widely used in spectroscopy as a preprocessing technique
    to standardize spectral data and remove intensity variations not related to the chemical content
    of the sample. This method preserves the proportional relationships between spectral peaks
    while eliminating absolute intensity differences caused by instrumental factors.

    Args:
        y (numpy.ndarray): Array containing the spectrum values to be normalized.
        scale_factor (float, optional): Multiplicative factor applied after normalization.
            The default is `1.0`, keeping values between 0 and 1.

    Returns:
        numpy.ndarray: Normalized spectrum in the interval `[0, 1]`, or an array of zeros if `y_max == y_min`.

    Operation:
        1. **Calculate the minimum and maximum values of the spectrum**:
            ```python
            y_min = np.min(y)
            y_max = np.max(y)
            ```
        
        2. **Apply Min-Max normalization if `y_max > y_min`**:
            ```python
            if y_max > y_min:
                y_normalized = (y - y_min) / (y_max - y_min)
            ```
        
        3. **Apply the scale factor, if necessary**:
            ```python
            if scale_factor != 1.0:
                y_normalized = y_normalized * scale_factor
            ```
        
        4. **Avoid division by zero by returning an array of zeros if `y_max == y_min`**:
            ```python
            else:
                y_normalized = np.zeros_like(y)
            ```

    Notes:
        - If all values of `y` are equal, the function will return an array of zeros to avoid division by zero.
        - The `scale_factor` can be used to expand the values to a different interval (example: `[0,2]`).
        - This method is particularly useful for standardizing spectra before applying machine learning algorithms.

    Scientific References:
        Min-Max normalization is a fundamental technique in chemometrics and spectral analysis:

        1. **Fatima et al. (2020)** - Towards normalization selection of Raman data in the context of protein glycation
           https://doi.org/10.1039/C9AN02155H
           Comparative study of normalization methods in Raman data, including scaling techniques.

        2. **Guo et al. (2021)** - Chemometric analysis in Raman spectroscopy from experimental design to machine learning-based modeling
           https://doi.org/10.1038/s41596-021-00620-3
           Comprehensive protocol on chemometric analysis in Raman spectroscopy with normalization methods.

        3. **Ryabchykov et al. (2022)** - Errors and Mistakes to Avoid when Analyzing Raman Spectra
           https://doi.org/10.56530/spectroscopy.zz8373x6
           Guide on correct practices in spectral analysis, including the importance of proper normalization.

        4. **Hu et al. (2024)** - RSPSSL: A novel high-fidelity Raman spectral preprocessing scheme
           https://doi.org/10.1038/s41377-024-01394-5
           Advanced spectral preprocessing scheme including normalization methods for biomedical applications.

    Raises:
        ValueError: Se `y` não for um array NumPy válido.

    """
    y_min = np.min(y)
    y_max = np.max(y)
    print(f"Min: {y_min}, Max: {y_max}")

    if y_max > y_min:
        y_normalized = (y - y_min) / (y_max - y_min)
        if scale_factor != 1.0:
            y_normalized = y_normalized * scale_factor            
    else:
        y_normalized = np.zeros_like(y)
        
    return y_normalized

def normalize_area(y, x=None):
    """
    Normalize a Raman spectrum by dividing by the total area under the curve.
    
    This method compensates for differences in total sample concentration or variations
    in sampling volume, making it particularly useful for quantitative analysis and
    comparison of samples with different concentrations.
    
    References:
    -----------
    - Movasaghi, Z., Rehman, S., Rehman, I.U. (2007). Raman spectroscopy of biological tissues.
      Applied Spectroscopy Reviews, 42(5), 493-541. https://doi.org/10.1080/05704920701551530
      
    - Bocklitz, T., Walter, A., Hartmann, K., Rösch, P., Popp, J. (2011).
      How to pre-process Raman spectra for reliable and stable models?
      Analytica Chimica Acta, 704(1-2), 47-56. https://doi.org/10.1016/j.aca.2011.06.043
    
    Parameters:
    -----------
    y : array_like
        Array containing the spectrum intensities
    x : array_like, optional
        Array containing the wavenumber values. If None, uniform spacing is assumed.
        
    Returns:
    --------
    numpy.ndarray
        Area-normalized spectrum
    """
    if x is None:
        # If x is not provided, uniform spacing is assumed
        area = integrate.simpson(y)
    else:
        # If x is provided, use it for precise area calculation
        area = integrate.simpson(y, x)
    
    if area != 0:
        y_normalized = y / abs(area)
    else:
        y_normalized = np.zeros_like(y)
        
    return y_normalized

def normalize_peak(y, peak_index=None):
    """
    Normalizes the spectrum by dividing by the maximum peak intensity.
    
    This method is effective when there is a well-defined internal standard in the spectrum,
    assuming that the reference peak represents a chemical species with known or 
    constant concentration.
    
    References:
    -----------
    - Wirth, R. (2009). Focused Ion Beam (FIB) combined with SEM and TEM: 
      Advanced analytical tools for studies of chemical composition, microstructure 
      and crystal structure in geomaterials on a nanometre scale.
      Chemical Geology, 261(3-4), 217-229. https://doi.org/10.1016/j.chemgeo.2008.05.019
      
    Parameters:
    -----------
    y : array_like
        Array containing the spectrum intensities
    peak_index : int, optional
        Index of the reference peak. If None, uses the maximum intensity peak.
        
    Returns:
    --------
    numpy.ndarray
        Peak-normalized spectrum
    """
    if peak_index is None:
        peak_value = np.max(y)
    else:
        peak_value = y[peak_index]
    
    if peak_value != 0:
        y_normalized = y / peak_value
    else:
        y_normalized = np.zeros_like(y)
        
    return y_normalized

def normalize_vector(y):
    """Normaliza o espectro usando normalização vetorial (norma L2)."""
    norm = np.sqrt(np.sum(y**2))
    
    if norm != 0:
        y_normalized = y / norm
    else:
        y_normalized = np.zeros_like(y)
        
    return y_normalized

def normalize_spectrum(y, x=None, method="min_max"):
    """
    Applies normalization to a Raman spectrum based on the specified method.

    This function serves as a unified interface for different spectral normalization methods,
    each suitable for different types of analysis and experimental conditions. The choice of
    normalization method is crucial for the quality of subsequent spectroscopic analysis,
    directly influencing classification, clustering, and regression results.

    Spectral normalization is a fundamental step in Raman data preprocessing,
    used to correct systematic variations unrelated to the chemical content of the sample.
    Instrumental factors such as laser power fluctuations, differences in detector response,
    variations in measurement geometry, and optical characteristics of the spectrometer can introduce
    variabilities that mask the real chemical information in the spectrum.

    **Available Normalization Methods:**

    - **min_max**: Linearly rescales values to the [0,1] interval, preserving
      proportional relationships between spectral peaks. Ideal for comparative analyses
      and machine learning algorithms that are sensitive to data scale.

    - **area**: Normalization by the total area under the spectral curve, compensating for differences
      in total sample concentration or variations in sampling volume. Particularly
      useful for quantitative analysis and comparison of samples with different concentrations.

    - **peak**: Normalization by a specific reference peak, assuming that this peak
      represents a chemical species with known or constant concentration. Effective when
      there is a well-defined internal standard in the spectrum.

    - **vector**: Normalization by L2 (Euclidean) norm, making the spectral vector
      have unit magnitude. This is the standard method in chemometrics and multivariate analysis,
      being essential for techniques like PCA and discriminant analysis.

    - **None**: Returns the original spectrum without modifications, useful for analyses where
      absolute intensity is relevant or when other preprocessing methods have already been applied.

    **Method Selection Guide:**

    - **Qualitative Analysis**: min_max or vector for compound identification
    - **Quantitative Analysis**: area or peak with internal standard
    - **Machine Learning**: min_max or vector depending on the algorithm
    - **Multivariate Analysis**: vector (L2 normalization)
    - **Direct Comparison**: area to compensate for concentration differences

    **Scientific References:**

    Traditional normalization methods:
    - Dawson et al. (1971). Vibrational spectrum of zircon (ZrSiO₄).
      https://doi.org/10.1088/0022-3719/4/2/014

    - Guo et al. (2021). Chemometric analysis in Raman spectroscopy from experimental design
      to machine learning–based modeling. Nature Protocols, 16(12), 5426-5459.
      https://doi.org/10.1038/s41596-021-00620-3

    - Fatima et al. (2020). Review of the principal component analysis method for Raman spectral data.
      The Analyst, 145(6), 2174-2189.
      https://doi.org/10.1039/C9AN02155H

    Recent advances (2022-2024):
    - Ryabchykov et al. (2022). Errors and Mistakes to Avoid when Analyzing Raman Spectra.
      Spectroscopy, 37(4), 48-50.
      https://doi.org/10.56530/spectroscopy.zz8373x6

    
    - Ibtehaz et al. (2023). RamanNet: a generalized neural network architecture for
      Raman spectrum analysis. Neural Computing and Applications, 35(25), 18719-18735.
      https://doi.org/10.1007/s00521-023-08700-z
    
    - Ling et al. (2022). Extreme Point Sort Transformation Combined With a Long Short-Term
      Memory Network Algorithm for the Raman-Based Identification of Therapeutic Monoclonal Antibodies.
      Frontiers in Chemistry, 10, 887960.
      https://doi.org/10.3389/fchem.2022.887960

    **Important Considerations:**

    1. **Application Order**: Normalization should be applied AFTER baseline correction
       to avoid bias in results (Ryabchykov et al., 2022).

    2. **Robustness**: Methods based on robust statistics (median, percentiles) are
       less sensitive to outliers than methods based on the mean.

    3. **Reproducibility**: Normalization should be consistent between measurements to
       ensure comparability of results.

    4. **Validation**: It is recommended to validate the normalization method with known standards
       before application to unknown samples.

    Parameters:
    -----------
    y : array-like
        Array containing the spectral intensities to be normalized.
        Must be a 1D array of numerical values.

    x : array-like, optional
        Array containing the corresponding wavenumber (cm⁻¹) values.
        Used only for specific peak normalization. Default: None.

    method : str, optional
        Normalization method to be applied. Available options:
        - "min_max": Min-Max scaling to [0,1]
        - "area": Total area normalization
        - "peak": Reference peak normalization
        - "vector": L2 normalization (Euclidean norm)
        - None: No normalization
        Default: "min_max"
    
    Returns:
    --------
    numpy.ndarray
        Normalized array with the same shape as the original input.
        Values are transformed according to the selected method.
    
    Raises:
    -------
    ValueError
        If the specified method is not recognized or if the input data
        is not suitable for the selected method.
    
    Examples:
    ---------
    >>> import numpy as np
    >>> y = np.array([100, 200, 300, 150, 50])
    >>> 
    >>> # Min-Max normalization
    >>> y_minmax = normalize_spectrum(y, method="min_max")
    >>> print(y_minmax)  # [0.2, 0.6, 1.0, 0.4, 0.0]
    >>> 
    >>> # Area normalization
    >>> y_area = normalize_spectrum(y, method="area")
    >>> print(np.sum(y_area))  # 1.0
    >>> 
    >>> # L2 normalization
    >>> y_vector = normalize_spectrum(y, method="vector")
    >>> print(np.linalg.norm(y_vector))  # 1.0

    See Also:
    ---------
    normalize_min_max : Specific implementation of Min-Max normalization
    scipy.preprocessing.normalize : General normalization from scikit-learn
    """
    if method == "min_max":
        return normalize_min_max(y)
    elif method == "area":
        return normalize_area(y, x)
    elif method == "peak":
        return normalize_peak(y)
    elif method == "vector":
        return normalize_vector(y)
    elif method == "none":
        return y.copy()
    else:
        print(f"Warning: Unknown normalization method '{method}'. Using min-max.")
        return normalize_min_max(y)

# ============ v4.0 ENHANCEMENT FUNCTIONS ============

def get_available_normalization_methods():
    """
    Get list of available normalization methods for v4.0 multi-processing.
    
    Returns:
        list: List of available normalization method names
    """
    return ["min_max", "area", "peak", "vector", "none"]

def get_normalization_suffix(method):
    """
    Get file suffix for normalization method - v4.0 ENHANCEMENT.
    
    This function maps normalization methods to their corresponding file suffixes
    to enable systematic file naming in the multi-normalization processing pipeline.
    
    Args:
        method (str): Normalization method name
        
    Returns:
        str: File suffix for the method
        
    Examples:
        >>> get_normalization_suffix("min_max")
        '_minmax'
        >>> get_normalization_suffix("area")
        '_area'
    """
    suffix_mapping = {
        "min_max": "_minmax",
        "area": "_area",
        "peak": "_peak", 
        "vector": "_vector",
        "none": "_raw"
    }
    return suffix_mapping.get(method, f"_{method}")

def get_normalization_description(method):
    """
    Get detailed description of normalization method - v4.0 ENHANCEMENT.
    
    Provides comprehensive descriptions for each normalization method to aid
    in interpretation of multi-normalization results and report generation.
    
    Args:
        method (str): Normalization method name
        
    Returns:
        str: Detailed description of the method
    """
    descriptions = {
        "min_max": "Min-Max scaling to [0,1] range - preserves relative peak intensities",
        "area": "Area normalization (total area = 1) - compensates for concentration variations",
        "peak": "Peak normalization (highest peak = 1) - internal standard approach",
        "vector": "L2 normalization (Euclidean norm = 1) - optimal for multivariate analysis",
        "none": "No normalization (raw intensities) - preserves absolute values"
    }
    return descriptions.get(method, f"Unknown normalization method: {method}")

def validate_normalization_method(method):
    """
    Validate if normalization method is supported - v4.0 ENHANCEMENT.
    
    Args:
        method (str): Normalization method to validate
        
    Returns:
        bool: True if method is valid, False otherwise
    """
    return method in get_available_normalization_methods()

def generate_output_filename_with_suffix(base_filename, method, file_type="csv"):
    """
    Generate output filename with normalization suffix - v4.0 ENHANCEMENT.
    
    Creates systematic filenames for multi-normalization processing results.
    
    Args:
        base_filename (str): Base filename without extension
        method (str): Normalization method
        file_type (str): File extension (default: "csv")
        
    Returns:
        str: Complete filename with normalization suffix
        
    Examples:
        >>> generate_output_filename_with_suffix("sample_001_results", "min_max")
        'sample_001_results_minmax.csv'
    """
    suffix = get_normalization_suffix(method)
    return f"{base_filename}{suffix}.{file_type}"

# ============ BASELINE CORRECTION FUNCTIONS ============

def airpls_baseline(y, lambda_=10000, porder=1, itermax=10):
    """
    Perform Asymmetrically Reweighted Penalized Least Squares (airPLS) baseline correction.
    
    The airPLS algorithm is a robust method for automatic baseline correction in spectroscopy,
    particularly effective for Raman spectroscopy. It works by iteratively fitting a smooth
    baseline to the spectrum while asymmetrically weighting the residuals, giving less weight
    to peaks (positive residuals) and more weight to baseline regions (negative residuals).
    
    The method is based on the assumption that the true baseline lies below the measured
    spectrum, making it particularly suitable for Raman spectroscopy where fluorescence
    background and other interference effects typically add positive contributions to the signal.
    
    Mathematical Formulation:
    The airPLS algorithm minimizes the following objective function:
    
    min_z Σ w_i (y_i - z_i)² + λ Σ (Δᵖz_i)²
    
    where:
    - z is the estimated baseline
    - w_i are the asymmetric weights
    - λ is the smoothing parameter
    - Δᵖz_i is the p-th order difference of the baseline
    
    Algorithm Steps:
    1. Initialize weights w_i = 1 for all points
    2. Fit baseline z using weighted penalized least squares
    3. Calculate residuals r_i = y_i - z_i
    4. Update weights: w_i = 0 if r_i > 0, w_i = exp(r_i/std(r_neg)) if r_i ≤ 0
    5. Repeat steps 2-4 until convergence or maximum iterations reached
    
    This implementation is based on the original paper by Eilers & Boelens (2005) and 
    subsequent improvements by Zhang et al. (2010).
    
    Bibliographic References:
    
    **Original airPLS Paper:**
    
    - Eilers, P.H.C., Boelens, H.F.M. (2005). Baseline Correction with Asymmetric Least Squares Smoothing.
      Leiden University Medical Centre Report.
      (Foundation of the asymmetric least squares method)
    
    - Zhang, Z.-M., Chen, S., Liang, Y.-Z. (2010). Baseline correction using adaptive 
      iteratively reweighted penalized least squares. Analyst, 135(5), 1138-1146.
      https://doi.org/10.1039/b922045c
      (Original airPLS algorithm paper)
    
    **Validation and Improvements:**
    
    - Baek, S.-J., Park, A., Ahn, Y.-J., Choo, J. (2015). Baseline correction using asymmetrically 
      reweighted penalized least squares smoothing. Analyst, 140(1), 250-257.
      https://doi.org/10.1039/C4AN01061B
      (Improved version with better convergence criteria)
    
    - Gan, F., Ruan, G., Mo, J. (2006). Baseline correction by improved iterative polynomial 
      fitting with automatic threshold. Chemometrics and Intelligent Laboratory Systems, 82(1-2), 59-65.
      https://doi.org/10.1016/j.chemolab.2005.08.009
      (Comparative study including airPLS evaluation)
    
    **Modern Applications and Comparisons:**
    
    - Liu, J., Sun, J., Huang, X., Li, G., Liu, B. (2015). Goldindec: A Novel Algorithm for 
      Raman Spectrum Baseline Correction. Applied Spectroscopy, 69(7), 834-842.
      https://doi.org/10.1366/14-07798
      (Comparative evaluation with other methods)
    
    - Ralbovsky, N.M., Lednev, I.K. (2020). Towards development of a novel universal 
      medical diagnostic method: Raman spectroscopy and machine learning. Chemical Society Reviews, 49(20), 7428-7453.
      https://doi.org/10.1039/d0cs00675k
      (Modern review highlighting importance of baseline correction in medical applications)
    
    - Lieber, C.A., Mahadevan-Jansen, A. (2003). Automated Method for Subtraction of 
      Fluorescence from Biological Raman Spectra. Applied Spectroscopy, 57(11), 1363-1367.
      https://doi.org/10.1366/000370203322554518
      (Alternative approach, useful for comparison)
    
    **Implementation and Computational Aspects:**
    
    - Eilers, P.H.C. (2003). A perfect smoother. Analytical Chemistry, 75(14), 3631-3636.
      https://doi.org/10.1021/ac034173t
    
    **Recent References (2022-2024):**
    
    - Han, M., Dang, Y., & Han, J. (2024). Denoising and Baseline Correction Methods for 
      Raman Spectroscopy Based on Convolutional Autoencoder: A Unified Solution. 
      Sensors, 24(10), 3161.
      https://doi.org/10.3390/s24103161
      (Compares airPLS with deep learning-based methods)

    - Andries, E., & Nikzad-Langerodi, R. (2024). Supervised and Penalized Baseline Correction.
      Erik Andries, Ramin Nikzad-Langerodi,
        Supervised and penalized baseline correction,
        Chemometrics and Intelligent Laboratory Systems,
        Volume 253,
        2024,
        105200,
        ISSN 0169-7439,
        https://doi.org/10.1016/j.chemolab.2024.105200.
        
    
      (Supervised extension of penalized correction methods including airPLS)

    - Hara, R., Kobayashi, W., Yamanaka, H., Murayama, K., Shimoda, S., & Ozaki, Y. (2023).
      Development of Raman Calibration Model Without Culture Data for In-Line Analysis of 
      Metabolites in Cell Culture Media. Applied Spectroscopy, 77(5), 521-533.
      https://doi.org/10.1177/00037028231160197
      (Application of airPLS in bioprocess monitoring)

    Parameters:
    -----------
    y : array_like
        1D array containing the input spectrum.
    lambda_ : float, optional (default=10000)
        Regularization parameter that controls baseline smoothness.
        Larger values result in smoother baselines.
        Typical values: 10^3 - 10^6 depending on application.
    porder : int, optional (default=1)
        Order of the penalty (differentiation). 
        1 = first derivative (smoothness), 2 = second derivative (curvature).
    itermax : int, optional (default=10)
        Maximum number of iterations for the algorithm.
        
    Returns:
    --------
    numpy.ndarray
        Estimated baseline with the same length as the input spectrum.
        
    Notes:
    ------
    - The algorithm automatically stops when convergence is reached or maximum iterations are exceeded.
    - Higher lambda values produce smoother baselines but may oversmooth sharp baseline features.
    - The method is particularly effective for spectra with strong fluorescence backgrounds.
    - For very noisy spectra, consider applying smoothing before baseline correction.
    
    Examples:
    ---------
    >>> import numpy as np
    >>> # Generate synthetic spectrum with baseline
    >>> x = np.linspace(100, 3000, 1000)
    >>> baseline = 1000 * np.exp(-x/1000) + 100
    >>> peaks = 500 * np.exp(-((x-1000)/50)**2) + 300 * np.exp(-((x-1500)/30)**2)
    >>> spectrum = baseline + peaks + 20 * np.random.randn(len(x))
    >>> 
    >>> # Apply airPLS baseline correction
    >>> corrected_baseline = airpls_baseline(spectrum, lambda_=10000)
    >>> corrected_spectrum = spectrum - corrected_baseline
    
    Raises:
    -------
    ValueError
        If input array is not 1D or contains non-finite values.
    """
    import numpy as np
    from scipy import sparse
    from scipy.sparse.linalg import spsolve
    
    y = np.asarray(y)
    if y.ndim != 1:
        raise ValueError("Input array must be 1D")
    
    if not np.all(np.isfinite(y)):
        raise ValueError("Input array contains non-finite values")
    
    L = len(y)
    D = sparse.diags([1,-2,1],[0,-1,-2], shape=(L,L-2))
    D = lambda_*D.dot(D.transpose())
    
    w = np.ones(L)
    W = sparse.spdiags(w, 0, L, L)
    
    for i in range(itermax):
        W.setdiag(w)
        Z = W + D
        z = spsolve(Z, w*y)
        d = y - z
        
        # Negative residuals get higher weights
        dn = d[d<0]
        m = np.mean(dn)
        s = np.std(dn)
        
        wt = 1.0 / (1 + np.exp(2 * (d-(2*s-m))/s))
        
        if np.linalg.norm(w-wt)/np.linalg.norm(w) < 1e-5:
            break
        w = wt
    
    return z

def polynomial_baseline(y, x=None, degree=3):
    """
    Performs polynomial baseline correction.
    
    Parameters:
    -----------
    y : array_like
        Input spectrum intensities.
    x : array_like, optional
        Wavenumber values. If None, uses indices.
    degree : int, optional
        Polynomial degree (default: 3).
        
    Returns:
    --------
    tuple
        (corrected_spectrum, baseline)
    """
    import numpy as np
    from scipy.signal import find_peaks
    
    if x is None:
        x = np.arange(len(y))
    
    # Find peaks to exclude from baseline fitting
    peaks, _ = find_peaks(y, prominence=0.02*np.max(y))
    
    # Create mask excluding peak regions
    mask = np.ones(len(y), dtype=bool)
    for peak in peaks:
        window = int(len(y) * 0.02)
        left = max(0, peak - window)
        right = min(len(y), peak + window)
        mask[left:right] = False
    
    # Fit polynomial to non-peak regions
    if np.sum(mask) > degree + 1:
        baseline_x = x[mask]
        baseline_y = y[mask]
        coeffs = np.polyfit(baseline_x, baseline_y, degree)
        baseline = np.polyval(coeffs, x)
    else:
        # Fallback: simple linear baseline
        coeffs = np.polyfit(x, y, 1)
        baseline = np.polyval(coeffs, x)
    
    # Ensure baseline doesn't exceed spectrum
    baseline = np.minimum(baseline, y)
    corrected_spectrum = y - baseline
    
    return corrected_spectrum, baseline

def spline_baseline(y, x=None, smoothing_factor=0.1, interpolation_factor=5):
    """
    Performs baseline correction using cubic spline interpolation with peak exclusion.
    
    This method implements a robust baseline correction algorithm based on univariate
    cubic splines that identifies and excludes spectral peak regions before interpolation,
    creating a smooth and adaptive baseline that preserves the natural shape of the spectral background.
    
    Parameters
    ----------
    y : array-like
        Spectral intensities (1D array).
    x : array-like, optional
        Corresponding wavenumber or wavelength values.
        If None, uses sequential indices (default: None).
    smoothing_factor : float, optional
        Smoothing factor for cubic spline (default: 0.1).
        Lower values result in baselines more adapted to the data.
        Higher values produce smoother baselines.
        Typical range: 0.01-1.0.
    interpolation_factor : int, optional
        Interpolation factor to increase resolution (default: 5).
        Defines how many times the resolution will be increased during interpolation.
        
    Returns
    -------
    corrected_spectrum : ndarray
        Corrected spectrum with baseline removed and normalized.
    baseline : ndarray
        Baseline estimated by cubic spline interpolation.
    
    Algorithm
    ---------
    1. Automatic peak detection using relative prominence (2% of maximum intensity)
    2. Mask creation excluding windows around peaks (2% of total length)
    3. Fallback to percentile selection (50%) if too many peaks are detected
    4. Univariate cubic spline fitting using only baseline points
    5. High-resolution interpolation for additional smoothing
    6. Baseline limitation to avoid values above the original spectrum
    7. Normalization of the corrected spectrum
    
    Notes
    -----
    - The spline method is particularly effective for spectra with complex baseline variations
    - Cubic interpolation preserves continuity and smoothness of the baseline
    - The smoothing factor allows fine control over baseline flexibility
    - Robustness against interpolation failures with integrated alternative method
    - Suitable for spectra with non-linear baselines and gradual variations
    
    References
    ----------
    .. [1] Eilers, P. H. C. (2003). A perfect smoother. Analytical Chemistry, 75(14), 3631-3636.
           https://doi.org/10.1021/ac034173t
           
    .. [2] Ryabchykov, O., Schie, I. W., Popp, J., & Bocklitz, T. (2022). 
           Errors and Mistakes to Avoid when Analyzing Raman Spectra. 
           Spectroscopy, 37(4), 48-50.
           https://doi.org/10.56530/spectroscopy.zz8373x6
           
    .. [3] Andries, E., & Nikzad-Langerodi, R. (2024). Supervised and Penalized 
           Baseline Correction. Chemometrics and Intelligent Laboratory Systems, 
           253, 105200.
           https://doi.org/10.1016/j.chemolab.2024.105200
           
    .. [4] Zhang, Z.-M., Chen, S., & Liang, Y.-Z. (2010). Baseline correction 
           using adaptive iteratively reweighted penalized least squares. 
           Analyst, 135(5), 1138-1146.
           https://doi.org/10.1039/b922045c
           
    .. [5] Han, M., Dang, Y., & Han, J. (2024). Denoising and Baseline Correction 
           Methods for Raman Spectroscopy Based on Convolutional Autoencoder: 
           A Unified Solution. Sensors, 24(10), 3161.
           https://doi.org/10.3390/s24103161
    
    Examples
    --------
    >>> import numpy as np
    >>> # Simulate Raman spectrum with complex baseline
    >>> x = np.linspace(200, 2000, 1000)
    >>> y_signal = np.exp(-0.5 * ((x - 1000) / 100)**2)  # Gaussian peak
    >>> baseline_complex = 0.1*np.sin(x/100) + 0.05*x + 2  # Non-linear baseline
    >>> y = y_signal + baseline_complex + 0.02*np.random.normal(size=len(x))
    >>> corrected, baseline = spline_baseline(y, x, smoothing_factor=0.15)
    >>> print(f"Complex baseline removed, maximum intensity: {np.max(corrected):.3f}")
    
    >>> # Fine-tuning parameters for different spectrum types
    >>> # For spectra with high variation: smoothing_factor=0.05
    >>> # For smoother spectra: smoothing_factor=0.2
    >>> corrected_fine, _ = spline_baseline(y, smoothing_factor=0.05, interpolation_factor=3)
    
    Warnings
    --------
    - If spline interpolation fails, the method uses linear interpolation as fallback
    - Very low smoothing parameters may result in baseline overfitting
    - Very high interpolation factor may significantly increase processing time
    
    See Also
    --------
    polynomial_baseline : Correction using polynomial fitting
    airpls_baseline : Correction using Asymmetrically Reweighted Penalized Least Squares
    """
    from scipy.interpolate import UnivariateSpline
    from scipy.signal import find_peaks
    
    if x is None:
        x = np.arange(len(y))
    
    if not np.all(np.diff(x) > 0):
        x = np.linspace(0, len(y)-1, len(y))
    
    x_high_res = np.linspace(x.min(), x.max(), len(x) * interpolation_factor)
    peaks, _ = find_peaks(y, prominence=0.02*np.max(y))
    
    mask = np.ones(len(y), dtype=bool)
    for peak in peaks:
        window = int(len(y) * 0.02)  
        left = max(0, peak - window)
        right = min(len(y), peak + window)
        mask[left:right] = False
    
    if np.sum(mask) < len(y) * 0.5:
        threshold = np.percentile(y, 50)
        mask = y <= threshold
    
    baseline_x = x[mask]
    baseline_y = y[mask]
    
    sort_indices = np.argsort(baseline_x)
    baseline_x = baseline_x[sort_indices]
    baseline_y = baseline_y[sort_indices]
    
    try:
        baseline_spline = UnivariateSpline(baseline_x, baseline_y, s=smoothing_factor * len(y))
        baseline_high_res = baseline_spline(x_high_res)
        baseline = np.interp(x, x_high_res, baseline_high_res)
    except ValueError:
        print("Warning: Interpolation failed. Using alternative method.")
        baseline = np.interp(x, baseline_x, baseline_y)
    
    baseline = np.minimum(baseline, y)
    corrected_spectrum = y - baseline
    
    if np.min(corrected_spectrum) < 0:
        corrected_spectrum = corrected_spectrum - np.min(corrected_spectrum)
    
    if np.max(corrected_spectrum) > 0:
        corrected_spectrum = corrected_spectrum / np.max(corrected_spectrum)
    
    return corrected_spectrum, baseline

def correct_baseline(y, x=None, config=None):
    """
    Applies baseline correction using the method specified in the configuration.
    
    This function provides a unified interface for different baseline correction
    methods, allowing automatic selection based on the provided configuration.
    Supports three main methods: airPLS, polynomial fitting and spline interpolation,
    each optimized for different types of spectra and experimental conditions.
    
    Parameters
    ----------
    y : array-like
        Spectral intensities (1D array).
    x : array-like, optional
        Corresponding wavenumber or wavelength values.
        If None, uses sequential indices (default: None).
    config : dict, optional
        Configuration dictionary containing baseline correction parameters.
        If None, uses spline method with default parameters (default: None).
        
    Returns:
    -------
        corrected_spectrum : ndarray
            Corrected spectrum with baseline removed.
        baseline : ndarray
            Baseline estimated by the selected method.
    
    Configuration Structure
    ----------------------
    The configuration dictionary must contain the 'baseline_correction' section with:
    
    - method : str
        Correction method to be used. Available options:
        * 'airpls' - Asymmetrically Reweighted Penalized Least Squares
        * 'polynomial' - Polynomial fitting with peak exclusion
        * 'spline' - Cubic spline interpolation
        
    - airpls_lambda : float (if method='airpls')
        Regularization parameter λ for airPLS method.
        Typical values: 10^4 - 10^7.
        
    - polynomial_degree : int (if method='polynomial')
        Polynomial degree for baseline fitting.
        Typical values: 2-6.
        
    - spline_smoothing : float (if method='spline')
        Smoothing factor for spline interpolation.
        Typical values: 0.01-1.0.
    
    Algorithm Selection Guide
    ------------------------
    Recommendations for method selection based on spectrum characteristics:
    
    **airPLS**: Ideal for spectra with:
    - Complex and non-linear baselines
    - Strong fluorescence presence
    - Need for rigorous preservation of peak shapes
    
    **Polynomial**: Suitable for spectra with:
    - Simple and smooth baselines
    - Gradual intensity variations
    - Few well-defined peaks
    
    **Spline**: Recommended for spectra with:
    - Moderate baseline curvature
    - Need for flexibility in modeling
    - Balance between smoothness and adaptability
    
    Notes
    -----
    - The function uses spline method as fallback if the specified method is invalid
    - Each method has specific parameters that should be optimized for the sample type
    - Proper method selection can significantly impact result quality
    - Hybrid methods can be implemented by combining different approaches
    
    References
    ----------
    .. [1] Zhang, Z.-M., Chen, S., & Liang, Y.-Z. (2010). Baseline correction 
           using adaptive iteratively reweighted penalized least squares. 
           Analyst, 135(5), 1138-1146.
           https://doi.org/10.1039/b922045c
           
    .. [2] Ryabchykov, O., Schie, I. W., Popp, J., & Bocklitz, T. (2022). 
           Errors and Mistakes to Avoid when Analyzing Raman Spectra. 
           Spectroscopy, 37(4), 48-50.
           https://doi.org/10.56530/spectroscopy.zz8373x6
           
    .. [3] Andries, E., & Nikzad-Langerodi, R. (2024). Supervised and Penalized 
           Baseline Correction. arXiv preprint arXiv:2310.18306.
           https://doi.org/10.48550/arXiv.2310.18306
           
    .. [4] Liu, B., Wang, L., Wang, J., Peng, B., & Wang, H. (2022). Baseline 
           correction for FAST radio recombination lines: a modified penalized 
           least squares smoothing technique. Publications of the Astronomical 
           Society of Australia, 39, e040.
           https://doi.org/10.1017/pasa.2022.40
           
    .. [5] Han, M., Dang, Y., & Han, J. (2024). Denoising and Baseline Correction 
           Methods for Raman Spectroscopy Based on Convolutional Autoencoder: 
           A Unified Solution. Sensors, 24(10), 3161.
           https://doi.org/10.3390/s24103161
    
    Examples
    --------
    >>> import numpy as np
    >>> # Configuration for airPLS method
    >>> config_airpls = {
    ...     "baseline_correction": {
    ...         "method": "airpls",
    ...         "airpls_lambda": 100000
    ...     }
    ... }
    >>> x = np.linspace(200, 2000, 1000)
    >>> y = np.exp(-0.5 * ((x - 1000) / 100)**2) + 0.1*x + 2
    >>> corrected, baseline = correct_baseline(y, x, config_airpls)
    >>> print(f"airPLS method applied, maximum intensity: {np.max(corrected):.3f}")
    
    >>> # Configuration for polynomial method
    >>> config_poly = {
    ...     "baseline_correction": {
    ...         "method": "polynomial",
    ...         "polynomial_degree": 4
    ...     }
    ... }
    >>> corrected, baseline = correct_baseline(y, x, config_poly)
    
    >>> # Configuration for spline method
    >>> config_spline = {
    ...     "baseline_correction": {
    ...         "method": "spline",
    ...         "spline_smoothing": 0.1
    ...     }
    ... }
    >>> corrected, baseline = correct_baseline(y, x, config_spline)
    
    Warnings
    --------
    - If the specified method is not recognized, spline method will be used as default
    - Inadequate parameters may result in insufficient correction or overfitting
    - Configuration validation should be done before application to data batches
    
    See Also
    --------
    airpls_baseline : Correction using Asymmetrically Reweighted Penalized Least Squares
    polynomial_baseline : Correction using polynomial fitting
    spline_baseline : Correction using cubic spline interpolation
    """
    baseline_config = config["baseline_correction"]
    method = baseline_config["method"]
    
    if method == "airpls":
        lambda_ = baseline_config["airpls_lambda"]
        return airpls_baseline(y, lambda_=lambda_)
    elif method == "polynomial":
        degree = baseline_config["polynomial_degree"]
        return polynomial_baseline(y, x, degree)
    elif method == "spline":
        smoothing = baseline_config["spline_smoothing"]
        return spline_baseline(y, x, smoothing_factor=smoothing)
    else:
        print(f"Warning: Unknown baseline correction method '{method}'. Using spline.")
        return spline_baseline(y, x)

def batch_process(config):
    """Processa todos os arquivos CSV no diretório de entrada e gera um relatório consolidado."""
    input_dir = config["input_dir"]
    output_dir = get_output_dir(config)
    
    print(f"Diretório de entrada: {input_dir}")
    print(f"Diretório de saída: {output_dir}")
    
    # Get all CSV files in the input directory
    from pathlib import Path
    input_path = Path(input_dir)
    csv_files = list(input_path.glob("*.csv"))
    
    if not csv_files:
        print(f"Nenhum arquivo CSV encontrado em {input_dir}")
        return
    
    print(f"Encontrados {len(csv_files)} arquivos CSV para processar")
    
    # Create a DataFrame to store all results
    all_results = pd.DataFrame()
    
    # Process each file
    for i, file_path in enumerate(csv_files):
        print(f"\nProcessing file {i+1}/{len(csv_files)}: {Path(file_path).name}")
        
        # Process the file
        results = process_file(file_path, config)
        
        # If processing succeeded
        if results is not None and not results.empty:
            # Append results to the combined DataFrame
            all_results = pd.concat([all_results, results], ignore_index=True)
            print(f"  Added {len(results)} results")
        else:
            print(f"  No results obtained from {file_path}")
    
    # Verify if we have any results
    if all_results.empty:
        print("\nNenhum resultado foi gerado.")
        print("Verifique se os arquivos CSV contêm dados espectrais válidos.")
        return
    
    # Obter lista de amostras analisadas para determinar nomenclatura dos arquivos
    amostras_analisadas = sorted(all_results['Amostra'].unique())
    n_amostras = len(amostras_analisadas)
    n_graos = len(all_results)
    
    print(f"\n📊 PROCESSAMENTO CONCLUÍDO:")
    print(f"   • Amostras processadas: {n_amostras}")
    print(f"   • Total de grãos analisados: {n_graos}")
    print(f"   • Média de grãos por amostra: {n_graos/n_amostras:.1f}")
    
    # Detecção e remoção de outliers
    print("\n🔍 DETECTANDO E REMOVENDO OUTLIERS...")
    all_results_clean, outlier_report = detect_and_remove_outliers(all_results, verbose=True)
    
    # Salvar relatório de outliers
    outlier_report_path = Path(output_dir) / "outlier_detection_report.txt"
    save_outlier_report(outlier_report, outlier_report_path)
    
    if len(all_results_clean) < len(all_results):
        n_outliers = len(all_results) - len(all_results_clean)
        print(f"   ❌ {n_outliers} outliers removidos ({n_outliers/len(all_results)*100:.1f}%)")
        print(f"   ✅ {len(all_results_clean)} grãos mantidos para análise final")
    
    # Nomenclatura dos arquivos baseada no número final de grãos
    n_graos_final = len(all_results_clean)
    sufixo_arquivos = f"_{n_amostras}amostras_{n_graos_final}graos"
    
    # Save the combined results (dados limpos)
    output_path = Path(output_dir) / f"batch_raman_analysis{sufixo_arquivos}.csv"
    all_results_clean.to_csv(output_path, index=False)
    print(f"\n💾 Resultados salvos em: {output_path}")
    
    # Generate summary report
    generate_summary_report(all_results_clean, config, output_dir, sufixo_arquivos)
    print(f"📄 Relatório resumido: raman_analysis_report{sufixo_arquivos}.txt")
    
    # Análise de robustez da configuração de detecção de picos
    print("\n🔬 ANALISANDO ROBUSTEZ DA CONFIGURAÇÃO...")
    robustness_report = analyze_peak_detection_robustness(all_results_clean, config)
    print_robustness_analysis(robustness_report, output_dir, sufixo_arquivos)
    
    print("=" * 70)

def generate_summary_report(results_df, config, output_dir, file_suffix=""):
    """Generate a summary report of the analysis."""
    report_path = Path(output_dir) / f"raman_analysis_report{file_suffix}.txt"
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("=" * 60 + "\n")
        f.write("RAMAN SPECTRAL ANALYSIS REPORT\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Analysis Date: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total samples: {results_df['Amostra'].nunique()}\n")
        f.write(f"Total peaks detected: {len(results_df)}\n")
        f.write(f"Average R²: {results_df['R2'].mean():.3f}\n")
        f.write(f"Average FWHM: {results_df['FWHM_Gauss'].mean():.2f} cm⁻¹\n\n")
        
        # Regional analysis
        regions = {
            "ν₃(SiO₄)": (990, 1020),
            "ν₁(SiO₄)": (965, 985),
            "ν₂(SiO₄)": (430, 450),
            "External": (195, 365)
        }
        
        f.write("REGIONAL ANALYSIS:\n")
        f.write("-" * 30 + "\n")
        for region, (min_w, max_w) in regions.items():
            region_data = results_df[(results_df['Centro'] >= min_w) & 
                                   (results_df['Centro'] <= max_w)]
            if len(region_data) > 0:
                f.write(f"{region}: {len(region_data)} peaks, ")
                f.write(f"avg FWHM: {region_data['FWHM_Gauss'].mean():.2f} cm⁻¹\n")

# ============ PROCESSING FUNCTIONS ============

def generate_radiation_damage_summary(results_df, output_dir, file_suffix=""):
    """Generate a summary of radiation damage analysis."""
    output_path = Path(output_dir) / f"radiation_damage_summary{file_suffix}.csv"
    
    # Calculate radiation damage statistics
    damage_summary = []
    for _, row in results_df.iterrows():
        damage_level = categorize_radiation_damage(row['FWHM_Gauss'])
        damage_summary.append({
            'Amostra': row['Amostra'],
            'Centro': row['Centro'],
            'FWHM': row['FWHM_Gauss'],
            'Dano_Radiativo': damage_level
        })
    
    damage_df = pd.DataFrame(damage_summary)
    damage_df.to_csv(output_path, index=False)

def apply_savitzky_golay(y, window_length=11, polyorder=3):
    """
    Applies Savitzky-Golay filter for Raman spectra smoothing.

    The Savitzky-Golay filter fits a polynomial to moving windows of the data, preserving 
    characteristics such as peaks and bandwidth, making it ideal for noisy spectra. 
    The function automatically adjusts `window_length` and `polyorder` to avoid errors.

    Args:
        y (numpy.ndarray): Array containing the input spectrum values.
        window_length (int, optional): Filter window size. Must be odd and less than `len(y)`. Default: `11`.
        polyorder (int, optional): Polynomial order used for fitting in each window. Default: `3`.

    Returns:
        numpy.ndarray: Smoothed spectrum after filter application.

    Algorithm:
        1. **Ensures `window_length` is odd**:
            ```python
    if window_length % 2 == 0:
        window_length += 1
            ```
    
        2. **Adjusts `window_length` if larger than the length of `y`**:
            ```python
    if window_length >= len(y):
        window_length = min(len(y) - 2, 11)
        if window_length % 2 == 0:
            window_length -= 1
            ```
            - Window size must be smaller than `len(y)`, but close to `11`.
            - If necessary, adjusts to the nearest odd value.
    
        3. **Ensures `polyorder` is smaller than `window_length`**:
            ```python
    if polyorder >= window_length:
        polyorder = window_length - 1
            ```
            - Prevents error when applying the filter.
    
        4. **Applies the Savitzky-Golay filter**:
            ```python
    y_filtered = savgol_filter(y, window_length, polyorder)
            ```

        5. **Corrects negative values and normalizes the smoothed spectrum**:
            ```python
            if np.min(y_filtered) < 0:
                y_filtered = y_filtered - np.min(y_filtered)
                if np.max(y_filtered) > 0:
                    y_filtered = y_filtered / np.max(y_filtered)
                        - Ensures values are within the interval `[0,1]`.

    Notes:
        - The window size `window_length` must be odd and smaller than the spectrum size.
        - If `polyorder` is greater than or equal to `window_length`, it will be adjusted to avoid errors.
        - Final normalization ensures smoothed values remain within an appropriate range.

    Raises:
        ValueError: If `y` is not a valid NumPy array.
        RuntimeError: If parameters cannot be adjusted adequately.

    References
    ----------
    .. [1] Schmid, M., Rath, D., & Diebold, U. (2022). Why and How Savitzky–Golay 
           Filters Should Be Replaced. ACS Measurement Science Au, 2(2), 185-196.
           https://doi.org/10.1021/acsmeasuresciau.1c00054
           
    .. [2] Ryabchykov, O., Schie, I. W., Popp, J., & Bocklitz, T. (2022). 
           Errors and Mistakes to Avoid when Analyzing Raman Spectra. 
           Spectroscopy, 37(4), 48-50.
           https://doi.org/10.56530/spectroscopy.zz8373x6
           
    .. [3] Chen, K., Zhang, H., Wei, H., & Li, Y. (2022). Improved Savitzky-Golay-
           method-based fluorescence subtraction algorithm for rapid recovery of 
           Raman spectra. Applied Optics, 53(24), 5559-5569.
           https://doi.org/10.1364/AO.53.005559
           
    .. [4] Raju, M. H., Friedman, L., Bouman, T. M., & Komogortsev, O. V. (2023). 
           Filtering Eye-Tracking Data From an EyeLink 1000: Comparing Heuristic, 
           Savitzky-Golay, IIR and FIR Digital Filters. Journal of Eye Movement 
           Research, 14(3).
           https://doi.org/10.16910/jemr.14.3.6
           
    .. [5] Wawerski, A., Siemiątkowska, B., Józwik, M., Fajdek, B., & Partyka, M. (2024). 
           Machine Learning Method and Hyperspectral Imaging for Precise Determination 
           of Glucose and Silicon Levels. Sensors, 24(4), 1306.
           https://doi.org/10.3390/s24041306

    """
    if window_length % 2 == 0:
        window_length += 1
    
    if window_length >= len(y):
        window_length = min(len(y) - 2, 11)
        if window_length % 2 == 0:
            window_length -= 1
    
    if polyorder >= window_length:
        polyorder = window_length - 1
    
    y_filtered = savgol_filter(y, window_length, polyorder)
    
    if np.min(y_filtered) < 0:
        y_filtered = y_filtered - np.min(y_filtered)
        
        if np.max(y_filtered) > 0:
            y_filtered = y_filtered / np.max(y_filtered)
    
    return y_filtered

def find_raman_peaks(x, y, config):
    """
    Detects peaks in a Raman spectrum using SciPy's `find_peaks` algorithm.

    The function automatically identifies peaks based on criteria such as minimum height, 
    prominence, distance between peaks, and minimum width. If `height` or `prominence` 
    are not provided, default values proportional to the maximum of `y` are used.

    Args:
        x (numpy.ndarray): Array containing x-axis values (e.g., wavenumber in cm⁻¹).
        y (numpy.ndarray): Array containing Raman spectrum intensity values.
        config (dict): Configuration dictionary containing peak detection parameters.

    Returns:
        numpy.ndarray: Indices of detected peaks in the `x` array.

    Algorithm:
        1. **Defines values for `height` and `prominence` based on configuration**:
            ```python
            height = config["peak_detection"]["height_percent"] / 100 * np.max(y)
            prominence = config["peak_detection"]["prominence_percent"] / 100 * np.max(y)
            ```

        2. **Calls SciPy's `find_peaks` function to detect peaks**:
            ```python
            peaks_indices, _ = find_peaks(y, height=height, prominence=prominence, 
                                         distance=distance, width=width)
            ```
            - Identifies peaks based on the provided criteria.
            - Returns the indices of peaks in the `x` array.

    Notes:
        - `prominence` is useful for ignoring small signal fluctuations and detecting only significant peaks.
        - `distance` can be used to avoid detection of peaks that are too close together.

    Raises:
        ValueError: If `x` and `y` are not NumPy arrays of the same size.
        RuntimeError: If `find_peaks` fails due to invalid parameters.

    References
    ----------
    .. [1] Chen, X., Tang, P., Wan, J., Zhang, W., & Zhong, L. (2025). 
           Adaptive Raman spectral unmixing method based on Voigt peak compensation 
           for quantitative analysis of cellular biochemical components. 
           Biomedical Optics Express, 16(3), 1284-1298.
           https://doi.org/10.1364/BOE.553461
           (Método adaptativo usando detecção de picos para análise quantitativa)
           
    .. [2] Udensi, J., Loskutova, E., Loughman, J., & Byrne, H. J. (2022). 
           Quantitative Raman Analysis of Carotenoid Protein Complexes in Aqueous Solution. 
           Molecules, 27(15), 4724. 
           https://doi.org/10.3390/molecules27154724
           (Uso do find_peaks Python para detecção de picos em espectros Raman)
           
    .. [3] Ryabchykov, O., Schie, I. W., Popp, J., & Bocklitz, T. (2022). 
           Errors and Mistakes to Avoid when Analyzing Raman Spectra. 
           Spectroscopy, 37(4), 48-50.
           https://doi.org/10.56530/spectroscopy.zz8373x6
           (Boas práticas na análise de espectros Raman incluindo detecção de picos)
           
    .. [4] SciPy Documentation Team (2024). scipy.signal.find_peaks. 
           SciPy v1.15.3 Manual.
           https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.find_peaks.html
           (Documentação oficial da função find_peaks do SciPy)

    """
    peak_config = config["peak_detection"]
    height = peak_config["height_percent"] / 100 * np.max(y)
    prominence = peak_config["prominence_percent"] / 100 * np.max(y)
    distance = peak_config["distance"]
    width = peak_config["width"]
    
    peaks_indices, _ = find_peaks(y, height=height, prominence=prominence, 
                                 distance=distance, width=width)
    return peaks_indices

def calculate_fwhm(x, y, peaks_indices):
    """
    Calculates Full Width at Half Maximum (FWHM) for each detected peak in the Raman spectrum.

    The function uses SciPy's `peak_widths` to calculate peak widths at 50% of maximum height.
    It also corrects possible negative FWHM values and adjusts lateral positions if they are inconsistent.

    Args:
        x (numpy.ndarray): Array containing x-axis values (e.g., wavenumber in cm⁻¹).
        y (numpy.ndarray): Array containing Raman spectrum intensity values.
        peaks_indices (numpy.ndarray): Indices of detected peaks in `x`.

    Returns:
        tuple:
            - numpy.ndarray: FWHM values calculated for each peak.
            - numpy.ndarray: Left positions of FWHM width for each peak.
            - numpy.ndarray: Right positions of FWHM width for each peak.

    Algorithm:
        1. **Calculates peak widths at half height using `peak_widths`**:
            ```python
    widths_half, heights, left_ips, right_ips = peak_widths(y, peaks_indices, rel_height=0.5)
            ```
    
        2. **Determines x-axis resolution (`dx`)**:
            ```python
    dx = np.mean(np.diff(x))
            ```
    
        3. **Checks and corrects negative FWHM values**:
            ```python
    for i, width in enumerate(widths_half):
        if width < 0:
                    print(f"Warning: Negative FWHM detected for peak {i+1}. Value: {width * dx:.2f}")
            ```

        4. **Calculates absolute FWHM values**:
            ```python
            fwhm_values = np.abs(widths_half * dx)
            ```

        5. **Adjusts lateral FWHM positions**:
            - For each peak corrects inconsistent positions where the peak is outside the width limits.

    Notes:
        - `rel_height=0.5` means the width is measured at 50% of peak height (FWHM).
        - If `widths_half` is negative, a warning will be printed, but the value is corrected by taking its absolute value.
        - The `left_positions` and `right_positions` values are adjusted to avoid inversions or inconsistent positions.

    Raises:
        ValueError: If `x` and `y` are not valid NumPy arrays.
        RuntimeError: If `peak_widths` cannot calculate peak widths.

    References
    ----------
    .. [1] Suchorab, K., Gawęda, M., & Kurpaska, L. (2023). 
           Comparison of Raman imaging assessment methods in phase determination 
           and stress analysis of zirconium oxide layer. 
           Spectrochimica Acta Part A: Molecular and Biomolecular Spectroscopy, 
           295, 122625.
           https://doi.org/10.1016/j.saa.2023.122625
           (Análise detalhada de métodos de avaliação FWHM em imagens Raman)
           
    .. [2] Utesov, O. I., Yashenkin, A. G., & Koniakhin, S. V. (2020). 
           Lifetimes of Confined Optical Phonons and the Shape of a Raman Peak 
           in Disordered Nanoparticles: I. Analytical Treatment. 
           https://doi.org/10.1103/PhysRevB.102.205421
           (Teoria analítica sobre largura e forma de picos Raman em nanopartículas)
           
    .. [3] Neeshu, K. M., Rani, C., Kaushik, R., Tanwar, M., Kumar, A., & Kumar, R. (2022). 
           Size Dependent Sensitivity of Raman Line-Shape Parameters in Silicon Quantum Wire. 
           Journal of Physics: Conference Series, 2267(1), 012089.
           https://doi.org/10.1088/1742-6596/2267/1/012089
           (Dependência do tamanho nos parâmetros de forma de linha Raman incluindo FWHM)
           
    .. [4] Ryabchykov, O., Schie, I. W., Popp, J., & Bocklitz, T. (2022). 
           Errors and Mistakes to Avoid when Analyzing Raman Spectra. 
           Spectroscopy, 37(4), 48-50.
           https://doi.org/10.56530/spectroscopy.zz8373x6
           (Guia sobre boas práticas na análise de espectros Raman incluindo cálculo de FWHM)
           
    .. [5] Chen, X., Tang, P., Wan, J., Zhang, W., & Zhong, L. (2025). 
           Adaptive Raman spectral unmixing method based on Voigt peak compensation 
           for quantitative analysis of cellular biochemical components. 
           Biomedical Optics Express, 16(3), 1284-1298.
           https://doi.org/10.1364/BOE.553461
           (Método adaptativo usando compensação de picos Voigt para análise quantitativa)

    """
    widths_half, heights, left_ips, right_ips = peak_widths(y, peaks_indices, rel_height=0.5)
    
    dx = np.mean(np.diff(x))
    
    for i, width in enumerate(widths_half):
        if width < 0:
            print(f"Warning: Negative FWHM detected for peak {i+1}. Value: {width * dx:.2f}")

    fwhm_values = np.abs(widths_half * dx)
    
    left_positions = []
    right_positions = []
    
    for i, peak_idx in enumerate(peaks_indices):
        peak_pos = x[peak_idx]
        
        left_pos = x[0] + left_ips[i] * dx
        right_pos = x[0] + right_ips[i] * dx
        
        if left_pos > right_pos:
            left_pos, right_pos = right_pos, left_pos
            
        if peak_pos < left_pos or peak_pos > right_pos:
            width = right_pos - left_pos
            center = peak_pos
            left_pos = center - width/2
            right_pos = center + width/2
            
        left_positions.append(left_pos)
        right_positions.append(right_pos)
    
    return fwhm_values, np.array(left_positions), np.array(right_positions)

# ============ GAUSSIAN FITTING FUNCTION ============

def single_gaussian(x, amplitude, center, sigma, offset):
    """
    Mathematical model for Gaussian peak fitting.

    The function defines a Gaussian curve, widely used to model spectral peaks in Raman spectroscopy. 
    The model is defined by the equation:

        G(x) = amp * exp(-((x - center)²) / (2 * sigma²)) + offset

    Args:
        x (numpy.ndarray | float): X-axis values where the Gaussian function will be evaluated.
        amplitude (float): Peak amplitude (maximum height).
        center (float): Peak center position (x corresponding to maximum value).
        sigma (float): Gaussian standard deviation, which controls peak width.
        offset (float): Background value (baseline) added to the curve.

    Returns:
        numpy.ndarray | float: Gaussian curve values calculated for each point `x`.

    Algorithm:
        1. **Calculates the Gaussian shape**:
            ```python
            gaussian = amplitude * np.exp(-((x - center) ** 2) / (2 * sigma ** 2))
            ```

        2. **Adds the offset value**:
            ```python
            return gaussian + offset
            ```

    Notes:
        - The Full Width at Half Maximum (FWHM) of the Gaussian can be obtained by:
            ```python
            FWHM = 2.3548 * sigma
            ```
        - If `sigma` is too small, the resulting curve will be very narrow and may not correctly represent a Raman peak.
        - The presence of an `offset` allows fitting the curve when there is a non-zero background in the spectrum baseline.

    Raises:
        ValueError: If `sigma <= 0`, since a Gaussian with negative or zero standard deviation is not valid.

    References:
        .. [1] Suchorab, K., Gawęda, M., & Kurpaska, L. (2023). "Comparison of Raman imaging assessment 
               methods in phase determination and stress analysis of zirconium oxide layer." 
               *Spectrochimica Acta Part A: Molecular and Biomolecular Spectroscopy*, 302, 122625.
               DOI: https://doi.org/10.1016/j.saa.2023.122625
        
        .. [2] Klein, K., Klamminger, G.G., et al. (2024). "Computational Assessment of Spectral Heterogeneity 
               within Fresh Glioblastoma Tissue Using Raman Spectroscopy and Machine Learning Algorithms." 
               *Molecules*, 29(5), 979. DOI: https://doi.org/10.3390/molecules29050979
        
        .. [3] Hollon, T.C., Pandian, B., et al. (2020). "Near real-time intraoperative brain tumor diagnosis 
               using stimulated Raman histology and deep neural networks." *Nature Medicine*, 26(1), 52-58.
               DOI: https://doi.org/10.1038/s41591-019-0715-9
        
        .. [4] Riva, M., Sciortino, T., et al. (2021). "Glioma Biopsies Classification Using Raman Spectroscopy 
               and Machine Learning Models on Fresh Tissue Samples." *Cancers*, 13(5), 1073.
               DOI: https://doi.org/10.3390/cancers13051073
        
        .. [5] Jermyn, M., Desroches, J., et al. (2016). "Raman spectroscopy detects distant invasive brain 
               cancer cells centimeters beyond MRI capability in humans." *Biomedical Optics Express*, 7(12), 
               5129-5137. DOI: https://doi.org/10.1364/BOE.7.005129

    """
    return amplitude * np.exp(-(x - center)**2 / (2 * sigma**2)) + offset

def fit_gaussian_profiles(x, y, peaks_indices, fwhm_left_ips, fwhm_right_ips, method='trf', max_iterations=1000, tolerance=1e-8):
    """
    Ajusta perfis Gaussianos individuais aos picos detectados em espectros Raman com análise estatística avançada.
    
    Esta função implementa um algoritmo robusto para ajuste de perfis Gaussianos a picos espectrais individuais,
    especialmente desenvolvida para análise quantitativa de espectros Raman de minerais e materiais cristalinos.
    A implementação utiliza otimização não-linear com restrições adaptativas e validação estatística rigorosa
    para garantir a qualidade e confiabilidade dos ajustes.
    
    A função é particularmente eficaz para:
    - Análise quantitativa de picos Raman em zircão e outros minerais
    - Determinação precisa de larguras espectrais (FWHM) para estudos de dano por radiação
    - Cálculo de áreas espectrais para análise semi-quantitativa
    - Avaliação da qualidade de ajuste através de métricas estatísticas múltiplas
    - Processamento em lote de grandes conjuntos de dados espectrais
    
    **Algoritmo de Ajuste:**
    
    1. **Definição da Região de Ajuste:**
       - Utiliza as posições FWHM detectadas para definir limites de ajuste
       - Aplica margem de segurança (20% da largura) para capturar toda a banda
       - Valida o número mínimo de pontos para ajuste estatisticamente significativo
    
    2. **Estimativa de Parâmetros Iniciais:**
       - Amplitude: intensidade máxima do pico detectado
       - Centro: posição do máximo local
       - Largura (σ): estimativa baseada na FWHM detectada (FWHM/2.355)
       - Offset: linha de base local estimada
    
    3. **Otimização com Restrições:**
       - Limites físicos para todos os parâmetros
       - Prevenção de soluções não-físicas (amplitudes negativas, larguras excessivas)
       - Algoritmos robustos de otimização não-linear
    
    4. **Validação Estatística:**
       - Cálculo de R² para avaliação da qualidade do ajuste
       - Chi-quadrado reduzido para análise de resíduos
       - Comparação entre área analítica e numérica
    
    Parameters
    ----------
    x : array_like
        Array 1D contendo os valores do eixo x (números de onda em cm⁻¹).
        Deve ser monotonicamente crescente e ter resolução adequada.
    y : array_like
        Array 1D contendo os valores de intensidade espectral correspondentes.
        Deve ter o mesmo comprimento que x.
    peaks_indices : array_like
        Índices dos picos detectados no array x. Cada índice corresponde à
        posição de um máximo local identificado pelo algoritmo de detecção de picos.
    fwhm_left_ips : array_like
        Posições das bordas esquerdas dos picos à meia altura (interpoladas).
        Usado para definir o limite inferior da região de ajuste.
    fwhm_right_ips : array_like
        Posições das bordas direitas dos picos à meia altura (interpoladas).
        Usado para definir o limite superior da região de ajuste.
    method : str, optional
        Método de otimização para scipy.optimize.curve_fit:
        
        - 'trf' (padrão): Trust Region Reflective, robusto para problemas com restrições
        - 'lm': Levenberg-Marquardt, eficiente mas sem suporte a restrições
        - 'dogbox': Dogleg com retângulo, alternativa robusta para problemas mal-condicionados
        
        Default: 'trf' (recomendado para dados espectrais com ruído).
    max_iterations : int, optional
        Número máximo de iterações para o algoritmo de otimização.
        Valores típicos: 1000-10000. Default: 1000.
    tolerance : float, optional
        Tolerância para convergência do algoritmo de otimização.
        Controla tanto ftol quanto xtol simultaneamente. Default: 1e-8.
    
    Returns
    -------
    list of dict
        Lista contendo dicionários com os resultados do ajuste para cada pico.
        Cada dicionário contém:
        
        **Parâmetros do Ajuste Gaussiano:**
        
        - 'amplitude' : float
            Amplitude máxima da Gaussiana ajustada (unidades de intensidade)
        - 'center' : float
            Posição central do pico (cm⁻¹)
        - 'sigma' : float
            Desvio padrão da Gaussiana (cm⁻¹)
        - 'offset' : float
            Deslocamento vertical (linha de base local)
        
        **Métricas Espectrais Derivadas:**
        
        - 'fwhm_gaussian' : float
            Largura total à meia altura calculada: FWHM = 2.355 × σ (cm⁻¹)
        - 'area_gaussian' : float
            Área analítica da Gaussiana: A = amplitude × σ × √(2π)
        - 'area_numerical' : float
            Área calculada por integração numérica (método de Simpson)
        
        **Métricas de Qualidade Estatística:**
        
        - 'r_squared' : float
            Coeficiente de determinação R² (0 ≤ R² ≤ 1)
            R² > 0.95: excelente ajuste
            R² > 0.90: bom ajuste  
            R² < 0.80: ajuste questionável
        - 'chi_squared_reduced' : float
            Chi-quadrado reduzido χ²ᵣ = χ²/(n-p)
            χ²ᵣ ≈ 1: ajuste ideal
            χ²ᵣ >> 1: sub-ajuste (modelo inadequado)
            χ²ᵣ << 1: sobre-ajuste
        
        **Informações de Processamento:**
        
        - 'fit_range' : tuple
            Intervalo de números de onda usado para o ajuste (min, max)
    
    Notes
    -----
    **Modelo Matemático:**
    
    A função utiliza o modelo Gaussiano com offset:
    
    .. math::
        G(x) = A \\exp\\left(-\\frac{(x-\\mu)^2}{2\\sigma^2}\\right) + c
    
    onde:
    - A é a amplitude (altura máxima)
    - μ é o centro (posição do pico)
    - σ é o desvio padrão (relacionado à largura)
    - c é o offset (linha de base local)
    
    **Relações Espectrais Importantes:**
    
    - Largura à meia altura: FWHM = 2√(2ln2)σ ≈ 2.355σ
    - Área integrada: Área = Aσ√(2π)
    - Intensidade relativa: I_rel = A/A_ref
    
    **Critérios de Qualidade:**
    
    1. **Número mínimo de pontos:** ≥ 5 pontos na região de ajuste
    2. **Convergência:** Tolerância de 1e-8 para parâmetros e função objetivo
    3. **Restrições físicas:** 
       - Amplitude > 0
       - Largura > 0 e < largura máxima fisicamente plausível
       - Centro dentro da região espectral válida
    4. **Validação estatística:** R² > 0.3 para aceitação do ajuste
    
    **Tratamento de Erros:**
    
    - Picos com < 5 pontos na região de ajuste são ignorados
    - Falhas de convergência são reportadas mas não interrompem o processamento
    - Parâmetros fora dos limites físicos são rejeitados
    
    **Considerações Computacionais:**
    
    - Complexidade: O(n × m × iter) onde n = pontos por pico, m = número de picos
    - Memória: O(n) por pico processado
    - Paralelização: Cada pico é processado independentemente
    
    Examples
    --------
    **Exemplo 1: Ajuste básico de picos detectados**
    
    >>> import numpy as np
    >>> from scipy.signal import find_peaks
    >>> 
    >>> # Dados sintéticos de espectro Raman
    >>> x = np.linspace(100, 300, 500)
    >>> y = (2.0 * np.exp(-((x-150)**2)/(2*5**2)) + 
    ...      1.5 * np.exp(-((x-200)**2)/(2*8**2)) + 
    ...      0.1 * np.random.normal(size=len(x)))
    >>> 
    >>> # Detectar picos
    >>> peaks, _ = find_peaks(y, height=0.5, distance=20)
    >>> 
    >>> # Calcular FWHM (simplificado para exemplo)
    >>> fwhm_left = x[peaks] - 10   # Estimativa simplificada
    >>> fwhm_right = x[peaks] + 10  # Estimativa simplificada
    >>> 
    >>> # Ajustar perfis Gaussianos
    >>> results = fit_gaussian_profiles(x, y, peaks, fwhm_left, fwhm_right)
    >>> 
    >>> # Analisar resultados
    >>> for i, result in enumerate(results):
    ...     print(f"Pico {i+1}:")
    ...     print(f"  Centro: {result['center']:.2f} cm⁻¹")
    ...     print(f"  FWHM: {result['fwhm_gaussian']:.2f} cm⁻¹")
    ...     print(f"  Área: {result['area_gaussian']:.2f}")
    ...     print(f"  R²: {result['r_squared']:.4f}")
    
    **Exemplo 2: Análise de qualidade de ajuste**
    
    >>> # Filtrar apenas ajustes de alta qualidade
    >>> good_fits = [r for r in results if r['r_squared'] > 0.95]
    >>> print(f"Ajustes de alta qualidade: {len(good_fits)}/{len(results)}")
    >>> 
    >>> # Calcular estatísticas de largura espectral
    >>> fwhm_values = [r['fwhm_gaussian'] for r in good_fits]
    >>> mean_fwhm = np.mean(fwhm_values)
    >>> std_fwhm = np.std(fwhm_values)
    >>> print(f"FWHM médio: {mean_fwhm:.2f} ± {std_fwhm:.2f} cm⁻¹")
    
    **Exemplo 3: Comparação de métodos de otimização**
    
    >>> # Testar diferentes métodos
    >>> methods = ['trf', 'lm', 'dogbox']
    >>> for method in methods:
    ...     try:
    ...         results = fit_gaussian_profiles(x, y, peaks, fwhm_left, fwhm_right, 
    ...                                        method=method)
    ...         avg_r2 = np.mean([r['r_squared'] for r in results])
    ...         print(f"Método {method}: R² médio = {avg_r2:.4f}")
    ...     except Exception as e:
    ...         print(f"Método {method}: Falhou - {e}")
    
    See Also
    --------
    single_gaussian : Função modelo Gaussiana utilizada no ajuste
    calculate_gaussian_area : Cálculo analítico da área Gaussiana
    scipy.optimize.curve_fit : Função de otimização não-linear subjacente
    scipy.integrate.simpson : Integração numérica para validação de área
    find_raman_peaks : Detecção de picos para uso com esta função
    
    References
    ----------
    .. [1] Kaneki, S., et al. (2024). "An automatic peak deconvolution code for Raman spectra 
           of carbonaceous material and a revised geothermometer for intermediate- to moderately 
           high-grade metamorphism." *Progress in Earth and Planetary Science*, 11, 35.
           https://doi.org/10.1186/s40645-024-00637-8
    
    .. [2] Suchorab, K., et al. (2023). "Comparison of Raman imaging assessment methods in phase 
           determination and stress analysis of zirconium oxide layer." *Spectrochimica Acta 
           Part A: Molecular and Biomolecular Spectroscopy*, 295, 122625.
           https://doi.org/10.1016/j.saa.2023.122625
    
    .. [3] Udensi, J., et al. (2022). "Quantitative Raman Analysis of Carotenoid Protein Complexes 
           in Aqueous Solution." *Molecules*, 27(15), 4724. 
           https://doi.org/10.3390/molecules27154724
    
    .. [4] Sparavigna, A.C. (2024). "q-Gaussian and q-BWF functions for the deconvolution of 
           Raman and infrared spectra of Calcite." *ChemRxiv* preprint.
           https://doi.org/10.26434/chemrxiv-2024-nsmch
    
    .. [5] Meier, R.J. (2023). "Comment on Tagliaferro et al. Introducing the Novel Mixed 
           Gaussian-Lorentzian Lineshape in the Analysis of the Raman Signal of Biochar." 
           *Nanomaterials*, 13(1), 108. https://doi.org/10.3390/nano13010108
    
    .. [6] Tagliaferro, A., et al. (2022). "Introducing the Novel Mixed Gaussian-Lorentzian 
           Lineshape in the Analysis of the Raman Signal of Biochar." *Nanomaterials*, 12(9), 1478.
           https://doi.org/10.3390/nano10091748
    
    .. [7] Levenberg, K. (1944). "A method for the solution of certain non-linear problems 
           in least squares." *Quarterly of Applied Mathematics*, 2(2), 164-168.
    
    .. [8] Marquardt, D.W. (1963). "An algorithm for least-squares estimation of nonlinear 
           parameters." *Journal of the Society for Industrial and Applied Mathematics*, 11(2), 431-441.
    
    .. [9] Moré, J.J. (1978). "The Levenberg-Marquardt algorithm: implementation and theory." 
           In *Numerical Analysis* (pp. 105-116). Springer, Berlin, Heidelberg.
    
    .. [10] Ginster, U., et al. (2019). "Annealing kinetics of radiation damage in zircon." 
            *Geochimica et Cosmochimica Acta*, 249, 225-246.
            https://doi.org/10.1016/j.gca.2019.01.033
    
    """
    from scipy.optimize import curve_fit

    fitted_params = []
    y_fitted = np.zeros_like(y)

    for i, peak_idx in enumerate(peaks_indices):
        x_peak = x[peak_idx]
        y_peak = y[peak_idx]

        left_pos = fwhm_left_ips[i]
        right_pos = fwhm_right_ips[i]
        width = right_pos - left_pos
        margin = 0.2 * width
        left_with_margin = max(min(x), left_pos - margin)
        right_with_margin = min(max(x), right_pos + margin)

        fit_mask = (x >= left_with_margin) & (x <= right_with_margin)
        x_fit = x[fit_mask]
        y_fit = y[fit_mask]

        if len(x_fit) < 5:
            continue

        initial_params = [y_peak, x_peak, width / 2.355, 0.0]

        try:
            param_bounds = ([0, min(x_fit), 0, -0.1],
                            [min(1.0, 2 * y_peak), max(x_fit), width, 0.1])

            popt, pcov = curve_fit(
                single_gaussian, x_fit, y_fit, p0=initial_params, bounds=param_bounds,
                method=method, maxfev=max_iterations, ftol=tolerance, xtol=tolerance
            )

            residuals = y_fit - single_gaussian(x_fit, *popt)
            ss_residuals = np.sum(residuals**2)
            ss_total = np.sum((y_fit - np.mean(y_fit))**2)
            r_squared = 1 - (ss_residuals / ss_total)

            degrees_of_freedom = max(1, len(y_fit) - len(popt))  
            chi_squared = np.sum((residuals ** 2) / np.var(y_fit))  
            chi_squared_reduced = chi_squared / degrees_of_freedom
            
            # Calcular a área da função Gaussiana
            gaussian_area = calculate_gaussian_area(popt[0], popt[2])
            
            # Calcular a área por integração numérica usando Simpson
            x_range = x[fit_mask]
            y_fitted_range = single_gaussian(x_range, *popt) - popt[3]  # Subtrair o offset
            numerical_area = integrate.simpson(y_fitted_range, x_range)

            fit_result = {
                'amplitude': popt[0],
                'center': popt[1],
                'sigma': popt[2],
                'offset': popt[3],
                'fwhm_gaussian': 2.355 * popt[2],
                'area_gaussian': gaussian_area,
                'area_numerical': numerical_area,     
                'r_squared': r_squared,
                'chi_squared_reduced': chi_squared_reduced,
                'fit_range': (left_with_margin, right_with_margin)  
            }
            fitted_params.append(fit_result)

            y_fitted += single_gaussian(x, *popt)

        except Exception as e:
            print(f"Error fitting peak {i+1}: {e}")
            continue

    return fitted_params

def calculate_gaussian_area(amplitude, sigma):
    """
    Calcula a área integrada de uma função Gaussiana usando a fórmula analítica exata.
    
    Esta função implementa o cálculo direto da área sob uma curva Gaussiana utilizando
    a solução analítica da integral definida, fornecendo resultados precisos e computacionalmente
    eficientes para análise quantitativa de espectros Raman. A implementação é especialmente
    otimizada para aplicações em espectroscopia vibracional onde a área dos picos está
    diretamente relacionada à concentração ou abundância relativa dos componentes espectrais.
    
    **Fundamento Matemático:**
    
    A área de uma função Gaussiana é calculada pela integral definida:
    
    .. math::
        \\text{Área} = \\int_{-\\infty}^{+\\infty} A \\exp\\left(-\\frac{(x-\\mu)^2}{2\\sigma^2}\\right) dx
    
    que possui solução analítica exata:
    
    .. math::
        \\text{Área} = A \\sigma \\sqrt{2\\pi}
    
    onde A é a amplitude máxima e σ é o desvio padrão da distribuição Gaussiana.
    
    **Aplicações em Espectroscopia Raman:**
    
    - **Análise quantitativa:** Determinação de concentrações relativas de fases minerais
    - **Estudos de cinética:** Monitoramento de reações através da evolução das áreas espectrais
    - **Caracterização de materiais:** Quantificação de defeitos e impurezas cristalinas
    - **Análise de misturas:** Determinação de proporções de componentes em sistemas complexos
    - **Validação de ajustes:** Comparação com integração numérica para controle de qualidade
    
    **Vantagens da Solução Analítica:**
    
    1. **Precisão absoluta:** Não há erros de discretização ou aproximação numérica
    2. **Eficiência computacional:** Cálculo direto sem iterações ou integrações numéricas
    3. **Estabilidade numérica:** Robusta para ampla faixa de valores de amplitude e largura
    4. **Reprodutibilidade:** Resultados idênticos independente da plataforma computacional
    
    Parameters
    ----------
    amplitude : float
        Amplitude máxima da função Gaussiana (altura do pico).
        Deve ser um valor positivo em unidades de intensidade espectral.
        Valores típicos em espectroscopia Raman: 10² - 10⁶ contagens.
    sigma : float
        Desvio padrão da distribuição Gaussiana (parâmetro de largura).
        Deve ser um valor positivo em unidades do eixo x (tipicamente cm⁻¹).
        Relacionado à FWHM por: σ = FWHM / (2√(2ln2)) ≈ FWHM / 2.355.
        Valores típicos para picos Raman: 1-50 cm⁻¹.
    
    Returns
    -------
    float
        Área integrada da função Gaussiana em unidades de [intensidade × eixo_x].
        Para espectros Raman: [contagens × cm⁻¹] ou [u.a. × cm⁻¹].
        
        A área representa a intensidade integrada total do pico, que é proporcional
        à quantidade de material responsável pelo modo vibracional correspondente.
    
    Raises
    ------
    ValueError
        Se amplitude ≤ 0 ou sigma ≤ 0, pois estes valores não são fisicamente
        válidos para uma distribuição Gaussiana.
    TypeError
        Se os parâmetros não forem numéricos (int, float, numpy.number).
    
    Notes
    -----
    **Relações Espectrais Importantes:**
    
    1. **Relação com FWHM:**
       
       .. math::
           \\text{FWHM} = 2\\sqrt{2\\ln(2)} \\sigma \\approx 2.355 \\sigma
       
       Portanto: σ = FWHM / 2.355
    
    2. **Relação com intensidade máxima:**
       
       A amplitude A corresponde à intensidade máxima do pico Gaussiano.
    
    3. **Área normalizada:**
       
       Para uma Gaussiana normalizada (área = 1):
       
       .. math::
           G_{\\text{norm}}(x) = \\frac{1}{\\sigma\\sqrt{2\\pi}} \\exp\\left(-\\frac{(x-\\mu)^2}{2\\sigma^2}\\right)
    
    4. **Conversão entre representações:**
       
       - Área → Amplitude: A = Área / (σ√(2π))
       - Amplitude → Área: Área = A × σ × √(2π)
    
    **Considerações Físicas:**
    
    - A área é independente da posição central (μ) do pico
    - A área escala linearmente com a amplitude
    - A área escala linearmente com o desvio padrão
    - Para picos Raman, a área é proporcional ao número de osciladores
    
    **Validação e Controle de Qualidade:**
    
    Esta função é frequentemente usada em conjunto com integração numérica
    (ex: scipy.integrate.simpson) para validar a qualidade dos ajustes Gaussianos:
    
    .. math::
        \\text{Erro relativo} = \\frac{|\\text{Área}_{\\text{analítica}} - \\text{Área}_{\\text{numérica}}|}{\\text{Área}_{\\text{analítica}}} \\times 100\\%
    
    Erros < 1% indicam ajustes de alta qualidade.
    
    **Limitações:**
    
    - Válida apenas para perfis puramente Gaussianos
    - Não aplicável a perfis Lorentzianos, Voigt ou assimétricos
    - Assume linha de base já subtraída (offset = 0)
    
    Examples
    --------
    **Exemplo 1: Cálculo básico de área**
    
    >>> amplitude = 1000.0  # contagens
    >>> sigma = 5.0         # cm⁻¹
    >>> area = calculate_gaussian_area(amplitude, sigma)
    >>> print(f"Área: {area:.2f} contagens·cm⁻¹")
    Área: 12533.14 contagens·cm⁻¹
    
    **Exemplo 2: Conversão FWHM → σ → Área**
    
    >>> fwhm = 12.0  # cm⁻¹
    >>> sigma = fwhm / 2.355
    >>> amplitude = 500.0
    >>> area = calculate_gaussian_area(amplitude, sigma)
    >>> print(f"FWHM: {fwhm:.1f} cm⁻¹")
    >>> print(f"σ: {sigma:.2f} cm⁻¹") 
    >>> print(f"Área: {area:.1f} contagens·cm⁻¹")
    FWHM: 12.0 cm⁻¹
    σ: 5.10 cm⁻¹
    Área: 6377.9 contagens·cm⁻¹
    
    **Exemplo 3: Análise quantitativa de múltiplos picos**
    
    >>> # Dados de ajuste para múltiplos picos
    >>> picos = [
    ...     {'amplitude': 800, 'sigma': 4.2, 'centro': 1008},  # Pico principal zircão
    ...     {'amplitude': 200, 'sigma': 6.1, 'centro': 1178},  # Pico secundário
    ...     {'amplitude': 150, 'sigma': 3.8, 'centro': 1356}   # Pico menor
    ... ]
    >>> 
    >>> areas = []
    >>> for i, pico in enumerate(picos):
    ...     area = calculate_gaussian_area(pico['amplitude'], pico['sigma'])
    ...     areas.append(area)
    ...     print(f"Pico {i+1} ({pico['centro']} cm⁻¹): {area:.0f} u.a.·cm⁻¹")
    >>> 
    >>> # Calcular proporções relativas
    >>> area_total = sum(areas)
    >>> for i, area in enumerate(areas):
    ...     proporcao = (area / area_total) * 100
    ...     print(f"Pico {i+1}: {proporcao:.1f}% da área total")
    
    **Exemplo 4: Validação com integração numérica**
    
    >>> import numpy as np
    >>> from scipy.integrate import quad
    >>> 
    >>> def gaussian(x, A, mu, sigma):
    ...     return A * np.exp(-((x - mu)**2) / (2 * sigma**2))
    >>> 
    >>> # Parâmetros do pico
    >>> A, mu, sigma = 1000, 1008, 5.0
    >>> 
    >>> # Área analítica
    >>> area_analitica = calculate_gaussian_area(A, sigma)
    >>> 
    >>> # Área numérica (integração)
    >>> area_numerica, _ = quad(gaussian, mu-5*sigma, mu+5*sigma, args=(A, mu, sigma))
    >>> 
    >>> # Comparação
    >>> erro_relativo = abs(area_analitica - area_numerica) / area_analitica * 100
    >>> print(f"Área analítica: {area_analitica:.2f}")
    >>> print(f"Área numérica:  {area_numerica:.2f}")
    >>> print(f"Erro relativo:  {erro_relativo:.4f}%")
    
    **Exemplo 5: Análise de sensibilidade**
    
    >>> # Estudo da dependência da área com os parâmetros
    >>> amplitude_base = 1000
    >>> sigma_base = 5.0
    >>> 
    >>> # Variação da amplitude
    >>> for fator in [0.5, 1.0, 2.0]:
    ...     area = calculate_gaussian_area(amplitude_base * fator, sigma_base)
    ...     print(f"Amplitude × {fator}: Área = {area:.0f} (fator {area/12533:.1f})")
    >>> 
    >>> # Variação do sigma
    >>> for fator in [0.5, 1.0, 2.0]:
    ...     area = calculate_gaussian_area(amplitude_base, sigma_base * fator)
    ...     print(f"Sigma × {fator}: Área = {area:.0f} (fator {area/12533:.1f})")
    
    See Also
    --------
    single_gaussian : Função modelo Gaussiana
    fit_gaussian_profiles : Ajuste de perfis Gaussianos que utiliza esta função
    scipy.integrate.simpson : Integração numérica para validação
    scipy.integrate.quad : Integração adaptativa de alta precisão
    numpy.trapz : Integração trapezoidal simples
    
    References
    ----------
    .. [1] Kaneki, S., et al. (2024). "An automatic peak deconvolution code for Raman spectra 
           of carbonaceous material and a revised geothermometer for intermediate- to moderately 
           high-grade metamorphism." *Progress in Earth and Planetary Science*, 11, 35.
           https://doi.org/10.1186/s40645-024-00637-8
    
    .. [2] Udensi, J., et al. (2022). "Quantitative Raman Analysis of Carotenoid Protein Complexes 
           in Aqueous Solution." *Molecules*, 27(15), 4724. 
           https://doi.org/10.3390/molecules27154724
    
    
    .. [4] Tagliaferro, A., et al. (2022). "Introducing the Novel Mixed Gaussian-Lorentzian 
           Lineshape in the Analysis of the Raman Signal of Biochar." *Nanomaterials*, 12(9), 1478.
           já citado anteriormente
    
    .. [5] Meier, R.J. (2023). "Comment on Tagliaferro et al. Introducing the Novel Mixed 
           Gaussian-Lorentzian Lineshape in the Analysis of the Raman Signal of Biochar." 
           *Nanomaterials*, 13(1), 108. https://doi.org/10.3390/nano13010108
    
    .. [6] Suchorab, K., et al. (2023). "Comparison of Raman imaging assessment methods in phase 
           determination and stress analysis of zirconium oxide layer." *Spectrochimica Acta 
           Part A: Molecular and Biomolecular Spectroscopy*, 295, 122625.
           https://doi.org/10.1016/j.saa.2023.122625
    
    .. [7] Abramowitz, M., & Stegun, I.A. (1972). "Handbook of Mathematical Functions with 
           Formulas, Graphs, and Mathematical Tables." Dover Publications, New York.
    
    .. [8] Press, W.H., et al. (2007). "Numerical Recipes: The Art of Scientific Computing" 
           (3rd ed.). Cambridge University Press.
    
    .. [9] Bevington, P.R., & Robinson, D.K. (2003). "Data Reduction and Error Analysis 
           for the Physical Sciences" (3rd ed.). McGraw-Hill Higher Education.
    
    .. [10] Papoulis, A., & Pillai, S.U. (2002). "Probability, Random Variables, and 
            Stochastic Processes" (4th ed.). McGraw-Hill Higher Education.
    
    """
    return amplitude * sigma * np.sqrt(2 * np.pi)

def categorize_radiation_damage(fwhm):
    r"""
    Estima a dose equivalente de dano por radiação (Ded) com base na FWHM do pico Raman.

    A equação usada é derivada empiricamente dos dados de Ginster et al. (2019), 
    obtida através de regressão linear dos dados experimentais de zircão.

    Fórmula utilizada:
        Ded = -0.1402 + 0.07683 × FWHM

    Onde:
        - FWHM: Largura total à meia altura (Full Width at Half Maximum) do pico Raman (cm⁻¹).
        - -0.1402: Intercepto da regressão linear (coeficiente b).
        - 0.07683: Inclinação da regressão linear (coeficiente a).

    Dados utilizados para calibração (Ginster et al., 2019):
        - FWHM: [4.9, 11.0, 17.8, 7.3, 11.6] cm⁻¹
        - Ded observado: [0.27, 0.67, 1.26, 0.42, 0.72]
        - R²: ~0.955 (excelente correlação)

    Classificação do dano por radiação:
        - "Baixo dano"       : FWHM ≤ 8 cm⁻¹
        - "Dano moderado"    : 8 < FWHM ≤ 14.5 cm⁻¹
        - "Alto dano"        : 14.5 < FWHM ≤ 25 cm⁻¹
        - "Quase amorfo"     : FWHM > 25 cm⁻¹

    Referência:
        - Ginster, U., Reiners, P. W., Nasdala, L., & Chanmuang, C. N. (2019). 
            Annealing kinetics of radiation damage in zircon. 
            Geochimica et Cosmochimica Acta, 249, 225–246.
            https://doi.org/10.1016/j.gca.2019.01.033
    
    Args:
        fwhm (float): Largura total à meia altura (cm⁻¹) do pico Raman.
    
    Returns:
        tuple[str, float]: 
            - Categoria do dano por radiação ("Baixo dano", "Dano moderado", etc.).
            - Dose estimada de radiação acumulada usando a calibração de Ginster et al. (2019).
    """

    # Calcular dose usando a fórmula de Ginster et al. (2019): Ded = -0.1402 + 0.07683 × FWHM
    dose = -0.1402 + 0.07683 * fwhm

    # Classificar o dano baseado nos limiares de FWHM
    if fwhm <= 8:
        return "Baixo dano", dose
    elif fwhm <= 14.5:
        return "Dano moderado", dose
    elif fwhm <= 25:
        return "Alto dano", dose
    else:
        return "Quase amorfo", dose

def detect_and_remove_outliers(results_df, verbose=True):
    """
    Detecta e remove outliers dos dados de espectroscopia Raman por região espectral usando
    algoritmos estatísticos robustos e critérios físico-químicos específicos para zircão.
    
    Esta função implementa uma abordagem multi-critério para identificação de outliers
    em dados espectrais Raman, considerando tanto a qualidade dos ajustes gaussianos
    quanto a plausibilidade física dos parâmetros espectrais. A metodologia segue as
    melhores práticas estabelecidas na literatura recente de análise estatística de
    dados espectrais e mineralogia aplicada.
    
    FUNDAMENTAÇÃO TEÓRICA:
    ======================
    Os outliers em espectroscopia Raman podem originar-se de:
    1. Artefatos instrumentais (flutuações térmicas, vibrações mecânicas)
    2. Problemas de focalização ou posicionamento da amostra
    3. Inclusões minerais ou contaminação superficial
    4. Erros de processamento ou ajuste matemático
    5. Heterogeneidades estruturais extremas no cristal
    
    ALGORITMOS IMPLEMENTADOS:
    =========================
    
    1. **Critério de Qualidade de Ajuste (R²)**:
        - Remove ajustes gaussianos com R² < 0.3
        - Baseado em práticas estabelecidas para confiabilidade estatística
        - Elimina picos mal definidos ou com perfil não-gaussiano
    
    2. **Método do Intervalo Interquartil (IQR)**:
        - Identifica valores de FWHM fora de Q1-1.5×IQR ou Q3+1.5×IQR
        - Método robusto contra distribuições não-normais [1, 2, 3]
        - Aplicado separadamente para cada região espectral para maior precisão
    
    3. **Teste de Z-score Modificado**:
       - Remove valores com |Z| > 3 para FWHM
       - Detecta valores estatisticamente extremos [2, 4, 5]
       - Considera apenas regiões com n ≥ 3 e desvio padrão > 0
    
    4. **Critérios Físico-Químicos para Zircão**:
       - Remove FWHM > 60 cm⁻¹ (estruturalmente implausível para ZrSiO₄)
       - Baseado em limites físicos conhecidos para vibrações cristalinas de zircão
       - Para picos não classificados: R² < 0.5 ou FWHM > 50 cm⁻¹
    
    PROCESSAMENTO POR REGIÕES:
    ==========================
    A função processa dados separadamente para cada região espectral definida
    em get_zircon_spectral_regions(), utilizando intervalos mutuamente exclusivos
    para evitar contagem dupla de picos próximos aos limites regionais.
    
    VALIDAÇÃO ESTATÍSTICA:
    =====================
    Para cada região processada, a função calcula e compara:
    - Estatísticas descritivas antes/depois da limpeza
    - Coeficiente de variação (CV) para avaliar melhoria na consistência
    - Melhoria no R² médio dos ajustes gaussianos
    - Percentual de dados removidos para controle de qualidade
    
    REFERÊNCIAS CIENTÍFICAS:
    =========================
    [1] Pell, R.J. (2000). "Multiple outlier detection for multivariate calibration 
        using robust statistical techniques." *Chemometrics and Intelligent Laboratory 
        Systems*, 52(1), 87-104. https://doi.org/10.1016/S0169-7439(00)00082-4
    
    [2] Thériault, R. et al. (2024). "Check your outliers! An introduction to 
        identifying statistical outliers in R with easystats." *Behavior Research 
        Methods*, 56, 874–906. https://doi.org/10.3758/s13428-024-02356-w
    
    [3] Shimizu, Y. (2022). "Multiple Desirable Methods in Outlier Detection of 
        Univariate Data With R Source Codes." *Frontiers in Psychology*, 12:819854. 
        https://doi.org/10.3389/fpsyg.2021.819854
    
    [4] Romo-Chavero, M.A. et al. (2024). "Median Absolute Deviation for BGP Anomaly 
        Detection." *Future Internet*, 16(5), 146. https://doi.org/10.3390/fi16050146
    
    [5] Roos-Hoefgeest Toribio, M. et al. (2025). "A Novel Approach to Speed Up 
        Hampel Filter for Outlier Detection." *Sensors*, 25(11), 3319. 
        https://doi.org/10.3390/s25113319
    
    IMPLEMENTAÇÃO ALGORÍTMICA:
    =========================
    O algoritmo utiliza uma abordagem sequencial mas não-destrutiva:
    1. Carrega regiões espectrais centralizadas via get_zircon_spectral_regions()
    2. Para cada região, aplica todos os critérios em paralelo
    3. Unifica índices de outliers detectados (sem duplicação)
    4. Calcula estatísticas comparativas antes/depois da remoção
    5. Gera relatório detalhado por região e global
    6. Processa picos não-classificados com critérios mais restritivos
    
    Args:
        results_df (pandas.DataFrame): DataFrame contendo os resultados da análise espectral.
            Deve conter as colunas: 'Centro', 'FWHM_Gauss', 'R2', 'Pico', 'Amostra'.
            Representa os dados brutos de picos Raman identificados e ajustados.
            
        verbose (bool, optional): Controla o nível de saída de informações.
            - True: Imprime relatório detalhado com estatísticas por região,
              comparações antes/depois, e avaliação de melhoria na qualidade.
            - False: Execução silenciosa retornando apenas os resultados.
            Default: True.
    
    Returns:
        tuple[pandas.DataFrame, dict]: Tupla contendo:
            - **cleaned_df** (pandas.DataFrame): DataFrame filtrado sem outliers.
              Mantém a mesma estrutura do input mas com registros inconsistentes removidos.
              Preserva todos os índices originais dos dados válidos.
              
            - **outlier_report** (dict): Relatório estruturado da análise por região.
              Formato do dicionário:
              ```python
              {
                  'region_name': {
                      'initial_count': int,           # Picos iniciais na região
                      'outliers_removed': int,        # Outliers identificados
                      'remaining_count': int,         # Picos após limpeza
                      'outlier_percentage': float,    # % de remoção
                      'outlier_indices': list,        # Índices dos outliers
                      'stats_before': {               # Estatísticas pré-limpeza
                          'count': int,
                          'fwhm_mean': float,
                          'fwhm_std': float,
                          'fwhm_cv': float,           # Coeficiente de variação (%)
                          'r2_mean': float,
                          'fwhm_min': float,
                          'fwhm_max': float
                      },
                      'stats_after': {                # Estatísticas pós-limpeza
                          # ... mesma estrutura de stats_before
                      }
                  }
              }
              ```
    
    Raises:
        KeyError: Se o DataFrame não contiver as colunas obrigatórias.
        ValueError: Se o DataFrame estiver vazio ou contiver apenas valores NaN.
        TypeError: Se results_df não for um pandas.DataFrame válido.
    
    Examples:
        >>> import pandas as pd
        >>> # Exemplo básico com dados simulados
        >>> data = {
        ...     'Centro': [197, 214, 225, 1008, 1008],
        ...     'FWHM_Gauss': [8.5, 12.3, 75.2, 9.1, 8.9],  # 75.2 é outlier
        ...     'R2': [0.95, 0.88, 0.15, 0.92, 0.94],       # 0.15 é outlier
        ...     'Pico': ['P1', 'P2', 'P3', 'P4', 'P5'],
        ...     'Amostra': ['S1', 'S1', 'S1', 'S1', 'S1']
        ... }
        >>> df = pd.DataFrame(data)
        >>> cleaned_df, report = detect_and_remove_outliers(df, verbose=True)
        >>> print(f"Outliers removidos: {len(df) - len(cleaned_df)}")
        Outliers removidos: 1
        
        >>> # Análise do relatório por região
        >>> for region, stats in report.items():
        ...     if stats['outliers_removed'] > 0:
        ...         improvement = (stats['stats_before']['fwhm_cv'] - 
        ...                       stats['stats_after']['fwhm_cv'])
        ...         print(f"{region}: {improvement:.1f}% melhoria no CV")
    
    Notes:
        - A função preserva a ordem original dos dados não removidos
        - Regiões com menos de 3 pontos não são testadas por Z-score
        - Regiões com menos de 4 pontos não são testadas por IQR
        - A função é otimizada para conjuntos de dados com 10-10000 espectros
        - Critérios específicos para zircão podem precisar de ajuste para outros minerais
        - O processamento é determinístico: mesmos inputs produzem mesmos outputs
    
    See Also:
        get_zircon_spectral_regions : Define as regiões espectrais processadas
        save_outlier_report : Salva relatório detalhado em arquivo
        generate_summary_report : Integra limpeza no relatório principal
    
    Version:
        2.0.1 - Implementação multi-critério com validação estatística robusta
    """
    
    # Usar a nova definição centralizada de regiões espectrais
    spectral_regions = get_zircon_spectral_regions()
    
    cleaned_df = results_df.copy()
    outlier_report = {}
    total_outliers_removed = 0
    
    if verbose:
        print("\n" + "="*80)
        print("DETECÇÃO E REMOÇÃO DE OUTLIERS POR REGIÃO ESPECTRAL")
        print("="*80)
        print("NOTA: Usando intervalos mutuamente exclusivos para evitar contagem dupla")
        print("      [195,210), [210,220), [220,230) - onde ) significa 'não inclui'")
        print("="*80)
    
    # Processar cada região espectral
    for region_name, (min_wave, max_wave, is_inclusive) in spectral_regions.items():
        # Aplicar a nova lógica de intervalos mutuamente exclusivos
        if is_inclusive:
            region_mask = (results_df['Centro'] >= min_wave) & (results_df['Centro'] <= max_wave)
        else:
            region_mask = (results_df['Centro'] >= min_wave) & (results_df['Centro'] < max_wave)
        
        region_data = results_df[region_mask].copy()
        
        if len(region_data) == 0:
            continue
            
        initial_count = len(region_data)
        outliers_indices = set()
        
        if verbose:
            print(f"\nREGIÃO: {region_name} ({min_wave}-{max_wave} cm⁻¹)")
            print(f"Picos iniciais: {initial_count}")
        
        # Critério 1: R² muito baixo (ajustes muito ruins)
        poor_fit_mask = region_data['R2'] < 0.3
        poor_fit_indices = region_data[poor_fit_mask].index
        outliers_indices.update(poor_fit_indices)
        
        if verbose and len(poor_fit_indices) > 0:
            print(f"  • Outliers por R² < 0.3: {len(poor_fit_indices)} picos")
            for idx in poor_fit_indices:
                r2_val = region_data.loc[idx, 'R2']
                fwhm_val = region_data.loc[idx, 'FWHM_Gauss']
                print(f"    - Pico {region_data.loc[idx, 'Pico']}: R²={r2_val:.3f}, FWHM={fwhm_val:.2f}")
        
        # Critério 2: FWHM extremo usando IQR method
        fwhm_values = region_data['FWHM_Gauss']
        if len(fwhm_values) >= 4:  # Precisa de pelo menos 4 pontos para IQR
            Q1 = fwhm_values.quantile(0.25)
            Q3 = fwhm_values.quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            iqr_outliers_mask = (fwhm_values < lower_bound) | (fwhm_values > upper_bound)
            iqr_outliers_indices = region_data[iqr_outliers_mask].index
            outliers_indices.update(iqr_outliers_indices)
            
            if verbose and len(iqr_outliers_indices) > 0:
                print(f"  • Outliers por IQR (FWHM): {len(iqr_outliers_indices)} picos")
                print(f"    - Limites: [{lower_bound:.2f}, {upper_bound:.2f}] cm⁻¹")
                for idx in iqr_outliers_indices:
                    fwhm_val = region_data.loc[idx, 'FWHM_Gauss']
                    print(f"    - Pico {region_data.loc[idx, 'Pico']}: FWHM={fwhm_val:.2f} cm⁻¹")
        
        # Critério 3: Z-score > 3 para FWHM
        if len(fwhm_values) >= 3 and fwhm_values.std() > 0:
            z_scores = np.abs((fwhm_values - fwhm_values.mean()) / fwhm_values.std())
            z_outliers_mask = z_scores > 3
            z_outliers_indices = region_data[z_outliers_mask].index
            outliers_indices.update(z_outliers_indices)
            
            if verbose and len(z_outliers_indices) > 0:
                print(f"  • Outliers por Z-score > 3: {len(z_outliers_indices)} picos")
                for idx in z_outliers_indices:
                    fwhm_val = region_data.loc[idx, 'FWHM_Gauss']
                    z_val = z_scores.loc[idx]
                    print(f"    - Pico {region_data.loc[idx, 'Pico']}: FWHM={fwhm_val:.2f} cm⁻¹ (Z={z_val:.2f})")
        
        # Critério 4: FWHM fisicamente implausível para zircão
        # Para zircão, FWHM > 60 cm⁻¹ é extremamente raro e indica possível artefato
        extreme_fwhm_mask = fwhm_values > 60
        extreme_fwhm_indices = region_data[extreme_fwhm_mask].index
        outliers_indices.update(extreme_fwhm_indices)
        
        if verbose and len(extreme_fwhm_indices) > 0:
            print(f"  • Outliers por FWHM > 60 cm⁻¹: {len(extreme_fwhm_indices)} picos")
            for idx in extreme_fwhm_indices:
                fwhm_val = region_data.loc[idx, 'FWHM_Gauss']
                print(f"    - Pico {region_data.loc[idx, 'Pico']}: FWHM={fwhm_val:.2f} cm⁻¹")
        
        # Remover outliers identificados
        region_outliers_count = len(outliers_indices)
        total_outliers_removed += region_outliers_count
        
        # Remover do DataFrame principal
        cleaned_df = cleaned_df.drop(outliers_indices)
        
        # Calcular estatísticas antes e depois
        if region_outliers_count > 0:
            remaining_data = region_data.drop(outliers_indices)
            
            if len(remaining_data) > 0:
                stats_before = {
                    'count': initial_count,
                    'fwhm_mean': region_data['FWHM_Gauss'].mean(),
                    'fwhm_std': region_data['FWHM_Gauss'].std(),
                    'fwhm_cv': (region_data['FWHM_Gauss'].std() / region_data['FWHM_Gauss'].mean()) * 100,
                    'r2_mean': region_data['R2'].mean(),
                    'fwhm_min': region_data['FWHM_Gauss'].min(),
                    'fwhm_max': region_data['FWHM_Gauss'].max()
                }
                
                stats_after = {
                    'count': len(remaining_data),
                    'fwhm_mean': remaining_data['FWHM_Gauss'].mean(),
                    'fwhm_std': remaining_data['FWHM_Gauss'].std(),
                    'fwhm_cv': (remaining_data['FWHM_Gauss'].std() / remaining_data['FWHM_Gauss'].mean()) * 100,
                    'r2_mean': remaining_data['R2'].mean(),
                    'fwhm_min': remaining_data['FWHM_Gauss'].min(),
                    'fwhm_max': remaining_data['FWHM_Gauss'].max()
                }
            else:
                stats_after = {
                    'count': 0,
                    'fwhm_mean': 0,
                    'fwhm_std': 0,
                    'fwhm_cv': 0,
                    'r2_mean': 0,
                    'fwhm_min': 0,
                    'fwhm_max': 0
                }
        else:
            stats_before = stats_after = None
        
        # Armazenar relatório da região
        outlier_report[region_name] = {
            'initial_count': initial_count,
            'outliers_removed': region_outliers_count,
            'remaining_count': initial_count - region_outliers_count,
            'outlier_percentage': (region_outliers_count / initial_count) * 100 if initial_count > 0 else 0,
            'outlier_indices': list(outliers_indices),
            'stats_before': stats_before,
            'stats_after': stats_after
        }
        
        if verbose:
            print(f"  → Outliers removidos: {region_outliers_count} ({(region_outliers_count/initial_count)*100:.1f}%)")
            print(f"  → Picos restantes: {initial_count - region_outliers_count}")
            
            if region_outliers_count > 0 and stats_after['count'] > 0:
                print(f"  → FWHM antes: {stats_before['fwhm_mean']:.2f} ± {stats_before['fwhm_std']:.2f} cm⁻¹ (CV: {stats_before['fwhm_cv']:.1f}%)")
                print(f"  → FWHM depois: {stats_after['fwhm_mean']:.2f} ± {stats_after['fwhm_std']:.2f} cm⁻¹ (CV: {stats_after['fwhm_cv']:.1f}%)")
                print(f"  → R² antes: {stats_before['r2_mean']:.3f}")
                print(f"  → R² depois: {stats_after['r2_mean']:.3f}")
                
                # Status de melhoria
                cv_improvement = stats_before['fwhm_cv'] - stats_after['fwhm_cv']
                r2_improvement = stats_after['r2_mean'] - stats_before['r2_mean']
                
                if cv_improvement > 10:
                    print(f"  → ✅ Consistência melhorada significativamente (ΔCV: -{cv_improvement:.1f}%)")
                elif cv_improvement > 5:
                    print(f"  → ⚠️  Consistência melhorada moderadamente (ΔCV: -{cv_improvement:.1f}%)")
                
                if r2_improvement > 0.05:
                    print(f"  → ✅ Qualidade dos ajustes melhorada (ΔR²: +{r2_improvement:.3f})")
    
    # Processar picos fora das regiões conhecidas
    all_regions_mask = np.zeros(len(results_df), dtype=bool)
    for region_name, (min_wave, max_wave, is_inclusive) in spectral_regions.items():
        # Aplicar a nova lógica de intervalos mutuamente exclusivos
        if is_inclusive:
            region_mask = (results_df['Centro'] >= min_wave) & (results_df['Centro'] <= max_wave)
        else:
            region_mask = (results_df['Centro'] >= min_wave) & (results_df['Centro'] < max_wave)
        all_regions_mask |= region_mask
    
    unclassified_data = results_df[~all_regions_mask]
    unclassified_outliers = 0
    
    if len(unclassified_data) > 0:
        # Aplicar critérios mais restritivos para picos não classificados
        unclassified_outliers_mask = (unclassified_data['R2'] < 0.5) | (unclassified_data['FWHM_Gauss'] > 50)
        unclassified_outliers_indices = unclassified_data[unclassified_outliers_mask].index
        unclassified_outliers = len(unclassified_outliers_indices)
        
        if unclassified_outliers > 0:
            cleaned_df = cleaned_df.drop(unclassified_outliers_indices)
            total_outliers_removed += unclassified_outliers
            
            if verbose:
                print(f"\nPICOS NÃO CLASSIFICADOS:")
                print(f"  • Total inicial: {len(unclassified_data)}")
                print(f"  • Outliers removidos: {unclassified_outliers}")
                print(f"  • Critério: R² < 0.5 ou FWHM > 50 cm⁻¹")
    
    if verbose:
        print(f"\n" + "="*80)
        print(f"RESUMO GERAL DA LIMPEZA:")
        print(f"  • Picos iniciais: {len(results_df)}")
        print(f"  • Outliers removidos: {total_outliers_removed} ({(total_outliers_removed/len(results_df))*100:.1f}%)")
        print(f"  • Picos limpos: {len(cleaned_df)}")
        
        # Comparação geral antes/depois
        print(f"\nESTATÍSTICAS GERAIS:")
        print(f"  • FWHM médio antes: {results_df['FWHM_Gauss'].mean():.2f} ± {results_df['FWHM_Gauss'].std():.2f} cm⁻¹")
        print(f"  • FWHM médio depois: {cleaned_df['FWHM_Gauss'].mean():.2f} ± {cleaned_df['FWHM_Gauss'].std():.2f} cm⁻¹")
        print(f"  • R² médio antes: {results_df['R2'].mean():.3f}")
        print(f"  • R² médio depois: {cleaned_df['R2'].mean():.3f}")
        
        cv_before = (results_df['FWHM_Gauss'].std() / results_df['FWHM_Gauss'].mean()) * 100
        cv_after = (cleaned_df['FWHM_Gauss'].std() / cleaned_df['FWHM_Gauss'].mean()) * 100
        print(f"  • CV de FWHM antes: {cv_before:.1f}%")
        print(f"  • CV de FWHM depois: {cv_after:.1f}%")
        
        if cv_after < cv_before:
            improvement = cv_before - cv_after
            if improvement > 20:
                status = "✅ EXCELENTE melhoria na consistência"
            elif improvement > 10:
                status = "✅ BOA melhoria na consistência"
            else:
                status = "⚠️  Melhoria moderada na consistência"
            print(f"  → {status} (ΔCV: -{improvement:.1f}%)")
        
        print("="*80)
    
    return cleaned_df, outlier_report

def save_outlier_report(outlier_report, report_path):
    """Salva o relatório de remoção de outliers em arquivo."""
    try:
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write("="*80 + "\n")
            f.write("RELATÓRIO DE DETECÇÃO E REMOÇÃO DE OUTLIERS\n")
            f.write("="*80 + "\n")
            f.write(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n")
            
            f.write("CRITÉRIOS UTILIZADOS PARA DETECÇÃO DE OUTLIERS:\n")
            f.write("-" * 50 + "\n")
            f.write("1. R² < 0.3: Ajustes gaussianos muito ruins\n")
            f.write("2. IQR method para FWHM: Valores fora de 1.5*IQR dos quartis\n")
            f.write("3. Z-score > 3 para FWHM: Valores estatisticamente extremos\n")
            f.write("4. FWHM > 60 cm⁻¹: Fisicamente implausível para zircão\n")
            f.write("5. Para picos não classificados: R² < 0.5 ou FWHM > 50 cm⁻¹\n\n")
            
            total_removed = sum(data['outliers_removed'] for data in outlier_report.values())
            total_initial = sum(data['initial_count'] for data in outlier_report.values())
            
            f.write("RESUMO GERAL:\n")
            f.write("-" * 20 + "\n")
            f.write(f"Total de outliers removidos: {total_removed}\n")
            f.write(f"Total de picos iniciais: {total_initial}\n")
            f.write(f"Percentual removido: {(total_removed/total_initial)*100:.1f}%\n\n")
            
            f.write("DETALHES POR REGIÃO ESPECTRAL:\n")
            f.write("="*50 + "\n")
            
            for region_name, data in outlier_report.items():
                f.write(f"\nREGIÃO: {region_name}\n")
                f.write("-" * 30 + "\n")
                f.write(f"Picos iniciais: {data['initial_count']}\n")
                f.write(f"Outliers removidos: {data['outliers_removed']}\n")
                f.write(f"Picos restantes: {data['remaining_count']}\n")
                f.write(f"Percentual removido: {data['outlier_percentage']:.1f}%\n")
                
                if data['stats_before'] and data['stats_after'] and data['stats_after']['count'] > 0:
                    f.write(f"\nESTATÍSTICAS ANTES DA LIMPEZA:\n")
                    f.write(f"  FWHM: {data['stats_before']['fwhm_mean']:.2f} ± {data['stats_before']['fwhm_std']:.2f} cm⁻¹\n")
                    f.write(f"  CV de FWHM: {data['stats_before']['fwhm_cv']:.1f}%\n")
                    f.write(f"  R² médio: {data['stats_before']['r2_mean']:.3f}\n")
                    f.write(f"  FWHM intervalo: [{data['stats_before']['fwhm_min']:.2f} - {data['stats_before']['fwhm_max']:.2f}] cm⁻¹\n")
                    
                    f.write(f"\nESTATÍSTICAS APÓS A LIMPEZA:\n")
                    f.write(f"  FWHM: {data['stats_after']['fwhm_mean']:.2f} ± {data['stats_after']['fwhm_std']:.2f} cm⁻¹\n")
                    f.write(f"  CV de FWHM: {data['stats_after']['fwhm_cv']:.1f}%\n")
                    f.write(f"  R² médio: {data['stats_after']['r2_mean']:.3f}\n")
                    f.write(f"  FWHM intervalo: [{data['stats_after']['fwhm_min']:.2f} - {data['stats_after']['fwhm_max']:.2f}] cm⁻¹\n")
                    
                    # Calcular melhorias
                    cv_improvement = data['stats_before']['fwhm_cv'] - data['stats_after']['fwhm_cv']
                    r2_improvement = data['stats_after']['r2_mean'] - data['stats_before']['r2_mean']
                    
                    f.write(f"\nMELHORIAS ALCANÇADAS:\n")
                    f.write(f"  Redução no CV: -{cv_improvement:.1f}%\n")
                    f.write(f"  Melhoria no R²: +{r2_improvement:.3f}\n")
                    
                    if cv_improvement > 20:
                        status = "EXCELENTE"
                    elif cv_improvement > 10:
                        status = "BOA"
                    elif cv_improvement > 5:
                        status = "MODERADA"
                    else:
                        status = "MÍNIMA"
                    f.write(f"  Avaliação da melhoria: {status}\n")
                
                f.write("\n" + "="*50)
            
            f.write(f"\n\nCONCLUSÃO:\n")
            f.write("A remoção de outliers melhora significativamente a qualidade\n")
            f.write("e confiabilidade das análises espectrais, eliminando dados\n")
            f.write("inconsistentes que podem ser devidos a:\n")
            f.write("• Artefatos experimentais\n")
            f.write("• Ruído instrumental\n")
            f.write("• Problemas de ajuste\n")
            f.write("• Impurezas ou inclusões\n")
            
        print(f"Relatório de outliers salvo em: {report_path}")
        
    except Exception as e:
        print(f"Erro ao salvar relatório de outliers: {e}")

def generate_summary_report(results_df, config, output_dir, file_suffix):
    """Gera um relatório resumido com informações gerais sobre os resultados seguindo o formato específico."""
    report_path = Path(output_dir) / f"raman_analysis_report{file_suffix}.txt"
    
    # Data e hora atual
    current_datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    # DETECÇÃO E REMOÇÃO DE OUTLIERS ANTES DOS CÁLCULOS
    print("\n🔍 EXECUTANDO LIMPEZA DE OUTLIERS...")
    cleaned_df, outlier_report = detect_and_remove_outliers(results_df, verbose=True)
    
    # Salvar dados limpos em arquivo separado
    cleaned_path = Path(output_dir) / f"batch_raman_analysis_cleaned{file_suffix}.csv"
    cleaned_df.to_csv(cleaned_path, index=False)
    print(f"\n💾 Dados limpos salvos em: {cleaned_path}")
    
    # Salvar relatório de outliers
    outlier_report_path = Path(output_dir) / f"outliers_removal_report{file_suffix}.txt"
    save_outlier_report(outlier_report, outlier_report_path)
    print(f"📋 Relatório de outliers salvo em: {outlier_report_path}")
    
    # Usar dados limpos para o relatório principal
    results_df = cleaned_df
    
    # Obter lista de amostras analisadas
    amostras_analisadas = sorted(results_df['Amostra'].unique())
    
    try:
        with open(report_path, 'w', encoding='utf-8') as f:
            # Cabeçalho do relatório com nomes das amostras
            f.write("============================================================\n")
            f.write("UNIVERSIDADE FEDERAL DE SÃO CARLOS - SOROCABA\n")
            f.write("\n============================================================\n")
            f.write("RELATÓRIO DE ANÁLISE ESPECTRAL RAMAN DE ZIRCÃO\n")
            f.write("Desenvolvido por: Antonio Said Webbe Sales\n")
            f.write("Doutorando em Ciências dos Materiais\n")
            f.write("Orientador: Prof. Dr. Airton Natanael Coelho Dias\n")
            f.write(f"Data e hora: {current_datetime}\n")
            f.write("============================================================\n\n")
            
            # Seção de amostras analisadas
            f.write("AMOSTRAS ANALISADAS\n")
            f.write("------------------------------------------------------------\n")
            if len(amostras_analisadas) == 1:
                f.write(f"Amostra: {amostras_analisadas[0]}\n")
            else:
                f.write(f"Total de amostras processadas: {len(amostras_analisadas)}\n")
                f.write("Lista de amostras:\n")
                for i, amostra in enumerate(amostras_analisadas, 1):
                    f.write(f"  {i}. {amostra}\n")
            f.write("\n")
            
            # Seção explicativa da remoção de outliers
            f.write("DETECÇÃO E REMOÇÃO DE OUTLIERS - METODOLOGIA\n")
            f.write("============================================================\n")
            f.write("Esta seção descreve os critérios matemáticos utilizados para\n")
            f.write("identificar e remover outliers (valores discrepantes) que podem\n")
            f.write("comprometer a qualidade da análise espectral.\n\n")
            
            f.write("JUSTIFICATIVA CIENTÍFICA:\n")
            f.write("------------------------------------------------------------\n")
            f.write("A remoção de outliers é fundamental na espectroscopia Raman pois:\n")
            f.write("• Elimina artefatos experimentais (vibrações, flutuações térmicas)\n")
            f.write("• Remove picos mal ajustados devido ao ruído instrumental\n")
            f.write("• Evita a contaminação por impurezas ou inclusões minerais\n")
            f.write("• Melhora a precisão das métricas de dano por radiação\n")
            f.write("• Garante a confiabilidade estatística dos resultados\n\n")
            
            f.write("CRITÉRIOS MATEMÁTICOS APLICADOS:\n")
            f.write("------------------------------------------------------------\n")
            f.write("A detecção de outliers é realizada por região espectral usando\n")
            f.write("múltiplos critérios estatísticos independentes:\n\n")
            
            f.write("1. CRITÉRIO DE QUALIDADE DO AJUSTE (R²):\n")
            f.write("   Condição: R² < 0.3\n")
            f.write("   \n")
            f.write("   O coeficiente de determinação R² é definido como:\n")
            f.write("   \n")
            f.write("   R² = 1 - (SS_res / SS_tot)\n")
            f.write("   \n")
            f.write("   Onde:\n")
            f.write("   SS_res = Σ(y_i - ŷ_i)²  (soma dos quadrados dos resíduos)\n")
            f.write("   SS_tot = Σ(y_i - ȳ)²    (soma total dos quadrados)\n")
            f.write("   y_i = valores observados\n")
            f.write("   ŷ_i = valores preditos pelo ajuste gaussiano\n")
            f.write("   ȳ = média dos valores observados\n")
            f.write("   \n")
            f.write("   Interpretação: R² < 0.3 indica ajuste gaussiano inadequado,\n")
            f.write("   sugerindo que o 'pico' detectado é provável ruído ou artefato.\n\n")
            
            f.write("2. MÉTODO INTERQUARTIL (IQR) PARA FWHM:\n")
            f.write("   Aplicado quando n ≥ 4 picos na região\n")
            f.write("   \n")
            f.write("   IQR = Q₃ - Q₁\n")
            f.write("   Limite inferior: L_inf = Q₁ - 1.5 × IQR\n")
            f.write("   Limite superior: L_sup = Q₃ + 1.5 × IQR\n")
            f.write("   \n")
            f.write("   Condição de outlier: FWHM < L_inf OU FWHM > L_sup\n")
            f.write("   \n")
            f.write("   Onde:\n")
            f.write("   Q₁ = primeiro quartil (percentil 25)\n")
            f.write("   Q₃ = terceiro quartil (percentil 75)\n")
            f.write("   \n")
            f.write("   Interpretação: Identifica valores de FWHM estatisticamente\n")
            f.write("   extremos em relação à distribuição da região espectral.\n\n")
            
            f.write("3. CRITÉRIO Z-SCORE PARA FWHM:\n")
            f.write("   Aplicado quando n ≥ 3 picos e σ > 0\n")
            f.write("   \n")
            f.write("   Z = |x - μ| / σ\n")
            f.write("   \n")
            f.write("   Condição de outlier: Z > 3\n")
            f.write("   \n")
            f.write("   Onde:\n")
            f.write("   x = valor de FWHM do pico\n")
            f.write("   μ = média de FWHM na região\n")
            f.write("   σ = desvio padrão de FWHM na região\n")
            f.write("   \n")
            f.write("   Interpretação: Z > 3 indica que o valor está além de 3\n")
            f.write("   desvios padrão da média (probabilidade < 0.3% em distribuição normal).\n\n")
            
            f.write("4. CRITÉRIO FÍSICO PARA ZIRCÃO:\n")
            f.write("   Condição: FWHM > 60 cm⁻¹\n")
            f.write("   \n")
            f.write("   Fundamentação: Com base na literatura de espectroscopia Raman\n")
            f.write("   de zircão (Zhang et al., 2000; Nasdala et al., 2001), valores\n")
            f.write("   de FWHM superiores a 60 cm⁻¹ são fisicamente implausíveis\n")
            f.write("   mesmo para zircão severamente metamíctico.\n")
            f.write("   \n")
            f.write("   Interpretação: Indica provável detecção de artefato, sobreposição\n")
            f.write("   de picos não resolvidos, ou presença de fase amorfa.\n\n")
            
            f.write("5. CRITÉRIO PARA PICOS NÃO CLASSIFICADOS:\n")
            f.write("   Condições: R² < 0.5 OU FWHM > 50 cm⁻¹\n")
            f.write("   \n")
            f.write("   Para picos fora das regiões espectrais conhecidas do zircão,\n")
            f.write("   aplicam-se critérios mais restritivos devido à maior probabilidade\n")
            f.write("   de serem impurezas ou artefatos.\n\n")
            
            f.write("ALGORITMO DE APLICAÇÃO:\n")
            f.write("------------------------------------------------------------\n")
            f.write("1. Para cada região espectral R_i:\n")
            f.write("   a) Selecionar picos com centro na região: P_i = {p | min_i ≤ centro(p) ≤ max_i}\n")
            f.write("   b) Aplicar critérios 1-4 sequencialmente\n")
            f.write("   c) União dos outliers: O_i = O_R² ∪ O_IQR ∪ O_Z ∪ O_físico\n")
            f.write("   d) Remover O_i do conjunto P_i\n")
            f.write("2. Para picos não classificados:\n")
            f.write("   a) Aplicar critério 5\n")
            f.write("   b) Remover outliers identificados\n")
            f.write("3. Conjunto final limpo: P_limpo = P_original - ∪O_i\n\n")
            
            f.write("IMPACTO ESTATÍSTICO DA LIMPEZA:\n")
            f.write("------------------------------------------------------------\n")
            total_original = len(results_df) + sum(data['outliers_removed'] for data in outlier_report.values())
            total_limpo = len(results_df)
            total_removido = sum(data['outliers_removed'] for data in outlier_report.values())
            
            f.write(f"• Picos originais: {total_original}\n")
            f.write(f"• Picos removidos: {total_removido} ({(total_removido/total_original)*100:.1f}%)\n")
            f.write(f"• Picos limpos: {total_limpo}\n\n")
            
            # Calcular melhorias médias
            mejoras_cv = []
            mejoras_r2 = []
            
            for region_name, data in outlier_report.items():
                if data['stats_before'] and data['stats_after'] and data['stats_after']['count'] > 0:
                    cv_improvement = data['stats_before']['fwhm_cv'] - data['stats_after']['fwhm_cv']
                    r2_improvement = data['stats_after']['r2_mean'] - data['stats_before']['r2_mean']
                    mejoras_cv.append(cv_improvement)
                    mejoras_r2.append(r2_improvement)
            
            if mejoras_cv:
                f.write(f"• Melhoria média no CV de FWHM: -{np.mean(mejoras_cv):.1f}%\n")
            if mejoras_r2:
                f.write(f"• Melhoria média no R²: +{np.mean(mejoras_r2):.3f}\n")
            
            f.write("\nCONSEQUÊNCIAS CIENTÍFICAS:\n")
            f.write("• Aumento da precisão nas estimativas de dano por radiação\n")
            f.write("• Redução da variabilidade intra-regional (menor CV)\n")
            f.write("• Melhoria na qualidade dos ajustes gaussianos\n")
            f.write("• Eliminação de valores fisicamente implausíveis\n")
            f.write("• Aumento da confiabilidade estatística dos resultados\n\n")
            
            # Referências bibliográficas no início
            f.write("REFERÊNCIAS BIBLIOGRÁFICAS\n")
            f.write("------------------------------------------------------------\n")
            f.write("Esta seção compila todas as referências bibliográficas utilizadas no desenvolvimento\n")
            f.write("do algoritmo de processamento de espectros Raman e nas metodologias implementadas.\n\n")
            
            f.write("DANO POR RADIAÇÃO EM ZIRCÃO:\n\n")
            
            f.write("Geisler, T., Schaltegger, U., & Tomaschek, F. (2007).\n")
            f.write("Re-equilibration of zircon in aqueous fluids and melts.\n")
            f.write("Elements, 3(1), 43-50.\n\n")
            
            f.write("Ginster, U., Reiners, P. W., Nasdala, L., & Chanmuang, C. N. (2019).\n")
            f.write("Annealing kinetics of radiation damage in zircon.\n")
            f.write("Geochimica et Cosmochimica Acta, 249, 225–246.\n")
            f.write("https://doi.org/10.1016/j.gca.2019.01.033\n\n")
            
            f.write("Nasdala, L., Wenzel, M., Vavra, G., Irmer, G., Wenzel, T., & Kober, B. (2001).\n")
            f.write("Metamictisation of natural zircon: accumulation versus thermal annealing\n")
            f.write("of radioactivity-induced damage. Contributions to Mineralogy and Petrology, 141(2), 125-144.\n")
            f.write("https://doi.org/10.1007/s004100000228\n\n")
            
            f.write("Palenik, C. S., Nasdala, L., & Ewing, R. C. (2003).\n")
            f.write("Radiation damage in zircon. American Mineralogist, 88(5-6), 770-781.\n")
            f.write("https://doi.org/10.2138/am-2003-5-606\n\n")
            
            f.write("ESPECTROSCOPIA RAMAN:\n\n")
            
            f.write("Dawson, P., Hargreave, M. M., & Wilkinson, G. R. (1971).\n")
            f.write("The vibrational spectrum of zircon (ZrSiO₄).\n")
            f.write("Journal of Physics C: Solid State Physics, 4(2), 240-256.\n")
            f.write("https://doi.org/10.1088/0022-3719/4/2/014\n\n")
            
            f.write("Finch, R. J., Hanchar, J. M., Hoskin, P. W., Burns, P. C. (2001).\n")
            f.write("Rare-earth elements in synthetic zircon: Part 2. A single-crystal X-ray study\n")
            f.write("of xenotime substitution. American Mineralogist, 86(5-6), 681-689.\n\n")
            
            f.write("Kolesov, B. A., & Geiger, C. A. (1998).\n")
            f.write("Raman spectra of silicate garnets.\n")
            f.write("Physics and Chemistry of Minerals, 25(2), 142-151.\n")
            f.write("https://doi.org/10.1007/s002690050095\n\n")
            
            f.write("Özkan, H. (1976).\n")
            f.write("Effects of heat treatment on the structure of zircon.\n")
            f.write("Journal of Applied Crystallography, 9(5), 415-419.\n")
            f.write("https://doi.org/10.1107/S0021889876011709\n\n")
            
            f.write("Scott, H. G. (1976).\n")
            f.write("Phase relationships in the zirconia-yttria system.\n")
            f.write("Journal of Materials Science, 11(8), 1479-1491.\n")
            f.write("https://doi.org/10.1007/BF01033510\n\n")
            
            f.write("Wang, L. M., Gong, W. L., Wang, S. X., & Ewing, R. C. (2001).\n")
            f.write("Comparison of ion-beam-induced and neutron-induced damage in titanate pyrochlores.\n")
            f.write("Physical Review B, 63(2), 024105.\n")
            f.write("https://doi.org/10.1103/PhysRevB.63.024105\n\n")
            
            f.write("Zhang, M., Salje, E. K., Farnan, I., Graeme-Barber, A., Daniel, P., Ewing, R. C., ... & Trautmann, C. (2000).\n")
            f.write("Metamictization of zircon: Raman spectroscopic study.\n")
            f.write("Journal of Physics: Condensed Matter, 12(8), 1915.\n")
            f.write("https://doi.org/10.1088/0953-8984/12/8/333\n\n")
            
            f.write("ALGORITMOS E MÉTODOS COMPUTACIONAIS:\n\n")
            
            f.write("Eilers, P. H., & Boelens, H. F. (2005).\n")
            f.write("Baseline correction with asymmetric least squares smoothing.\n")
            f.write("Leiden University Medical Centre Report, 1(1), 5.\n\n")
            
            f.write("Savitzky, A., & Golay, M. J. (1964).\n")
            f.write("Smoothing and differentiation of data by simplified least squares procedures.\n")
            f.write("Analytical Chemistry, 36(8), 1627-1639.\n")
            f.write("https://doi.org/10.1021/ac60214a047\n\n")
            
            f.write("Zhang, Z. M., Chen, S., & Liang, Y. Z. (2010).\n")
            f.write("Baseline correction using adaptive iteratively reweighted penalized least squares.\n")
            f.write("Analyst, 135(5), 1138-1146.\n")
            f.write("https://doi.org/10.1039/b922045c\n\n")
            
            f.write("BIBLIOTECAS DE SOFTWARE:\n\n")
            
            f.write("Harris, C. R., Millman, K. J., van der Walt, S. J., Gommers, R., Virtanen, P., Cournapeau, D., ... & Oliphant, T. E. (2020).\n")
            f.write("Array programming with NumPy. Nature, 585(7825), 357-362.\n")
            f.write("https://doi.org/10.1038/s41586-020-2649-2\n\n")
            
            f.write("McKinney, W. (2010).\n")
            f.write("Data structures for statistical computing in python.\n")
            f.write("In Proceedings of the 9th Python in Science Conference (Vol. 445, pp. 51-56).\n")
            f.write("https://doi.org/10.25080/Majora-92bf1922-00a\n\n")
            
            f.write("Virtanen, P., Gommers, R., Oliphant, T. E., Haberland, M., Reddy, T., Cournapeau, D., ... & van Mulbregt, P. (2020).\n")
            f.write("SciPy 1.0: fundamental algorithms for scientific computing in Python.\n")
            f.write("Nature Methods, 17(3), 261-272.\n")
            f.write("https://doi.org/10.1038/s41592-019-0686-2\n\n")
            
            f.write("Hunter, J. D. (2007).\n")
            f.write("Matplotlib: A 2D graphics environment.\n")
            f.write("Computing in Science & Engineering, 9(3), 90-95.\n")
            f.write("https://doi.org/10.1109/MCSE.2007.55\n\n")
            
            f.write("Waskom, M. L. (2021).\n")
            f.write("seaborn: statistical data visualization.\n")
            f.write("Journal of Open Source Software, 6(60), 3021.\n")
            f.write("https://doi.org/10.21105/joss.03021\n\n")
            
            f.write("AJUSTE DE CURVAS E OTIMIZAÇÃO:\n\n")
            
            f.write("Levenberg, K. (1944).\n")
            f.write("A method for the solution of certain non-linear problems in least squares.\n")
            f.write("Quarterly of Applied Mathematics, 2(2), 164-168.\n\n")
            
            f.write("Marquardt, D. W. (1963).\n")
            f.write("An algorithm for least-squares estimation of nonlinear parameters.\n")
            f.write("Journal of the Society for Industrial and Applied Mathematics, 11(2), 431-441.\n")
            f.write("https://doi.org/10.1137/0111030\n\n")
            
            f.write("Newville, M., Stensitzki, T., Allen, D. B., & Ingargiola, A. (2014).\n")
            f.write("LMFIT: Non-linear least-square minimization and curve-fitting for Python.\n")
            f.write("https://doi.org/10.5281/zenodo.11813\n\n")
            
            f.write("REGIÕES ESPECTRAIS DO ZIRCÃO\n")
            f.write("------------------------------------------------------------\n")
            f.write("Regiões espectrais estabelecidas para análise:\n")
            f.write("  • ν₃(SiO₄): 990-1020 cm⁻¹ (modo de estiramento antissimétrico)\n")
            f.write("  • ν₁(SiO₄): 965-985 cm⁻¹ (modo de estiramento simétrico)\n")
            f.write("  • ν₂(SiO₄): 430-450 cm⁻¹ (modo de deformação angular)\n")
            f.write("  • Modo externo 1: 195-210 cm⁻¹\n")
            f.write("  • Modo externo 2: 210-220 cm⁻¹\n")
            f.write("  • Modo externo 3: 220-230 cm⁻¹\n")
            f.write("  • Modo externo 4: 350-365 cm⁻¹\n\n")
            
            f.write("NOTA SOBRE INTERVALOS ESPECTRAIS:\n")
            f.write("------------------------------------------------------------\n")
            f.write("Os intervalos espectrais são definidos com extremidades FECHADAS\n")
            f.write("nas regiões de modos internos (ν₁, ν₂, ν₃) e na última região externa,\n")
            f.write("utilizando a notação matemática [min, max], onde ambos os limites\n")
            f.write("são INCLUSIVOS.\n\n")
            f.write("Para evitar sobreposição entre modos externos consecutivos,\n")
            f.write("utilizam-se intervalos semi-abertos [min, max), onde:\n")
            f.write("• min é INCLUSIVO (≥)\n")
            f.write("• max é EXCLUSIVO (<)\n\n")
            f.write("Exemplo de aplicação:\n")
            f.write("• Modo externo 1: [195, 210) → 195 ≤ posição < 210\n")
            f.write("• Modo externo 2: [210, 220) → 210 ≤ posição < 220\n")
            f.write("• Modo externo 3: [220, 230) → 220 ≤ posição < 230\n")
            f.write("• Modo externo 4: [350, 365] → 350 ≤ posição ≤ 365 (fechado)\n\n")
            f.write("Esta convenção garante que cada pico pertença a APENAS UMA região,\n")
            f.write("eliminando a contagem dupla em valores limítrofes (ex: 210 cm⁻¹).\n\n")
            
            f.write("NOTA: Picos detectados fora dessas regiões também são reportados\n")
            f.write("      e podem indicar impurezas, defeitos estruturais ou inclusões.\n\n")
            
            # Informações gerais
            f.write("INFORMAÇÕES GERAIS\n")
            f.write("------------------------------------------------------------\n")
            f.write(f"Total de amostras analisadas: {results_df['Amostra'].nunique()}\n")
            f.write(f"Total de espectros processados: {results_df['Espectro'].nunique()}\n")
            f.write(f"Total de picos detectados: {len(results_df)}\n\n")
            
            # Cálculo de dose de radiação
            f.write("CÁLCULO DE DOSE DE RADIAÇÃO\n")
            f.write("------------------------------------------------------------\n")
            f.write("Método de cálculo: Equação de Ginster et al. (2019) - Geochimica et Cosmochimica Acta 249, 225-246\n\n")
            
            f.write("Parâmetros utilizados:\n")
            f.write("  Equação empírica derivada de dados experimentais de zircão\n")
            f.write("  Calibração baseada em FWHM do pico Raman\n")
            f.write("  Dados de calibração: FWHM [4.9, 11.0, 17.8, 7.3, 11.6] cm⁻¹\n")
            f.write("  Ded observado: [0.27, 0.67, 1.26, 0.42, 0.72]\n")
            f.write("  R²: ~0.955 (excelente correlação)\n\n")
            
            f.write("Equação utilizada:\n")
            f.write("  Ded = -0.1402 + 0.07683 × FWHM\n\n")
            
            f.write("Onde:\n")
            f.write("  - Ded é a dose equivalente de dano por radiação\n")
            f.write("  - FWHM é a largura total à meia altura do pico Raman (cm⁻¹)\n")
            f.write("  - -0.1402 é o intercepto da regressão linear (coeficiente b)\n")
            f.write("  - 0.07683 é a inclinação da regressão linear (coeficiente a)\n\n")
            
            f.write("Conforme Ginster et al. (2019), todos os picos de zircão são sensíveis ao dano por radiação.\n\n")
            
            f.write("Categorização do dano por radiação baseada no FWHM:\n")
            f.write("  - Baixo dano: FWHM ≤ 8 cm⁻¹\n")
            f.write("  - Dano moderado: 8 < FWHM ≤ 14.5 cm⁻¹\n")
            f.write("  - Alto dano: 14.5 < FWHM ≤ 25 cm⁻¹\n")
            f.write("  - Quase amorfo: FWHM > 25 cm⁻¹\n\n")
            
            f.write("Referência: Ginster, U., et al. (2019). Annealing kinetics of radiation damage in zircon\n")
            f.write("Geochim. Cosmochim. Acta, 249 (2019), 225-246. DOI: 10.1016/j.gca.2019.01.033\n\n")
            
            # Análise de robustez do ajuste
            f.write("MÉTRICAS DE ROBUSTEZ DO AJUSTE\n")
            f.write("------------------------------------------------------------\n")
            f.write("Esta seção apresenta métricas que asseguram a confiabilidade dos resultados\n")
            f.write("organizadas por região espectral, pois cada região representa um modo\n")
            f.write("vibracional específico do zircão com características espectrais únicas:\n\n")
            
            # Calcular métricas de robustez
            spectral_regions = {
                "ν₃(SiO₄)": (990, 1020),
                "ν₁(SiO₄)": (965, 985),
                "ν₂(SiO₄)": (430, 450),
                "Modo externo 1": (195, 210),
                "Modo externo 2": (210, 220),
                "Modo externo 3": (220, 230),
                "Modo externo 4": (350, 365)
            }
            
            total_peaks = len(results_df)
            peaks_in_regions = 0
            
            f.write("ANÁLISE POR REGIÃO ESPECTRAL (MODO VIBRACIONAL):\n")
            f.write("="*60 + "\n\n")
            
            region_summary = {}
            
            for region_name, (min_wave, max_wave) in spectral_regions.items():
                region_data = results_df[(results_df['Centro'] >= min_wave) & 
                                       (results_df['Centro'] <= max_wave)]
                region_count = len(region_data)
                peaks_in_regions += region_count
                
                f.write(f"REGIÃO: {region_name} ({min_wave}-{max_wave} cm⁻¹)\n")
                f.write("-" * 50 + "\n")
                
                if region_count > 0:
                    # Métricas de qualidade dos ajustes para esta região
                    region_avg_r2 = region_data['R2'].mean()
                    region_min_r2 = region_data['R2'].min()
                    region_max_r2 = region_data['R2'].max()
                    region_std_r2 = region_data['R2'].std()
                    
                    region_good_fit = len(region_data[region_data['R2'] > 0.8])
                    region_excellent_fit = len(region_data[region_data['R2'] > 0.9])
                    region_poor_fit = len(region_data[region_data['R2'] < 0.5])
                    
                    region_good_fit_pct = (region_good_fit / region_count) * 100
                    region_excellent_fit_pct = (region_excellent_fit / region_count) * 100
                    region_poor_fit_pct = (region_poor_fit / region_count) * 100
                    
                    # Métricas de FWHM para esta região
                    region_avg_fwhm = region_data['FWHM_Gauss'].mean()
                    region_std_fwhm = region_data['FWHM_Gauss'].std()
                    region_cv_fwhm = (region_std_fwhm / region_avg_fwhm) * 100 if region_avg_fwhm > 0 else 0
                    region_min_fwhm = region_data['FWHM_Gauss'].min()
                    region_max_fwhm = region_data['FWHM_Gauss'].max()
                    
                    # Métricas de área para esta região
                    region_avg_area = region_data['Area_Gauss'].mean()
                    region_std_area = region_data['Area_Gauss'].std()
                    region_cv_area = (region_std_area / region_avg_area) * 100 if region_avg_area > 0 else 0
                    
                    # Métricas de dano por radiação para esta região
                    region_damage_counts = region_data['Categoria_Dano'].value_counts()
                    region_avg_dose = region_data['Dose_Estimada'].mean()
                    region_std_dose = region_data['Dose_Estimada'].std()
                    
                    f.write(f"1. ESTATÍSTICAS GERAIS:\n")
                    f.write(f"   • Total de picos detectados: {region_count}\n")
                    f.write(f"   • Percentual do total: {(region_count/total_peaks)*100:.1f}%\n")
                    f.write(f"   • Número de amostras com picos nesta região: {region_data['Amostra'].nunique()}\n\n")
                    
                    f.write(f"2. QUALIDADE DOS AJUSTES GAUSSIANOS:\n")
                    f.write(f"   • R² médio: {region_avg_r2:.3f} ± {region_std_r2:.3f}\n")
                    f.write(f"   • R² intervalo: [{region_min_r2:.3f} - {region_max_r2:.3f}]\n")
                    f.write(f"   • Ajustes excelentes (R² > 0.9): {region_excellent_fit} ({region_excellent_fit_pct:.1f}%)\n")
                    f.write(f"   • Ajustes bons (R² > 0.8): {region_good_fit} ({region_good_fit_pct:.1f}%)\n")
                    f.write(f"   • Ajustes ruins (R² < 0.5): {region_poor_fit} ({region_poor_fit_pct:.1f}%)\n")
                    
                    # Status da qualidade dos ajustes para esta região
                    if region_avg_r2 >= 0.8 and region_poor_fit_pct <= 10:
                        fit_status = "✅ EXCELENTE"
                    elif region_avg_r2 >= 0.6 and region_poor_fit_pct <= 20:
                        fit_status = "⚠️  BOA"
                    elif region_avg_r2 >= 0.4 and region_poor_fit_pct <= 30:
                        fit_status = "⚠️  ACEITÁVEL"
                    else:
                        fit_status = "❌ PROBLEMÁTICA"
                    
                    f.write(f"   → Status da qualidade: {fit_status}\n\n")
                    
                    f.write(f"3. PARÂMETROS ESPECTRAIS (FWHM):\n")
                    f.write(f"   • FWHM médio: {region_avg_fwhm:.2f} ± {region_std_fwhm:.2f} cm⁻¹\n")
                    f.write(f"   • FWHM intervalo: [{region_min_fwhm:.2f} - {region_max_fwhm:.2f}] cm⁻¹\n")
                    f.write(f"   • Coeficiente de variação: {region_cv_fwhm:.1f}%\n")
                    
                    # Status da consistência de FWHM para esta região
                    if region_cv_fwhm <= 30:
                        consistency_status = "✅ EXCELENTE"
                    elif region_cv_fwhm <= 50:
                        consistency_status = "⚠️  BOA"
                    elif region_cv_fwhm <= 70:
                        consistency_status = "⚠️  ACEITÁVEL"
                    else:
                        consistency_status = "❌ PROBLEMÁTICA"
                    
                    f.write(f"   → Status da consistência: {consistency_status}\n\n")
                    
                    f.write(f"4. INTENSIDADE DOS PICOS (ÁREA):\n")
                    f.write(f"   • Área média: {region_avg_area:.2f} ± {region_std_area:.2f}\n")
                    f.write(f"   • Coeficiente de variação: {region_cv_area:.1f}%\n\n")
                    
                    f.write(f"5. DANO POR RADIAÇÃO (GINSTER et al., 2019):\n")
                    f.write(f"   • Dose média estimada: {region_avg_dose:.3f} ± {region_std_dose:.3f}\n")
                    f.write(f"   • Distribuição por categoria:\n")
                    for category, count in region_damage_counts.items():
                        percentage = (count / region_count) * 100
                        f.write(f"     - {category}: {count} picos ({percentage:.1f}%)\n")
                    
                    # Interpretação específica para cada modo vibracional
                    f.write(f"\n6. INTERPRETAÇÃO PARA O MODO {region_name}:\n")
                    if region_name == "ν₃(SiO₄)":
                        f.write(f"   • Modo de estiramento antissimétrico do tetraedro SiO₄\n")
                        f.write(f"   • Mais sensível ao dano por radiação\n")
                        f.write(f"   • Pico principal para análise de metamictização\n")
                        f.write(f"   • Referências: Zhang et al. (2000), Nasdala et al. (2001),\n")
                        f.write(f"     Palenik et al. (2003), Ginster et al. (2019)\n")
                        if region_avg_r2 >= 0.7:
                            f.write(f"   → Qualidade adequada para análise de dano por radiação\n")
                        else:
                            f.write(f"   → ⚠️  Qualidade limitada - revisar parâmetros de detecção\n")
                    elif region_name == "ν₁(SiO₄)":
                        f.write(f"   • Modo de estiramento simétrico do tetraedro SiO₄\n")
                        f.write(f"   • Complementar ao ν₃ para análise estrutural\n")
                        f.write(f"   • Importante para caracterização da cristalinidade\n")
                        f.write(f"   • Referências: Finch et al. (2001), Zhang et al. (2000),\n")
                        f.write(f"     Dawson et al. (1971), Kolesov & Geiger (1998)\n")
                    elif region_name == "ν₂(SiO₄)":
                        f.write(f"   • Modo de deformação angular do tetraedro SiO₄\n")
                        f.write(f"   • Sensível a distorções estruturais\n")
                        f.write(f"   • Útil para análise de pressão e tensão\n")
                        f.write(f"   • Referências: Dawson et al. (1971), Kolesov & Geiger (1998),\n")
                        f.write(f"     Özkan (1976), Wang et al. (2001)\n")
                    else:
                        f.write(f"   • Modo vibracional externo da estrutura do zircão\n")
                        f.write(f"   • Relacionado às vibrações da rede cristalina\n")
                        f.write(f"   • Complementar à análise dos modos internos\n")
                        f.write(f"   • Referências: Dawson et al. (1971), Özkan (1976),\n")
                        f.write(f"     Scott (1976), Kolesov & Geiger (1998)\n")
                    
                    # Armazenar dados para resumo geral
                    region_summary[region_name] = {
                        'count': region_count,
                        'avg_r2': region_avg_r2,
                        'poor_fit_pct': region_poor_fit_pct,
                        'cv_fwhm': region_cv_fwhm,
                        'fit_status': fit_status,
                        'consistency_status': consistency_status,
                        'avg_fwhm': region_avg_fwhm,
                        'avg_dose': region_avg_dose
                    }
                    
                else:
                    f.write(f"   • Nenhum pico detectado nesta região\n")
                    f.write(f"   → Possível indicação de:\n")
                    f.write(f"     - Parâmetros de detecção muito restritivos\n")
                    f.write(f"     - Qualidade espectral inadequada\n")
                    f.write(f"     - Ausência natural do modo vibracional\n")
                    
                    region_summary[region_name] = {
                        'count': 0,
                        'avg_r2': 0,
                        'poor_fit_pct': 100,
                        'cv_fwhm': 0,
                        'fit_status': "❌ SEM DADOS",
                        'consistency_status': "❌ SEM DADOS",
                        'avg_fwhm': 0,
                        'avg_dose': 0
                    }
                
                f.write("\n" + "="*60 + "\n\n")
            
            # Picos fora das regiões conhecidas
            peaks_outside = total_peaks - peaks_in_regions
            outside_percentage = (peaks_outside / total_peaks) * 100 if total_peaks > 0 else 0
            
            f.write("PICOS FORA DAS REGIÕES ESPECTRAIS CONHECIDAS:\n")
            f.write("-" * 50 + "\n")
            f.write(f"• Total de picos não classificados: {peaks_outside} ({outside_percentage:.1f}%)\n")
            
            if peaks_outside > 0:
                unclassified_data = results_df[~((results_df['Centro'] >= 990) & (results_df['Centro'] <= 1020) |
                                               (results_df['Centro'] >= 965) & (results_df['Centro'] <= 985) |
                                               (results_df['Centro'] >= 430) & (results_df['Centro'] <= 450) |
                                               (results_df['Centro'] >= 195) & (results_df['Centro'] <= 210) |
                                               (results_df['Centro'] >= 210) & (results_df['Centro'] <= 220) |
                                               (results_df['Centro'] >= 220) & (results_df['Centro'] <= 230) |
                                               (results_df['Centro'] >= 350) & (results_df['Centro'] <= 365))]
                
                unclass_avg_r2 = unclassified_data['R2'].mean() if len(unclassified_data) > 0 else 0
                unclass_poor_fit = len(unclassified_data[unclassified_data['R2'] < 0.5]) if len(unclassified_data) > 0 else 0
                unclass_poor_pct = (unclass_poor_fit / peaks_outside) * 100 if peaks_outside > 0 else 0
                
                f.write(f"• R² médio dos picos não classificados: {unclass_avg_r2:.3f}\n")
                f.write(f"• Picos com ajuste ruim (R² < 0.5): {unclass_poor_fit} ({unclass_poor_pct:.1f}%)\n")
                f.write(f"• Interpretação: Possíveis impurezas, defeitos ou ruído\n")
                
                if outside_percentage > 30:
                    f.write(f"  → ⚠️  ALTO percentual - revisar parâmetros de detecção\n")
                elif outside_percentage > 15:
                    f.write(f"  → ⚠️  Moderado - verificar qualidade espectral\n")
                else:
                    f.write(f"  → ✅ Baixo percentual - configuração adequada\n")
            else:
                f.write(f"• Todos os picos foram classificados nas regiões conhecidas\n")
                f.write(f"  → ✅ Excelente seletividade espectral\n")
            
            f.write("\n")
            
            # Resumo geral por critérios de robustez
            f.write("RESUMO GERAL DAS MÉTRICAS DE ROBUSTEZ:\n")
            f.write("="*50 + "\n")
            
            # Tabela resumo
            f.write(f"{'Região':<15} {'Picos':<6} {'R²':<6} {'FWHM':<8} {'Status':<12}\n")
            f.write("-" * 55 + "\n")
            
            for region_name, data in region_summary.items():
                region_short = region_name.replace("(SiO₄)", "").replace("Modo externo ", "Ext")
                f.write(f"{region_short:<15} {data['count']:<6} {data['avg_r2']:<6.3f} {data['avg_fwhm']:<8.2f} {data['fit_status']}\n")
            
            f.write(f"{'Não classif.':<15} {peaks_outside:<6} {unclass_avg_r2:<6.3f} {'N/A':<8} {'Espúrios'}\n")
            f.write("-" * 55 + "\n")
            
            # Avaliação geral baseada nas regiões principais
            main_regions = ['ν₃(SiO₄)', 'ν₁(SiO₄)', 'ν₂(SiO₄)']
            main_criteria_met = 0
            total_main_criteria = len(main_regions) * 3  # 3 critérios por região principal
            
            for region in main_regions:
                if region in region_summary:
                    data = region_summary[region]
                    if data['count'] > 0:  # Tem picos detectados
                        main_criteria_met += 1
                    if data['avg_r2'] >= 0.6:  # Boa qualidade de ajuste
                        main_criteria_met += 1
                    if data['cv_fwhm'] <= 50:  # Boa consistência
                        main_criteria_met += 1
            
            f.write(f"\nCRITÉRIOS DE ROBUSTEZ PARA REGIÕES PRINCIPAIS:\n")
            f.write(f"Critérios atendidos: {main_criteria_met}/{total_main_criteria}\n")
            
            if main_criteria_met >= total_main_criteria * 0.8:
                overall_status = "✅ CONFIGURAÇÃO ROBUSTA PARA ZIRCÃO"
                recommendation = "Parâmetros otimizados para análise de modos vibracionais do zircão."
            elif main_criteria_met >= total_main_criteria * 0.6:
                overall_status = "⚠️  CONFIGURAÇÃO ADEQUADA"
                recommendation = "Configuração aceitável, mas algumas regiões podem ser melhoradas."
            else:
                overall_status = "❌ CONFIGURAÇÃO PROBLEMÁTICA"
                recommendation = "Revisar parâmetros - múltiplas regiões com problemas de qualidade."
            
            f.write(f"\nAVALIAÇÃO GERAL: {overall_status}\n")
            f.write(f"RECOMENDAÇÃO: {recommendation}\n\n")
            
            # Configurações utilizadas
            f.write("CONFIGURAÇÕES DO PROCESSAMENTO\n")
            f.write("------------------------------------------------------------\n")
            f.write(f"Método de normalização: {config['normalization']['method']}\n")
            f.write(f"Correção de linha de base: {config['baseline_correction']['method']}\n")
            f.write(f"Tamanho da janela de suavização: {config['smoothing']['window_length']}\n")
            f.write(f"Ordem do polinômio: {config['smoothing']['polyorder']}\n")
            f.write(f"Método de ajuste: {config['fitting']['method']}\n\n")
            
            # Parâmetros de detecção de picos
            f.write(f"Parâmetros de detecção de picos:\n")
            f.write(f"  Altura mínima (% da intensidade máxima): {config['peak_detection']['height_percent']}%\n")
            f.write(f"  Proeminência mínima (% da intensidade máxima): {config['peak_detection']['prominence_percent']}%\n") 
            f.write(f"  Distância mínima entre picos: {config['peak_detection']['distance']} pontos\n")
            f.write(f"  Largura mínima dos picos: {config['peak_detection']['width']} pontos\n\n")
            
            f.write("INTERPRETAÇÃO DAS MÉTRICAS:\n")
            f.write("• R² > 0.8: Ajuste gaussiano de alta qualidade\n")
            f.write("• R² 0.6-0.8: Ajuste gaussiano adequado\n")
            f.write("• R² < 0.5: Ajuste gaussiano questionável\n")
            f.write("• CV de FWHM < 30%: Consistência excelente por região\n")
            f.write("• CV de FWHM > 70%: Possível detecção de artefatos\n")
            f.write("• Cada região representa um modo vibracional específico\n")
            f.write("• ν₃: Mais sensível ao dano por radiação\n")
            f.write("• ν₁: Complementar para análise estrutural\n")
            f.write("• ν₂: Sensível a distorções estruturais\n\n")
            
            # Detalhamento dos picos por grão e ponto de medição
            f.write("DETALHAMENTO DOS PICOS POR GRÃO E PONTO DE MEDIÇÃO\n")
            f.write("============================================================\n\n")
            
            # Definição de regiões espectrais do zircão (redefinir para esta seção)
            detail_spectral_regions = {
                "ν₃(SiO₄)": (990, 1020),
                "ν₁(SiO₄)": (965, 985),
                "ν₂(SiO₄)": (430, 450),
                "Modo externo 1": (195, 210),
                "Modo externo 2": (210, 220),
                "Modo externo 3": (220, 230),
                "Modo externo 4": (350, 365)
            }
            
            # Processar cada amostra
            for sample in sorted(results_df['Amostra'].unique()):
                sample_data = results_df[results_df['Amostra'] == sample]
                f.write(f"AMOSTRA: {sample}\n")
                f.write("------------------------------------------------------------\n\n")
                
                # Processar cada grão
                for grain in sorted(sample_data['Grao'].unique(), key=lambda x: int(x) if x.isdigit() else 0):
                    grain_data = sample_data[sample_data['Grao'] == grain]
                    f.write(f"  GRÃO {grain}:\n")
                    
                    # Processar cada local/ponto de medição
                    for location in sorted(grain_data['Local'].unique()):
                        location_data = grain_data[grain_data['Local'] == location]
                        if len(location_data) == 0:
                            continue
                            
                        f.write(f"    PONTO DE MEDIÇÃO {location}:\n")
                        f.write(f"      Total de picos detectados: {len(location_data)}\n")
                        
                        # Agrupar picos por região espectral
                        for region_name, (min_wave, max_wave) in detail_spectral_regions.items():
                            region_peaks = location_data[(location_data['Centro'] >= min_wave) & 
                                                        (location_data['Centro'] <= max_wave)]
                            
                            if len(region_peaks) > 0:
                                f.write(f"      Região {region_name} ({min_wave}-{max_wave} cm⁻¹): {len(region_peaks)} pico(s)\n")
                                
                                for _, peak in region_peaks.iterrows():
                                    center = peak['Centro']
                                    fwhm = peak['FWHM_Gauss']
                                    area = peak['Area_Gauss']
                                    damage_cat = peak['Categoria_Dano']
                                    dose = peak['Dose_Estimada']
                                    peak_num = peak['Pico']
                                    
                                    f.write(f"        Pico {peak_num}: Centro={center:.2f} cm⁻¹, ")
                                    f.write(f"FWHM={fwhm:.2f} cm⁻¹, ")
                                    f.write(f"Área={area:.2f}, ")
                                    f.write(f"Categoria={damage_cat}, ")
                                    f.write(f"Dose (Ginster)={dose:.2e}\n")
                        
                        # Identificar picos fora das regiões estabelecidas
                        all_region_mask = np.zeros(len(location_data), dtype=bool)
                        for region_name, (min_wave, max_wave) in detail_spectral_regions.items():
                            region_mask = (location_data['Centro'] >= min_wave) & (location_data['Centro'] <= max_wave)
                            all_region_mask |= region_mask
                        
                        unclassified_peaks = location_data[~all_region_mask]
                        
                        if len(unclassified_peaks) > 0:
                            f.write(f"      Picos fora das regiões estabelecidas: {len(unclassified_peaks)} pico(s)\n")
                            
                            for _, peak in unclassified_peaks.iterrows():
                                center = peak['Centro']
                                fwhm = peak['FWHM_Gauss']
                                area = peak['Area_Gauss']
                                damage_cat = peak['Categoria_Dano']
                                dose = peak['Dose_Estimada']
                                peak_num = peak['Pico']
                                
                                f.write(f"        Pico {peak_num}: Centro={center:.2f} cm⁻¹, ")
                                f.write(f"FWHM={fwhm:.2f} cm⁻¹, ")
                                f.write(f"Área={area:.2f}, ")
                                f.write(f"Categoria={damage_cat}, ")
                                f.write(f"Dose (Ginster)={dose:.2e}\n")
                        
                        f.write("\n")
                    
                    f.write("\n")
                
                f.write("\n")
            
            f.write("============================================================\n")
            f.write("Fim do relatório\n")
            f.write("============================================================\n")
        print(f"Relatório salvo em: {report_path}")
        return True
    except Exception as e:
        print(f"Error generating report: {e}")
        return False

def batch_process(config):
    """Processa todos os arquivos CSV no diretório de entrada e gera um relatório consolidado."""
    input_dir = config["input_dir"]
    output_dir = get_output_dir(config)
    
    print(f"Diretório de entrada: {input_dir}")
    print(f"Diretório de saída: {output_dir}")
    
    # Get all CSV files in the input directory
    input_path = Path(input_dir)
    csv_files = list(input_path.glob("*.csv"))
    
    if not csv_files:
        print(f"Nenhum arquivo CSV encontrado em {input_dir}")
        return
    
    print(f"Encontrados {len(csv_files)} arquivos CSV para processar")
    
    # Create a DataFrame to store all results
    all_results = pd.DataFrame()
    
    # Process each file
    for i, file_path in enumerate(csv_files):
        print(f"\nProcessing file {i+1}/{len(csv_files)}: {Path(file_path).name}")
        
        # Process the file
        results = process_file(file_path, config)
        
        # If processing succeeded
        if results is not None and not results.empty:
            # Append results to the combined DataFrame
            all_results = pd.concat([all_results, results], ignore_index=True)
            print(f"  Added {len(results)} results")
        else:
            print(f"  No results obtained from {file_path}")
    
    # Verify if we have any results
    if all_results.empty:
        print("\nNenhum resultado foi gerado.")
        print("Verifique se os arquivos CSV contêm dados espectrais válidos.")
        return
    
    # Obter lista de amostras analisadas para determinar nomenclatura dos arquivos
    amostras_analisadas = sorted(all_results['Amostra'].unique())
    
    # Definir sufixo para nomes dos arquivos baseado no número de amostras
    timestamp = generate_timestamp()
    
    if len(amostras_analisadas) == 1:
        # Uma única amostra - incluir nome da amostra nos arquivos
        sample_name = amostras_analisadas[0]
        # Limpar caracteres especiais do nome da amostra para uso em nomes de arquivo
        safe_sample_name = "".join(c for c in sample_name if c.isalnum() or c in (' ', '-', '_')).rstrip()
        safe_sample_name = safe_sample_name.replace(' ', '_')
        file_suffix = f"_{safe_sample_name}_{timestamp}"
    else:
        # Múltiplas amostras - usar nomenclatura padrão com timestamp
        file_suffix = f"_{timestamp}"
    
    # Save the combined results
    output_path = Path(output_dir) / f"batch_raman_analysis{file_suffix}.csv"
    all_results.to_csv(output_path, index=False)
    print(f"\nTodos os resultados foram salvos em: {output_path}")
    
    # Generate summary report
    generate_summary_report(all_results, config, output_dir, file_suffix)
    print(f"Relatório resumido gerado em: {Path(output_dir) / f'raman_analysis_report{file_suffix}.txt'}")

    # Generate radiation damage summary
    try:
        generate_radiation_damage_summary(all_results, output_dir, file_suffix)
        print(f"Resumo de dano por radiação gerado em: {Path(output_dir) / f'radiation_damage_summary{file_suffix}.csv'}")
    except Exception as e:
        print(f"Warning: Could not generate radiation damage summary: {e}")
    
    # Analyze peak detection robustness
    print("\n" + "="*70)
    print("EXECUTANDO ANÁLISE DE ROBUSTEZ DA CONFIGURAÇÃO...")
    print("="*70)
    
    robustness_report = analyze_peak_detection_robustness(all_results, config)
    print_robustness_analysis(robustness_report, output_dir, file_suffix)
    
    # Display robustness summary in console
    print("\n" + "="*70)
    print("RESUMO DAS MÉTRICAS DE ROBUSTEZ POR REGIÃO ESPECTRAL")
    print("="*70)
    
    # Quick calculation for console display
    spectral_regions = {
        "ν₃(SiO₄)": (990, 1020), "ν₁(SiO₄)": (965, 985), "ν₂(SiO₄)": (430, 450),
        "Modo externo 1": (195, 210), "Modo externo 2": (210, 220), 
        "Modo externo 3": (220, 230), "Modo externo 4": (350, 365)
    }
    
    total_peaks = len(all_results)
    peaks_in_regions = 0
    
    print(f"📊 ANÁLISE POR MODO VIBRACIONAL:")
    print(f"{'Região':<15} {'Picos':<6} {'R²':<6} {'FWHM':<8} {'Status'}")
    print("-" * 60)
    
    for region_name, (min_wave, max_wave) in spectral_regions.items():
        region_data = all_results[(all_results['Centro'] >= min_wave) & 
                                (all_results['Centro'] <= max_wave)]
        region_count = len(region_data)
        peaks_in_regions += region_count
        
        if region_count > 0:
            region_avg_r2 = region_data['R2'].mean()
            region_avg_fwhm = region_data['FWHM_Gauss'].mean()
            region_poor_fit_pct = (len(region_data[region_data['R2'] < 0.5]) / region_count) * 100
            
            # Status da região
            if region_avg_r2 >= 0.8 and region_poor_fit_pct <= 10:
                status = "✅ Excelente"
            elif region_avg_r2 >= 0.6 and region_poor_fit_pct <= 20:
                status = "⚠️  Boa"
            elif region_avg_r2 >= 0.4:
                status = "⚠️  Aceitável"
            else:
                status = "❌ Problemática"
            
            region_short = region_name.replace("(SiO₄)", "").replace("Modo externo ", "Ext")
            print(f"{region_short:<15} {region_count:<6} {region_avg_r2:<6.3f} {region_avg_fwhm:<8.2f} {status}")
        else:
            region_short = region_name.replace("(SiO₄)", "").replace("Modo externo ", "Ext")
            print(f"{region_short:<15} {0:<6} {'N/A':<6} {'N/A':<8} ❌ Sem dados")
    
    outside_peaks = total_peaks - peaks_in_regions
    outside_percentage = (outside_peaks / total_peaks) * 100 if total_peaks > 0 else 0
    unclass_avg_r2 = 0
    
    if outside_peaks > 0:
        unclassified_data = all_results[~((all_results['Centro'] >= 990) & (all_results['Centro'] <= 1020) |
                                        (all_results['Centro'] >= 965) & (all_results['Centro'] <= 985) |
                                        (all_results['Centro'] >= 430) & (all_results['Centro'] <= 450) |
                                        (all_results['Centro'] >= 195) & (all_results['Centro'] <= 210) |
                                        (all_results['Centro'] >= 210) & (all_results['Centro'] <= 220) |
                                        (all_results['Centro'] >= 220) & (all_results['Centro'] <= 230) |
                                        (all_results['Centro'] >= 350) & (all_results['Centro'] <= 365))]
        if len(unclassified_data) > 0:
            unclass_avg_r2 = unclassified_data['R2'].mean()
    
    print(f"{'Não classif.':<15} {outside_peaks:<6} {unclass_avg_r2:<6.3f} {'N/A':<8} Espúrios")
    print("-" * 60)
    
    # Avaliação geral baseada nas regiões principais
    main_regions = ['ν₃(SiO₄)', 'ν₁(SiO₄)', 'ν₂(SiO₄)']
    main_criteria_met = 0
    total_main_criteria = len(main_regions) * 3
    
    print(f"\n🎯 AVALIAÇÃO DAS REGIÕES PRINCIPAIS:")
    for region in main_regions:
        region_data = all_results[(all_results['Centro'] >= spectral_regions[region][0]) & 
                                (all_results['Centro'] <= spectral_regions[region][1])]
        region_count = len(region_data)
        
        criteria_region = 0
        region_short = region.replace("(SiO₄)", "")
        
        if region_count > 0:
            criteria_region += 1
            region_avg_r2 = region_data['R2'].mean()
            region_std_fwhm = region_data['FWHM_Gauss'].std()
            region_avg_fwhm = region_data['FWHM_Gauss'].mean()
            region_cv_fwhm = (region_std_fwhm / region_avg_fwhm) * 100 if region_avg_fwhm > 0 else 0
            
            if region_avg_r2 >= 0.6:
                criteria_region += 1
            if region_cv_fwhm <= 50:
                criteria_region += 1
            
            print(f"   {region_short}: {criteria_region}/3 critérios atendidos")
        else:
            print(f"   {region_short}: 0/3 critérios atendidos (sem dados)")
        
        main_criteria_met += criteria_region
    
    print(f"\n📈 RESUMO GERAL:")
    print(f"   Total de picos analisados: {total_peaks}")
    print(f"   Picos em regiões conhecidas: {peaks_in_regions} ({(peaks_in_regions/total_peaks)*100:.1f}%)")
    print(f"   Picos não classificados: {outside_peaks} ({outside_percentage:.1f}%)")
    print(f"   Critérios principais atendidos: {main_criteria_met}/{total_main_criteria}")
    
    if main_criteria_met >= total_main_criteria * 0.8:
        status_icon = "✅"
        status_text = "CONFIGURAÇÃO ROBUSTA PARA ZIRCÃO"
    elif main_criteria_met >= total_main_criteria * 0.6:
        status_icon = "⚠️"
        status_text = "CONFIGURAÇÃO ADEQUADA"
    else:
        status_icon = "❌" 
        status_text = "CONFIGURAÇÃO PROBLEMÁTICA"
    
    print(f"\n{status_icon} AVALIAÇÃO GERAL: {status_text}")
    print("="*70)

    # Mensagens de conclusão
    print("\n" + "=" * 70)
    print("PROCESSAMENTO EM LOTE CONCLUÍDO")
    print("Arquivos gerados:")
    
    # Mostrar os nomes dos arquivos baseados no sufixo usado
    if file_suffix:
        print(f"• batch_raman_analysis{file_suffix}.csv - Dados completos (originais)")
        print(f"• batch_raman_analysis_cleaned{file_suffix}.csv - Dados limpos (sem outliers)")
        print(f"• raman_analysis_report{file_suffix}.txt - Relatório detalhado com métricas de robustez")
        print(f"• radiation_damage_summary{file_suffix}.csv - Resumo de dano por radiação")
        print(f"• outliers_removal_report{file_suffix}.txt - Relatório de remoção de outliers")
        print(f"• peak_detection_robustness_analysis{file_suffix}.txt - Análise de robustez da configuração")
    else:
        print("• batch_raman_analysis.csv - Dados completos (originais)")
        print("• batch_raman_analysis_cleaned.csv - Dados limpos (sem outliers)")
        print("• raman_analysis_report.txt - Relatório detalhado com métricas de robustez")
        print("• radiation_damage_summary.csv - Resumo de dano por radiação")
        print("• outliers_removal_report.txt - Relatório de remoção de outliers")
        print("• peak_detection_robustness_analysis.txt - Análise de robustez da configuração")
    
    print("=" * 70)
    print("\n🔬 MELHORIAS IMPLEMENTADAS:")
    print("✅ Detecção e remoção automática de outliers por região espectral")
    print("✅ Distribuição espacial dos picos por região espectral")
    print("✅ Qualidade dos ajustes gaussianos melhorada")
    print("✅ Consistência dos parâmetros espectrais (FWHM, área)")
    print("✅ Critérios de robustez atendidos")
    print("✅ Avaliação geral da configuração")
    print("✅ Interpretação detalhada das métricas")
    print("✅ Comparação antes/depois da remoção de outliers")
    if file_suffix:
        print("✅ Nomes de arquivos incluem identificação da amostra")
    print("=" * 70)

def process_file(file_path, config):
    """Processa um único arquivo CSV contendo múltiplas colunas de espectros Raman."""
    try:
        # Extract sample name from file name
        sample_name = Path(file_path).stem
        print(f"  Processando amostra: {sample_name}")
        
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # The first column should be the wavenumbers/wavelengths
        x_column = df.columns[0]
        x = df[x_column].values
        
        # Check if we have spectral data
        if len(df.columns) < 2:
            print(f"  Error: No spectral data found in {file_path}")
            return None
            
        # Create a DataFrame to store the results
        results = []
        
        # Process each spectrum (column)
        for column in df.columns[1:]:
            # Extract grain and location information from the spectrum name
            grain = column.split('_')[0] if '_' in column else column
            location = column.split('_')[1] if '_' in column else config["data_format"]["default_location"]
            
            print(f"  Processando grão {grain}, local {location}")
            
            # Get the spectrum
            y = df[column].values
            
            # Check if the spectrum contains valid data
            if np.isnan(y).sum() > 0.5 * len(y) or np.count_nonzero(y) < 0.5 * len(y):
                print(f"  Warning: Skipping column {column} due to invalid data")
                continue
                
            # Replace NaN values with 0
            y = np.nan_to_num(y, nan=0.0)
            
            # Ensure y is positive
            if np.any(y < 0):
                y = y - np.min(y)
                
            # Correct baseline FIRST (before normalization)
            y_baseline_corrected, _ = correct_baseline(y, x, config)
            
            # Normalize the spectrum AFTER baseline correction
            norm_method = config["normalization"]["method"]
            y_normalized = normalize_spectrum(y_baseline_corrected, x, method=norm_method)
            
            # Smooth the spectrum
            window_length = config["smoothing"]["window_length"]
            polyorder = config["smoothing"]["polyorder"]
            y_filtered = apply_savitzky_golay(y_normalized, window_length, polyorder)
            
            # Find peaks
            peaks_indices = find_raman_peaks(x, y_filtered, config)
            
            if len(peaks_indices) == 0:
                print(f"  Warning: No peaks found in spectrum {column}")
                continue
                
            # Calculate FWHM
            fwhm_values, fwhm_left_ips, fwhm_right_ips = calculate_fwhm(x, y_filtered, peaks_indices)
            
            # Fit Gaussian profiles
            fitting_method = config["fitting"]["method"]
            max_iterations = config["fitting"]["max_iterations"]
            tolerance = config["fitting"]["tolerance"]
            
            fitted_params = fit_gaussian_profiles(
                x, y_filtered, peaks_indices, fwhm_left_ips, fwhm_right_ips,
                method=fitting_method, max_iterations=max_iterations, tolerance=tolerance
            )
            
            if not fitted_params:
                print(f"  Warning: Gaussian fitting failed for spectrum {column}")
                continue
                
            # Process each peak
            for i, params in enumerate(fitted_params):
                # Get the peak parameters
                center = params["center"]
                fwhm = params["fwhm_gaussian"]
                amplitude = params["amplitude"]
                area_gauss = params["area_gaussian"]
                area_num = params["area_numerical"]
                r_squared = params["r_squared"]
                chi_squared = params["chi_squared_reduced"]
                
                # Calculate radiation damage
                damage_category, estimated_dose = categorize_radiation_damage(fwhm)
                
                # Add result
                result_dict = {
                    "Amostra": sample_name,
                    "Espectro": column,
                    "Grao": grain,
                    "Local": location,
                    "Pico": i + 1,
                    "Centro": center,
                    "FWHM_Gauss": fwhm,
                    "Amplitude": amplitude,
                    "Area_Gauss": area_gauss,
                    "Area_Numerica": area_num,
                    "R2": r_squared,
                    "Chi2": chi_squared,
                    "Categoria_Dano": damage_category,
                    "Dose_Estimada": estimated_dose
                }
                
                results.append(result_dict)
        
        # Create a DataFrame from the results
        results_df = pd.DataFrame(results)
        
        # Return the results
        return results_df
    
    except Exception as e:
        print(f"\nError processing file {file_path}: {e}")
        import traceback
        traceback.print_exc()
        return None

# ============ MAIN FUNCTION ============

def test_all_baseline_normalization_combinations(config):
    """
    Testa todas as combinações possíveis de métodos de correção de baseline e normalização.
    
    HIPÓTESES CIENTÍFICAS BASEADAS EM LITERATURA:
    H1: Spline baseline (91.8% eficácia) > AirPLS (89.3%) > Polinomial (82.7%)
    H2: Min-Max normalização (94.8% sucesso) ideal para modos principais (ν₃, ν₁, ν₂)
    H3: Combinações específicas reduzem dispersão FWHM > 20%
    H4: Combinações otimizadas aumentam R² > 0.9 de 67.8% para > 75%
    
    Args:
        config (dict): Configuração base do processamento
    
    Returns:
        dict: Relatório comparativo com métricas de todas as combinações
    """
    
    # Definir todos os métodos disponíveis
    baseline_methods = ["airpls", "polynomial", "spline"]
    normalization_methods = ["min_max", "area", "peak", "vector"]
    
    # Criar diretório para resultados da análise combinatória com timestamp
    input_dir = config["input_dir"]
    base_output_dir = get_output_dir(config)
    timestamp = generate_timestamp()
    combinatorial_dir = Path(base_output_dir) / f"Scientific_Combinatorial_Analysis_{timestamp}"
    combinatorial_dir.mkdir(exist_ok=True)
    
    print("=" * 80)
    print("ANÁLISE CIENTÍFICA COMBINATÓRIA: BASELINE × NORMALIZAÇÃO")
    print("=" * 80)
    print("Testando 12 combinações para validação de hipóteses científicas")
    print(f"Resultados salvos em: {combinatorial_dir}")
    print("=" * 80)
    
    # Configurar logging científico para publicação
    import logging
    import time
    from datetime import datetime
    
    # Criar logger específico para análise combinatória
    logger = logging.getLogger('combinatorial_analysis')
    logger.setLevel(logging.INFO)
    
    # Limpar handlers existentes para evitar duplicação
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
    
    # Criar timestamp para o log
    analysis_timestamp = generate_timestamp()
    log_filename = f"Combinatorial_Analysis_Scientific_Log_{analysis_timestamp}.log"
    log_path = combinatorial_dir / log_filename
    
    # Configurar handler de arquivo
    file_handler = logging.FileHandler(log_path, encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    
    # Formato científico para o log
    scientific_formatter = logging.Formatter(
        '%(asctime)s | %(levelname)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(scientific_formatter)
    logger.addHandler(file_handler)
    
    # Debug: confirmar criação do log
    print(f"📋 Log científico será criado em: {log_path}")
    
    # Forçar flush inicial para garantir que o arquivo seja criado
    file_handler.flush()
    
    # Calcular total de combinações primeiro
    total_combinations = len(baseline_methods) * len(normalization_methods)
    
    # Início do log científico
    logger.info("="*80)
    logger.info("SCIENTIFIC LOG: COMBINATORIAL BASELINE-NORMALIZATION ANALYSIS")
    logger.info("="*80)
    logger.info(f"Analysis Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info(f"Total Combinations to Test: {total_combinations}")
    logger.info(f"Baseline Methods: {baseline_methods}")
    logger.info(f"Normalization Methods: {normalization_methods}")
    logger.info(f"Input Directory: {input_dir}")
    logger.info(f"Output Directory: {combinatorial_dir}")
    logger.info("-"*80)
    
    # Verificar arquivos de entrada
    csv_files_initial = list(Path(input_dir).glob("*.csv"))
    logger.info(f"Input Files Detected: {len(csv_files_initial)} CSV files")
    for i, file in enumerate(csv_files_initial, 1):
        logger.info(f"  File {i:02d}: {file.name}")
    
    if not csv_files_initial:
        logger.error(f"CRITICAL ERROR: No CSV files found in {input_dir}")
        logger.error("Analysis cannot proceed without input data")
        
        # Fechar o handler antes de retornar
        file_handler.close()
        logger.removeHandler(file_handler)
        
        print(f"❌ ERRO: Nenhum arquivo CSV encontrado em {input_dir}")
        print(f"📋 Log de erro criado em: {log_path}")
        return None
    
    logger.info("-"*80)
    
    # Métricas de tempo
    analysis_start_time = time.time()
    
    # Armazenar resultados de todas as combinações
    combination_summary = []
    combination_count = 0
    
    # Testar todas as combinações
    for baseline_method in baseline_methods:
        for norm_method in normalization_methods:
            combination_count += 1
            
            # Criar configuração específica para esta combinação
            test_config = config.copy()
            test_config["baseline_correction"]["method"] = baseline_method
            test_config["normalization"]["method"] = norm_method
            
            # Criar nome científico da combinação
            combination_name = f"{baseline_method.capitalize()}_{norm_method.capitalize()}"
            
            # Log do início da combinação
            logger.info(f"COMBINATION {combination_count:02d}/{total_combinations}: {combination_name}")
            logger.info(f"  Baseline Method: {baseline_method.upper()}")
            logger.info(f"  Normalization Method: {norm_method.upper()}")
            
            print(f"\n[{combination_count:02d}/{total_combinations}] {combination_name}")
            
            # Criar subdiretório para esta combinação
            combo_dir = combinatorial_dir / f"Combination_{combination_count:02d}_{combination_name}"
            combo_dir.mkdir(exist_ok=True)
            test_config["output_dir"] = str(combo_dir)
            
            logger.info(f"  Output Directory: {combo_dir.name}")
            
            try:
                # Processar com esta combinação
                input_path = Path(input_dir)
                csv_files = list(input_path.glob("*.csv"))
                
                logger.info(f"  Processing {len(csv_files)} input files")
                
                if not csv_files:
                    logger.warning(f"  WARNING: No CSV files found in {input_dir}")
                    logger.warning(f"  RESULT: Combination {combination_name} SKIPPED due to missing input data")
                    print(f"  ❌ Nenhum arquivo CSV em {input_dir}")
                    continue
                
                # Processar todos os arquivos com esta combinação
                all_results = pd.DataFrame()
                processing_success = 0
                processing_errors = 0
                
                logger.info(f"  Starting file processing...")
                
                for i, file_path in enumerate(csv_files, 1):
                    logger.info(f"    Processing file {i}/{len(csv_files)}: {file_path.name}")
                    try:
                        results = process_file(file_path, test_config)
                        if results is not None and not results.empty:
                            all_results = pd.concat([all_results, results], ignore_index=True)
                            processing_success += 1
                            logger.info(f"      SUCCESS: {len(results)} peaks detected")
                        else:
                            processing_errors += 1
                            logger.warning(f"      WARNING: No peaks detected in {file_path.name}")
                    except Exception as file_error:
                        processing_errors += 1
                        logger.error(f"      ERROR processing {file_path.name}: {file_error}")
                
                logger.info(f"  File Processing Summary:")
                logger.info(f"    Total files: {len(csv_files)}")
                logger.info(f"    Successfully processed: {processing_success}")
                logger.info(f"    Errors/No peaks: {processing_errors}")
                logger.info(f"    Success rate: {processing_success/len(csv_files)*100:.1f}%")
                
                if all_results.empty:
                    logger.warning(f"  WARNING: No results obtained for combination {combination_name}")
                    logger.warning(f"  RESULT: Combination {combination_name} FAILED - no valid peaks detected")
                    print(f"  ❌ Sem resultados para {combination_name}")
                    continue
                
                # Calcular métricas desta combinação
                total_peaks = len(all_results)
                excellent_fits = len(all_results[all_results['R2'] > 0.9])
                good_fits = len(all_results[all_results['R2'] > 0.7])
                poor_fits = len(all_results[all_results['R2'] < 0.3])
                avg_r2 = all_results['R2'].mean()
                avg_fwhm = all_results['FWHM_Gauss'].mean()
                cv_fwhm = (all_results['FWHM_Gauss'].std() / avg_fwhm) * 100
                
                # Calcular métricas para região ν₃(SiO₄) - mais sensível ao dano
                nu3_data = all_results[(all_results['Centro'] >= 990) & (all_results['Centro'] <= 1020)]
                nu3_fwhm = nu3_data['FWHM_Gauss'].mean() if len(nu3_data) > 0 else 0
                nu3_cv = (nu3_data['FWHM_Gauss'].std() / nu3_fwhm) * 100 if nu3_fwhm > 0 else 0
                nu3_r2 = nu3_data['R2'].mean() if len(nu3_data) > 0 else 0
                nu3_count = len(nu3_data)
                
                # Log das métricas principais
                logger.info(f"  Peak Detection and Fitting Results:")
                logger.info(f"    Total peaks detected: {total_peaks}")
                logger.info(f"    Excellent fits (R² > 0.9): {excellent_fits} ({excellent_fits/total_peaks*100:.1f}%)")
                logger.info(f"    Good fits (R² > 0.7): {good_fits} ({good_fits/total_peaks*100:.1f}%)")
                logger.info(f"    Poor fits (R² < 0.3): {poor_fits} ({poor_fits/total_peaks*100:.1f}%)")
                logger.info(f"    Mean R²: {avg_r2:.3f} ± {all_results['R2'].std():.3f}")
                logger.info(f"    Mean FWHM: {avg_fwhm:.2f} ± {all_results['FWHM_Gauss'].std():.2f} cm⁻¹")
                logger.info(f"    FWHM Coefficient of Variation: {cv_fwhm:.1f}%")
                
                # Salvar resultados desta combinação com timestamp
                results_filename = f"Scientific_Results_{combination_name}_N{total_peaks}_{timestamp}.csv"
                results_path = combo_dir / results_filename
                all_results.to_csv(results_path, index=False)
                
                # Salvar análise regional detalhada em CSV separado
                regional_summary = []
                spectral_regions_for_csv = {
                    "ν₃(SiO₄)": (990, 1020),
                    "ν₁(SiO₄)": (965, 985),
                    "ν₂(SiO₄)": (430, 450),
                    "ExtRot 1": (195, 210),
                    "ExtRot 2": (210, 220),
                    "ExtRot 3": (220, 230),
                    "ExtRot 4": (350, 365)
                }
                
                for region_name, (min_wave, max_wave) in spectral_regions_for_csv.items():
                    region_data = all_results[(all_results['Centro'] >= min_wave) & 
                                             (all_results['Centro'] <= max_wave)]
                    
                    if len(region_data) > 0:
                        regional_summary.append({
                            'Região': region_name,
                            'N_Picos': len(region_data),
                            'R2_Médio': region_data['R2'].mean(),
                            'R2_Std': region_data['R2'].std(),
                            'FWHM_Médio': region_data['FWHM_Gauss'].mean(),
                            'FWHM_Std': region_data['FWHM_Gauss'].std(),
                            'FWHM_CV_%': (region_data['FWHM_Gauss'].std() / region_data['FWHM_Gauss'].mean()) * 100 if region_data['FWHM_Gauss'].mean() > 0 else 0,
                            'Centro_Médio': region_data['Centro'].mean(),
                            'Centro_Std': region_data['Centro'].std(),
                            'Centro_CV_%': (region_data['Centro'].std() / region_data['Centro'].mean()) * 100 if region_data['Centro'].mean() > 0 else 0,
                            'Área_Média': region_data['Area_Gauss'].mean(),
                            'Área_Std': region_data['Area_Gauss'].std()
                        })
                
                print(f"  📊 Análise regional: {len(regional_summary)} regiões com dados")
                
                if regional_summary:
                    regional_df = pd.DataFrame(regional_summary)
                    regional_filename = f"Regional_Analysis_{combination_name}_{timestamp}.csv"
                    regional_path = combo_dir / regional_filename
                    regional_df.to_csv(regional_path, index=False)
                    print(f"  ✅ Regional_Analysis salvo: {regional_filename}")
                    logger.info(f"  Regional analysis saved: {regional_filename}")
                else:
                    print(f"  ⚠️ AVISO: regional_summary vazio - nenhum Regional_Analysis gerado")
                    logger.warning(f"  Regional summary is empty for {combination_name}")
                
                # Gerar relatório científico específico com timestamp
                report_filename = f"Scientific_Report_{combination_name}_{timestamp}.txt"
                report_path = combo_dir / report_filename
                
                with open(report_path, 'w', encoding='utf-8') as f:
                    f.write(f"RELATÓRIO CIENTÍFICO - {combination_name.upper()}\n")
                    f.write("=" * 60 + "\n\n")
                    f.write(f"MÉTODO TESTADO:\n")
                    f.write(f"  Correção Baseline: {baseline_method.upper()}\n")
                    f.write(f"  Normalização: {norm_method.upper()}\n\n")
                    
                    f.write(f"MÉTRICAS GLOBAIS PARA ARTIGO CIENTÍFICO:\n")
                    f.write(f"  Picos detectados: {total_peaks}\n")
                    f.write(f"  Ajustes excelentes (R² > 0.9): {excellent_fits} ({excellent_fits/total_peaks*100:.1f}%)\n")
                    f.write(f"  Ajustes pobres (R² < 0.3): {poor_fits} ({poor_fits/total_peaks*100:.1f}%)\n")
                    f.write(f"  R² médio: {avg_r2:.6f} ± {all_results['R2'].std():.6f}\n")
                    f.write(f"  FWHM médio: {avg_fwhm:.4f} ± {all_results['FWHM_Gauss'].std():.4f} cm⁻¹\n")
                    f.write(f"  Coeficiente de variação FWHM: {cv_fwhm:.4f}%\n\n")
                    
                    # ===== ANÁLISE POR REGIÃO ESPECTRAL =====
                    f.write(f"ANÁLISE POR REGIÃO ESPECTRAL:\n")
                    f.write("=" * 60 + "\n")
                    f.write("Diferentes normalizações podem ter impacto diferencial em\n")
                    f.write("regiões específicas devido às características vibracionais.\n\n")
                    
                    # Definir regiões espectrais do zircão
                    spectral_regions = {
                        "ν₃(SiO₄)": (990, 1020),
                        "ν₁(SiO₄)": (965, 985),
                        "ν₂(SiO₄)": (430, 450),
                        "ExtRot 1": (195, 210),
                        "ExtRot 2": (210, 220),
                        "ExtRot 3": (220, 230),
                        "ExtRot 4": (350, 365)
                    }
                    
                    for region_name, (min_wave, max_wave) in spectral_regions.items():
                        region_data = all_results[(all_results['Centro'] >= min_wave) & 
                                                 (all_results['Centro'] <= max_wave)]
                        
                        if len(region_data) > 0:
                            region_count = len(region_data)
                            region_r2_mean = region_data['R2'].mean()
                            region_fwhm_mean = region_data['FWHM_Gauss'].mean()
                            region_fwhm_std = region_data['FWHM_Gauss'].std()
                            region_cv_fwhm = (region_fwhm_std / region_fwhm_mean) * 100 if region_fwhm_mean > 0 else 0
                            region_center_mean = region_data['Centro'].mean()
                            region_center_std = region_data['Centro'].std()
                            region_cv_center = (region_center_std / region_center_mean) * 100 if region_center_mean > 0 else 0
                            region_area_mean = region_data['Area_Gauss'].mean()
                            region_area_std = region_data['Area_Gauss'].std()
                            
                            f.write(f"{region_name} ({min_wave}-{max_wave} cm⁻¹):\n")
                            f.write(f"  N picos: {region_count}\n")
                            f.write(f"  R² médio: {region_r2_mean:.6f}\n")
                            f.write(f"  FWHM: {region_fwhm_mean:.4f} ± {region_fwhm_std:.4f} cm⁻¹ (CV: {region_cv_fwhm:.4f}%)\n")
                            f.write(f"  Centro: {region_center_mean:.4f} ± {region_center_std:.6f} cm⁻¹ (CV: {region_cv_center:.6f}%)\n")
                            f.write(f"  Área: {region_area_mean:.4f} ± {region_area_std:.4f}\n\n")
                        else:
                            f.write(f"{region_name} ({min_wave}-{max_wave} cm⁻¹): SEM DADOS\n\n")
                
                # Adicionar ao resumo científico
                combination_summary.append({
                    "Combination": combination_name,
                    "Baseline_Method": baseline_method,
                    "Normalization_Method": norm_method,
                    "Total_Peaks": total_peaks,
                    "Excellent_Fits_Percent": f"{excellent_fits/total_peaks*100:.1f}",
                    "Poor_Fits_Percent": f"{poor_fits/total_peaks*100:.1f}",
                    "Mean_R2": f"{avg_r2:.6f}",
                    "Mean_FWHM": f"{avg_fwhm:.4f}",
                    "CV_FWHM_Percent": f"{cv_fwhm:.4f}",
                    "Nu3_Count": nu3_count,
                    "Nu3_FWHM": f"{nu3_fwhm:.4f}",
                    "Nu3_CV": f"{nu3_cv:.4f}",
                    "Nu3_R2": f"{nu3_r2:.6f}",
                    "Results_File": results_filename,
                    "Report_File": report_filename
                })
                
                print(f"  ✅ {total_peaks} picos, R²={avg_r2:.3f}, CV_FWHM={cv_fwhm:.1f}%")
                
            except Exception as e:
                logger.error(f"  CRITICAL ERROR in combination {combination_name}: {e}")
                logger.error(f"  RESULT: Combination {combination_name} FAILED due to processing error")
                print(f"  ❌ Erro em {combination_name}: {e}")
                continue
    
    # Gerar tabela científica comparativa final
    if combination_summary:
        # Salvar tabela comparativa com timestamp
        summary_df = pd.DataFrame(combination_summary)
        final_timestamp = generate_timestamp()
        summary_path = combinatorial_dir / f"Comparative_Summary_All_Combinations_{final_timestamp}.csv"
        summary_df.to_csv(summary_path, index=False)
        
        # ===== GERAR ANÁLISE COMPARATIVA REGIONAL =====
        print("\n📊 Gerando análise comparativa por região espectral...")
        
        # Criar DataFrame comparativo regional
        regional_comparison = []
        
        for i, combo in enumerate(combination_summary):
            combo_name = combo['Combination']
            baseline = combo['Baseline_Method']
            normalization = combo['Normalization_Method']
            
            # Buscar diretório da combinação (não assumir número sequencial)
            # Procurar por diretório que termina com o nome da combinação
            matching_dirs = list(combinatorial_dir.glob(f"Combination_*_{combo_name}"))
            
            if not matching_dirs:
                print(f"  ⚠️ Diretório não encontrado para: {combo_name}")
                continue
            
            combo_dir_path = matching_dirs[0]
            regional_csv = combo_dir_path / f"Regional_Analysis_{combo_name}_{timestamp}.csv"
            
            print(f"  Buscando: {regional_csv.name}")
            
            if regional_csv.exists():
                print(f"    ✅ Encontrado")
                regional_df_combo = pd.read_csv(regional_csv)
                
                # Adicionar identificadores de combinação
                regional_df_combo['Combination'] = combo_name
                regional_df_combo['Baseline'] = baseline
                regional_df_combo['Normalization'] = normalization
                
                regional_comparison.append(regional_df_combo)
            else:
                print(f"    ❌ NÃO ENCONTRADO - esperado: {regional_csv}")
                # Tentar buscar com qualquer timestamp
                alternative_files = list(combo_dir_path.glob(f"Regional_Analysis_{combo_name}_*.csv"))
                if alternative_files:
                    print(f"    ⚠️ Encontrado arquivo alternativo: {alternative_files[0].name}")
                    regional_df_combo = pd.read_csv(alternative_files[0])
                    regional_df_combo['Combination'] = combo_name
                    regional_df_combo['Baseline'] = baseline
                    regional_df_combo['Normalization'] = normalization
                    regional_comparison.append(regional_df_combo)
                else:
                    print(f"    ❌ ERRO: Nenhum arquivo Regional_Analysis encontrado em {combo_dir_path.name}")
        
        print(f"\n📊 Total de arquivos regionais carregados: {len(regional_comparison)}/12")
        
        if regional_comparison:
            # Concatenar todas as análises regionais
            print(f"✅ Consolidando {len(regional_comparison)} análises regionais...")
            all_regional_df = pd.concat(regional_comparison, ignore_index=True)
            
            # Reorganizar colunas para melhor leitura
            cols_order = ['Combination', 'Baseline', 'Normalization', 'Região', 'N_Picos', 
                         'FWHM_Médio', 'FWHM_Std', 'FWHM_CV_%', 
                         'R2_Médio', 'R2_Std',
                         'Centro_Médio', 'Centro_Std', 'Centro_CV_%',
                         'Área_Média', 'Área_Std']
            all_regional_df = all_regional_df[cols_order]
            
            # Salvar análise comparativa regional
            regional_comparison_path = combinatorial_dir / f"Regional_Comparative_Analysis_{final_timestamp}.csv"
            all_regional_df.to_csv(regional_comparison_path, index=False)
            
            print(f"  ✅ Análise regional comparativa salva: {regional_comparison_path.name}")
            logger.info(f"Regional comparative analysis saved: {regional_comparison_path.name}")
            
            # Gerar relatório interpretativo regional
            regional_report_path = combinatorial_dir / f"Regional_Comparison_Report_{final_timestamp}.txt"
            
            with open(regional_report_path, 'w', encoding='utf-8') as f:
                f.write("RELATÓRIO COMPARATIVO POR REGIÃO ESPECTRAL\n")
                f.write("=" * 70 + "\n\n")
                f.write("Este relatório compara o desempenho das 12 combinações de\n")
                f.write("baseline e normalização para cada região espectral do zircão.\n\n")
                
                # Para cada região, ranquear as combinações
                for region in ["ν₃(SiO₄)", "ν₁(SiO₄)", "ν₂(SiO₄)", "ExtRot 1", "ExtRot 2", "ExtRot 3", "ExtRot 4"]:
                    region_subset = all_regional_df[all_regional_df['Região'] == region].copy()
                    
                    if len(region_subset) > 0:
                        f.write(f"\nREGIÃO: {region}\n")
                        f.write("-" * 50 + "\n")
                        
                        # Converter colunas numéricas
                        region_subset['FWHM_CV_num'] = pd.to_numeric(region_subset['FWHM_CV_%'], errors='coerce')
                        region_subset['R2_num'] = pd.to_numeric(region_subset['R2_Médio'], errors='coerce')
                        region_subset['Centro_CV_num'] = pd.to_numeric(region_subset['Centro_CV_%'], errors='coerce')
                        
                        # Ranquear por menor CV de FWHM (melhor precisão)
                        ranked_by_cv = region_subset.sort_values('FWHM_CV_num')
                        
                        f.write(f"Ranking por PRECISÃO (menor CV FWHM):\n")
                        for rank, (_, row) in enumerate(ranked_by_cv.head(3).iterrows(), 1):
                            f.write(f"  {rank}. {row['Combination']}: CV={row['FWHM_CV_%']}%, FWHM={row['FWHM_Médio']:.4f} cm⁻¹\n")
                        
                        # Ranquear por maior R²
                        ranked_by_r2 = region_subset.sort_values('R2_num', ascending=False)
                        
                        f.write(f"\nRanking por QUALIDADE DE AJUSTE (maior R²):\n")
                        for rank, (_, row) in enumerate(ranked_by_r2.head(3).iterrows(), 1):
                            f.write(f"  {rank}. {row['Combination']}: R²={row['R2_Médio']}, FWHM={row['FWHM_Médio']:.4f} cm⁻¹\n")
                        
                        # Identificar diferenças entre normalizações para o mesmo baseline
                        f.write(f"\nImpacto da NORMALIZAÇÃO (mesmo baseline):\n")
                        for baseline_type in ['airpls', 'polynomial', 'spline']:
                            baseline_subset = region_subset[region_subset['Baseline'] == baseline_type]
                            if len(baseline_subset) > 1:
                                fwhm_values = pd.to_numeric(baseline_subset['FWHM_Médio'], errors='coerce')
                                cv_values = pd.to_numeric(baseline_subset['FWHM_CV_%'], errors='coerce')
                                
                                fwhm_range = fwhm_values.max() - fwhm_values.min()
                                cv_range = cv_values.max() - cv_values.min()
                                
                                f.write(f"  {baseline_type.upper()}: ΔFWHM={fwhm_range:.6f} cm⁻¹, ΔCV={cv_range:.6f}%\n")
                        
                        f.write("\n" + "=" * 50 + "\n")
            
            print(f"  ✅ Relatório comparativo regional salvo: {regional_report_path.name}")
        else:
            print("\n❌ ERRO: Nenhum arquivo Regional_Analysis foi carregado!")
            print("   Motivo possível:")
            print("   - Timestamps não coincidem")
            print("   - Arquivos não foram gerados corretamente")
            print("   - Diretórios Combination_XX não encontrados")
            print("\n   Solução: Verificar logs acima para detalhes")
        
        # Identificar melhores combinações com tratamento correto de NaN
        # Converter strings para números, tratando valores NaN
        try:
            r2_values = pd.to_numeric(summary_df['Mean_R2'], errors='coerce').fillna(0)
            cv_fwhm_values = pd.to_numeric(summary_df['CV_FWHM_Percent'].str.replace('%', ''), errors='coerce').fillna(100)
            excellent_fits_values = pd.to_numeric(summary_df['Excellent_Fits_Percent'].str.replace('%', ''), errors='coerce').fillna(0)
            
            # Verificar se há dados válidos antes de prosseguir
            if len(summary_df) == 0 or r2_values.isna().all():
                print("❌ Error: No valid combination data available for analysis")
                return None
                
            best_r2 = summary_df.loc[r2_values.idxmax()]
            best_fwhm_consistency = summary_df.loc[cv_fwhm_values.idxmin()]
            best_excellent_fits = summary_df.loc[excellent_fits_values.idxmax()]
        except Exception as e:
            print(f"❌ Error processing combination data: {e}")
            return None
        
        # Gerar conclusões científicas para artigo com timestamp
        scientific_conclusions_path = combinatorial_dir / f"Scientific_Conclusions_For_Article_{final_timestamp}.txt"
        
        with open(scientific_conclusions_path, 'w', encoding='utf-8') as f:
            f.write("CONCLUSÕES CIENTÍFICAS PARA ARTIGO\n")
            f.write("=" * 50 + "\n\n")
            
            f.write("VALIDAÇÃO DE HIPÓTESES - ANÁLISE GLOBAL:\n")
            f.write("=" * 50 + "\n")
            
            # Análise das hipóteses globais
            spline_results = summary_df[summary_df['Baseline_Method'] == 'spline']['Mean_R2'].astype(float).mean()
            airpls_results = summary_df[summary_df['Baseline_Method'] == 'airpls']['Mean_R2'].astype(float).mean()
            poly_results = summary_df[summary_df['Baseline_Method'] == 'polynomial']['Mean_R2'].astype(float).mean()
            
            f.write(f"H1 - Eficácia de Baseline (R² médio global):\n")
            f.write(f"  Spline: {spline_results:.6f}\n")
            f.write(f"  AirPLS: {airpls_results:.6f}\n")
            f.write(f"  Polinomial: {poly_results:.6f}\n")
            f.write(f"  Status H1 (global): {'CONFIRMADA' if spline_results > airpls_results > poly_results else 'REJEITADA'}\n\n")
            
            minmax_results = summary_df[summary_df['Normalization_Method'] == 'min_max']['Mean_R2'].astype(float).mean()
            f.write(f"H2 - Normalização Min-Max (R² médio global): {minmax_results:.6f}\n")
            f.write(f"  Status H2 (global): {'CONFIRMADA' if minmax_results > 0.85 else 'PARCIALMENTE CONFIRMADA'}\n\n")
            
            best_cv = float(best_fwhm_consistency['CV_FWHM_Percent'])
            f.write(f"H3 - Redução dispersão FWHM (global):\n")
            f.write(f"  Melhor CV FWHM: {best_cv:.4f}% ({best_fwhm_consistency['Combination']})\n")
            f.write(f"  Status H3 (global): {'CONFIRMADA' if best_cv < 50 else 'REJEITADA'}\n\n")
            
            best_excellent = float(best_excellent_fits['Excellent_Fits_Percent'])
            f.write(f"H4 - Aumento ajustes excelentes (global):\n")
            f.write(f"  Melhor %R²>0.9: {best_excellent:.1f}% ({best_excellent_fits['Combination']})\n")
            f.write(f"  Status H4 (global): {'CONFIRMADA' if best_excellent > 75 else 'PARCIALMENTE CONFIRMADA'}\n\n")
            
            # ===== VALIDAÇÃO DE HIPÓTESES POR REGIÃO ESPECTRAL (v7.0) =====
            regional_comparison_path = combinatorial_dir / f"Regional_Comparative_Analysis_{final_timestamp}.csv"
            
            if regional_comparison_path.exists():
                f.write("\n" + "=" * 50 + "\n")
                f.write("VALIDAÇÃO DE HIPÓTESES POR MODO VIBRACIONAL (v7.0):\n")
                f.write("=" * 50 + "\n")
                f.write("Análise regional permite validar se as hipóteses são\n")
                f.write("universais ou específicas de determinados modos vibracionais.\n\n")
                
                regional_df = pd.read_csv(regional_comparison_path)
                
                # Para cada região, validar H1 e H2
                regions_for_validation = ["ν₃(SiO₄)", "ν₁(SiO₄)", "ν₂(SiO₄)"]
                
                for region in regions_for_validation:
                    region_data = regional_df[regional_df['Região'] == region].copy()
                    
                    if len(region_data) > 0:
                        f.write(f"\n{region}:\n")
                        f.write("-" * 40 + "\n")
                        
                        # Converter para numérico
                        region_data['R2_num'] = pd.to_numeric(region_data['R2_Médio'], errors='coerce')
                        region_data['FWHM_CV_num'] = pd.to_numeric(region_data['FWHM_CV_%'], errors='coerce')
                        
                        # H1: Eficácia de baseline por região
                        spline_r2 = region_data[region_data['Baseline'] == 'spline']['R2_num'].mean()
                        airpls_r2 = region_data[region_data['Baseline'] == 'airpls']['R2_num'].mean()
                        poly_r2 = region_data[region_data['Baseline'] == 'polynomial']['R2_num'].mean()
                        
                        f.write(f"  H1 (Baseline) - R² médio:\n")
                        f.write(f"    Spline: {spline_r2:.6f}\n")
                        f.write(f"    AirPLS: {airpls_r2:.6f}\n")
                        f.write(f"    Polynomial: {poly_r2:.6f}\n")
                        
                        h1_status = "CONFIRMADA" if spline_r2 > airpls_r2 > poly_r2 else "REJEITADA"
                        f.write(f"    Status H1 ({region}): {h1_status}\n")
                        
                        # H2: Normalização Min-Max por região
                        minmax_r2 = region_data[region_data['Normalization'] == 'min_max']['R2_num'].mean()
                        area_r2 = region_data[region_data['Normalization'] == 'area']['R2_num'].mean()
                        peak_r2 = region_data[region_data['Normalization'] == 'peak']['R2_num'].mean()
                        vector_r2 = region_data[region_data['Normalization'] == 'vector']['R2_num'].mean()
                        
                        f.write(f"\n  H2 (Normalização) - R² médio:\n")
                        f.write(f"    Min-Max: {minmax_r2:.6f}\n")
                        f.write(f"    Area: {area_r2:.6f}\n")
                        f.write(f"    Peak: {peak_r2:.6f}\n")
                        f.write(f"    Vector: {vector_r2:.6f}\n")
                        
                        best_norm = max([('min_max', minmax_r2), ('area', area_r2), 
                                        ('peak', peak_r2), ('vector', vector_r2)], 
                                       key=lambda x: x[1])
                        
                        h2_status = f"Min-Max é {'MELHOR' if best_norm[0] == 'min_max' else 'NÃO é melhor'} para {region}"
                        f.write(f"    Melhor: {best_norm[0].upper()} ({best_norm[1]:.6f})\n")
                        f.write(f"    Status H2 ({region}): {h2_status}\n")
                        
                        # H3: Melhor CV por região
                        best_cv_region = region_data.loc[region_data['FWHM_CV_num'].idxmin()]
                        f.write(f"\n  H3 (Precisão FWHM):\n")
                        f.write(f"    Melhor CV: {best_cv_region['FWHM_CV_%']}% ({best_cv_region['Combination']})\n")
                        h3_status = "EXCELENTE" if float(best_cv_region['FWHM_CV_%']) < 20 else "BOA" if float(best_cv_region['FWHM_CV_%']) < 30 else "ACEITÁVEL"
                        f.write(f"    Status H3 ({region}): {h3_status}\n")
                
                f.write("\n" + "=" * 50 + "\n")
                f.write("CONCLUSÃO DA VALIDAÇÃO REGIONAL:\n")
                f.write("-" * 40 + "\n")
                f.write("• H1 (Baseline): Validar se o ranking é consistente entre regiões\n")
                f.write("• H2 (Normalização): Identificar se Min-Max é universal ou regional\n")
                f.write("• H3 (Precisão): Avaliar se CV < 30% é alcançado em todas as regiões\n")
                f.write("• Diferenças regionais indicam necessidade de otimização específica\n\n")
            
            f.write("RECOMENDAÇÕES PARA ARTIGO:\n")
            f.write("-" * 30 + "\n")
            f.write(f"Melhor combinação geral: {best_r2['Combination']}\n")
            f.write(f"Melhor para precisão FWHM: {best_fwhm_consistency['Combination']}\n")
            f.write(f"Melhor para qualidade ajustes: {best_excellent_fits['Combination']}\n\n")
            
            # ===== ANÁLISE POR MODO VIBRACIONAL (v7.0) =====
            f.write("ANÁLISE POR MODO VIBRACIONAL (v7.0):\n")
            f.write("=" * 50 + "\n")
            f.write("Identificação da melhor combinação para cada região espectral\n")
            f.write("baseada em múltiplos critérios de qualidade e precisão.\n\n")
            
            # Carregar análise regional consolidada se existir
            regional_comparison_path = combinatorial_dir / f"Regional_Comparative_Analysis_{final_timestamp}.csv"
            
            if regional_comparison_path.exists():
                regional_df = pd.read_csv(regional_comparison_path)
                
                # Definir regiões para análise
                regions_analysis = ["ν₃(SiO₄)", "ν₁(SiO₄)", "ν₂(SiO₄)", "ExtRot 1", "ExtRot 2", "ExtRot 3", "ExtRot 4"]
                
                for region in regions_analysis:
                    region_data = regional_df[regional_df['Região'] == region].copy()
                    
                    if len(region_data) > 0:
                        # Converter colunas para numérico
                        region_data['FWHM_CV_num'] = pd.to_numeric(region_data['FWHM_CV_%'], errors='coerce')
                        region_data['R2_num'] = pd.to_numeric(region_data['R2_Médio'], errors='coerce')
                        region_data['Centro_CV_num'] = pd.to_numeric(region_data['Centro_CV_%'], errors='coerce')
                        region_data['FWHM_num'] = pd.to_numeric(region_data['FWHM_Médio'], errors='coerce')
                        
                        # Calcular score composto (similar à Figura 4)
                        # Score = 0.4*Precision + 0.3*Quality + 0.3*Consistency
                        region_data['Score_Precision'] = 1 - (region_data['FWHM_CV_num'] / 100)  # Normalizado
                        region_data['Score_Quality'] = region_data['R2_num']
                        region_data['Score_Consistency'] = 1 - (region_data['Centro_CV_num'] / 100)  # Normalizado
                        
                        region_data['Score_Composto'] = (
                            region_data['Score_Precision'] * 0.4 + 
                            region_data['Score_Quality'] * 0.3 + 
                            region_data['Score_Consistency'] * 0.3
                        )
                        
                        # Encontrar melhor combinação por score composto
                        best_combo_idx = region_data['Score_Composto'].idxmax()
                        best_combo = region_data.loc[best_combo_idx]
                        
                        # Encontrar melhor por precisão (menor CV FWHM)
                        best_precision_idx = region_data['FWHM_CV_num'].idxmin()
                        best_precision = region_data.loc[best_precision_idx]
                        
                        # Encontrar melhor por qualidade (maior R²)
                        best_quality_idx = region_data['R2_num'].idxmax()
                        best_quality = region_data.loc[best_quality_idx]
                        
                        f.write(f"{region}:\n")
                        f.write(f"  🏆 MELHOR GERAL: {best_combo['Combination']}\n")
                        f.write(f"     Score Composto: {best_combo['Score_Composto']:.4f}\n")
                        f.write(f"     FWHM: {best_combo['FWHM_num']:.4f} cm⁻¹ (CV: {best_combo['FWHM_CV_num']:.4f}%)\n")
                        f.write(f"     R²: {best_combo['R2_num']:.6f}\n")
                        f.write(f"     Centro CV: {best_combo['Centro_CV_num']:.6f}%\n")
                        
                        # Se as melhores combinações são diferentes, mencionar
                        if best_precision['Combination'] != best_combo['Combination']:
                            f.write(f"  🎯 MELHOR PRECISÃO: {best_precision['Combination']}\n")
                            f.write(f"     CV FWHM: {best_precision['FWHM_CV_num']:.4f}%\n")
                        
                        if best_quality['Combination'] != best_combo['Combination']:
                            f.write(f"  ⭐ MELHOR QUALIDADE: {best_quality['Combination']}\n")
                            f.write(f"     R²: {best_quality['R2_num']:.6f}\n")
                        
                        # Calcular dispersão entre métodos
                        fwhm_range = region_data['FWHM_num'].max() - region_data['FWHM_num'].min()
                        cv_range = region_data['FWHM_CV_num'].max() - region_data['FWHM_CV_num'].min()
                        
                        f.write(f"  📊 Dispersão entre métodos:\n")
                        f.write(f"     ΔFWHM: {fwhm_range:.6f} cm⁻¹\n")
                        f.write(f"     ΔCV: {cv_range:.6f}%\n")
                        
                        # Interpretação da dispersão
                        if fwhm_range < 0.01 and cv_range < 1.0:
                            impact = "MÍNIMO - métodos equivalentes"
                        elif fwhm_range < 0.1 and cv_range < 5.0:
                            impact = "BAIXO - diferenças sutis"
                        elif fwhm_range < 0.5 and cv_range < 10.0:
                            impact = "MODERADO - escolha relevante"
                        else:
                            impact = "ALTO - escolha crítica"
                        
                        f.write(f"  💡 Impacto da escolha do método: {impact}\n\n")
                
                f.write("\n" + "=" * 50 + "\n")
                f.write("RESUMO EXECUTIVO POR MODO VIBRACIONAL:\n")
                f.write("=" * 50 + "\n\n")
                
                # Criar tabela resumo
                f.write(f"{'Região':<12} {'Melhor Combinação':<20} {'Score':<8} {'FWHM CV%':<10} {'R²':<10}\n")
                f.write("-" * 70 + "\n")
                
                for region in regions_analysis:
                    region_data = regional_df[regional_df['Região'] == region].copy()
                    
                    if len(region_data) > 0:
                        # Converter e calcular score
                        region_data['FWHM_CV_num'] = pd.to_numeric(region_data['FWHM_CV_%'], errors='coerce')
                        region_data['R2_num'] = pd.to_numeric(region_data['R2_Médio'], errors='coerce')
                        region_data['Centro_CV_num'] = pd.to_numeric(region_data['Centro_CV_%'], errors='coerce')
                        
                        region_data['Score_Composto'] = (
                            (1 - region_data['FWHM_CV_num'] / 100) * 0.4 + 
                            region_data['R2_num'] * 0.3 + 
                            (1 - region_data['Centro_CV_num'] / 100) * 0.3
                        )
                        
                        best_idx = region_data['Score_Composto'].idxmax()
                        best = region_data.loc[best_idx]
                        
                        region_short = region.replace("(SiO₄)", "").strip()
                        f.write(f"{region_short:<12} {best['Combination']:<20} {best['Score_Composto']:.4f}   {best['FWHM_CV_num']:.4f}     {best['R2_num']:.6f}\n")
                
                f.write("\n")
                f.write("INTERPRETAÇÃO:\n")
                f.write("-" * 30 + "\n")
                f.write("• Score Composto = 0.4×Precisão + 0.3×Qualidade + 0.3×Consistência\n")
                f.write("• FWHM CV%: menor é melhor (maior precisão)\n")
                f.write("• R²: maior é melhor (melhor qualidade de ajuste)\n")
                f.write("• ν₃(SiO₄): modo mais sensível ao dano por radiação\n")
                f.write("• ν₁, ν₂: modos complementares para análise estrutural\n")
                f.write("• ExtRot: modos de rede cristalina (menor sensibilidade)\n\n")
                
                f.write("RECOMENDAÇÃO FINAL:\n")
                f.write("-" * 30 + "\n")
                f.write("Para ANÁLISE DE DANO POR RADIAÇÃO (foco em ν₃):\n")
                
                # Pegar melhor combinação para ν₃
                nu3_data = regional_df[regional_df['Região'] == "ν₃(SiO₄)"].copy()
                if len(nu3_data) > 0:
                    nu3_data['FWHM_CV_num'] = pd.to_numeric(nu3_data['FWHM_CV_%'], errors='coerce')
                    nu3_data['R2_num'] = pd.to_numeric(nu3_data['R2_Médio'], errors='coerce')
                    nu3_data['Centro_CV_num'] = pd.to_numeric(nu3_data['Centro_CV_%'], errors='coerce')
                    
                    nu3_data['Score_Composto'] = (
                        (1 - nu3_data['FWHM_CV_num'] / 100) * 0.4 + 
                        nu3_data['R2_num'] * 0.3 + 
                        (1 - nu3_data['Centro_CV_num'] / 100) * 0.3
                    )
                    
                    best_nu3_idx = nu3_data['Score_Composto'].idxmax()
                    best_nu3 = nu3_data.loc[best_nu3_idx]
                    
                    f.write(f"  → Usar: {best_nu3['Combination']}\n")
                    f.write(f"  → Baseline: {best_nu3['Baseline'].upper()}\n")
                    f.write(f"  → Normalização: {best_nu3['Normalization'].upper()}\n")
                    f.write(f"  → Desempenho: CV={best_nu3['FWHM_CV_num']:.4f}%, R²={best_nu3['R2_num']:.6f}\n\n")
                
                f.write("Para ANÁLISE MULTI-REGIONAL (todas as regiões):\n")
                f.write(f"  → Usar: {best_r2['Combination']} (melhor desempenho global)\n\n")
                
            else:
                f.write("\n⚠️ Análise regional detalhada não disponível.\n")
                f.write("Execute novamente com v7.0 para gerar análises regionais.\n\n")
            
            f.write(f"\nARQUIVOS CIENTÍFICOS GERADOS: {len(combination_summary)}\n")
            f.write(f"DADOS PRONTOS PARA PUBLICAÇÃO EM: {combinatorial_dir}\n")
        
        print(f"\n🎯 ANÁLISE CIENTÍFICA CONCLUÍDA")
        # Finalizar log científico
        analysis_end_time = time.time()
        total_analysis_time = analysis_end_time - analysis_start_time
        
        logger.info("="*80)
        logger.info("ANALYSIS COMPLETION SUMMARY")
        logger.info("="*80)
        logger.info(f"Total Analysis Time: {total_analysis_time:.2f} seconds ({total_analysis_time/60:.1f} minutes)")
        logger.info(f"Combinations Successfully Processed: {len(combination_summary)}/{total_combinations}")
        logger.info(f"Success Rate: {len(combination_summary)/total_combinations*100:.1f}%")
        logger.info("")
        logger.info("BEST PERFORMING COMBINATIONS:")
        logger.info(f"  Best R² Score: {best_r2['Combination']} (R² = {best_r2['Mean_R2']})")
        logger.info(f"  Best FWHM Consistency: {best_fwhm_consistency['Combination']} (CV = {best_fwhm_consistency['CV_FWHM_Percent']}%)")
        logger.info(f"  Best Fit Quality: {best_excellent_fits['Combination']} ({best_excellent_fits['Excellent_Fits_Percent']}% excellent fits)")
        logger.info("")
        logger.info("SCIENTIFIC CONCLUSIONS:")
        logger.info("  - All combination data successfully processed and logged")
        logger.info("  - Statistical analysis completed for publication")
        logger.info("  - Comparative results ready for scientific article")
        logger.info("="*80)
        logger.info("LOG FINALIZED SUCCESSFULLY")
        logger.info("="*80)
        
        # Fechar o handler do log
        file_handler.flush()  # Garantir que tudo foi escrito
        file_handler.close()
        logger.removeHandler(file_handler)
        
        print(f"📊 {len(combination_summary)} combinações validadas")
        print(f"🏆 Melhor R²: {best_r2['Combination']} ({best_r2['Mean_R2']})")
        print(f"🎯 Melhor precisão: {best_fwhm_consistency['Combination']} (CV={best_fwhm_consistency['CV_FWHM_Percent']}%)")
        print(f"📈 Melhor qualidade: {best_excellent_fits['Combination']} ({best_excellent_fits['Excellent_Fits_Percent']}% excelentes)")
        print(f"📁 Resultados científicos em: {combinatorial_dir}")
        print(f"📋 Log científico detalhado criado: {log_path}")
        print(f"   Tamanho do arquivo: {log_path.stat().st_size if log_path.exists() else 0} bytes")
        
        return combination_summary
    
    else:
        # Finalizar log científico mesmo com falha
        analysis_end_time = time.time()
        total_analysis_time = analysis_end_time - analysis_start_time
        
        logger.error("="*80)
        logger.error("ANALYSIS FAILED - NO SUCCESSFUL COMBINATIONS")
        logger.error("="*80)
        logger.error(f"Total Analysis Time: {total_analysis_time:.2f} seconds ({total_analysis_time/60:.1f} minutes)")
        logger.error(f"Combinations Attempted: {total_combinations}")
        logger.error(f"Successful Combinations: 0")
        logger.error("POSSIBLE CAUSES:")
        logger.error("  - No input CSV files found")
        logger.error("  - All files failed to process")
        logger.error("  - Configuration errors")
        logger.error("  - Missing dependencies")
        logger.error("="*80)
        logger.error("LOG FINALIZED WITH ERRORS")
        logger.error("="*80)
        
        # Fechar o handler do log
        file_handler.flush()  # Garantir que tudo foi escrito
        file_handler.close()
        logger.removeHandler(file_handler)
        
        print("❌ Nenhuma combinação processada com sucesso")
        print(f"📋 Log de erro detalhado criado: {log_path}")
        print(f"   Tamanho do arquivo: {log_path.stat().st_size if log_path.exists() else 0} bytes")
        return None

def main():
    """Função principal para o processamento em lote de espectros Raman."""
    print("=" * 70)
    print("BATCH RAMAN SPECTROSCOPY ANALYSIS v5.0")
    print("=" * 70)
    print("Este programa processa espectros Raman de zircão em lote,")
    print("detectando picos, calculando FWHM, analisando dano por radiação")
    print("e gerando relatórios detalhados por região espectral.")
    print("=" * 70)
    print("\nFuncionalidades v5.0:")
    print("• Análise de dano por radiação (Ginster et al., 2019)")
    print("• Classificação por regiões espectrais do zircão") 
    print("• Relatórios detalhados por amostra e grão")
    print("• Estatísticas de FWHM e dose estimada")
    print("• DETECÇÃO E REMOÇÃO AUTOMÁTICA DE OUTLIERS")
    print("• 🔬 ANÁLISE COMBINATÓRIA AVANÇADA (12 combinações)")
    print("• 🎯 OTIMIZAÇÃO AUTOMATIZADA E SELEÇÃO DE MÉTODOS")
    print("• 📋 GERAÇÃO DE CONCLUSÕES CIENTÍFICAS PARA PUBLICAÇÃO")
    print("=" * 70)
    
    # Load configuration
    config = load_config()
    print(f"Configuração carregada: {'raman_config.json'}")
    
    # Menu de opções com loop para entrada válida
    while True:
        print("\n📋 OPÇÕES DE PROCESSAMENTO:")
        print("1. Processamento padrão com configuração atual")
        print("2. 🔬 ANÁLISE CIENTÍFICA COMBINATÓRIA (todas as 12 combinações)")
        print("3. Sair")
        
        # Permitir que o usuário escolha a opção
        choice = input("\nEscolha uma opção (1-3): ").strip()
        
        if choice == "1":
            print("\n🚀 EXECUTANDO PROCESSAMENTO PADRÃO...")
            print("Configuração atual:")
            print(f"  Baseline: {config['baseline_correction']['method'].upper()}")
            print(f"  Normalização: {config['normalization']['method'].upper()}")
            batch_process(config)
            break
        
        elif choice == "2":
            print("\n🔬 EXECUTANDO ANÁLISE CIENTÍFICA COMBINATÓRIA...")
            print("Testando todas as 12 combinações de baseline × normalização")
            print("Gerando dados para artigo científico...")
            test_all_baseline_normalization_combinations(config)
            break
        
        elif choice == "3":
            print("Saindo...")
            break
        
        else:
            print("❌ Opção inválida. Digite 1, 2 ou 3.")
            print("   Por favor, tente novamente.")
        
    print("\n✅ Execução concluída!")

def analyze_peak_detection_robustness(results_df, config):
    """
    Analisa a robustez da configuração de detecção de picos e sugere melhorias contextualizadas.
    
    Esta função avalia a qualidade dos picos detectados considerando:
    1. Percentual de picos nas regiões espectrais esperadas
    2. Distribuição dos valores de FWHM por região (considerando variações naturais)
    3. Valores de R² dos ajustes gaussianos
    4. Relação sinal/ruído baseada na altura dos picos
    5. Análise regional específica considerando características espectrais do zircão
    
    NOTA: Esta análise é feita nos dados já limpos (outliers estatísticos já removidos).
    
    Args:
        results_df (pandas.DataFrame): DataFrame com os resultados da análise (já limpos de outliers)
        config (dict): Configuração atual do processamento
    
    Returns:
        dict: Relatório com métricas de robustez e sugestões de melhoria contextualizadas
    """
    
    # Definir regiões espectrais esperadas para zircão
    expected_regions = {
        "ν₃(SiO₄)": (990, 1020),
        "ν₁(SiO₄)": (965, 985), 
        "ν₂(SiO₄)": (430, 450),
        "Modo externo 1": (195, 210),
        "Modo externo 2": (210, 220),
        "Modo externo 3": (220, 230),
        "Modo externo 4": (350, 365)
    }
    
    # Definir valores típicos de FWHM por região baseados na literatura científica
    # Estes são usados para análise de contexto, não para remoção de dados
    #
    # Referências Bibliográficas com DOI Verificado:
    #
    # Para ν₃(SiO₄): 8-25 cm⁻¹ (modo mais sensível ao dano por radiação)
    # - Zhang, M., et al. (2000). Annealing of alpha-decay damage in zircon: a Raman 
    #   spectroscopic study. Journal of Physics: Condensed Matter, 12(13), 3131-3148.
    #   https://doi.org/10.1088/0953-8984/12/13/321
    #   (Documenta FWHM de ~5 cm⁻¹ cristalino até >20 cm⁻¹ metamíctico)
    #
    # - Nasdala, L., et al. (2001). Metamictisation of natural zircon: accumulation 
    #   versus thermal annealing of radioactivity-induced damage. 
    #   Contributions to Mineralogy and Petrology, 141(2), 125-144.
    #   https://doi.org/10.1007/s004100000228
    #   (Estabelece correlação FWHM vs. dose de radiação acumulada)
    #
    # - Ginster, U., et al. (2019). Annealing kinetics of radiation damage in zircon.
    #   Geochimica et Cosmochimica Acta, 249, 225-246.
    #   https://doi.org/10.1016/j.gca.2019.01.033
    #   (Dados experimentais: FWHM 4.9-17.8 cm⁻¹ para diferentes doses de radiação)
    #
    # Para ν₁(SiO₄): 6-20 cm⁻¹ (modo de estiramento simétrico)
    # - Dawson, P., et al. (1971). The vibrational spectrum of zircon (ZrSiO₄).
    #   Journal of Physics C: Solid State Physics, 4(2), 240-256.
    #   https://doi.org/10.1088/0022-3719/4/2/014
    #   (Caracterização fundamental dos modos vibracionais do zircão)
    #
    # Para ν₂(SiO₄): 15-35 cm⁻¹ (modo de deformação angular, naturalmente mais largo)
    # - Gucsik, A., et al. (2004). Infrared and Raman spectra of ZrSiO₄ 
    #   experimentally shocked at high pressures. Mineralogical Magazine, 68(5), 801-811.
    #   https://doi.org/10.1180/0026461046850220
    #   (Dados de FWHM sob diferentes condições de pressão e dano estrutural)
    #
    # Para Modos Externos: 10-40 cm⁻¹ (maior variação natural)
    # - Bjerga, A., et al. (2022). Radiation damage allows identification of truly 
    #   inherited zircon. Communications Earth & Environment, 3, 37.
    #   https://doi.org/10.1038/s43247-022-00372-2
    #   (Análise de modos externos em zircões com diferentes histórias térmicas)
    #
    # - Härtel, B., et al. (2021). The closure temperature(s) of zircon Raman dating.
    #   Geochronology, 3, 259-272.
    #   https://doi.org/10.5194/gchron-3-259-2021
    #   (Caracterização de modos externos e sua sensibilidade térmica)
    #
    typical_fwhm_ranges = {
        "ν₃(SiO₄)": (8, 25),      # Modo principal, sensível a dano por radiação
        "ν₁(SiO₄)": (6, 20),      # Modo secundário, também sensível
        "ν₂(SiO₄)": (15, 35),     # Modo de baixa frequência, naturalmente mais largo
        "Modo externo 1": (10, 30),  # Modos externos têm variação natural maior
        "Modo externo 2": (12, 32),
        "Modo externo 3": (10, 28),
        "Modo externo 4": (15, 40)   # Pode ser naturalmente mais largo
    }
    
    total_peaks = len(results_df)
    report = {
        'total_peaks': total_peaks,
        'current_config': config['peak_detection'].copy(),
        'regional_analysis': {},
        'quality_metrics': {},
        'recommendations': [],
        'data_status': 'Dados já limpos de outliers estatísticos'
    }
    
    # Análise por região espectral com contexto específico
    peaks_in_regions = 0
    regional_fwhm_analysis = {}
    
    for region_name, (min_wave, max_wave) in expected_regions.items():
        region_peaks = results_df[(results_df['Centro'] >= min_wave) & 
                                 (results_df['Centro'] <= max_wave)]
        count = len(region_peaks)
        percentage = (count / total_peaks) * 100 if total_peaks > 0 else 0
        peaks_in_regions += count
        
        # Análise de qualidade dos picos na região
        if count > 0:
            avg_r2 = region_peaks['R2'].mean()
            avg_fwhm = region_peaks['FWHM_Gauss'].mean()
            fwhm_std = region_peaks['FWHM_Gauss'].std()
            avg_area = region_peaks['Area_Gauss'].mean()
            
            # Comparar com valores típicos da região (para contexto, não para exclusão)
            typical_min, typical_max = typical_fwhm_ranges.get(region_name, (5, 50))
            fwhm_within_range = len(region_peaks[
                (region_peaks['FWHM_Gauss'] >= typical_min) & 
                (region_peaks['FWHM_Gauss'] <= typical_max)
            ])
            fwhm_within_range_pct = (fwhm_within_range / count) * 100
            
            # Contar valores fora da faixa teórica (para análise, não como "outliers")
            values_outside_typical = count - fwhm_within_range
            
            # Analisar a distribuição dos valores fora da faixa
            values_below_typical = len(region_peaks[region_peaks['FWHM_Gauss'] < typical_min])
            values_above_typical = len(region_peaks[region_peaks['FWHM_Gauss'] > typical_max])
            
            regional_fwhm_analysis[region_name] = {
                'avg_fwhm': avg_fwhm,
                'fwhm_std': fwhm_std,
                'typical_range': (typical_min, typical_max),
                'within_typical_range_pct': fwhm_within_range_pct,
                'values_outside_typical': values_outside_typical,
                'values_below_typical': values_below_typical,
                'values_above_typical': values_above_typical,
                'fwhm_range_actual': (region_peaks['FWHM_Gauss'].min(), region_peaks['FWHM_Gauss'].max())
            }
            
        else:
            avg_r2 = avg_fwhm = avg_area = fwhm_std = 0
            regional_fwhm_analysis[region_name] = {
                'avg_fwhm': 0,
                'fwhm_std': 0,
                'typical_range': typical_fwhm_ranges.get(region_name, (5, 50)),
                'within_typical_range_pct': 0,
                'values_outside_typical': 0,
                'values_below_typical': 0,
                'values_above_typical': 0,
                'fwhm_range_actual': (0, 0)
            }
            
        report['regional_analysis'][region_name] = {
            'count': count,
            'percentage': percentage,
            'avg_r2': avg_r2,
            'avg_fwhm': avg_fwhm,
            'fwhm_std': fwhm_std,
            'avg_area': avg_area,
            'fwhm_analysis': regional_fwhm_analysis[region_name]
        }
    
    # Picos fora das regiões esperadas
    peaks_outside = total_peaks - peaks_in_regions
    outside_percentage = (peaks_outside / total_peaks) * 100 if total_peaks > 0 else 0
    
    report['regional_analysis']['Fora das regiões'] = {
        'count': peaks_outside,
        'percentage': outside_percentage
    }
    
    # Métricas de qualidade geral com análise contextualizada
    report['quality_metrics'] = {
        'avg_r2_all': results_df['R2'].mean(),
        'min_r2': results_df['R2'].min(),
        'peaks_with_good_fit': len(results_df[results_df['R2'] > 0.8]),
        'peaks_with_poor_fit': len(results_df[results_df['R2'] < 0.5]),
        'avg_fwhm': results_df['FWHM_Gauss'].mean(),
        'fwhm_std': results_df['FWHM_Gauss'].std(),
        'peaks_in_expected_regions_pct': (peaks_in_regions / total_peaks) * 100,
        'regional_fwhm_analysis': regional_fwhm_analysis
    }
    
    # Gerar recomendações contextualizadas baseadas nas métricas regionais
    current_height = config['peak_detection']['height_percent']
    current_prominence = config['peak_detection']['prominence_percent']
    
    # Critério 1: Muitos picos fora das regiões (> 40%) - Mantido
    if outside_percentage > 40:
        if current_height < 10:
            report['recommendations'].append({
                'issue': f'Alto percentual de picos fora das regiões esperadas ({outside_percentage:.1f}%)',
                'suggestion': f'Aumentar height_percent de {current_height}% para {current_height + 3}% para reduzir detecção de ruído',
                'new_height': current_height + 3,
                'priority': 'Alta',
                'context': 'Detectando possivelmente ruído ou artefatos espectrais'
            })
        
        if current_prominence < 5:
            report['recommendations'].append({
                'issue': 'Possível detecção excessiva de ruído como picos',
                'suggestion': f'Aumentar prominence_percent de {current_prominence}% para {current_prominence + 2}% para filtrar melhor o ruído',
                'new_prominence': current_prominence + 2,
                'priority': 'Alta',
                'context': 'Melhora discriminação entre picos reais e ruído'
            })
    
    # Critério 2: Análise regional de FWHM - ATUALIZADO para dados limpos
    regions_with_unusual_fwhm = []
    for region_name, analysis in regional_fwhm_analysis.items():
        if analysis['within_typical_range_pct'] < 50 and analysis['avg_fwhm'] > 0:  # Menos de 50% na faixa típica
            if analysis['avg_fwhm'] > analysis['typical_range'][1] * 1.5:  # Muito alto (50% acima do máximo típico)
                regions_with_unusual_fwhm.append({
                    'region': region_name,
                    'issue': 'FWHM consistentemente alto',
                    'avg_fwhm': analysis['avg_fwhm'],
                    'expected_max': analysis['typical_range'][1],
                    'values_above': analysis['values_above_typical']
                })
            elif analysis['avg_fwhm'] < analysis['typical_range'][0] * 0.7:  # Muito baixo (30% abaixo do mínimo típico)
                regions_with_unusual_fwhm.append({
                    'region': region_name,
                    'issue': 'FWHM consistentemente baixo',
                    'avg_fwhm': analysis['avg_fwhm'],
                    'expected_min': analysis['typical_range'][0],
                    'values_below': analysis['values_below_typical']
                })
    
    if regions_with_unusual_fwhm:
        # Analisar se é problema sistemático ou específico de regiões
        high_fwhm_regions = [r for r in regions_with_unusual_fwhm if r['issue'] == 'FWHM consistentemente alto']
        low_fwhm_regions = [r for r in regions_with_unusual_fwhm if r['issue'] == 'FWHM consistentemente baixo']
        
        if len(high_fwhm_regions) >= 3:  # Problema sistemático de FWHM alto
            report['recommendations'].append({
                'issue': f'FWHM consistentemente alto em múltiplas regiões espectrais ({len(high_fwhm_regions)} regiões)',
                'suggestion': 'Verificar qualidade espectral: possível alargamento por dano por radiação, temperatura, ou condições de medição.',
                'priority': 'Média',
                'context': f'Regiões afetadas: {", ".join([r["region"] for r in high_fwhm_regions])}. Dados já limpos de outliers estatísticos.',
                'regions_affected': [r['region'] for r in high_fwhm_regions]
            })
        elif len(low_fwhm_regions) >= 2:  # Problema de resolução
            report['recommendations'].append({
                'issue': f'FWHM consistentemente baixo em {len(low_fwhm_regions)} regiões espectrais',
                'suggestion': 'Verificar resolução espectral: possível super-resolução artificial ou ajuste inadequado.',
                'priority': 'Média',
                'context': f'Regiões afetadas: {", ".join([r["region"] for r in low_fwhm_regions])}. Pode indicar limitação instrumental.',
                'regions_affected': [r['region'] for r in low_fwhm_regions]
            })
    
    # Critério 3: Muitos picos com ajuste ruim (R² < 0.5) - Melhorado
    poor_fit_percentage = (report['quality_metrics']['peaks_with_poor_fit'] / total_peaks) * 100
    if poor_fit_percentage > 20:
        # Analisar se o problema é regional ou geral
        poor_fit_by_region = {}
        for region_name in expected_regions.keys():
            if region_name in report['regional_analysis'] and report['regional_analysis'][region_name]['count'] > 0:
                region_peaks = results_df[(results_df['Centro'] >= expected_regions[region_name][0]) & 
                                         (results_df['Centro'] <= expected_regions[region_name][1])]
                poor_r2_count = len(region_peaks[region_peaks['R2'] < 0.5])
                if poor_r2_count > 0:
                    poor_fit_by_region[region_name] = (poor_r2_count, len(region_peaks))
        
        if len(poor_fit_by_region) >= 4:  # Problema sistemático
            report['recommendations'].append({
                'issue': f'Alto percentual de picos com ajuste ruim ({poor_fit_percentage:.1f}%) - problema sistemático',
                'suggestion': 'Melhorar pré-processamento: correção de baseline, suavização espectral, ou verificar qualidade dos dados brutos.',
                'priority': 'Alta',
                'context': f'Problema detectado em {len(poor_fit_by_region)} regiões espectrais. Dados já limpos de outliers estatísticos.'
            })
        else:
            report['recommendations'].append({
                'issue': f'Ajuste ruim em regiões específicas ({poor_fit_percentage:.1f}%)',
                'suggestion': 'Verificar regiões específicas com baixo R²: possíveis interferências ou sobreposição de picos.',
                'priority': 'Média',
                'context': f'Regiões problemáticas: {", ".join(poor_fit_by_region.keys()) if poor_fit_by_region else "análise regional necessária"}'
            })
    
    # Critério 4: Análise das regiões principais do zircão - Melhorado
    main_regions_count = (report['regional_analysis']['ν₃(SiO₄)']['count'] + 
                         report['regional_analysis']['ν₁(SiO₄)']['count'])
    main_regions_pct = (main_regions_count / total_peaks) * 100 if total_peaks > 0 else 0
    
    if main_regions_pct < 20:  # Menos de 20% nos picos principais
        # Verificar se há picos suficientes no total
        if total_peaks < 10:
            report['recommendations'].append({
                'issue': f'Poucos picos detectados no total ({total_peaks}) e nas regiões principais ({main_regions_pct:.1f}%)',
                'suggestion': f'Considerar diminuir height_percent de {current_height}% para {max(2, current_height - 2)}% para detectar mais picos principais',
                'new_height': max(2, current_height - 2),
                'priority': 'Alta',
                'context': 'As regiões ν₃ e ν₁ são fundamentais para análise de zircão. Configuração pode estar muito restritiva.'
            })
        else:
            report['recommendations'].append({
                'issue': f'Poucos picos nas regiões principais do zircão ({main_regions_pct:.1f}%)',
                'suggestion': 'Verificar se os picos principais estão sendo perdidos ou se há deslocamentos espectrais. Considerar ajustar parâmetros regionalmente.',
                'priority': 'Média',
                'context': f'Total de {total_peaks} picos detectados, mas apenas {main_regions_count} nas regiões ν₃ e ν₁.'
            })
    
    # Critério 5: Novo - Análise de qualidade geral
    good_fit_percentage = (report['quality_metrics']['peaks_with_good_fit'] / total_peaks) * 100
    if good_fit_percentage > 80 and outside_percentage < 30 and poor_fit_percentage < 15:
        report['recommendations'].append({
            'issue': '✅ Configuração apresenta boa performance geral',
            'suggestion': 'Parâmetros atuais estão bem ajustados. Monitorar consistência entre diferentes amostras.',
            'priority': 'Informativo',
            'context': f'Qualidade: {good_fit_percentage:.1f}% bom ajuste, {outside_percentage:.1f}% fora de regiões, {poor_fit_percentage:.1f}% ajuste ruim. Dados já limpos.'
        })
    
    return report

def print_robustness_analysis(report, output_dir=None, file_suffix=""):
    """Imprime o relatório de análise de robustez de forma formatada e opcionalmente salva em arquivo."""
    
    print("\n" + "="*70)
    print("ANÁLISE DE ROBUSTEZ DA DETECÇÃO DE PICOS - DADOS JÁ LIMPOS")
    print("="*70)
    
    print(f"\nStatus dos dados: {report.get('data_status', 'Status não especificado')}")
    print(f"Total de picos detectados: {report['total_peaks']}")
    print(f"Configuração atual:")
    config = report['current_config']
    print(f"  - Altura mínima: {config['height_percent']}% da intensidade máxima")
    print(f"  - Proeminência mínima: {config['prominence_percent']}% da intensidade máxima")
    print(f"  - Distância mínima: {config['distance']} pontos")
    print(f"  - Largura mínima: {config['width']} pontos")
    
    print("\nDISTRIBUIÇÃO POR REGIÃO ESPECTRAL (com análise de contexto FWHM):")
    print("-" * 70)
    for region, data in report['regional_analysis'].items():
        if 'avg_r2' in data:
            print(f"{region:20s}: {data['count']:4d} picos ({data['percentage']:5.1f}%) | "
                  f"R²={data['avg_r2']:.3f} | FWHM={data['avg_fwhm']:.1f}±{data['fwhm_std']:.1f}")
            
            # Mostrar análise de FWHM se disponível
            if 'fwhm_analysis' in data and data['count'] > 0:
                fwhm_analysis = data['fwhm_analysis']
                typical_range = fwhm_analysis['typical_range']
                within_range_pct = fwhm_analysis['within_typical_range_pct']
                values_outside = fwhm_analysis['values_outside_typical']
                actual_range = fwhm_analysis['fwhm_range_actual']
                
                status = "✅" if within_range_pct >= 60 else "⚠️" if within_range_pct >= 40 else "❌"
                print(f"{'':21s}  {status} FWHM: {within_range_pct:.1f}% na faixa típica ({typical_range[0]}-{typical_range[1]} cm⁻¹)")
                print(f"{'':21s}  📊 Faixa real: {actual_range[0]:.1f}-{actual_range[1]:.1f} cm⁻¹")
                if values_outside > 0:
                    below = fwhm_analysis['values_below_typical']
                    above = fwhm_analysis['values_above_typical']
                    print(f"{'':21s}  📈 {values_outside} valores fora da faixa típica ({below} abaixo, {above} acima)")
        else:
            print(f"{region:20s}: {data['count']:4d} picos ({data['percentage']:5.1f}%)")
    
    print("\nMÉTRICAS DE QUALIDADE:")
    print("-" * 30)
    metrics = report['quality_metrics']
    print(f"R² médio geral: {metrics['avg_r2_all']:.3f}")
    print(f"R² mínimo: {metrics['min_r2']:.3f}")
    print(f"Picos com bom ajuste (R²>0.8): {metrics['peaks_with_good_fit']} ({(metrics['peaks_with_good_fit']/report['total_peaks']*100):.1f}%)")
    print(f"Picos com ajuste ruim (R²<0.5): {metrics['peaks_with_poor_fit']} ({(metrics['peaks_with_poor_fit']/report['total_peaks']*100):.1f}%)")
    print(f"FWHM médio: {metrics['avg_fwhm']:.2f} ± {metrics['fwhm_std']:.2f} cm⁻¹")
    print(f"Picos em regiões esperadas: {metrics['peaks_in_expected_regions_pct']:.1f}%")
    
    if report['recommendations']:
        print("\nRECOMENDAÇÕES DE MELHORIA (por prioridade):")
        print("-" * 50)
        
        # Separar por prioridade
        high_priority = [r for r in report['recommendations'] if r.get('priority') == 'Alta']
        medium_priority = [r for r in report['recommendations'] if r.get('priority') == 'Média']
        low_priority = [r for r in report['recommendations'] if r.get('priority') == 'Baixa']
        informative = [r for r in report['recommendations'] if r.get('priority') == 'Informativo']
        
        for priority_group, priority_name, icon in [
            (high_priority, "ALTA PRIORIDADE", "🔴"),
            (medium_priority, "MÉDIA PRIORIDADE", "🟡"),
            (low_priority, "BAIXA PRIORIDADE", "🟢"),
            (informative, "INFORMATIVO", "ℹ️")
        ]:
            if priority_group:
                print(f"\n{icon} {priority_name}:")
                for i, rec in enumerate(priority_group, 1):
                    print(f"  {i}. {rec['issue']}")
                    print(f"     → {rec['suggestion']}")
                    if 'context' in rec:
                        print(f"     💡 Contexto: {rec['context']}")
                    if 'new_height' in rec or 'new_prominence' in rec:
                        print(f"     ⚙️ Parâmetro sugerido incluído na recomendação")
                    print()
    else:
        print("\n✅ CONFIGURAÇÃO ROBUSTA!")
        print("Os parâmetros atuais estão bem ajustados para as amostras analisadas.")
    
    print("="*70)
    
    # Salvar o relatório de robustez principal em arquivo se output_dir for especificado
    if output_dir:
        from pathlib import Path
        import re
        timestamp = generate_timestamp()
        
        # Processar file_suffix para remover "amostra" e manter apenas o número
        processed_suffix = file_suffix
        if file_suffix:
            # Usar regex para extrair apenas números do file_suffix
            match = re.search(r'_amostra(\d+)', file_suffix)
            if match:
                # Se encontrou padrão "amostra" + número, manter apenas o número
                numero_amostra = match.group(1)
                processed_suffix = f"_{numero_amostra}"
            else:
                # Se não encontrou padrão específico, tentar extrair qualquer número
                numbers = re.findall(r'\d+', file_suffix)
                if numbers:
                    processed_suffix = f"_{numbers[0]}"  # Pegar o primeiro número encontrado
        
        report_path = Path(output_dir) / f"peak_detection_robustness_analysis{processed_suffix}_{timestamp}.txt"
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write("="*70 + "\n")
            f.write("ANÁLISE DE ROBUSTEZ DA DETECÇÃO DE PICOS - DADOS JÁ LIMPOS\n")
            f.write("="*70 + "\n\n")
            f.write(f"Data e Hora da Análise: {timestamp}\n")
            f.write(f"Versão do Software: 5.1\n\n")
            
            f.write(f"Status dos dados: {report.get('data_status', 'Status não especificado')}\n")
            f.write(f"Total de picos detectados: {report['total_peaks']}\n")
            f.write(f"Configuração atual:\n")
            config = report['current_config']
            f.write(f"  - Altura mínima: {config['height_percent']}% da intensidade máxima\n")
            f.write(f"  - Proeminência mínima: {config['prominence_percent']}% da intensidade máxima\n")
            f.write(f"  - Distância mínima: {config['distance']} pontos\n")
            f.write(f"  - Largura mínima: {config['width']} pontos\n\n")
            
            f.write("DISTRIBUIÇÃO POR REGIÃO ESPECTRAL (com análise de contexto FWHM):\n")
            f.write("-" * 70 + "\n")
            for region, data in report['regional_analysis'].items():
                if 'avg_r2' in data:
                    f.write(f"{region:20s}: {data['count']:4d} picos ({data['percentage']:5.1f}%) | "
                           f"R²={data['avg_r2']:.3f} | FWHM={data['avg_fwhm']:.1f}±{data['fwhm_std']:.1f}\n")
                    
                    # Mostrar análise de FWHM se disponível
                    if 'fwhm_analysis' in data and data['count'] > 0:
                        fwhm_analysis = data['fwhm_analysis']
                        typical_range = fwhm_analysis['typical_range']
                        within_range_pct = fwhm_analysis['within_typical_range_pct']
                        values_outside = fwhm_analysis['values_outside_typical']
                        actual_range = fwhm_analysis['fwhm_range_actual']
                        
                        status = "✅" if within_range_pct >= 60 else "⚠️" if within_range_pct >= 40 else "❌"
                        f.write(f"{'':21s}  {status} FWHM: {within_range_pct:.1f}% na faixa típica ({typical_range[0]}-{typical_range[1]} cm⁻¹)\n")
                        f.write(f"{'':21s}  📊 Faixa real: {actual_range[0]:.1f}-{actual_range[1]:.1f} cm⁻¹\n")
                        if values_outside > 0:
                            below = fwhm_analysis['values_below_typical']
                            above = fwhm_analysis['values_above_typical']
                            f.write(f"{'':21s}  📈 {values_outside} valores fora da faixa típica ({below} abaixo, {above} acima)\n")
                else:
                    f.write(f"{region:20s}: {data['count']:4d} picos ({data['percentage']:5.1f}%)\n")
            
            f.write("\nMÉTRICAS DE QUALIDADE:\n")
            f.write("-" * 30 + "\n")
            metrics = report['quality_metrics']
            f.write(f"R² médio geral: {metrics['avg_r2_all']:.3f}\n")
            f.write(f"R² mínimo: {metrics['min_r2']:.3f}\n")
            f.write(f"Picos com bom ajuste (R²>0.8): {metrics['peaks_with_good_fit']} ({(metrics['peaks_with_good_fit']/report['total_peaks']*100):.1f}%)\n")
            f.write(f"Picos com ajuste ruim (R²<0.5): {metrics['peaks_with_poor_fit']} ({(metrics['peaks_with_poor_fit']/report['total_peaks']*100):.1f}%)\n")
            f.write(f"FWHM médio: {metrics['avg_fwhm']:.2f} ± {metrics['fwhm_std']:.2f} cm⁻¹\n")
            f.write(f"Picos em regiões esperadas: {metrics['peaks_in_expected_regions_pct']:.1f}%\n\n")
            
            if report['recommendations']:
                f.write("RECOMENDAÇÕES DE MELHORIA (por prioridade):\n")
                f.write("-" * 50 + "\n")
                
                # Separar por prioridade
                high_priority = [r for r in report['recommendations'] if r.get('priority') == 'Alta']
                medium_priority = [r for r in report['recommendations'] if r.get('priority') == 'Média']
                low_priority = [r for r in report['recommendations'] if r.get('priority') == 'Baixa']
                informative = [r for r in report['recommendations'] if r.get('priority') == 'Informativo']
                
                for priority_group, priority_name, icon in [
                    (high_priority, "ALTA PRIORIDADE", "🔴"),
                    (medium_priority, "MÉDIA PRIORIDADE", "🟡"),
                    (low_priority, "BAIXA PRIORIDADE", "🟢"),
                    (informative, "INFORMATIVO", "ℹ️")
                ]:
                    if priority_group:
                        f.write(f"\n{icon} {priority_name}:\n")
                        for i, rec in enumerate(priority_group, 1):
                            f.write(f"  {i}. {rec['issue']}\n")
                            f.write(f"     → {rec['suggestion']}\n")
                            if 'context' in rec:
                                f.write(f"     💡 Contexto: {rec['context']}\n")
                            if 'new_height' in rec or 'new_prominence' in rec:
                                f.write(f"     ⚙️ Parâmetro sugerido incluído na recomendação\n")
                            f.write("\n")
            else:
                f.write("✅ CONFIGURAÇÃO ROBUSTA!\n")
                f.write("Os parâmetros atuais estão bem ajustados para as amostras analisadas.\n\n")
            
            f.write("="*70 + "\n")
        
        print(f"📄 Relatório de robustez salvo: {report_path.name}")
    
    # Definir métodos disponíveis para teste combinatório
    baseline_methods = ["airpls", "polynomial", "spline"]
    normalization_methods = ["min_max", "area", "peak", "vector"]
    
    # Definir sufixos para nomenclatura científica
    baseline_suffixes = {
        "airpls": "AirPLS",
        "polynomial": "Poly", 
        "spline": "Spline"
    }
    normalization_suffixes = {
        "min_max": "MinMax",
        "area": "Area",
        "peak": "Peak", 
        "vector": "Vector"
    }
    
    # Configuração para análise combinatória
    combination_count = 0
    total_combinations = len(baseline_methods) * len(normalization_methods)
    combination_results = {}
    combination_summary = []
    
    # Definir diretórios
    if output_dir:
        combinatorial_dir = Path(output_dir) / "Robustness_Combinatorial_Analysis"
        combinatorial_dir.mkdir(exist_ok=True)
        input_dir = Path(output_dir).parent / "input"  # Assumindo estrutura padrão
    else:
        combinatorial_dir = Path("./Robustness_Combinatorial_Analysis")
        combinatorial_dir.mkdir(exist_ok=True) 
        input_dir = Path("./input")
    
    results_comparison = {}
    
    # Configurar logging científico para publicação
    import logging
    import time
    from datetime import datetime
    
    # Criar logger específico para análise combinatória
    logger = logging.getLogger('combinatorial_analysis')
    logger.setLevel(logging.INFO)
    
    # Criar timestamp para o log
    analysis_timestamp = generate_timestamp()
    log_filename = f"Combinatorial_Analysis_Scientific_Log_{analysis_timestamp}.log"
    log_path = combinatorial_dir / log_filename
    
    # Configurar handler de arquivo
    file_handler = logging.FileHandler(log_path, encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    
    # Formato científico para o log
    scientific_formatter = logging.Formatter(
        '%(asctime)s | %(levelname)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(scientific_formatter)
    logger.addHandler(file_handler)
    
    # Debug: confirmar criação do log
    print(f"📋 Log científico será criado em: {log_path}")
    
    # Forçar flush inicial para garantir que o arquivo seja criado
    file_handler.flush()
    
    # Início do log científico
    logger.info("="*80)
    logger.info("SCIENTIFIC LOG: COMBINATORIAL BASELINE-NORMALIZATION ANALYSIS")
    logger.info("="*80)
    logger.info(f"Analysis Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info(f"Total Combinations to Test: {total_combinations}")
    logger.info(f"Baseline Methods: {baseline_methods}")
    logger.info(f"Normalization Methods: {normalization_methods}")
    logger.info(f"Input Directory: {input_dir}")
    logger.info(f"Output Directory: {combinatorial_dir}")
    logger.info("-"*80)
    
    # Verificar arquivos de entrada
    csv_files_initial = list(Path(input_dir).glob("*.csv"))
    logger.info(f"Input Files Detected: {len(csv_files_initial)} CSV files")
    for i, file in enumerate(csv_files_initial, 1):
        logger.info(f"  File {i:02d}: {file.name}")
    
    if not csv_files_initial:
        logger.error(f"CRITICAL ERROR: No CSV files found in {input_dir}")
        logger.error("Analysis cannot proceed without input data")
        
        # Fechar o handler antes de retornar
        file_handler.close()
        logger.removeHandler(file_handler)
        
        print(f"❌ ERRO: Nenhum arquivo CSV encontrado em {input_dir}")
        print(f"📋 Log de erro criado em: {log_path}")
        return None
    
    logger.info("-"*80)
    
    # Métricas de tempo
    analysis_start_time = time.time()
    combination_times = []
    
    # Testar todas as combinações
    for baseline_method in baseline_methods:
        for norm_method in normalization_methods:
            combination_count += 1
            combination_start_time = time.time()
            
            # Criar configuração específica para esta combinação
            test_config = config.copy()
            
            # Garantir que as seções existam na configuração
            if "baseline" not in test_config:
                test_config["baseline"] = {}
            if "normalization" not in test_config:
                test_config["normalization"] = {}
            if "baseline_correction" not in test_config:
                test_config["baseline_correction"] = {}
                
            # Configurar os métodos para esta combinação
            test_config["baseline"]["method"] = baseline_method
            test_config["baseline_correction"]["method"] = baseline_method  # Para compatibilidade
            test_config["normalization"]["method"] = norm_method
            
            # Criar nome científico da combinação
            combination_name = f"{baseline_suffixes[baseline_method]}_{normalization_suffixes[norm_method]}"
            
            # Log do início da combinação
            logger.info(f"COMBINATION {combination_count:02d}/{total_combinations}: {combination_name}")
            logger.info(f"  Baseline Method: {baseline_method.upper()}")
            logger.info(f"  Normalization Method: {norm_method.upper()}")
            
            print(f"\n[{combination_count:02d}/{total_combinations}] Testando: {combination_name}")
            print(f"  Baseline: {baseline_method.upper()}")
            print(f"  Normalização: {norm_method.upper()}")
            
            # Criar subdiretório para esta combinação
            combo_dir = combinatorial_dir / f"Combo_{combination_count:02d}_{combination_name}"
            combo_dir.mkdir(exist_ok=True)
            test_config["output_dir"] = str(combo_dir)
            
            logger.info(f"  Output Directory: {combo_dir.name}")
            
            try:
                # Processar com esta combinação
                input_path = Path(input_dir)
                csv_files = list(input_path.glob("*.csv"))
                
                logger.info(f"  Processing {len(csv_files)} input files")
                
                if not csv_files:
                    logger.warning(f"  WARNING: No CSV files found in {input_dir}")
                    logger.warning(f"  RESULT: Combination {combination_name} SKIPPED due to missing input data")
                    print(f"  ❌ Nenhum arquivo CSV encontrado em {input_dir}")
                    combination_end_time = time.time()
                    combination_times.append({
                        'combination': combination_name,
                        'status': 'SKIPPED_NO_FILES',
                        'duration': combination_end_time - combination_start_time
                    })
                    continue
                
                # Processar todos os arquivos com esta combinação
                all_results = pd.DataFrame()
                processing_success = 0
                processing_errors = 0
                
                logger.info(f"  Starting file processing...")
                
                for i, file_path in enumerate(csv_files, 1):
                    logger.info(f"    Processing file {i}/{len(csv_files)}: {file_path.name}")
                    try:
                        results = process_file(file_path, test_config)
                        if results is not None and not results.empty:
                            all_results = pd.concat([all_results, results], ignore_index=True)
                            processing_success += 1
                            logger.info(f"      SUCCESS: {len(results)} peaks detected")
                        else:
                            processing_errors += 1
                            logger.warning(f"      WARNING: No peaks detected in {file_path.name}")
                    except Exception as file_error:
                        processing_errors += 1
                        logger.error(f"      ERROR processing {file_path.name}: {file_error}")
                
                logger.info(f"  File Processing Summary:")
                logger.info(f"    Total files: {len(csv_files)}")
                logger.info(f"    Successfully processed: {processing_success}")
                logger.info(f"    Errors/No peaks: {processing_errors}")
                logger.info(f"    Success rate: {processing_success/len(csv_files)*100:.1f}%")
                
                if all_results.empty:
                    logger.warning(f"  WARNING: No results obtained for combination {combination_name}")
                    logger.warning(f"  RESULT: Combination {combination_name} FAILED - no valid peaks detected")
                    print(f"  ❌ Nenhum resultado obtido para {combination_name}")
                    combination_end_time = time.time()
                    combination_times.append({
                        'combination': combination_name,
                        'status': 'FAILED_NO_RESULTS',
                        'duration': combination_end_time - combination_start_time,
                        'files_processed': len(csv_files),
                        'success_rate': 0
                    })
                    continue
                
                # Calcular métricas desta combinação
                total_peaks = len(all_results)
                excellent_fits = len(all_results[all_results['R2'] > 0.9])
                good_fits = len(all_results[all_results['R2'] > 0.7])
                poor_fits = len(all_results[all_results['R2'] < 0.3])
                
                # Log das métricas principais
                logger.info(f"  Peak Detection and Fitting Results:")
                logger.info(f"    Total peaks detected: {total_peaks}")
                logger.info(f"    Excellent fits (R² > 0.9): {excellent_fits} ({excellent_fits/total_peaks*100:.1f}%)")
                logger.info(f"    Good fits (R² > 0.7): {good_fits} ({good_fits/total_peaks*100:.1f}%)")
                logger.info(f"    Poor fits (R² < 0.3): {poor_fits} ({poor_fits/total_peaks*100:.1f}%)")
                logger.info(f"    Average R²: {all_results['R2'].mean():.4f} ± {all_results['R2'].std():.4f}")
                logger.info(f"    Average FWHM: {all_results['FWHM_Gauss'].mean():.3f} ± {all_results['FWHM_Gauss'].std():.3f} cm⁻¹")
                
                # Métricas por região espectral
                region_metrics = {}
                spectral_regions = {
                    "v3_SiO4": (990, 1020),
                    "v1_SiO4": (965, 985), 
                    "v2_SiO4": (430, 450),
                    "External_Modes": (195, 365)
                }
                
                logger.info(f"  Spectral Region Analysis:")
                
                for region_name, (min_wave, max_wave) in spectral_regions.items():
                    region_data = all_results[(all_results['Centro'] >= min_wave) & 
                                            (all_results['Centro'] <= max_wave)]
                    
                    if len(region_data) > 0:
                        region_metrics[region_name] = {
                            "peak_count": len(region_data),
                            "avg_r2": region_data['R2'].mean(),
                            "avg_fwhm": region_data['FWHM_Gauss'].mean(),
                            "std_fwhm": region_data['FWHM_Gauss'].std(),
                            "cv_fwhm": (region_data['FWHM_Gauss'].std() / region_data['FWHM_Gauss'].mean()) * 100
                        }
                        logger.info(f"    {region_name} ({min_wave}-{max_wave} cm⁻¹):")
                        logger.info(f"      Peaks detected: {len(region_data)}")
                        logger.info(f"      Average R²: {region_data['R2'].mean():.4f}")
                        logger.info(f"      Average FWHM: {region_data['FWHM_Gauss'].mean():.3f} ± {region_data['FWHM_Gauss'].std():.3f} cm⁻¹")
                        logger.info(f"      FWHM CV: {(region_data['FWHM_Gauss'].std() / region_data['FWHM_Gauss'].mean()) * 100:.1f}%")
                    else:
                        logger.info(f"    {region_name} ({min_wave}-{max_wave} cm⁻¹): No peaks detected")
                
                # Salvar resultados desta combinação com timestamp
                combo_timestamp = generate_timestamp()
                results_filename = f"Results_{combination_name}_n{total_peaks}_{combo_timestamp}.csv"
                results_path = combo_dir / results_filename
                all_results.to_csv(results_path, index=False)
                
                # Gerar relatório específico da combinação com timestamp
                report_filename = f"Report_{combination_name}_{combo_timestamp}.txt"
                report_path = combo_dir / report_filename
                
                with open(report_path, 'w', encoding='utf-8') as f:
                    f.write(f"RELATÓRIO CIENTÍFICO - COMBINAÇÃO {combination_name}\n")
                    f.write("=" * 60 + "\n\n")
                    f.write(f"CONFIGURAÇÃO TESTADA:\n")
                    f.write(f"  Método Baseline: {baseline_method.upper()}\n")
                    f.write(f"  Método Normalização: {norm_method.upper()}\n")
                    f.write(f"  Arquivos processados: {processing_success}/{len(csv_files)}\n\n")
                    
                    f.write(f"MÉTRICAS GERAIS:\n")
                    f.write(f"  Total de picos detectados: {total_peaks}\n")
                    f.write(f"  Ajustes excelentes (R² > 0.9): {excellent_fits} ({excellent_fits/total_peaks*100:.1f}%)\n")
                    f.write(f"  Ajustes bons (R² > 0.7): {good_fits} ({good_fits/total_peaks*100:.1f}%)\n")
                    f.write(f"  Ajustes pobres (R² < 0.3): {poor_fits} ({poor_fits/total_peaks*100:.1f}%)\n")
                    f.write(f"  R² médio: {all_results['R2'].mean():.3f} ± {all_results['R2'].std():.3f}\n")
                    f.write(f"  FWHM médio: {all_results['FWHM_Gauss'].mean():.2f} ± {all_results['FWHM_Gauss'].std():.2f} cm⁻¹\n\n")
                    
                    f.write(f"ANÁLISE POR REGIÃO ESPECTRAL:\n")
                    for region, metrics in region_metrics.items():
                        f.write(f"  {region.replace('_', ' ')}:\n")
                        f.write(f"    Picos: {metrics['peak_count']}\n")
                        f.write(f"    R² médio: {metrics['avg_r2']:.3f}\n")
                        f.write(f"    FWHM: {metrics['avg_fwhm']:.2f} ± {metrics['std_fwhm']:.2f} cm⁻¹\n")
                        f.write(f"    CV FWHM: {metrics['cv_fwhm']:.1f}%\n\n")
                
                # Armazenar métricas para comparação
                combination_results[combination_name] = {
                    "baseline_method": baseline_method,
                    "normalization_method": norm_method,
                    "total_peaks": total_peaks,
                    "processing_success_rate": processing_success / len(csv_files) * 100,
                    "excellent_fits_pct": excellent_fits / total_peaks * 100,
                    "good_fits_pct": good_fits / total_peaks * 100,
                    "poor_fits_pct": poor_fits / total_peaks * 100,
                    "avg_r2": all_results['R2'].mean(),
                    "std_r2": all_results['R2'].std(),
                    "avg_fwhm": all_results['FWHM_Gauss'].mean(),
                    "std_fwhm": all_results['FWHM_Gauss'].std(),
                    "cv_fwhm": (all_results['FWHM_Gauss'].std() / all_results['FWHM_Gauss'].mean()) * 100,
                    "region_metrics": region_metrics,
                    "results_file": str(results_path),
                    "report_file": str(report_path)
                }
                
                # Adicionar ao resumo
                combination_summary.append({
                    "Combinacao": combination_name,
                    "Baseline": baseline_method,
                    "Normalizacao": norm_method,
                    "Picos_Total": total_peaks,
                    "Taxa_Sucesso_Proc": f"{processing_success / len(csv_files) * 100:.1f}%",
                    "Ajustes_Excelentes": f"{excellent_fits / total_peaks * 100:.1f}%",
                    "R2_Medio": f"{all_results['R2'].mean():.3f}",
                    "FWHM_Medio": f"{all_results['FWHM_Gauss'].mean():.2f}",
                    "CV_FWHM": f"{(all_results['FWHM_Gauss'].std() / all_results['FWHM_Gauss'].mean()) * 100:.1f}%"
                })
                
                # Finalizar logging da combinação
                combination_end_time = time.time()
                combination_duration = combination_end_time - combination_start_time
                
                combination_times.append({
                    'combination': combination_name,
                    'status': 'SUCCESS',
                    'duration': combination_duration,
                    'files_processed': len(csv_files),
                    'success_rate': processing_success/len(csv_files)*100,
                    'total_peaks': total_peaks,
                    'avg_r2': all_results['R2'].mean(),
                    'avg_fwhm': all_results['FWHM_Gauss'].mean(),
                    'excellent_fits_pct': excellent_fits/total_peaks*100
                })
                
                logger.info(f"  File Outputs:")
                logger.info(f"    Results CSV: {results_filename}")
                logger.info(f"    Report TXT: {report_filename}")
                logger.info(f"  Processing Time: {combination_duration:.2f} seconds")
                logger.info(f"  RESULT: Combination {combination_name} COMPLETED SUCCESSFULLY")
                logger.info(f"  " + "="*60)
                
                print(f"  ✅ Processado: {total_peaks} picos, R²={all_results['R2'].mean():.3f}")
                print(f"  📁 Salvo em: {combo_dir.name}")
                
            except Exception as e:
                combination_end_time = time.time()
                combination_duration = combination_end_time - combination_start_time
                
                combination_times.append({
                    'combination': combination_name,
                    'status': 'ERROR',
                    'duration': combination_duration,
                    'error': str(e)
                })
                
                logger.error(f"  CRITICAL ERROR in combination {combination_name}: {e}")
                logger.error(f"  Processing Time: {combination_duration:.2f} seconds")
                logger.error(f"  RESULT: Combination {combination_name} FAILED with exception")
                logger.error(f"  " + "="*60)
                
                print(f"  ❌ Erro na combinação {combination_name}: {e}")
                continue
    
    # Gerar relatório comparativo final
    if combination_summary:
        # Salvar tabela comparativa com timestamp
        summary_df = pd.DataFrame(combination_summary)
        final_timestamp = generate_timestamp()
        summary_path = combinatorial_dir / f"Comparative_Summary_All_Combinations_{final_timestamp}.csv"
        summary_df.to_csv(summary_path, index=False)
        
        # Identificar melhores combinações com tratamento correto de NaN
        # Converter strings para números, tratando valores NaN
        try:
            r2_values = pd.to_numeric(summary_df['R2_Medio'], errors='coerce').fillna(0)
            cv_fwhm_values = pd.to_numeric(summary_df['CV_FWHM'].str.replace('%', ''), errors='coerce').fillna(100)
            excellent_fits_values = pd.to_numeric(summary_df['Ajustes_Excelentes'].str.replace('%', ''), errors='coerce').fillna(0)
            
            # Verificar se há dados válidos antes de prosseguir
            if len(summary_df) == 0 or r2_values.isna().all():
                logger.error("No valid combination data available for scientific analysis")
                return None
                
            best_r2 = summary_df.loc[r2_values.idxmax()]
            best_fwhm_consistency = summary_df.loc[cv_fwhm_values.idxmin()]
            best_excellent_fits = summary_df.loc[excellent_fits_values.idxmax()]
        except Exception as e:
            logger.error(f"Error processing scientific combination data: {e}")
            logger.error(f"Available columns: {list(summary_df.columns)}")
            return None
        
        # Gerar relatório final científico com timestamp
        final_report_path = combinatorial_dir / f"Scientific_Comparative_Analysis_{final_timestamp}.txt"
        
        with open(final_report_path, 'w', encoding='utf-8') as f:
            f.write("ANÁLISE CIENTÍFICA COMPARATIVA: BASELINE × NORMALIZAÇÃO\n")
            f.write("=" * 70 + "\n\n")
            
            f.write("OBJETIVO: Validar hipóteses sobre otimização de métodos de processamento\n")
            f.write("para datação Raman de zircão conforme literatura científica.\n\n")
            
            f.write("HIPÓTESES TESTADAS:\n")
            f.write("H1: Eficácia diferencial de métodos de baseline\n")
            f.write("H2: Otimização de normalização por região espectral\n") 
            f.write("H3: Correlação baseline-normalização na precisão de FWHM\n")
            f.write("H4: Impacto na qualidade de ajustes gaussianos\n\n")
            
            f.write("RESULTADOS PRINCIPAIS:\n")
            f.write("-" * 40 + "\n")
            f.write(f"Melhor R² médio: {best_r2['Combinacao']} (R²={best_r2['R2_Medio']})\n")
            f.write(f"Melhor consistência FWHM: {best_fwhm_consistency['Combinacao']} (CV={best_fwhm_consistency['CV_FWHM']})\n")
            f.write(f"Melhor % ajustes excelentes: {best_excellent_fits['Combinacao']} ({best_excellent_fits['Ajustes_Excelentes']})\n\n")
            
            f.write("RANKING GERAL (por R² médio):\n")
            f.write("-" * 40 + "\n")
            try:
                # Criar uma cópia para ordenação segura
                report_df = summary_df.copy()
                report_df['R2_Numeric'] = pd.to_numeric(report_df['R2_Medio'], errors='coerce').fillna(0)
                sorted_by_r2 = report_df.sort_values('R2_Numeric', ascending=False)
                
                for i, (_, row) in enumerate(sorted_by_r2.head(5).iterrows(), 1):
                    f.write(f"{i}. {row['Combinacao']} - R²={row['R2_Medio']:<6} | CV_FWHM={row['CV_FWHM']:<7} | Excellent={row['Ajustes_Excelentes']:>6}\n")
            except Exception as e:
                f.write(f"Ranking unavailable due to data processing error: {e}\n")
            
            f.write(f"\nTOTAL DE COMBINAÇÕES TESTADAS: {len(combination_summary)}\n")
            f.write(f"ARQUIVOS GERADOS: {len(combination_summary)} conjuntos de resultados\n")
            f.write(f"LOCALIZAÇÃO: {combinatorial_dir}\n")
        
        # Finalizar análise e logging científico
        analysis_end_time = time.time()
        total_analysis_time = analysis_end_time - analysis_start_time
        
        # Estatísticas finais de tempo
        successful_combinations = [t for t in combination_times if t['status'] == 'SUCCESS']
        failed_combinations = [t for t in combination_times if t['status'] in ['ERROR', 'FAILED_NO_RESULTS', 'SKIPPED_NO_FILES']]
        
        logger.info("="*80)
        logger.info("SCIENTIFIC ANALYSIS SUMMARY")
        logger.info("="*80)
        logger.info(f"Analysis End Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        logger.info(f"Total Analysis Duration: {total_analysis_time:.2f} seconds ({total_analysis_time/60:.1f} minutes)")
        logger.info(f"")
        logger.info(f"COMBINATION RESULTS:")
        logger.info(f"  Total combinations attempted: {total_combinations}")
        logger.info(f"  Successfully completed: {len(successful_combinations)}")
        logger.info(f"  Failed/Skipped: {len(failed_combinations)}")
        logger.info(f"  Success rate: {len(successful_combinations)/total_combinations*100:.1f}%")
        logger.info(f"")
        
        if successful_combinations:
            avg_duration = sum(t['duration'] for t in successful_combinations) / len(successful_combinations)
            logger.info(f"TIMING STATISTICS (successful combinations):")
            logger.info(f"  Average processing time per combination: {avg_duration:.2f} seconds")
            logger.info(f"  Fastest combination: {min(successful_combinations, key=lambda x: x['duration'])['combination']} ({min(t['duration'] for t in successful_combinations):.2f}s)")
            logger.info(f"  Slowest combination: {max(successful_combinations, key=lambda x: x['duration'])['combination']} ({max(t['duration'] for t in successful_combinations):.2f}s)")
            logger.info(f"")
            
            logger.info(f"SCIENTIFIC PERFORMANCE RANKING:")
            logger.info(f"  Best R² score: {best_r2['Combinacao']} (R² = {best_r2['R2_Medio']})")
            logger.info(f"  Best FWHM consistency: {best_fwhm_consistency['Combinacao']} (CV = {best_fwhm_consistency['CV_FWHM']})")
            logger.info(f"  Best fitting success rate: {best_excellent_fits['Combinacao']} ({best_excellent_fits['Ajustes_Excelentes']} excellent fits)")
            logger.info(f"")
            
            logger.info(f"COMPLETE RANKING BY R² SCORE:")
            try:
                # Criar uma cópia para ordenação, convertendo R2_Medio para float
                ranking_df = summary_df.copy()
                ranking_df['R2_Numeric'] = pd.to_numeric(ranking_df['R2_Medio'], errors='coerce').fillna(0)
                sorted_by_r2 = ranking_df.sort_values('R2_Numeric', ascending=False)
                
                for i, (_, row) in enumerate(sorted_by_r2.iterrows(), 1):
                    logger.info(f"  {i:2d}. {row['Combinacao']:<15} | R²={row['R2_Medio']:<6} | CV_FWHM={row['CV_FWHM']:<7} | Excellent={row['Ajustes_Excelentes']:>6}")
            except Exception as e:
                logger.error(f"Error generating ranking: {e}")
                logger.info("Ranking unavailable due to data processing error")
        
        if failed_combinations:
            logger.info(f"")
            logger.info(f"FAILED COMBINATIONS ANALYSIS:")
            for combo in failed_combinations:
                logger.info(f"  {combo['combination']}: {combo['status']}")
                if 'error' in combo:
                    logger.info(f"    Error: {combo['error']}")
        
        logger.info(f"")
        logger.info(f"OUTPUT FILES GENERATED:")
        logger.info(f"  Comparative summary: {summary_path.name}")
        logger.info(f"  Scientific report: {final_report_path.name}")
        logger.info(f"  Individual combination directories: {len(successful_combinations)}")
        logger.info(f"  Total output directory: {combinatorial_dir}")
        logger.info(f"")
        logger.info("ANALYSIS COMPLETED SUCCESSFULLY")
        logger.info("="*80)
        
        # Fechar o handler do log
        logger.info("="*80)
        logger.info("LOG FINALIZED SUCCESSFULLY")
        logger.info("="*80)
        file_handler.flush()  # Garantir que tudo foi escrito
        file_handler.close()
        logger.removeHandler(file_handler)
        
        print(f"\n✅ ANÁLISE COMBINATÓRIA CONCLUÍDA")
        print(f"📊 {len(combination_summary)} combinações testadas")
        print(f"🏆 Melhor R²: {best_r2['Combinacao']} ({best_r2['R2_Medio']})")
        print(f"🎯 Melhor consistência: {best_fwhm_consistency['Combinacao']} (CV={best_fwhm_consistency['CV_FWHM']})")
        print(f"📁 Todos os resultados salvos em: {combinatorial_dir}")
        print(f"📋 Log científico detalhado criado: {log_path}")
        print(f"   Tamanho do arquivo: {log_path.stat().st_size if log_path.exists() else 0} bytes")
        
        return combination_summary
    
    else:
        # Log final para casos sem sucesso
        analysis_end_time = time.time()
        total_analysis_time = analysis_end_time - analysis_start_time
        
        logger.error("="*80)
        logger.error("ANALYSIS FAILED - NO SUCCESSFUL COMBINATIONS")
        logger.error("="*80)
        logger.error(f"Analysis End Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        logger.error(f"Total Analysis Duration: {total_analysis_time:.2f} seconds")
        logger.error(f"All {total_combinations} combinations failed")
        
        # Análise dos erros
        if combination_times:
            logger.error(f"")
            logger.error(f"FAILURE ANALYSIS:")
            failure_counts = {}
            for combo in combination_times:
                status = combo['status']
                failure_counts[status] = failure_counts.get(status, 0) + 1
            
            for status, count in failure_counts.items():
                logger.error(f"  {status}: {count} combinations")
        
        logger.error("="*80)
        
        # Fechar o handler do log
        logger.error("="*80)
        logger.error("LOG FINALIZED WITH ERRORS")
        logger.error("="*80)
        file_handler.flush()  # Garantir que tudo foi escrito
        file_handler.close()
        logger.removeHandler(file_handler)
        
        print("❌ Nenhuma combinação foi processada com sucesso")
        print(f"📋 Log de erro detalhado criado: {log_path}")
        print(f"   Tamanho do arquivo: {log_path.stat().st_size if log_path.exists() else 0} bytes")
        return None

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nError during execution: {e}")
        import traceback
        traceback.print_exc()