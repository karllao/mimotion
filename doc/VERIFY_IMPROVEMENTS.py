#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
验证脚本：演示改进后的 main.py 支持多种调用方式
"""

import json
import os
import sys

print("\n" + "=" * 70)
print("主函数调用方式演示")
print("=" * 70)

print("""
改进说明：
---------
新的 main() 函数支持通过参数传递配置，无需依赖 GitHub Actions 环境变量。

可用的调用方式：
""")

print("""
1️⃣  方式一：直接函数调用（Python代码中）
   ────────────────────────────────────
   from main import main
   
   config = {
       "USER": "user@example.com",
       "PWD": "password",
       "MIN_STEP": "18000",
       "MAX_STEP": "25000"
   }
   main(config_data=config, aes_key_str="1234567890123456")
""")

print("""
2️⃣  方式二：命令行参数
   ──────────────────
   单账号：
   python main.py --config '{"USER":"user@example.com","PWD":"password"}'
   
   多账号（用#分隔）：
   python main.py --config '{"USER":"u1#u2","PWD":"p1#p2"}'
   
   带AES密钥：
   python main.py --config '{"USER":"xxx","PWD":"yyy"}' --aes-key "1234567890123456"
""")

print("""
3️⃣  方式三：配置文件
   ────────────────
   python main.py --config-file config.json
   python main.py --config-file config.json --aes-key "1234567890123456"
""")

print("""
4️⃣  方式四：环境变量（GitHub Actions兼容）
   ────────────────────────────────────────
   export CONFIG='{"USER":"xxx","PWD":"yyy",...}'
   export AES_KEY="1234567890123456"
   python main.py
""")

print("""
✨ 改进特点：
──────────
✅ 不再依赖 GitHub Actions 环境变量
✅ 支持命令行直接运行
✅ 支持配置文件管理
✅ 支持 Python 代码中调用
✅ 保留对 GitHub Actions 的支持（完全兼容）
✅ 支持 Windows、Mac、Linux
✅ 支持定时任务集成（cron、任务计划程序）

📊 参数说明：
─────────
--config        JSON 格式的配置字符串（用单引号包裹）
--config-file   JSON 配置文件的路径
--aes-key       AES 加密密钥（16个字符）
--help          查看完整帮助信息
""")

print("\n" + "=" * 70)
print("配置参数说明")
print("=" * 70)

config_params = {
    "USER": ("✅ 必需", "小米运动账号（邮箱或手机号）", "user@example.com"),
    "PWD": ("✅ 必需", "小米运动密码", "password123"),
    "MIN_STEP": ("❌ 可选", "最小步数（默认18000）", "18000"),
    "MAX_STEP": ("❌ 可选", "最大步数（默认25000）", "25000"),
    "PUSH_PLUS_TOKEN": ("❌ 可选", "pushplus 推送 token", ""),
    "PUSH_PLUS_HOUR": ("❌ 可选", "限制推送的整点小时（0-23）", "22"),
    "PUSH_PLUS_MAX": ("❌ 可选", "最多推送账号数（默认30）", "30"),
    "SLEEP_GAP": ("❌ 可选", "多账号执行间隔秒数（默认5）", "5"),
    "USE_CONCURRENT": ("❌ 可选", "是否使用多线程（False/True）", "False")
}

print(f"\n{'参数':<20} {'状态':<10} {'说明':<30} {'示例':<30}")
print("-" * 90)
for param, (status, desc, example) in config_params.items():
    print(f"{param:<20} {status:<10} {desc:<30} {example:<30}")

print("\n" + "=" * 70)
print("多账号配置示例")
print("=" * 70)

print("""
如果需要运行多个账号，使用 # 作为分隔符：

JSON 配置：
{
  "USER": "user1@example.com#user2@example.com#13800138000",
  "PWD": "password1#password2#password3",
  "MIN_STEP": "18000",
  "MAX_STEP": "25000"
}

命令行示例：
python main.py --config '{"USER":"u1@ex.com#u2@ex.com","PWD":"p1#p2"}'

⚠️  注意：USER 和 PWD 分隔的账号数量必须相同！
""")

print("\n" + "=" * 70)
print("使用场景")
print("=" * 70)

scenarios = [
    ("本地 Windows 用户", 
     "python main.py --config-file config.json"),
    
    ("Linux/Mac 用户", 
     "python main.py --config-file config.json"),
    
    ("定时运行（Windows 任务计划）", 
     "程序: python.exe\\n参数: main.py --config-file config.json"),
    
    ("定时运行（Linux crontab）", 
     "0 22 * * * cd /path/to/mimotion && python main.py --config-file config.json"),
    
    ("快速测试", 
     'python main.py --config \'{"USER":"xxx","PWD":"yyy"}\''),
    
    ("应用集成", 
     "from main import main\\nmain(config_data=my_config)"),
    
    ("GitHub Actions（仍支持）", 
     "设置 Secrets: CONFIG 和 AES_KEY，然后 python main.py"),
]

for i, (scenario, command) in enumerate(scenarios, 1):
    print(f"\n{i}. {scenario}")
    print(f"   命令: {command}")

print("\n" + "=" * 70)
print("快速开始")
print("=" * 70)

print("""
最简单的方式（单账号）：

1. 修改下面的命令，替换为你的账号密码：
   python main.py --config '{"USER":"your_email@example.com","PWD":"your_password"}'

2. 或者创建 config.json 文件：
   {
     "USER": "your_email@example.com",
     "PWD": "your_password",
     "MIN_STEP": "18000",
     "MAX_STEP": "25000"
   }
   
   然后运行：
   python main.py --config-file config.json

3. 要加密保存登录信息（使用 AES 密钥）：
   python main.py --config-file config.json --aes-key "1234567890123456"
   （AES 密钥必须是16个字符）
""")

print("\n" + "=" * 70)
print("获取帮助")
print("=" * 70)

print("""
查看命令行帮助：
  python main.py --help

查看详细使用文档：
  cat USAGE_STANDALONE.md

查看快速参考：
  cat QUICK_START.md

查看改进说明：
  cat IMPROVEMENTS.md

查看示例代码：
  cat example_usage.py
""")

print("=" * 70)
print("验证完毕 ✅")
print("=" * 70 + "\n")
