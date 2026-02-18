FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl ca-certificates gnupg git && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy project files
COPY pyproject.toml README.md ./
COPY nanobot/ nanobot/
COPY bridge/ bridge/

# Install nanobot
RUN uv pip install --system --no-cache .

# Create config directory
RUN mkdir -p /root/.nanobot

# Copy startup script and health server
COPY start.sh /app/start.sh
COPY health_server.py /app/health_server.py
RUN chmod +x /app/start.sh

# Expose ports (10000 for Render health checks, 7860 for nanobot)
EXPOSE 10000
EXPOSE 7860

# Start the bot
CMD ["/app/start.sh"]
