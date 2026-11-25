"""Tenant and app-registration settings.

Values are read from environment variables so no secrets live in source control.
See .env.example for the variable names.
"""
import os

TENANT_ID = os.environ["ENTRA_TENANT_ID"]
CLIENT_ID = os.environ["ENTRA_CLIENT_ID"]
CLIENT_SECRET = os.environ["ENTRA_CLIENT_SECRET"]
