\# Day 3：RAG 产品技术支持助手



\## 1. 今日目标



在 Day 2 Retrieval Baseline 基础上建立完整 RAG 问答链路，

验证检索结果经过 LLM 后能否形成准确、完整且可追溯的技术支持回答。



\## 2. System Configuration



\- Platform：RAGFlow Cloud

\- LLM：qwen3.7-plus

\- Embedding：text-embedding-v4

\- Dataset：RAGFlow

\- Chunk：General

\- Reranker：None



\## 3. 今日完成



\- 将 Dataset 扩充至核心 MaxKB 产品文档；

\- 创建 MaxKB 产品技术支持 Chat；

\- 关联产品文档 Dataset；

\- 配置知识库外问题 Empty Response；

\- 设计 System Prompt；

\- 测试普通知识问答；

\- 测试产品操作问题；

\- 测试故障排查；

\- 测试口语化 Query；

\- 测试知识库外问题；

\- 检查答案引用；

\- 建立 Chat Baseline V1；

\- 记录失败案例。



\## 4. 当前主要问题



根据实际情况填写，例如：



\- 部分口语化问题正确证据排名偏低；

\- 某些长步骤回答存在信息遗漏；

\- 信息不足时模型仍倾向直接回答；

\- 部分 OOD Query 能够正确拒答；

\- 个别引用虽相关但无法完整支持答案。



\## 5. 下一步



Day 4：

针对 Baseline 中暴露的问题进行 Chunk 与 Retrieval 优化，

重点分析专业术语、口语化 Query、长步骤以及错误召回问题。

