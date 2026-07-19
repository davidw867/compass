# First Agent Tutorial

This tutorial walks you through creating your first agent in the Compass/Systrix framework.

Overview
- Purpose: Create a minimal, working agent that can receive a prompt and return a response.
- Scope: Introduction-level; focuses on directory layout, configuration, and a minimal example.

Steps
1. Create a new folder under agents/ (e.g., agents/example-agent) and add an entrypoint.
2. Implement the agent interface defined in shared/interfaces/ (see shared/interfaces/README.md for placeholders).
3. Add configuration for the agent (credentials, scopes) in a secure config store.
4. Run the agent locally and test with a sample prompt.

Example

Here's a simple pseudo-code example to demonstrate the lifecycle:

```pseudo
// Initialise agent
agent = new Agent("first-agent")
agent.registerHandler(async (prompt) => {
  // simple echo behaviour
  return `Received: ${prompt}`
})

// Run agent
await agent.run()
```

Next steps
- Expand the handler to call an LLM provider from providers/ and add retries/error handling.
- Add unit tests under tests/unit for agent behaviour.

