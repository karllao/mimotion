# 快速参考指南

## 🚀 最快开始方式

### 1. 单账号 - 最简单

```bash
python main.py --config '{"USER":"your_email@example.com","PWD":"your_password","MIN_STEP":"18000","MAX_STEP":"25000"}'
```

### 2. 多账号 - 使用 # 分隔

```bash
python main.py --config '{"USER":"user1@example.com#user2@example.com","PWD":"pwd1#pwd2","MIN_STEP":"18000","MAX_STEP":"25000"}'
```

### 3. 从配置文件 - 推荐生产环境

```bash
python main.py --config-file config.json
```

### 4. 在 Python 代码中调用

```python
from main import main

config = {"USER":"your_email@example.com","PWD":"your_password"}
main(config_data=config)
```

---

## 📋 配置项速查表

### 必需项
- **USER**: 小米运动账号（邮箱或手机号）
- **PWD**: 小米运动密码

### 可选项
- **MIN_STEP**: 最小步数，默认 18000
- **MAX_STEP**: 最大步数，默认 25000
- **PUSH_PLUS_TOKEN**: pushplus推送token，留空则不推送
- **PUSH_PLUS_HOUR**: 推送的整点小时（0-23），留空则每次都推送
- **SLEEP_GAP**: 多账号间隔秒数，默认 5
- **USE_CONCURRENT**: 是否多线程，默认 False

---

## 🔐 AES 密钥加密

保存登录令牌，避免每次都要输入密码：

```bash
python main.py --config-file config.json --aes-key "1234567890123456"
```

**关键点**：
- 密钥必须是16个字符
- 不要泄露密钥
- 加密后的令牌保存在 `encrypted_tokens.data`

---

## ⏰ 定时执行

### Windows 任务计划器
```
程序: python.exe
参数: main.py --config-file config.json
```

### Linux/Mac Crontab
```bash
0 22 * * * cd /path/to/mimotion && python main.py --config-file config.json
```

---

## 🛠️ 常见操作

| 需求 | 命令 |
|-----|------|
| 查看帮助 | `python main.py --help` |
| 单账号 | `python main.py --config '{"USER":"xxx","PWD":"yyy"}'` |
| 多账号 | `python main.py --config '{"USER":"u1#u2","PWD":"p1#p2"}'` |
| 配置文件 | `python main.py --config-file config.json` |
| 带密钥 | `python main.py --config-file config.json --aes-key "key16chars"` |

---

## 📚 详细文档

- 完整使用指南：查看 `USAGE_STANDALONE.md`
- Python 调用示例：查看 `example_usage.py`
- 配置文件示例：查看 `config_example.json`

---

## ⚠️ 注意事项

1. **账号密码**：USER 和 PWD 的分隔符是 `#`，多账号时数量必须相等
2. **AES密钥**：必须是16个字符，否则无法加密
3. **时间范围**：步数范围会随着北京时间增长，22点达到最大值
4. **接口限制**：同IP多账号登录过频繁可能被限制(429)，建议设置 SLEEP_GAP

---

## 🔗 相关链接

- pushplus 申请：https://www.pushplus.plus/
- 账号测试：https://steps.hubp.de/
- 项目仓库：https://github.com/TonyJiangWJ/mimotion

---

## 📞 遇到问题？

1. 检查网络连接
2. 验证账号密码是否正确
3. 查看错误日志输出
4. 阅读详细文档 `USAGE_STANDALONE.md`
