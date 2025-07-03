#!/usr/bin/env python3
"""
Divergent Thinking MCP Server
An MCP server that enhances divergent thinking and creativity through prompt engineering
and context design, leveraging existing Agent/LLM capabilities.
"""

import asyncio
from typing import List, Dict, Any
from mcp.server.models import InitializationOptions
from mcp.server import NotificationOptions, Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool
import mcp.types as types
from jinja2 import Environment, BaseLoader


app = Server("divergent_thinking_mcp")


@app.list_tools()
async def handle_list_tools() -> list[Tool]:
    """List available divergent thinking tools."""
    return [
        Tool(
            name="divergent_thinking",
            description="A comprehensive tool for generating creative thoughts and branches through structured divergent thinking processes.\n\nThis tool facilitates non-linear idea generation by exploring multiple thinking paths, questioning assumptions, and combining diverse perspectives. It helps break through mental blocks by systematically applying creative thinking techniques.\n\nWhen to use this tool:\n- Generating multiple solutions to a single problem\n- Exploring creative alternatives to conventional approaches\n- Breaking out of linear thinking patterns\n- Developing innovative concepts or ideas\n- Expanding on initial ideas with diverse perspectives\n- Creating branching thought pathways\n\nKey features:\n- Supports both linear thought progression and branching exploration\n- Applies various creative thinking techniques through prompt_type parameter\n- Maintains thought history for context-aware generation\n- Allows introduction of creative constraints\n- Enables perspective shifting to generate alternative insights\n- Combines multiple thoughts into novel concepts\n\nParameters explained:\n- thought: Current thinking step or idea to build upon\n- thoughtNumber: Position of current thought in sequence (for tracking progress)\n- totalThoughts: Expected number of thoughts in the complete sequence\n- nextThoughtNeeded: Whether to generate another thought in the current path\n- generate_branches: If true, creates multiple divergent paths from current thought\n- prompt_type: Technique to apply (branch_generation, creative_constraint, perspective_shift, combination)\n- constraint: Creative limitation to apply when prompt_type is creative_constraint\n- perspective_type: Viewpoint to adopt when prompt_type is perspective_shift\n- branchId: Identifier for tracking specific thought branches\n\nUsage guidelines:\n1. Start with a clear initial thought or problem statement\n2. Use generate_branches=true to explore multiple directions\n3. Apply different prompt_types to stimulate diverse thinking\n4. Adjust totalThoughts as your exploration expands\n5. Use branchId to track promising thought pathways\n6. Combine insights from different branches for innovative solutions\n7. Continue until nextThoughtNeeded=false when ideas are sufficiently developed",
            inputSchema={
                "type": "object",
                "properties": {
                    "thought": {
                        "type": "string",
                        "description": "Current thought to process",
                    },
                    "thoughtNumber": {
                        "type": "integer",
                        "description": "Current thought number",
                    },
                    "totalThoughts": {
                        "type": "integer",
                        "description": "Total number of thoughts expected",
                    },
                    "nextThoughtNeeded": {
                        "type": "boolean",
                        "description": "Whether another thought is needed",
                    },
                    "generate_branches": {
                        "type": "boolean",
                        "description": "Whether to generate branches from this thought",
                        "default": "false",
                    },
                    "prompt_type": {
                        "type": "string",
                        "enum": [
                            "branch_generation",
                            "creative_constraint",
                            "perspective_shift",
                            "combination",
                        ],
                        "description": "Type of prompt to generate",
                        "default": "creative_constraint",
                    },
                    "constraint": {
                        "type": "string",
                        "description": "Creative constraint to apply",
                    },
                    "perspective_type": {
                        "type": "string",
                        "enum": [
                            "inanimate_object",
                            "abstract_concept",
                            "impossible_being",
                        ],
                        "description": "Type of perspective to use for shift",
                    },
                    "branchId": {
                        "type": "string",
                        "description": "Branch identifier if this is part of a branch",
                    },
                },
                "required": [
                    "thought",
                    "thoughtNumber",
                    "totalThoughts",
                    "nextThoughtNeeded",
                ],
            },
        ),
        Tool(
            name="generate_branches",
            description="Generate multiple creative branches from a single thought",
            inputSchema={
                "type": "object",
                "properties": {
                    "thought": {
                        "type": "string",
                        "description": "Thought to generate branches from",
                    }
                },
                "required": ["thought"],
            },
        ),
        Tool(
            name="perspective_shift",
            description="Shift perspective on a thought to generate new insights",
            inputSchema={
                "type": "object",
                "properties": {
                    "thought": {
                        "type": "string",
                        "description": "Thought to shift perspective on",
                    },
                    "perspective_type": {
                        "type": "string",
                        "enum": [
                            "inanimate_object",
                            "abstract_concept",
                            "impossible_being",
                        ],
                        "description": "Type of perspective to use",
                        "default": "inanimate_object",
                    },
                },
                "required": ["thought"],
            },
        ),
        Tool(
            name="creative_constraint",
            description="Apply creative constraints to transform a thought",
            inputSchema={
                "type": "object",
                "properties": {
                    "thought": {
                        "type": "string",
                        "description": "Thought to transform",
                    },
                    "constraint": {
                        "type": "string",
                        "description": "Creative constraint to apply",
                        "default": "introduce an impossible element",
                    },
                },
                "required": ["thought"],
            },
        ),
        Tool(
            name="combine_thoughts",
            description="Combine two divergent thoughts into something new",
            inputSchema={
                "type": "object",
                "properties": {
                    "thought1": {
                        "type": "string",
                        "description": "First thought to combine",
                    },
                    "thought2": {
                        "type": "string",
                        "description": "Second thought to combine",
                    },
                },
                "required": ["thought1", "thought2"],
            },
        ),
    ]


@app.call_tool()
async def handle_call_tool(
    name: str, arguments: dict | None
) -> list[types.TextContent]:
    """Handle tool calls for divergent thinking functions using prompt engineering"""
    server = DivergentThinkingServer()
    thought_data = arguments or {}

    try:
        if name == "divergent_thinking":
            # Process thought using the DivergentThinkingServer
            result = server.process_thought(thought_data)
            return [types.TextContent(type="text", text=str(result))]

        elif name == "generate_branches":
            # Generate branch prompt
            prompt = server.generate_prompt(
                "branch_generation", thought=thought_data.get("thought", "")
            )
            return [types.TextContent(type="text", text=prompt)]

        elif name == "perspective_shift":
            # Generate perspective shift prompt
            prompt = server.generate_prompt(
                "perspective_shift",
                thought=thought_data.get("thought", ""),
                perspective_type=thought_data.get(
                    "perspective_type", "alive_object"
                ),
            )
            return [types.TextContent(type="text", text=prompt)]

        elif name == "creative_constraint":
            # Generate creative constraint prompt
            prompt = server.generate_prompt(
                "creative_constraint",
                thought=thought_data.get("thought", ""),
                constraint=thought_data.get(
                    "constraint", "make it impossible but logical"
                ),
            )
            return [types.TextContent(type="text", text=prompt)]

        elif name == "combine_thoughts":
            # Generate combination prompt
            prompt = server.generate_prompt(
                "combination",
                thought1=thought_data.get("thought1", ""),
                thought2=thought_data.get("thought2", ""),
            )
            return [types.TextContent(type="text", text=prompt)]

        else:
            return [types.TextContent(type="text", text=f"Unknown tool: {name}")]
    except Exception as e:
        return [
            types.TextContent(type="text", text=f"Error processing thought: {str(e)}")
        ]


async def main():
    # Run the server using stdin/stdout streams
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="divergent-thinking",
                server_version="1.0.0",
                capabilities=app.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )


def run():
    
    asyncio.run(main())


if __name__ == "__main__":
    run()


PROMPT_TEMPLATES = {
    "branch_generation": "Generate 3 distinct creative branches from this thought: {{thought}}\nEach branch should explore a completely different direction.",
    "creative_constraint": "Apply this creative constraint: {{constraint}}\nTransform the following thought: {{thought}}\nOutput only the transformed thought.",
    "perspective_shift": "View this thought from the perspective of a {{perspective_type}}:\n{{thought}}\nProvide a radically different interpretation.",
    "combination": "Combine these two divergent thoughts:\n1. {{thought1}}\n2. {{thought2}}\nCreate something entirely new that incorporates elements from both.",
}


class DivergentThinkingServer:
    def __init__(self):
        self.thought_history: List[Dict[str, Any]] = []
        self.branches: Dict[str, List[Dict[str, Any]]] = {}
        self.prompt_env = Environment(loader=BaseLoader())

    def validate_thought_data(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Validate thought data structure and content"""
        required_fields = [
            "thought",
            "thoughtNumber",
            "totalThoughts",
            "nextThoughtNeeded",
        ]
        for field in required_fields:
            if field not in input_data:
                raise ValueError(f"Missing required field: {field}")

        if (
            not isinstance(input_data["thought"], str)
            or len(input_data["thought"]) == 0
        ):
            raise ValueError("Thought must be a non-empty string")

        if (
            not isinstance(input_data["thoughtNumber"], int)
            or input_data["thoughtNumber"] < 1
        ):
            raise ValueError("thoughtNumber must be a positive integer")

        if (
            not isinstance(input_data["totalThoughts"], int)
            or input_data["totalThoughts"] < 1
        ):
            raise ValueError("totalThoughts must be a positive integer")

        if not isinstance(input_data["nextThoughtNeeded"], bool):
            raise ValueError("nextThoughtNeeded must be a boolean")

        return input_data

    def format_thought(self, thought_data: Dict[str, Any]) -> str:
        """Format thought for display"""
        prefix = "🌱 Branch" if thought_data.get("branchId") else "💭 Thought"
        branch_info = (
            f" (Branch {thought_data['branchId']})"
            if thought_data.get("branchId")
            else ""
        )
        return f"{prefix} {thought_data['thoughtNumber']}/{thought_data['totalThoughts']}{branch_info}: {thought_data['thought']}"

    def generate_prompt(self, template_name: str, **kwargs) -> str:
        """Generate prompt using Jinja2 template"""
        if template_name not in PROMPT_TEMPLATES:
            raise ValueError(f"Unknown template: {template_name}")
        template = self.prompt_env.from_string(PROMPT_TEMPLATES[template_name])
        return template.render(**kwargs)

    def process_thought(self, thought_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process thought and generate next thought or branches"""
        # Validate input data
        validated_data = self.validate_thought_data(thought_data)

        # Add to history
        self.thought_history.append(validated_data)

        # Generate branches if needed
        if (
            validated_data.get("generate_branches", False)
            and len(self.thought_history) > 0
        ):
            prompt = self.generate_prompt(
                "branch_generation", thought=validated_data["thought"]
            )
            return {
                "prompt": prompt,
                "action": "generate_branches",
                "current_thought": validated_data,
            }

        # Determine next action
        if validated_data["nextThoughtNeeded"]:
            # Generate prompt for next thought
            prompt_type = validated_data.get("prompt_type", "creative_constraint")
            constraint = validated_data.get(
                "constraint", "introduce an impossible element"
            )

            prompt = self.generate_prompt(
                prompt_type,
                thought=validated_data["thought"],
                constraint=constraint,
                perspective_type=validated_data.get(
                    "perspective_type", "inanimate_object"
                ),
            )

            return {
                "prompt": prompt,
                "action": "continue_thought",
                "current_thought": validated_data,
            }
        else:
            return {"action": "complete", "thought_history": self.thought_history}


# def format_thought(self, thought_data: Dict[str, Any]) -> str:
#     """Format thought for display"""
#     prefix = "🌱 Branch" if thought_data.get('branchId') else "💭 Thought"
#     branch_info = f" (Branch {thought_data['branchId']})" if thought_data.get('branchId') else ""
#     return f"{prefix} {thought_data['thoughtNumber']}/{thought_data['totalThoughts']}{branch_info}: {thought_data['thought']}"

# def generate_prompt(self, template_name: str, **kwargs) -> str:
#     """Generate prompt using Jinja2 template"""
#     if template_name not in PROMPT_TEMPLATES:
#         raise ValueError(f"Unknown template: {template_name}")
#     template = self.prompt_env.from_string(PROMPT_TEMPLATES[template_name])
#     return template.render(** kwargs)

# def process_thought(self, thought_data: Dict[str, Any]) -> Dict[str, Any]:
#     """Process thought and generate next thought or branches"""
#     # Validate input data
#     validated_data = self.validate_thought_data(thought_data)

#     # Add to history
#     self.thought_history.append(validated_data)

#     # Generate branches if needed
#     if validated_data.get('generate_branches', False) and len(self.thought_history) > 0:
#         prompt = self.generate_prompt(
#             "branch_generation",
#             thought=validated_data['thought']
#         )
#         return {
#             "prompt": prompt,
#             "action": "generate_branches",
#             "current_thought": validated_data
#         }

#     # Determine next action
#     if validated_data['nextThoughtNeeded']:
#         # Generate prompt for next thought
#         prompt_type = validated_data.get('prompt_type', 'creative_constraint')
#         constraint = validated_data.get('constraint', 'introduce an impossible element')

#         prompt = self.generate_prompt(
#             prompt_type,
#             thought=validated_data['thought'],
#             constraint=constraint,
#             perspective_type=validated_data.get('perspective_type', 'inanimate_object')
#         )

#         return {
#             "prompt": prompt,
#             "action": "continue_thought",
#             "current_thought": validated_data
#         }
#     else:
#         return {
#             "action": "complete",
#             "thought_history": self.thought_history
#         }
