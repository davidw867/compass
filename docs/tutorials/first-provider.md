# First Provider Tutorial

This tutorial explains how to add a new LLM provider integration under providers/.

Overview
- Purpose: Integrate a provider (OpenAI, Anthropic, Mistral, etc.) so that agents can call different model endpoints via a common interface.
- Scope: Provider adapter pattern, configuration, and an example request/response flow.

Steps
1. Create a new provider directory under providers/ (e.g., providers/example-provider).
2. Implement the provider adapter to expose methods such as `createCompletion`, `chat`, and `healthCheck`.
3. Wire configuration (API keys, base URLs) via the project's config system.
4. Add tests to verify the provider's adapter behavior (mocking external calls).

Example

Pseudo-code adapter:

```pseudo
class ExampleProviderAdapter {
  constructor(config) { this.config = config }
  async chat(messages) {
    // perform HTTP call to provider using this.config.apiKey
    return response
  }
}
```

Security
- Do not log sensitive API keys.
- Rate limit retries and backoff logic should be implemented.

