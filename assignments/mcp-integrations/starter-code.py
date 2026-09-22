class MCPTool:
    def __init__(self, name, description, handler):
        self.name = name
        self.description = description
        self.handler = handler


class MCPClient:
    def __init__(self, tools):
        self.tools = {tool.name: tool for tool in tools}

    def call_tool(self, tool_name, **kwargs):
        if tool_name not in self.tools:
            return {"status": "error", "message": f"Tool '{tool_name}' not found."}

        tool = self.tools[tool_name]
        return tool.handler(**kwargs)


# Example tools

def get_weather(city):
    return {"status": "success", "city": city, "temperature": "22C", "condition": "Sunny"}


def lookup_ticket(ticket_id):
    return {"status": "success", "ticket_id": ticket_id, "status": "Open", "assignee": "Alex"}


tools = [
    MCPTool("get_weather", "Returns weather information for a city.", get_weather),
    MCPTool("lookup_ticket", "Returns data for a support ticket.", lookup_ticket),
]

client = MCPClient(tools)

print(client.call_tool("get_weather", city="Lisbon"))
print(client.call_tool("lookup_ticket", ticket_id="INC-1042"))
print(client.call_tool("missing_tool", city="Paris"))
