# 问卷星自动填写助手

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi)
![Playwright](https://img.shields.io/badge/Playwright-1.48-45ba4b?logo=playwright)

一个基于 FastAPI + Playwright 的问卷星智能批量填写工具

[功能特性](#功能特性) • [快速开始](#快速开始) • [使用方法](#使用方法) • [项目结构](#项目结构)

</div>

---

## ✨ 功能特性

- 🚀 **批量自动填写** - 支持一键批量完成多份问卷填写
- 🖥️ **可视化界面** - 基于 FastAPI 的 Web 界面，支持远程访问
- 🔄 **实时进度追踪** - 实时显示任务状态和完成进度
- 🐛 **调试模式** - 可选显示浏览器界面，便于调试和查看填写过程
- 🎯 **智能填写策略** - 单选题、多选题、矩阵题自动随机填写
- 📊 **任务管理** - 支持多任务并发，状态独立管理

## 🛠️ 技术栈

- **后端框架**: FastAPI 0.115
- **自动化引擎**: Playwright (Chromium)
- **包管理器**: uv
- **Python 版本**: 3.12

## 📦 快速开始

### 前置要求

- Python 3.12
- uv (推荐) 或 pip

### 安装步骤

1. **克隆仓库**

```bash
git clone https://github.com/koen666/wenjx.git
cd wenjx
```

2. **安装依赖**

使用 uv（推荐）：
```bash
uv sync
```

或使用 pip：
```bash
pip install -e .
```

3. **安装 Playwright 浏览器**

```bash
python -m playwright install chromium
```

### 启动服务

```bash
uv run app
```

服务将在 `http://127.0.0.1:8000` 启动，浏览器访问即可使用。

## 📖 使用方法

### Web 界面使用

1. 访问 `http://127.0.0.1:8000`
2. 输入问卷星问卷链接（如 `https://www.wjx.cn/vm/XXX.aspx`）
3. 设置填写份数（1-50）
4. 可选：勾选"显示浏览器界面"以查看填写过程
5. 点击"开始填写"按钮
6. 实时查看任务状态和日志

### API 接口

#### 创建填写任务

```bash
POST /run
Content-Type: application/json

{
  "url": "https://www.wjx.cn/vm/QHzdwQy.aspx",
  "times": 5,
  "show_browser": false
}
```

响应：
```json
{
  "job_id": "9f82abed319741f18915320e606d5d6c"
}
```

#### 查询任务状态

```bash
GET /status/{job_id}
```

响应：
```json
{
  "status": "running",
  "logs": ["第 1 份完成", "第 2 份完成"],
  "error": null
}
```

## 📂 项目结构

```
wenjx-auto/
├── api/                    # API 路由模块
│   ├── __init__.py
│   └── routes.py          # FastAPI 路由定义
├── models/                # 数据模型
│   ├── __init__.py
│   └── schemas.py         # Pydantic 数据模型
├── services/              # 业务逻辑
│   ├── __init__.py
│   └── wenjx_service.py   # 问卷填写核心逻辑
├── templates/             # 前端模板
│   └── index.py           # HTML 模板（Apple 风格）
├── app.py                 # FastAPI 应用入口
├── pyproject.toml         # 项目配置和依赖
├── .gitignore
└── README.md
```

## 🎯 填写逻辑说明

当前版本针对特定问卷结构进行了配置，支持：

- **单选题** (Question 1, 4): 从 5 个选项中随机选择
- **单选题** (Question 2, 3): 从 2 个选项中随机选择
- **多选题** (Question 5-9): 根据权重分布随机选择 1-5 个选项
- **矩阵评分题** (Question 10): 每行随机选择评分

如需适配其他问卷，请修改 `services/wenjx_service.py` 中的 `_fill_form` 函数。

## ⚙️ 配置说明

### 修改绑定地址和端口

编辑 `app.py` 文件：

```python
def main():
    import uvicorn
    uvicorn.run(
        "app:app",
        host="0.0.0.0",  # 改为 0.0.0.0 允许外部访问
        port=8000,       # 修改端口
        reload=False,
        log_level="info",
    )
```

### 自定义问卷填写逻辑

编辑 `services/wenjx_service.py`，修改 `_fill_form` 函数中的题目配置：

```python
async def _fill_form(page):
    # 根据实际问卷结构修改
    single_5 = [1, 4]      # 5 选 1 的题目编号
    single_2 = [2, 3]      # 2 选 1 的题目编号
    multi_5 = [5, 6, 7, 8, 9]  # 多选题编号
    # ...
```

## 🐛 常见问题

### 1. 浏览器未安装

**错误信息**：`Executable doesn't exist at ...`

**解决方法**：
```bash
python -m playwright install chromium
```

### 2. 端口被占用

**错误信息**：`[Errno 10048] error while attempting to bind`

**解决方法**：修改 `app.py` 中的 `port` 参数为其他端口。

### 3. 任务 404 错误

重启服务后任务状态会丢失（存储在内存中）。如需持久化，可改用 Redis 或数据库存储。

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## ⚠️ 免责声明

本工具仅供学习交流使用，请勿用于任何违反问卷星服务条款或法律法规的行为。使用本工具产生的任何后果由使用者自行承担。

## 📮 联系方式

如有问题或建议，欢迎通过 [Issues](https://github.com/your-username/wenjx-auto/issues) 反馈。

---

<div align="center">

Made with ❤️ by KeHe

</div>
