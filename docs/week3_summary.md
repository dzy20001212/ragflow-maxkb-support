\# Week 3 Summary



\## Project



基于 RAGFlow 的 MaxKB 产品文档智能问答系统



\## 1. Data Engineering



\- 数据来源：MaxKB 官方 V2 文档

\- 文档数量：15

\- 使用 Python 完成网页采集

\- HTML 转 Markdown

\- UTF-8 编码处理

\- 建立 doc\_id、module、source\_url、version 等元数据



\## 2. Knowledge Base



\- Platform：RAGFlow Cloud

\- Embedding：text-embedding-v4

\- Chunk：General

\- Documents：15



\## 3. Retrieval Baseline



Baseline V1：



\- Threshold：0.20

\- Vector Weight：0.30

\- Full-text Weight：0.70

\- Top N：10

\- Reranker：None



\## 4. Retrieval Optimization



Optimized V2：



\- Threshold：0.3

\- Vector Weight：0.5

\- Full-text Weight：0.5



优化方法：



通过精确术语、口语化、操作流程及故障排查 Query，

对比正确证据 Rank，分析向量检索与全文检索权重对召回效果的影响。



\## 5. Chat Evaluation



\- Test Questions：16

\- Answer Accuracy：100%

\- Citation Accuracy：78.5%

\- Refusal Accuracy：100%



\## 6. Failure Cases



主要包括：



\- Retrieval Error

\- Ranking Error

\- Incomplete Answer

\- Citation Error

\- Hallucination

\- OOD Refusal Error



\## 7. Week 3 Result



完成从官方文档采集、知识库构建、Hybrid Retrieval、

RAG Chat 到基础评测及 Bad Case 分析的完整流程。



\## 8. Next Week



\- Reranker

\- Retrieval V3

\- 扩充测试集

\- Bad Case 复测

\- 最终结果对比

\- README 与简历项目整理

