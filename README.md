# Making Diffusion Models Faster with Quantization

# !!!!!!!!! To run Q-Diffusion !!!!!!!!!

### Environment Setup

To reproduce this notebook:

1. Create a new environment (e.g. `qdiffusion` with Python 3.11).
2. Install PyTorch with CUDA following https://pytorch.org/get-started/locally/ (GPU users).
3. Install remaining dependencies:

ON CMD
pip install -r Q_diffusion_requirements.txt

# !!!!!!!!! End !!!!!!!!!

## Overview

This model aims to optimize diffusion model inference using dynamic quantization techniques to achieve a 30% latency reduction while maintaining acceptable image quality.

## Objectives

1. Implement diffusion models with multiple quantization levels (FP32, FP16, INT8, INT4)
2. Develop an adaptive quantization strategy based on request load and latency requirements
3. Achieve 30% latency reduction compared to baseline (FP32) without significant quality degradation
4. Design a system that dynamically adjusts quantization levels based on system load

## Structure

```
.
├── README.md                           # Main project documentation
├── requirements.txt                    # Python dependencies
├── config.py                           # Configuration settings
├── PROJECT_OVERVIEW.md                # Comprehensive project overview
├── NOTEBOOK_GUIDE.md                  # Notebook implementation guide
│
├── 01_data_preparation.ipynb          # Dataset loading and preprocessing
├── 02_baseline_model.ipynb            # Baseline diffusion model (FP32)
├── 03_quantization_implementation.ipynb # Different quantization levels
├── 04_performance_benchmarking.ipynb   # Performance metrics comparison
├── 05_adaptive_quantization.ipynb     # Dynamic quantization algorithm
├── 06_load_testing.ipynb              # Load testing under different conditions
└── 07_results_analysis.ipynb          # Comprehensive results analysis

├── outputs/                           # Generated outputs (created at runtime)
├── results/                           # Performance results (created at runtime)
└── generated_images/                  # Generated images (created at runtime)
```

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run notebooks in order:
   - Start with `01_data_preparation.ipynb`
   - Follow the sequence through the notebooks

## Configuration

Edit `config.py` to adjust:
- Model selection
- Dataset paths
- Quantization levels
- Performance targets
- Load testing parameters

## Additional Resources

- Edit `config.py` to adjust model, dataset, and testing parameters


