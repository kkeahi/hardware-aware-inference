# hardware-aware-inference
Analysis and rescheduling of YOLO inference using NVIDIA GPU profiling tools to reduce hardware-level bottlenecks and tail latency


## Windows Setup
Install latest NVIDIA GPU driver
https://www.nvidia.com/en-us/drivers/

Install Visual Studio 2022 (not 2026) with "Desktop development with C++" workload https://aka.ms/vs/17/release/vs_community.exe

Install CUDA Toolkit https://developer.nvidia.com/cuda-downloads
- Test installation with `nvcc --version`

Install Python https://www.python.org/downloads/windows/

Install PyTorch (with CUDA) https://pytorch.org/get-started/locally/
- Get CUDA version with `nvidia-smi`

Install Ultralytics `pip install ultralytics`
