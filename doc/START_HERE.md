# 👋 开始使用 - 选择你的路径

欢迎使用改进后的小米运动自动刷步数工具！

根据你的情况，选择对应的路径 👇

---

## 🟢 我是新用户，想在本地运行

**推荐文档：** `LOCAL_SETUP.md`

这份文档只需要 3 步，10 分钟，就能让你在自己的电脑上运行刷步数程序。

**快速预览：**
```bash
# 第一次运行（单账号）
python main.py --config '{"USER":"your_email@example.com","PWD":"your_password"}'
```

👉 [打开 LOCAL_SETUP.md](LOCAL_SETUP.md)

---

## 🟡 我需要快速查看命令和选项

**推荐文档：** `QUICK_START.md`

这份文档展示了常用的命令，多账号配置，以及各种参数。

**快速预览：**
```bash
# 配置文件方式（推荐）
python main.py --config-file config.json

# 多账号
python main.py --config '{"USER":"u1#u2","PWD":"p1#p2"}'
```

👉 [打开 QUICK_START.md](QUICK_START.md)

---

## 🔵 我想详细了解所有功能

**推荐文档：** `USAGE_STANDALONE.md`

这是最详细的使用指南，涵盖所有功能、参数说明、定时运行设置等。

**包含内容：**
- 详细的参数说明表
- 多种使用方式对比
- 定时执行配置（Windows/Linux/Mac）
- 常见问题解答
- 进阶功能说明

👉 [打开 USAGE_STANDALONE.md](USAGE_STANDALONE.md)

---

## 💻 我是开发者，想在 Python 代码中调用

**推荐文件：** `example_usage.py`

7 个实际的 Python 代码示例，展示如何在应用中集成。

**快速预览：**
```python
from main import main

config = {
    "USER": "your_email@example.com",
    "PWD": "your_password"
}

main(config_data=config)
```

👉 [打开 example_usage.py](example_usage.py)

---

## 🔍 我想了解这次改进的技术细节

**推荐文档：** `IMPROVEMENTS.md`

这份文档详细说明了代码如何从 GitHub Actions 专用改造为多场景支持，包含技术细节和架构设计。

👉 [打开 IMPROVEMENTS.md](IMPROVEMENTS.md)

---

## 📋 我想看配置文件的示例

**推荐文件：** `config_example.json`

一个完整的配置文件示例，包含所有可用的参数和说明。

复制这个文件为 `config.json`，然后编辑填入你的信息。

👉 [打开 config_example.json](config_example.json)

---

## 🤖 我是 GitHub Actions 用户，想继续使用

**好消息：** 无需任何改变！✅

- 你现有的所有配置继续有效
- 你的工作流继续正常运行
- 所有功能保持不变

如果你想在本地也运行一份，可以参考 `LOCAL_SETUP.md`。

---

## 📊 我想看改进的完整报告

**推荐文档：** `COMPLETION_REPORT.md`

完整的改进报告，包括：
- 改进了哪些功能
- 支持的新使用方式
- 功能对比表
- 安全建议

👉 [打开 COMPLETION_REPORT.md](COMPLETION_REPORT.md)

---

## 🎉 整体改进总结

**推荐文档：** `SUMMARY.md`

一个简明扼要的改进总结，适合快速了解整体情况。

👉 [打开 SUMMARY.md](SUMMARY.md)

---

## ❓ 我遇到了问题

**查看这些资源：**

1. **常见问题？** → 查看 `USAGE_STANDALONE.md` 的"常见问题"部分
2. **命令语法？** → 运行 `python main.py --help`
3. **配置问题？** → 参考 `config_example.json` 的结构
4. **Python 集成？** → 看 `example_usage.py` 的相应示例

---

## 🚀 最流行的三种使用方式

### 方式 1：命令行（最简单）
```bash
python main.py --config '{"USER":"email@example.com","PWD":"password"}'
```

### 方式 2：配置文件（最实用）
```bash
python main.py --config-file config.json
```

### 方式 3：Python 代码（最灵活）
```python
from main import main
main(config_data={"USER":"email@example.com","PWD":"password"})
```

---

## 📚 文档导航图

```
你想做什么？

├─ 快速上手本地运行？
│  └─ 👉 LOCAL_SETUP.md (3步，10分钟)
│
├─ 查看常用命令？
│  └─ 👉 QUICK_START.md (速查表)
│
├─ 全面了解所有功能？
│  └─ 👉 USAGE_STANDALONE.md (完整指南)
│
├─ 在 Python 代码中使用？
│  └─ 👉 example_usage.py (7个示例)
│
├─ 了解改进细节？
│  └─ 👉 IMPROVEMENTS.md (技术说明)
│
├─ 查看配置文件格式？
│  └─ 👉 config_example.json (模板)
│
├─ 看改进完成报告？
│  └─ 👉 COMPLETION_REPORT.md (全面报告)
│
└─ 我用 GitHub Actions
   └─ 👉 无需改变，继续使用！✅
```

---

## 💡 我的建议

**按这个顺序阅读：**

1. **这个文件** ← 你现在正在看 ✓
2. **LOCAL_SETUP.md** ← 快速上手（推荐首先）
3. **QUICK_START.md** ← 保存为速查表
4. **其他文档** ← 根据需要查看

---

## ✨ 核心改进一览

| 之前 | 现在 |
|-----|------|
| ❌ 只能 GitHub Actions | ✅ 本地、GitHub Actions、定时任务都支持 |
| ❌ 必须环境变量 | ✅ 命令行、配置文件、Python 代码都支持 |
| ❌ 文档很少 | ✅ 9 篇详细文档 |
| ✅ 支持单账号 | ✅ 还支持多账号、加密、推送等 |

---

## 🎯 下一步行动

选择一个开始：

- **🟢 新手** → 打开 `LOCAL_SETUP.md`
- **🟡 快速上手** → 打开 `QUICK_START.md`  
- **🔵 详细学习** → 打开 `USAGE_STANDALONE.md`
- **💻 开发者** → 打开 `example_usage.py`
- **🤖 GitHub Actions 用户** → 无需改变，享受新的本地运行功能

---

**还有问题？** 所有答案都在对应的文档中。祝你使用愉快！🎉

