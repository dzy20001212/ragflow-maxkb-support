\# Day 4 Retrieval Optimization



\## Baseline V1



\- Embedding：text-embedding-v4

\- Chunk Method：General

\- Similarity Threshold：0.20

\- Vector Similarity Weight：0.30

\- Full-text Weight：0.70

\- Top：10

\- Reranker：None

\- Knowledge Graph：OFF

### Results

- Hit@3：12/16=0.75
- Hit@5：13/16=0.8125
- MRR：0.67
- OOD错误召回：实际结果



## Optimized V2

- Similarity Threshold：0.30
- Vector Similarity Weight：0.50
- Full-text Weight：0.50
- Top N：10
- Reranker：None

### Results

- Hit@3：14/16=0.875
- Hit@5：14/16=0.875
- MRR：0.72
- OOD错误召回：实际结果