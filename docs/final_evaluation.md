\# Final RAG Evaluation 

\## 1. Evaluation Set - Total Questions：16 - In-domain：16 - OOD：2

\## 2. Baseline V1 - Threshold：0.20 - Vector Weight：0.30 - Full-text Weight：0.70 - Reranker：None 

\## 3. Final Version - Threshold：0.30 - Weight：0.50 - Reranker：qwen3ranker  实际配置 - Top：10

\## 4. Results

| Metric | Baseline V1 | Final | 

|---|---:|---:| 

| Answer Accuracy | 90% | 95% | 

| Citation Accuracy | 90% | 90% | 

| Refusal Accuracy |100% | 100% | 

| Top3 Hit Rate | 80% | 87.5% | 

\## 5. Key Findings 

\### Retrieval 填写实际结论。 

\### Generation 填写实际结论。 

\### Citation 填写实际结论。 

\### OOD Refusal 填写实际结论。 

\## 6. Conclusion :使用v3版本加rerank会使实验结果有所提升，但是提升不多

