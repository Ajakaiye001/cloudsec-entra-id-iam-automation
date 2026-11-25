# Microsoft Entra ID — Automated Onboarding & Identity Protection

Python + Microsoft Graph automation that bulk-provisions users into Entra ID from a CSV, as the first step of an identity-governance build-out (groups, Administrative Units, Conditional Access, PIM).

```bash
cd provisioning
pip install -r requirements.txt
# set ENTRA_TENANT_ID, ENTRA_CLIENT_ID, ENTRA_CLIENT_SECRET (see .env.example)
python create_users.py
```

Work in progress.
