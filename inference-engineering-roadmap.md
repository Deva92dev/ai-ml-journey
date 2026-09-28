# Inference Engineering — Chapter Reading + Project Roadmap

**Book:** *Inference Engineering* — Philip Kiely  
**Goal:** Study the book deeply while building one progressively harder inference-engineering system.

## How to use this roadmap

For every chapter:

1. Read the selected sections.
2. Take notes in your own words.
3. Implement the related project.
4. Benchmark or measure whenever possible.
5. Break something deliberately and debug it.
6. Document the result.
7. Move the same codebase forward into the next project.

The projects are intentionally cumulative:

```text
Project 1 → Project 2 → Project 3 → Project 4 → Project 5 → Project 6 → Project 7
```

The book's progression is: prerequisites → model mechanics → hardware → software → optimization techniques → modalities → production. This roadmap follows that structure.

---

# Chapter 1 — Prerequisites

## What to Read

### 1.1 Scale and Specialization
Understand:
- Why inference requirements depend on the workload.
- Why constraints help define an optimization target.

### 1.2 About Your App
Read:
- 1.2.1 AI-Native Applications
- 1.2.2 Online versus Offline
- 1.2.3 Consumer versus B2B

Understand:
- Online vs offline inference.
- Latency-sensitive vs throughput-oriented workloads.
- Consumer vs B2B inference requirements.
- How traffic patterns change infrastructure requirements.

### 1.3 Model Selection
Read:
- 1.3.1 Model Evaluation
- 1.3.2 Fine-Tuning for Domain-Specific Quality
- 1.3.3 Distillation

Focus on:
- Model selection.
- Application-specific evals.
- Baselines.
- Quality vs latency vs cost.
- Smaller vs larger models.
- When fine-tuning or distillation can improve inference.

### 1.4 Measuring Latency and Throughput
Read:
- 1.4.1 Latency Percentiles
- 1.4.2 End-to-End Metrics

Master:
- TTFT
- ITL
- TPS
- P50 / P90 / P95 / P99
- End-to-end latency
- Throughput
- Cost/request

## Project 1 — Inference Benchmark Lab

**Difficulty:** ★★☆☆☆☆☆☆

### Objective
Build a model-selection and inference benchmarking system for one real workload.

Choose one:
- Document extraction
- SQL generation
- Customer-support classification
- Coding assistance
- Structured information extraction

### Architecture

```text
                    Benchmark Runner
                           |
            +--------------+--------------+
            |              |              |
          Model A        Model B        Model C
            |              |              |
            +--------------+--------------+
                           |
                    Metrics Engine
                           |
            +--------------+--------------+
            |              |              |
         Quality        Latency          Cost
```

### Measure
- Quality
- TTFT
- ITL
- TPS
- P50/P95/P99
- Throughput
- Cost/request

### Deliverables

```text
01-inference-benchmark/
├── models/
├── benchmark/
├── evals/
├── metrics/
├── reports/
└── README.md
```

README must explain:
- Which model performed best?
- Why?
- What was the quality/latency/cost tradeoff?
- What would you choose for production?
- What would you optimize next?

**Core lesson:** Measure and define the target before optimizing.

---

# Chapter 2 — Models

## What to Read

### 2.1 Neural Networks
Read:
- 2.1.1 Linear Layers and Matmul
- 2.1.2 Activation Functions

Understand:
- Matrix multiplication.
- Linear layers.
- Activations.
- Why matmul matters to inference performance.

### 2.2 LLM Inference Mechanics
Read:
- 2.2.1 LLM Architecture
- 2.2.2 Transformer Blocks
- 2.2.3 Attention
- 2.2.4 Mixture of Experts Models

Master:

```text
Input
  ↓
Tokenization
  ↓
Embeddings
  ↓
Transformer blocks
  ↓
Attention
  ↓
MLP
  ↓
Logits
  ↓
Sampling
  ↓
Next token
```

Understand:
- Transformer blocks
- Q/K/V
- Attention
- KV cache
- MoE at a conceptual level

### 2.3 Image Generation Inference Mechanics
Read:
- 2.3.1 Image Generation Model Architecture
- 2.3.2 Few-Step Image Generation Models
- 2.3.3 Video Generation

Understand the architectural differences and inference implications without making this your deepest area.

### 2.4 Calculating Inference Bottlenecks
Read:
- 2.4.1 Ops:Byte Ratio and Arithmetic Intensity
- 2.4.2 LLM Inference Bottlenecks
- 2.4.3 Image Generation Inference Bottlenecks

Master:
- Compute-bound workloads
- Memory-bound workloads
- Arithmetic intensity
- Ops:Byte ratio
- Roofline reasoning
- Prefill vs decode

### 2.5 Optimizing Attention
Read the full section.

Understand:
- Why attention is expensive.
- How sequence length affects inference.
- How KV caching changes the workload.

## Project 2 — Mini LLM Inference Engine

**Difficulty:** ★★★☆☆☆☆☆

### Objective
Build a small Transformer inference engine and profiler so you understand what actually happens during inference.

### Build

```text
Tokenizer
   ↓
Embedding
   ↓
Transformer Block
   ↓
Q/K/V
   ↓
Attention
   ↓
MLP
   ↓
Logits
   ↓
Sampling
```

Separate inference into:

```text
                Inference
                   |
          +--------+--------+
          |                 |
       Prefill            Decode
          |                 |
        TTFT                TPS
```

### Implement / inspect
- Tokenization
- Embeddings
- Attention
- KV cache
- Transformer blocks
- Sampling
- Prefill
- Decode

### Build a profiler
Measure:
- Tokenization time
- Prefill time
- Decode time
- Attention time
- MLP time
- Memory usage
- KV-cache size

### Add analysis
Calculate or estimate:
- FLOPs
- Memory traffic
- Arithmetic intensity

Classify important operations as:
- Compute-bound
- Memory-bound

### Deliverables

```text
02-mini-inference-engine/
├── model/
├── attention/
├── kv_cache/
├── tokenizer/
├── sampling/
├── profiler/
├── benchmark/
└── README.md
```

**Core lesson:** Understand how the model executes before trying to make it faster.

---

# Chapter 3 — Hardware

## What to Read

### 3.1 GPU Architecture
Read:
- 3.1.1 Compute
- 3.1.2 Memory and Caches

Master:
- GPU compute
- GPU memory
- Memory bandwidth
- Caches
- Tensor-oriented computation
- Compute vs memory bottlenecks

### 3.2 GPU Architecture Generations
Read:
- 3.2.1 Hopper GPUs
- 3.2.2 Ada Lovelace GPUs
- 3.2.3 Blackwell GPUs
- 3.2.4 Rubin GPUs
- 3.2.5 Grace and Vera CPUs

Focus on architectural differences and inference implications. Do not spend excessive time memorizing SKU specifications.

### 3.3 Instances
Read:
- 3.3.1 Multi-GPU Instances
- 3.3.2 Multi-Instance GPUs

Understand:
- Multi-GPU inference
- GPU partitioning
- When multiple GPUs are needed

### 3.4 Other Datacenter Accelerator Options
Read for awareness.

### 3.5 Local Inference
Read:
- 3.5.1 Desktop Inference
- 3.5.2 Mobile Inference

Focus on practical hardware constraints.

## Project 3 — GPU Performance Lab

**Difficulty:** ★★★★☆☆☆☆

### Objective
Build a GPU performance laboratory that connects hardware characteristics to actual inference behavior.

### Experiment 1 — Memory
Measure:
- GPU memory usage
- Memory bandwidth
- Host → GPU transfer
- GPU → host transfer

### Experiment 2 — Matrix multiplication
Benchmark different:
- Matrix sizes
- Batch sizes
- Precisions

Compare:
- FP32
- FP16
- BF16

### Experiment 3 — LLM inference
Vary:
- Batch size
- Input length
- Output length
- Concurrency

Measure:
- VRAM
- GPU utilization
- TTFT
- TPS
- Throughput

### Experiment 4 — Bottleneck analysis

```text
Benchmark
   ↓
GPU metrics
   ↓
Arithmetic intensity
   ↓
Bottleneck analysis
   ↓
Compute-bound / Memory-bound
```

### Deliverables

```text
03-gpu-performance-lab/
├── benchmarks/
├── gpu_tests/
├── inference_tests/
├── profiler/
├── analysis/
├── results/
└── README.md
```

README must explain **why** a workload is bottlenecked, not just report numbers.

**Core lesson:** Connect model behavior to hardware behavior.

---

# Chapter 4 — Software

## What to Read

### 4.1 CUDA
Read:
- 4.1.1 CUDA Kernels for Inference
- 4.1.2 CUDA Kernel Selection
- 4.1.3 Reducing Memory Accesses with Kernel Fusion

Understand:
- CUDA execution model at a practical level.
- Kernels.
- Kernel selection.
- Kernel fusion.
- Why memory accesses matter.

You do not need to become a CUDA kernel specialist yet.

### 4.2 Deep Learning Frameworks and Libraries
Read:
- 4.2.1 PyTorch
- 4.2.2 Model File Formats
- 4.2.3 ONNX Runtime and TensorRT
- 4.2.4 Transformers and Diffusers

Understand:

```text
CUDA
  ↓
PyTorch
  ↓
Transformers / Diffusers
  ↓
Inference Runtime
```

### 4.3 Inference Engines
Read deeply:
- 4.3.1 vLLM
- 4.3.2 SGLang
- 4.3.3 TensorRT-LLM

Learn:
- Architecture
- Serving model
- Configuration
- Scheduling
- Performance characteristics
- When each engine makes sense

### 4.4 NVIDIA Dynamo
Read for understanding of distributed inference infrastructure.

### 4.5 Performance Benchmarking and Load Testing
Read:
- 4.5.1 Performance Benchmarking Tooling
- 4.5.2 Performance Benchmarking Tips
- 4.5.3 Profiling Performance

Master:
- Benchmark design
- Load testing
- Profiling
- Reproducibility
- Interpreting benchmark results

## Project 4 — Inference Engine Benchmark Platform

**Difficulty:** ★★★★★☆☆☆

### Objective
Build a platform that compares multiple inference runtimes under controlled workloads.

### Engines
At minimum:
- Transformers
- vLLM
- SGLang

Add TensorRT-LLM when your available hardware/environment supports it.

### Architecture

```text
                    Benchmark API
                         |
                  Test Configuration
                         |
                  Benchmark Runner
                         |
              +----------+----------+
              |          |          |
        Transformers   vLLM      SGLang
              |          |          |
              +----------+----------+
                         |
                   Metrics Engine
                         |
                 Results Database
                         |
                     Dashboard
```

### Benchmark dimensions
- Model
- Engine
- GPU
- Batch size
- Input length
- Output length
- Concurrency
- Precision

### Measure
- TTFT
- ITL
- TPS
- P50/P95/P99
- Throughput
- VRAM
- GPU utilization
- Cost

### Deliverables

```text
04-inference-engine-benchmark/
├── engines/
│   ├── transformers/
│   ├── vllm/
│   ├── sglang/
│   └── tensorrt_llm/
├── workloads/
├── benchmark/
├── metrics/
├── dashboard/
├── results/
└── README.md
```

Required conclusion:

> Do not simply say which engine was faster. Explain why the result changed under different workloads.

**Core lesson:** Runtime choice depends on workload, model, hardware and constraints.

---

# Chapter 5 — Techniques

## What to Read

### 5.1 Quantization
Read:
- 5.1.1 Number Formats
- 5.1.2 Quantization Approaches
- 5.1.3 Measuring Quality Impact

Master:
- FP32
- FP16
- BF16
- FP8
- INT8
- INT4
- Precision vs memory
- Precision vs performance
- Quality degradation
- Post-training quantization
- Evaluation after quantization

### 5.2 Speculative Decoding
Read:
- 5.2.1 Draft-Target Speculative Decoding
- 5.2.2 Medusa
- 5.2.3 EAGLE
- 5.2.4 N-gram Speculation and Lookahead Decoding

Understand the core mechanism deeply before worrying about every variant.

### 5.3 Caching
Read:
- 5.3.1 Prefix Caching and KV Cache Re-Use
- 5.3.2 Where to Store the KV Cache
- 5.3.3 Cache-Aware Routing
- 5.3.4 Long Context Handling

Master:
- KV cache
- Prefix caching
- Cache reuse
- Cache-aware routing
- Long-context implications

### 5.4 Parallelism
Read the sections on:
- Tensor parallelism
- Expert parallelism
- Multi-GPU
- Multi-node inference

Understand:
- Why parallelism is required.
- Communication costs.
- Latency vs throughput tradeoffs.

### 5.5 Disaggregation
Read the full section.

Understand:

```text
Prefill workers
      ↓
KV transfer
      ↓
Decode workers
```

Understand why prefill and decode can benefit from separate scaling.

## Project 5 — Inference Optimization Lab

**Difficulty:** ★★★★★★☆☆

### Objective
Build an experimentation framework that searches for faster/cheaper inference configurations while preserving model quality.

Extend Project 4.

### Stage 1 — Quantization
Compare:
- BF16
- FP8
- INT8
- INT4

Measure:
- VRAM
- TTFT
- TPS
- Throughput
- Quality

### Stage 2 — KV cache
Compare:

```text
No prefix caching
        vs
Prefix caching
```

Test:
- Context lengths
- Repeated prefixes
- Concurrency

Measure:
- TTFT
- VRAM
- Throughput
- Cache hit rate

### Stage 3 — Speculative decoding
Compare:

```text
Normal decoding
       vs
Speculative decoding
```

Measure:
- TPS
- Latency
- Acceptance rate
- Quality

### Stage 4 — Batching
Experiment with:
- Batch size
- Concurrency
- Input length
- Output length

Find the best throughput/latency tradeoff.

### Stage 5 — Optimization search

```text
                  Search Space
                       |
        +--------------+--------------+
        |              |              |
   Quantization    Batch Size       Cache
        |              |              |
        +--------------+--------------+
                       |
                   Benchmark
                       |
                 Quality Eval
                       |
                  Cost Model
                       |
                 Best Config
```

Example objective:

```text
Minimize cost

subject to:

quality >= target
P95 TTFT <= target
TPS >= target
VRAM <= target
```

### Deliverables

```text
05-inference-optimization/
├── quantization/
├── speculative/
├── caching/
├── batching/
├── optimization/
├── benchmarks/
├── evals/
├── results/
└── README.md
```

**Core lesson:** Inference optimization is empirical: change one variable, measure, verify quality, and compare tradeoffs.

---

# Chapter 6 — Modalities

## What to Read

### 6.1 Vision Language Models
Study:
- VLM architecture
- VLM inference
- How LLM inference techniques transfer to multimodal models

### 6.2 Embedding Models
Study:
- Embedding inference
- Throughput-oriented serving
- Batch inference
- Retrieval-system implications

### 6.3 Automatic Speech Recognition
Study:
- ASR inference
- Latency considerations
- Streaming vs batch use cases

### 6.4 Text-to-Speech
Study:
- TTS inference
- Streaming considerations
- Latency and quality tradeoffs

### Image and Video Generation
Study the relevant Chapter 2 material together with Chapter 6.

Focus on understanding how inference differs from autoregressive LLM serving.

Do not make image/video optimization your deepest specialization unless a later project requires it.

## Project 6 — Multimodal Inference Gateway

**Difficulty:** ★★★★★★★☆

### Objective
Build a unified inference gateway that routes requests to different optimized model services.

### Supported modalities

```text
Text
  ↓
LLM

Image + Text
  ↓
VLM

Text
  ↓
Embedding

Audio
  ↓
ASR

Text
  ↓
TTS
```

### Gateway
Expose APIs such as:

```text
POST /generate
POST /vision
POST /embed
POST /transcribe
POST /synthesize
```

### Architecture

```text
                         Client
                           |
                           ↓
                  Inference Gateway
                           |
             +-------------+-------------+
             |             |             |
           Text          Image         Audio
             |             |             |
             ↓             ↓             ↓
            LLM           VLM           ASR
             |                           |
             |                           ↓
             |                          TTS
             |
             ↓
        Embedding Model
```

### Intelligent routing

```text
Request
   ↓
Detect modality
   ↓
Select model
   ↓
Select inference engine
   ↓
Select service
   ↓
Execute
   ↓
Stream result
```

### Failure handling
Implement:
- Timeout
- Retry
- Fallback model
- Fallback worker
- Queueing
- Overload handling

### Measure
For every modality:
- Latency
- Throughput
- Memory
- Cost
- Quality

### Deliverables

```text
06-multimodal-gateway/
├── gateway/
├── routers/
├── llm/
├── vlm/
├── embeddings/
├── asr/
├── tts/
├── benchmarks/
├── observability/
└── README.md
```

**Core lesson:** Apply inference-engineering principles across different model types.

---

# Chapter 7 — Production

## What to Read

Read the production chapter deeply.

### Containerization
Understand:
- Containerized model serving
- Dependency management
- GPU runtime requirements
- Reproducible deployment

### Autoscaling
Study:
- Scaling inference workloads
- GPU-aware scaling
- Queue-based scaling
- Latency-aware scaling

### Concurrency and Batching
Master:
- Concurrent requests
- Dynamic batching
- Batch-size tradeoffs
- Throughput vs latency

### Cold Starts
Understand:
- Container startup
- Model loading
- GPU initialization
- Warm-up
- First-request latency

### Routing / Load Balancing / Queueing
Study:
- Request routing
- Load balancing
- Queueing
- Backpressure
- Model-aware routing

### Scale-to-Zero
Understand:
- When it helps
- Cold-start tradeoffs
- Cost implications

### Independent Component Scaling
Understand why:

```text
Gateway
   +
Router
   +
Prefill
   +
Decode
   +
Model workers
```

may need different scaling policies.

### Reliability
Study:
- Failure handling
- Recovery
- Availability
- Graceful degradation

### Security
Study inference-service security considerations.

### Deployment
Study:
- Rolling deployment
- Zero-downtime deployment
- Version management

### Cost
Study:
- GPU utilization
- Cost/request
- Cost/token
- Capacity planning

### Observability
Master:
- Logs
- Metrics
- Traces
- Inference metrics
- GPU metrics
- Latency percentiles
- Error rates

### Async Inference
Understand:
- Queues
- Long-running jobs
- Async APIs
- Streaming

## Project 7 — Production Inference Platform

**Difficulty:** ★★★★★★★★

### Objective
Build a production-oriented inference platform that operates the optimized models from Projects 1–6.

Use Kubernetes and your DevOps knowledge for deployment and operations.

### Target architecture

```text
                         Internet
                            |
                            ↓
                    API Gateway / LB
                            |
                            ↓
                    Inference Router
                            |
          +-----------------+-----------------+
          |                 |                 |
          ↓                 ↓                 ↓
       LLM Pool          VLM Pool          ASR Pool
          |                 |                 |
      GPU workers       GPU workers       GPU workers
          |                 |                 |
          +-----------------+-----------------+
                            |
                            ↓
                 Metrics / Tracing / Logs
```

### Required capabilities

#### 1. Autoscaling
Scale using meaningful inference signals:
- Queue depth
- Concurrency
- Request rate
- Latency
- GPU utilization

#### 2. Dynamic batching

```text
Request 1 ─┐
Request 2 ─┤
Request 3 ─┼──→ Dynamic Batch → GPU
Request 4 ─┤
Request 5 ─┘
```

Measure:
- Throughput
- Latency
- GPU utilization

#### 3. Queueing

```text
Incoming Requests
        ↓
      Queue
        ↓
    Scheduler
        ↓
   GPU Workers
```

Implement:
- Backpressure
- Queue limits
- Timeouts
- Failure handling

#### 4. Cold-start experiments

Measure:
- 0 → 1 worker
- 1 → 2 workers
- Model load time
- Container startup
- Warm-up time
- First-request latency

#### 5. Observability

Dashboard:
- Request rate
- Error rate
- TTFT
- TPS
- P50
- P95
- P99
- GPU utilization
- VRAM
- Queue depth
- Model load time
- Cost/request

#### 6. Reliability experiments

Intentionally test:

```text
Kill worker
   ↓
Observe
   ↓
Detect
   ↓
Recover
   ↓
Reroute traffic
```

Also test:
- OOM
- Slow requests
- Network failures
- Traffic spikes
- Model crashes
- Worker failures

#### 7. Zero-downtime deployment
Deploy a new model/service version without interrupting existing traffic.

#### 8. Cost analysis

Report:
- Cost/request
- Cost/1M tokens
- GPU utilization
- Idle capacity
- Throughput/GPU

### Deliverables

```text
07-production-inference-platform/
├── gateway/
├── router/
├── models/
├── inference-services/
├── batching/
├── queue/
├── autoscaling/
├── kubernetes/
├── observability/
├── load-tests/
├── failure-tests/
├── benchmarks/
├── cost-analysis/
└── README.md
```

README should contain:
1. Architecture diagram
2. Deployment instructions
3. Benchmark methodology
4. Performance results
5. Scaling behavior
6. Failure experiments
7. Observability screenshots
8. Cost analysis
9. Optimization decisions
10. Tradeoffs
11. Known limitations
12. Future improvements

---

# Final Difficulty Progression

```text
CHAPTER 1
Inference Benchmark Lab
★★☆☆☆☆☆☆
"Which model is best for this workload?"
        ↓
CHAPTER 2
Mini LLM Inference Engine
★★★☆☆☆☆☆
"How does inference actually execute?"
        ↓
CHAPTER 3
GPU Performance Lab
★★★★☆☆☆☆
"Why is inference slow on this hardware?"
        ↓
CHAPTER 4
Inference Engine Benchmark Platform
★★★★★☆☆☆
"Which runtime serves this model best?"
        ↓
CHAPTER 5
Inference Optimization Lab
★★★★★★☆☆
"How can I make inference faster and cheaper?"
        ↓
CHAPTER 6
Multimodal Inference Gateway
★★★★★★★☆
"How do I serve multiple model modalities?"
        ↓
CHAPTER 7
Production Inference Platform
★★★★★★★★
"How do I operate optimized inference reliably at scale?"
```

# Cumulative System

The seven projects should eventually become one system:

```text
Project 1 — Model Benchmarking
          ↓
Project 2 — Model Understanding
          ↓
Project 3 — GPU Profiling
          ↓
Project 4 — Runtime Benchmarking
          ↓
Project 5 — Inference Optimization
          ↓
Project 6 — Multimodal Model Serving
          ↓
Project 7 — Production AI Platform
```

# Final Outcome

By the end, you should be able to reason through:

```text
Product requirement
      ↓
Model selection
      ↓
Quality baseline
      ↓
Latency / throughput target
      ↓
Model architecture
      ↓
Hardware
      ↓
Inference runtime
      ↓
Optimization
      ↓
Multimodal serving
      ↓
Kubernetes deployment
      ↓
Autoscaling
      ↓
Observability
      ↓
Reliability
      ↓
Cost optimization
```

This is the progression from **AI Engineering → Inference Engineering → Production AI Infrastructure**.
