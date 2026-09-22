# 📘 Assignment: MCP in Integration Development

## 🎯 Objective

Explore how Model Context Protocol (MCP) can be used to connect AI-powered tools to external systems such as APIs, data sources, and internal services. In this activity, students will design a simple integration flow that uses MCP concepts to make a tool or workflow more structured, reusable, and maintainable.

## 📝 Tasks

### 🛠️ Understand the MCP Concept

#### Description
Research the basic idea behind MCP and explain how it helps standardize communication between AI clients and tools.

#### Requirements
The completed activity must:

- Define what MCP is in your own words.
- Explain why it is useful in integrations.
- Identify at least three common scenarios where MCP improves system interoperability.
- Write a short summary of the benefits of a protocol-based approach compared to hardcoded tool calls.

### 🛠️ Design an Integration Workflow

#### Description
Plan an integration that connects an AI assistant to a real-world system, such as a ticketing system, weather API, or project board.

#### Requirements
The completed activity must:

- Select one external system to integrate.
- Describe the inputs the system receives.
- Describe the outputs it returns.
- Define the main actions that an AI assistant should be able to trigger.
- Present the workflow as a simple sequence of steps or a diagram in text.

### 🛠️ Build a Minimal MCP-Inspired Client

#### Description
Create a small Python script that simulates an MCP-like interaction between a client and a set of tools.

#### Requirements
The completed project must:

- Include a `Tool` or `MCPTool` structure with a name and description.
- Define at least two actions, such as `get_weather`, `lookup_ticket`, or `search_docs`.
- Create a client that chooses a tool based on a user request.
- Return a formatted result showing which tool was called and what data was returned.
- Keep the code clean and easy to extend.

### 🛠️ Add Error Handling and Observability

#### Description
Improve the integration by handling invalid requests, missing data, and tool execution problems.

#### Requirements
The completed project must:

- Validate user input before calling a tool.
- Return a clear error message when a tool is missing or a parameter is invalid.
- Log important events, such as which tool was called and the result status.
- Add a final reflection explaining how this pattern scales in a real production environment.

## ✅ Challenge Extension

Try to add one of the following improvements:

- Support multiple tools with automatic routing based on intent.
- Add a mock API response layer to simulate external system calls.
- Build a small JSON schema for tool inputs and outputs.
- Add documentation describing how the integration would work in a real MCP server.

## 💡 Tips

- Think of MCP as a standard way for tools and clients to communicate clearly.
- Keep the exercise focused on a single workflow instead of trying to build a full platform.
- Use realistic examples that connect AI behavior to a system that students already understand, like help desk tools or data lookup apps.
