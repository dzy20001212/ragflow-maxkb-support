\# Day 2：RAGFlow Cloud 基线知识库搭建



\## 今日完成



\- 完成 RAGFlow Cloud 模型配置；

\- 默认 LLM 使用 qwen3.7-plus；

\- Embedding 使用 text-embedding-v4；

\- 创建 MaxKB 产品文档 Dataset；

\- 使用 General 分段模板；

\- 导入首批 5 篇 MaxKB 官方文档；

\- 完成文档解析及 Chunk 检查；

\- 对 doclist.md 的 4 个 Chunk 进行人工检查；

\- 完成 5 道 Retrieval Testing；

\- 记录召回文档及排名；

\- 建立 Baseline V1。



\## Baseline V1



\- Embedding：text-embedding-v4

\- Chunk Method：General

\- Chunk Parameters：Default

\- Retrieval Parameters：Default

\- Reranker：None



\## 当前发现



根据今天真实测试结果填写，例如：

\- 精确问题能够稳定命中正确文档；

\- 口语化表达也能够召回相关内容；

\- 某些问题存在正确文档排名靠后的情况；

\- 当前 Chunk 结构总体正常。



\## 下一步



Day 3：

\- 上传剩余 MaxKB 文档；

\- 创建完整知识库；

\- 配置 Chat；

\- 编写 System Prompt；

\- 设置知识库外问题拒答规则；

\- 测试答案和引用来源。

