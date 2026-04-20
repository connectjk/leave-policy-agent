# Deployment Guide – Leave-Policy-Agent

## Overview
This project is structured for deployment to **Azure AI Foundry** using the
Azure Developer CLI (`azd`) with the Foundry agent extension.

## Prerequisites
- [Azure Developer CLI (azd)](https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/)
- Azure subscription with AI Foundry access
- Python 3.10+

## Using the Foundry azd Agent Extension

The Foundry azd agent extension supports importing agent definitions and
scaffolding deployment environments.

Reference: https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/extensions/azure-ai-foundry-extension

### Workflow

1. **Initialize your environment** – Use `azd init` to set up the project
   scaffold with Foundry-compatible templates.

2. **Import agent definition** – The `agent.yaml` in this repository follows
   the Microsoft Agent Framework declarative agent format. The azd Foundry
   extension can import this definition to configure your agent in Foundry.

3. **Configure environment variables** – Copy `.env.example` to `.env` and
   fill in your Azure resource details. The `azd` workflow will use these
   during provisioning and deployment.

4. **Provision & Deploy** – Use standard `azd` commands to provision cloud
   resources and deploy the agent service.

## SDK-Based Agent Creation
For programmatic agent creation, see `src/foundry_create_agent.py` which
demonstrates using `AIProjectClient` and `PromptAgentDefinition`.

Reference: https://learn.microsoft.com/en-us/azure/foundry/quickstarts/get-started-code

## CI/CD Notes
- No secrets should be committed to this repository.
- Use environment variables or Azure Key Vault for sensitive configuration.
- The repo layout is designed to be CI/CD-friendly with clear separation of
  source code, tests, and deployment configuration.
