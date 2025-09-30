#!/usr/bin/env bash
# Inicia a aplicação Python usando Uvicorn, como definido no Procfile

exec uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}