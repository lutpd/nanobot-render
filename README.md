---
title: nanobot AI Assistant
emoji: 🐈
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
---

# nanobot AI Assistant

Ultra-lightweight personal AI assistant running on Hugging Face Spaces with Telegram integration.

## Configuration

This Space requires the following secrets to be configured in the Space Settings:

- `APIKEY`: Your OpenAI-compatible API key
- `APIBASE`: Your API base URL (e.g., https://opencode.ai/zen/v1)
- `MODELID`: The model ID to use (e.g., minimax-m2.5-free)
- `TELEGRAMTOKEN`: Your Telegram bot token from @BotFather

## Features

- 🤖 AI-powered conversations
- 💬 Telegram integration
- 🧠 Memory and context awareness
- 🛠️ Tool use capabilities
- ⏰ Scheduled tasks support

## How to Use

1. Fork this Space
2. Go to Settings → Secrets and add your API credentials
3. Restart the Space
4. Message your Telegram bot!
