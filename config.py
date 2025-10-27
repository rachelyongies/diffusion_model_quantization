"""
Configuration file for Diffusion Model Quantization
"""

# Model Configuration
MODEL_NAME = "runwayml/stable-diffusion-v1-5"  
MODEL_CACHE_DIR = "./models" 

# Quantization Levels
QUANTIZATION_LEVELS = {
    'FP32': {'dtype': 'float32', 'enabled': True},
    'FP16': {'dtype': 'float16', 'enabled': True},
    'INT8': {'dtype': 'int8', 'enabled': True},
    'INT4': {'dtype': 'int4', 'enabled': True},  
}

# Dataset Configuration
DATASET_NAME = "fusing/fill50k" 
DATASET_SIZE = 1000 
BATCH_SIZE = 1  

# Performance Targets
BASELINE_TARGET = 'FP32'  # Baseline for comparison
LATENCY_REDUCTION_TARGET = 0.30  # 30% reduction target
MAX_QUALITY_LOSS = 0.10  # Maximum acceptable quality degradation (10%)

# Load Testing Parameters
LOAD_TEST_CONFIG = {
    'requests_per_second': [1, 2, 5, 10], 
    'duration_per_level': 60, 
    'warmup_duration': 10,  
}

# Adaptive Quantization Thresholds
ADAPTIVE_THRESHOLDS = {
    'low_latency_threshold': 2.0,  
    'high_quality_threshold': 1.5,  
    'load_threshold_high': 8,  
    'load_threshold_low': 3,   
}

# Image Generation Parameters
GENERATION_CONFIG = {
    'num_inference_steps': 50, 
    'guidance_scale': 7.5,  
    'image_size': 512,  
}

# Evaluation Metrics
METRICS = {
    'latency': True,
    'throughput': True,
    'memory_usage': True,
    'image_quality': True,  # PSNR, SSIM, FID
}

# Output Directories
OUTPUT_DIR = "./outputs"
RESULTS_DIR = "./results"
IMAGES_DIR = "./generated_images"
