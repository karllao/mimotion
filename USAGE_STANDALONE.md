# 独立运行使用指南

本文档说明如何在不依赖 GitHub Actions 的情况下运行刷步数程序。

## 安装依赖

```bash
pip install -r requirements.txt
```

或者使用 pyproject.toml：

```bash
pip install pycryptodome>=3.23.0 pytz>=2025.2 requests>=2.32.5
```

## 使用方式

### 方式1：通过命令行参数运行

#### 基础用法 - 单账号

```bash
python main.py --config '{"USER":"user@example.com","PWD":"password","MIN_STEP":"18000","MAX_STEP":"25000"}'
```

#### 完整配置 - 包含所有选项

```bash
python main.py --config '{"USER":"user@example.com","PWD":"password","MIN_STEP":"18000","MAX_STEP":"25000","PUSH_PLUS_TOKEN":"","PUSH_PLUS_HOUR":"","SLEEP_GAP":"5","USE_CONCURRENT":"False"}'
```

#### 多账号运行（用#分隔账号和密码）

```bash
python main.py --config '{"USER":"user1@example.com#user2@example.com","PWD":"pwd1#pwd2","MIN_STEP":"18000","MAX_STEP":"25000"}'
```

#### 使用 AES 加密密钥保存登录信息

```bash
python main.py --config '{"USER":"user@example.com","PWD":"password","MIN_STEP":"18000","MAX_STEP":"25000"}' --aes-key "1234567890123456"
```

注意：AES密钥必须是16个字符

### 方式2：通过配置文件运行

#### 1. 创建配置文件 config.json

复制 `config_example.json` 并修改为：

```json
{
  "USER": "your_email@example.com",
  "PWD": "your_password",
  "MIN_STEP": "18000",
  "MAX_STEP": "25000",
  "PUSH_PLUS_TOKEN": "your_pushplus_token",
  "PUSH_PLUS_HOUR": "22",
  "PUSH_PLUS_MAX": "30",
  "SLEEP_GAP": "5",
  "USE_CONCURRENT": "False"
}
```

#### 2. 运行程序

```bash
python main.py --config-file config.json --aes-key "1234567890123456"
```

### 方式3：在Python代码中调用

```python
from main import main

# 配置字典
config = {
    "USER": "user@example.com",
    "PWD": "password",
    "MIN_STEP": "18000",
    "MAX_STEP": "25000"
}

# 直接调用主函数
main(config_data=config, aes_key_str="1234567890123456")
```

或者通过 JSON 字符串：

```python
from main import main
import json

config_json = '{"USER":"user@example.com","PWD":"password","MIN_STEP":"18000","MAX_STEP":"25000"}'
main(config_data=config_json, aes_key_str="1234567890123456")
```

## 配置参数说明

| 参数 | 必须 | 说明 | 示例 |
|-----|------|------|-----|
| USER | ✅ | 小米运动登录账号（邮箱或手机号） | user@example.com 或 13800138000 |
| PWD | ✅ | 小米运动登录密码 | password123 |
| MIN_STEP | ❌ | 最小步数（默认18000） | 18000 |
| MAX_STEP | ❌ | 最大步数（默认25000） | 25000 |
| PUSH_PLUS_TOKEN | ❌ | pushplus推送token | - |
| PUSH_PLUS_HOUR | ❌ | 限制推送的整点（0-23） | 22 |
| PUSH_PLUS_MAX | ❌ | 最多推送账号数（默认30） | 30 |
| SLEEP_GAP | ❌ | 多账号执行间隔（秒，默认5） | 5 |
| USE_CONCURRENT | ❌ | 是否使用多线程（False/True） | False |

## 多账号配置

如果需要运行多个账号，使用 `#` 作为分隔符：

```json
{
  "USER": "user1@example.com#user2@example.com#13800138000",
  "PWD": "password1#password2#password3",
  "MIN_STEP": "18000",
  "MAX_STEP": "25000"
}
```

**注意：** USER 和 PWD 分隔的账号数量必须相同！

## AES 密钥加密说明

- **AES_KEY**: 必须是16个字符的字符串，用于加密保存登录令牌
- 第一次使用新的AES密钥时，程序会自动加密保存登录信息到 `encrypted_tokens.data`
- 之后登录时会优先使用已保存的令牌，减少登录次数
- **请妥善保管密钥，不要泄露！**

## 环境变量支持（GitHub Actions 兼容）

程序同时支持通过环境变量配置（用于 GitHub Actions）：

```bash
export CONFIG='{"USER":"user@example.com","PWD":"password",...}'
export AES_KEY="1234567890123456"
python main.py
```

## 定时执行

### Windows 定时任务

1. 打开任务计划程序（Task Scheduler）
2. 创建基本任务
3. 设置触发器（例如每天22:00）
4. 设置操作：程序为 `python.exe`，参数为 `main.py --config-file config.json`

### Linux/Mac Crontab

在 crontab 中添加（每天22:00执行）：

```bash
0 22 * * * cd /path/to/mimotion && python main.py --config-file config.json
```

## 常见问题

### Q: 提示"密钥不正确或者加密内容损坏"？
A: 这通常是第一次使用新的AES密钥时的正常现象。程序会自动生成新的加密文件，下次运行就正常了。

### Q: 刷步数失败怎么办？
A: 
1. 检查账号密码是否正确
2. 建议先到官方网站验证账号（https://steps.hubp.de/）
3. 检查网络连接
4. 查看详细的错误日志输出

### Q: 支持哪些账号类型？
A: 仅支持小米运动/Zepp Life 账号对应的邮箱或手机号，不支持小米账号

## 获取帮助

运行以下命令查看完整的命令行帮助：

```bash
python main.py --help
```
