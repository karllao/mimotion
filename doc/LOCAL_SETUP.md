# 🎯 本地运行指南 (仅 3 步)

> 如果你想在自己的电脑上运行刷步数程序，而不是用 GitHub Actions，这个指南就是给你的！

## 第一步：安装依赖（一次性）

```bash
pip install pycryptodome pytz requests
```

## 第二步：准备配置

### 方法 A：快速开始（推荐新手）

```bash
python main.py --config '{"USER":"your_email@example.com","PWD":"your_password"}'
```

将 `your_email@example.com` 和 `your_password` 替换为你的小米运动账号和密码。

### 方法 B：使用配置文件（推荐长期使用）

1. 复制 `config_example.json` 为 `config.json`
2. 编辑 `config.json`，填入你的账号信息：
   ```json
   {
     "USER": "your_email@example.com",
     "PWD": "your_password",
     "MIN_STEP": "18000",
     "MAX_STEP": "25000"
   }
   ```
3. 添加到 `.gitignore`（防止泄露密码）：
   ```bash
   echo config.json >> .gitignore
   ```

## 第三步：运行

```bash
# 方法 A 对应
python main.py --config '{"USER":"your_email@example.com","PWD":"your_password"}'

# 方法 B 对应
python main.py --config-file config.json
```

## ✅ 就这样！

如果看到类似下面的输出说明成功了：

```
[2025-11-15 22:00:00]
账号：user***om
已设置为随机步数范围(18000~25000) 随机值:21234
修改步数（21234）[success]
```

---

## 🔧 进阶用法

### 保存登录令牌（避免每次输入密码）

```bash
python main.py --config-file config.json --aes-key "1234567890123456"
```

注意：AES 密钥必须是 16 个字符

### 运行多个账号

在 `config.json` 中用 `#` 分隔：

```json
{
  "USER": "user1@example.com#user2@example.com",
  "PWD": "password1#password2"
}
```

### 启用推送通知

在 config.json 中添加：

```json
{
  "PUSH_PLUS_TOKEN": "你的pushplus_token",
  "PUSH_PLUS_HOUR": "22"
}
```

申请 pushplus token：https://www.pushplus.plus/

---

## ⏰ 设置定时运行

### Windows（任务计划程序）

1. 打开 "任务计划程序"
2. 创建基本任务
3. **触发器**：每天 22:00
4. **操作**：
   - 程序：`python.exe` 的完整路径
   - 参数：`main.py --config-file config.json`
   - 开始位置：项目目录路径

### Linux/Mac（Crontab）

```bash
# 编辑 crontab
crontab -e

# 添加这一行（每天 22:00 运行）
0 22 * * * cd /path/to/mimotion && /usr/bin/python3 main.py --config-file config.json
```

---

## ❓ 遇到问题？

| 问题 | 解决方案 |
|-----|--------|
| **提示"账号或密码错误"** | 检查 config.json 中的 USER 和 PWD 是否正确 |
| **提示"ModuleNotFoundError"** | 运行 `pip install pycryptodome pytz requests` |
| **长时间无反应** | 可能网络较慢，耐心等待或检查网络连接 |
| **刷步数失败** | 建议先到 https://steps.hubp.de/ 验证账号 |
| **密钥错误提示** | 第一次使用新密钥是正常的，下次就好了 |

---

## 📚 更多信息

- 📖 完整文档：[USAGE_STANDALONE.md](USAGE_STANDALONE.md)
- ⚡ 快速参考：[QUICK_START.md](QUICK_START.md)
- 💡 代码示例：[example_usage.py](example_usage.py)
- ✨ 改进说明：[IMPROVEMENTS.md](IMPROVEMENTS.md)

---

## 🎁 福利

现在你可以：

✅ **本地运行** - 不再依赖 GitHub  
✅ **灵活配置** - 支持文件、命令行、Python 代码  
✅ **定时运行** - 与任何定时系统集成  
✅ **多账号** - 批量管理多个账号  
✅ **加密保存** - AES 加密保护密码  

所有这些，同时保留对 GitHub Actions 的完全支持！

---

**Happy automating! 🎉**
