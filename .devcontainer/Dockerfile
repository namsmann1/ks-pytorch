FROM ghcr.io/astral-sh/uv:0.12.21 AS uv
FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm

COPY --from=uv /uv /uvx /usr/local/bin/
ENV UV_LINK_MODE=copy
