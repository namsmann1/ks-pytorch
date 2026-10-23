FROM ghcr.io/astral-sh/uv:0.13.5 AS uv
FROM mcr.microsoft.com/devcontainers/python:3-3.12-bookworm

COPY --from=uv /uv /uvx /usr/local/bin/
ENV UV_LINK_MODE=copy
