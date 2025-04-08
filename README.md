# Telegram Anti-Spam Bot

这是一个用于自动监管 Telegram 群组的机器人，功能包括：
- 自动删除所有包含链接的消息；
- 自动删除引用外部频道/群的消息（不包括本群内的回复）；
- 部署到 Railway 后可 24 小时在线运行。

## 使用方式

1. 修改 `bot.py` 中的 `BOT_TOKEN` 为你的 Bot Token。
2. 上传到 GitHub 或本地运行。
3. Railway 部署指令：`python bot.py`
