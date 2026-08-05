from __future__ import annotations

import csv
import re
import time
from datetime import date
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify


# 项目根目录
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# 原始文档保存目录
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"

# 文档目录表
CATALOG_PATH = PROJECT_ROOT / "data" / "catalog.csv"


DOCUMENTS = [
    {
        "doc_id": "DOC001",
        "module": "quick_start",
        "title": "快速入门",
        "filename": "quick_start.md",
        "url": "https://maxkb.cn/docs/v2/quick_start/",
    },
    {
        "doc_id": "DOC002",
        "module": "model",
        "title": "模型概述",
        "filename": "model_summary.md",
        "url": "https://maxkb.cn/docs/v2/user_manual/model/model_summary/",
    },
    {
        "doc_id": "DOC003",
        "module": "model",
        "title": "模型操作",
        "filename": "model_param.md",
        "url": "https://maxkb.cn/docs/v2/user_manual/model/model_param/",
    },
    {
        "doc_id": "DOC004",
        "module": "knowledge_base",
        "title": "知识库概述",
        "filename": "dataset.md",
        "url": "https://maxkb.cn/docs/v2/user_manual/dataset/dataset/",
    },
    {
        "doc_id": "DOC005",
        "module": "knowledge_base",
        "title": "文档管理",
        "filename": "doclist.md",
        "url": "https://maxkb.cn/docs/v2/user_manual/dataset/doclist/",
    },
    {
        "doc_id": "DOC006",
        "module": "knowledge_base",
        "title": "问题管理",
        "filename": "problem.md",
        "url": "https://maxkb.cn/docs/v2/user_manual/dataset/problem/",
    },
    {
        "doc_id": "DOC007",
        "module": "knowledge_base",
        "title": "工作流知识库",
        "filename": "dataset_workflow.md",
        "url": "https://maxkb.cn/docs/v2/user_manual/dataset/workflow/",
    },
    {
        "doc_id": "DOC008",
        "module": "agent",
        "title": "智能体概述",
        "filename": "agent_overview.md",
        "url": "https://maxkb.cn/docs/v2/user_manual/app/app/",
    },
    {
        "doc_id": "DOC009",
        "module": "agent",
        "title": "简易智能体",
        "filename": "simple_agent.md",
        "url": "https://maxkb.cn/docs/v2/user_manual/app/simple_app/",
    },
    {
        "doc_id": "DOC010",
        "module": "agent",
        "title": "高级智能体",
        "filename": "workflow_agent.md",
        "url": "https://maxkb.cn/docs/v2/user_manual/app/workflow_app/",
    },
    {
        "doc_id": "DOC011",
        "module": "agent",
        "title": "智能体概览与API",
        "filename": "agent_view.md",
        "url": "https://maxkb.cn/docs/v2/user_manual/app/app-view/",
    },
    {
        "doc_id": "DOC012",
        "module": "agent",
        "title": "对话日志",
        "filename": "conversation_log.md",
        "url": "https://maxkb.cn/docs/v2/user_manual/app/log/",
    },
    {
        "doc_id": "DOC013",
        "module": "faq",
        "title": "安装部署常见问题",
        "filename": "install_faq.md",
        "url": "https://maxkb.cn/docs/v2/faq/install_configuration/",
    },
    {
        "doc_id": "DOC014",
        "module": "faq",
        "title": "知识库常见问题",
        "filename": "knowledge_base_faq.md",
        "url": "https://maxkb.cn/docs/v2/faq/knowledge_base/",
    },
    {
        "doc_id": "DOC015",
        "module": "faq",
        "title": "知识库文档如何合理分段",
        "filename": "document_segmentation.md",
        "url": "https://maxkb.cn/docs/v2/faq/doc_segment/",
    },
]


def clean_markdown(text: str) -> str:
    """清理转换后 Markdown 中的常见噪声。"""

    # 删除页面锚点符号
    text = text.replace("¶", "")

    # 删除单独的图片占位说明
    text = re.sub(r"(?m)^Image:.*$", "", text)

    # 删除过多空行
    text = re.sub(r"\n{3,}", "\n\n", text)

    # 删除页面底部常见导航文字
    text = re.sub(r"(?m)^回到页面顶部\s*$", "", text)

    return text.strip() + "\n"


def extract_main_content(html: str) -> str:
    """从 MaxKB 文档页面中提取正文并转换为 Markdown。"""

    soup = BeautifulSoup(html, "html.parser")

    # MaxKB 文档站点可能使用的正文容器
    content = (
        soup.select_one("article.md-content__inner")
        or soup.select_one("article")
        or soup.select_one("main")
    )

    if content is None:
        raise ValueError("没有找到网页正文区域")

    # 删除不需要进入知识库的网页组件
    unwanted_selectors = [
        "script",
        "style",
        "nav",
        "header",
        "footer",
        "button",
        "svg",
        "img",
        ".headerlink",
        ".md-source",
        ".md-footer",
        ".md-sidebar",
        ".md-content__button",
    ]

    for selector in unwanted_selectors:
        for node in content.select(selector):
            node.decompose()

    markdown_text = markdownify(
        str(content),
        heading_style="ATX",
        bullets="-",
    )

    return clean_markdown(markdown_text)


def download_document(
    session: requests.Session,
    document: dict[str, str],
) -> dict[str, str]:
    """下载并保存一篇文档。"""

    response = session.get(document["url"], timeout=30)
    response.raise_for_status()

    # MaxKB 官方文档网页使用 UTF-8 编码。
    # 强制按照 UTF-8 解码，防止中文正文乱码。
    html = response.content.decode("utf-8")

    markdown_content = extract_main_content(html)

    module_dir = RAW_DATA_DIR / document["module"]
    module_dir.mkdir(parents=True, exist_ok=True)

    output_path = module_dir / document["filename"]

    metadata = f"""---
doc_id: {document["doc_id"]}
title: {document["title"]}
module: {document["module"]}
source_url: {document["url"]}
document_version: v2
collected_date: {date.today().isoformat()}
---

"""

    output_path.write_text(
        metadata + markdown_content,
        encoding="utf-8",
    )

    return {
        "doc_id": document["doc_id"],
        "module": document["module"],
        "title": document["title"],
        "source_url": document["url"],
        "raw_file": str(output_path.relative_to(PROJECT_ROOT)),
        "status": "downloaded",
        "notes": "",
    }

def write_catalog(rows: list[dict[str, str]]) -> None:
    """生成文档目录表。"""

    CATALOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "doc_id",
        "module",
        "title",
        "source_url",
        "raw_file",
        "status",
        "notes",
    ]

    with CATALOG_PATH.open(
        "w",
        newline="",
        encoding="utf-8-sig",
    ) as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    session = requests.Session()
    session.headers.update(
        {
            "User-Agent": (
                "Mozilla/5.0 MaxKB-RAG-Research-Project/1.0"
            )
        }
    )

    catalog_rows: list[dict[str, str]] = []

    for index, document in enumerate(DOCUMENTS, start=1):
        print(
            f"[{index}/{len(DOCUMENTS)}] "
            f"正在下载：{document['title']}"
        )

        try:
            row = download_document(session, document)
            catalog_rows.append(row)
            print(f"  成功：{row['raw_file']}")
        except Exception as error:
            print(f"  失败：{error}")

            catalog_rows.append(
                {
                    "doc_id": document["doc_id"],
                    "module": document["module"],
                    "title": document["title"],
                    "source_url": document["url"],
                    "raw_file": "",
                    "status": "failed",
                    "notes": str(error),
                }
            )

        # 避免连续、快速请求
        time.sleep(0.8)

    write_catalog(catalog_rows)

    success_count = sum(
        row["status"] == "downloaded"
        for row in catalog_rows
    )

    print()
    print("下载任务完成")
    print(f"成功：{success_count}")
    print(f"失败：{len(catalog_rows) - success_count}")
    print(f"目录表：{CATALOG_PATH}")


if __name__ == "__main__":
    main()