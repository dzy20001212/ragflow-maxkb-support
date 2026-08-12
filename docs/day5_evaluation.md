\# Day 5 Chat Evaluation



\## 1. Configuration



\- Platform：RAGFlow Cloud

\- Dataset：MaxKB\_Product\_Docs\_Baseline

\- Documents：15

\- LLM：qwen3.7-plus

\- Embedding：text-embedding-v4

\- Chunk：General

\- Threshold：0.3

\- Vector Weight：0.5

\- Full-text Weight：0.5

\- Top N：10

\- Reranker：None



\## 2. Evaluation Set



\- In-domain Questions：14

\- OOD Questions：2

\- Total：16



\## 3. Results



\- Answer Accuracy：100%

\- Citation Accuracy：11/14=78.5%

\- Refusal Accuracy：100%



\## 4. Typical Success Case



Query：我想改一下模型配置，要去哪里操作？



填写。



Result：要修改模型配置，请按照以下步骤操作：



操作步骤



进入 MaxKB 的【模型】页面。

找到您需要修改的模型卡片。

点击模型右下角的更多菜单（通常为三个点图标）。

在弹出的菜单中点击\*\*【编辑】\*\*。

在打开的页面中，您可以修改已创建的模型配置信息（如 API Key、基础 URL、模型名称等）。

修改完成后，点击保存即可 

注意事项

如果您只是想查看或调整模型的运行参数（如温度、Top P 等），可以在更多菜单中选择\*\*【模型参数设置】\*\*进行配置 。

修改配置后，建议测试一下该模型在智能体中的使用情况，确保连接正常。



填写。



Analysis：



填写。



\## 5. Typical Failure Case



Query：如何配置模型？、文档上传成功但知识库不显示怎么办？、文档上传成功但知识库不显示怎么办？



填写。



Result：结果我觉得回答写的没问题，但是引用资料不对，不只是这三个，其他问起引用的资料包含正确文献，但是也存在其他干扰项



填写。



Failure Type：操作流程类、故障类



填写。



Possible Cause：



填写。



\## 6. Conclusion



根据实际实验结果填写：优化引用的准确率

