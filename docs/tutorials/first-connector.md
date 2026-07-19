# First Connector Tutorial

This tutorial shows how to create a connector (e.g., to GitHub, Google Drive) for use by agents and other components.

Overview
- Purpose: Implement a connector that exposes a consistent interface for reading and writing data from a third-party service.
- Scope: Basic connector structure, authentication hints, and a small example.

Steps
1. Create a new connector directory under connectors/ (e.g., connectors/example).
2. Implement the connector interface (see shared/interfaces/connector.md or shared/interfaces/README.md).
3. Add secure storage for credentials and environment variables.
4. Provide a minimal example client that performs an authenticated API call.

Example

Pseudo-code:

```pseudo
connector = new Connector("example-connector")
await connector.authenticate({apiKey: process.env.EXAMPLE_API_KEY})
files = await connector.listFiles("/path")
return files
```

Notes
- Always follow the provider's recommended auth flows (OAuth2 for Google, personal access tokens for GitHub, etc.).
- Keep secrets out of source control — use environment variables or a secrets manager.

