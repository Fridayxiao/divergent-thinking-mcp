"""
Tool definitions for the Divergent Thinking MCP Server.

This module contains comprehensive tool definitions with proper schemas,
validation, and documentation for all divergent thinking tools.
"""

from typing import List
from mcp.types import Tool

from .mcp_utils import MCPToolBuilder


def create_divergent_thinking_tools() -> List[Tool]:
    """
    Create the unified divergent thinking tool definition.

    Returns:
        List[Tool]: Single comprehensive MCP tool definition
    """
    # Return only the unified tool to reduce agent confusion
    return [_create_unified_divergent_thinking_tool()]


def _create_unified_divergent_thinking_tool() -> Tool:
    """Create the unified divergent thinking tool definition."""

    properties = {
        "thought": MCPToolBuilder.create_string_property(
            description="The primary thought, idea, or concept to work with",
            min_length=1,
            max_length=5000
        ),
        "thinking_method": MCPToolBuilder.create_string_property(
            description="The divergent thinking method to apply",
            enum=[
                "structured_process",
                "generate_branches",
                "perspective_shift",
                "creative_constraint",
                "combine_thoughts",
                "reverse_brainstorming"
            ],
            default="structured_process"
        ),
        "thought2": MCPToolBuilder.create_string_property(
            description="Second thought for combination method (required only for combine_thoughts)",
            min_length=1,
            max_length=5000
        ),
        "constraint": MCPToolBuilder.create_string_property(
            description="Creative limitation to apply (for creative_constraint method)",
            max_length=500,
            default="introduce an impossible element"
        ),
        "perspective_type": MCPToolBuilder.create_string_property(
            description="Viewpoint to adopt (for perspective_shift method)",
            enum=["inanimate_object", "abstract_concept", "impossible_being"],
            default="inanimate_object"
        ),
        "use_advanced_techniques": MCPToolBuilder.create_boolean_property(
            description="Enable advanced creativity techniques (Six Thinking Hats, SCAMPER, etc.)",
            default=False
        ),
        "seed": MCPToolBuilder.create_integer_property(
            description="Random seed for deterministic results (optional)",
            minimum=1,
            maximum=999999
        ),
        # Additional parameters for structured_process
        "thoughtNumber": MCPToolBuilder.create_integer_property(
            description="Position of current thought in sequence (for structured_process)",
            minimum=1,
            maximum=1000,
            default=1
        ),
        "totalThoughts": MCPToolBuilder.create_integer_property(
            description="Expected total thoughts in sequence (for structured_process)",
            minimum=1,
            maximum=1000,
            default=3
        ),
        "nextThoughtNeeded": MCPToolBuilder.create_boolean_property(
            description="Whether to continue the thinking sequence (for structured_process)",
            default=True
        ),
        "generate_branches": MCPToolBuilder.create_boolean_property(
            description="Whether to create multiple divergent paths (for structured_process)",
            default=False
        )
    }

    required = ["thought", "thinking_method"]
    
    description = """A comprehensive tool for generating creative thoughts and breakthrough ideas through structured divergent thinking processes.

## 1) CONCISE DESCRIPTION
This unified tool provides access to 6 powerful creativity methods through a single interface. It offers both comprehensive multi-turn exploration (structured_process) and quick single-shot creative techniques, eliminating the confusion of choosing between multiple similar tools.

## 2) WHEN TO USE THIS TOOL
- **Primary use:** Complex creative challenges requiring systematic exploration (use structured_process)
- **Quick tasks:** Need rapid creative input or specific creative techniques (use single-shot methods)
- **Problem solving:** Breaking through mental blocks and conventional thinking patterns
- **Innovation:** Developing breakthrough solutions and novel concepts
- **Ideation:** Generating multiple creative directions and alternatives

## 3) KEY FEATURES
- **Multi-turn structured exploration:** Complete guided creative journey with thought tracking and branching (structured_process - 多轮且结构完整的思考模式)
- **Single-shot quick methods:** Rapid creative techniques for specific needs (单次响应方法)
- **Advanced creativity algorithms:** SCAMPER, Six Thinking Hats, morphological analysis, reverse brainstorming
- **Intelligent parameter routing:** Single tool interface with method-specific parameter handling
- **Comprehensive coverage:** 6 proven creativity methodologies in one unified interface
- **Adaptive depth:** Adjusts exploration complexity based on problem requirements

## 4) PARAMETERS EXPLAINED
**Required:**
- `thought`: Your primary idea, problem, or concept to work with (1-5000 characters)
- `thinking_method`: Which creativity technique to apply (default: structured_process)
  - `structured_process`: Multi-turn comprehensive exploration (RECOMMENDED DEFAULT)
  - `generate_branches`: Create 3 different creative directions (single response)
  - `perspective_shift`: View through unusual viewpoints (single response)
  - `creative_constraint`: Apply strategic limitations (single response)
  - `combine_thoughts`: Merge two concepts (single response)
  - `reverse_brainstorming`: Explore failure modes (single response)

**Method-Specific:**
- `thought2`: Second concept for combination (required only for combine_thoughts)
- `constraint`: Creative limitation to apply (for creative_constraint, default: "introduce an impossible element")
- `perspective_type`: Viewpoint to adopt (for perspective_shift: inanimate_object, abstract_concept, impossible_being)

**Structured Process Options:**
- `thoughtNumber`: Position in thinking sequence (default: 1)
- `totalThoughts`: Expected total thoughts (default: 3)
- `nextThoughtNeeded`: Continue sequence (default: true)
- `generate_branches`: Create multiple paths (default: false)

**Enhancement Options:**
- `use_advanced_techniques`: Enable SCAMPER, Six Thinking Hats, etc. (default: false)
- `seed`: Random seed for consistent results (1-999999)

## 5) YOU SHOULD
1. **Start with structured_process** for most creative challenges - it provides the complete multi-turn thinking experience
2. **Use single-shot methods** only when you need quick, specific creative input rather than comprehensive exploration
3. **Provide clear, specific thoughts** as input - the more detailed your thought, the better the creative output
4. **Choose appropriate thinking_method** based on your specific creative need:
   - Complex problems → structured_process
   - Quick brainstorming → generate_branches
   - Stuck in conventional thinking → perspective_shift
   - Need breakthrough innovation → creative_constraint
   - Have multiple ideas to merge → combine_thoughts
   - Standard methods not working → reverse_brainstorming
5. **Enable use_advanced_techniques** for more sophisticated creativity algorithms when dealing with complex challenges
6. **Use seed parameter** when you need consistent, reproducible creative outputs across multiple runs
7. **Iterate thoughtfully** - let each creative output inform your next exploration direction"""
    
    examples = [
        {
            "description": "Complete structured creative exploration (RECOMMENDED DEFAULT)",
            "parameters": {
                "thought": "Develop sustainable transportation solution",
                "thinking_method": "structured_process",
                "use_advanced_techniques": True
            }
        },
        {
            "description": "Multi-turn systematic innovation process",
            "parameters": {
                "thought": "Design an innovative electric fan",
                "thinking_method": "structured_process"
            }
        },
        {
            "description": "Quick creative directions generation",
            "parameters": {
                "thought": "Create a new type of office chair",
                "thinking_method": "generate_branches"
            }
        },
        {
            "description": "Apply creative constraints to force innovation",
            "parameters": {
                "thought": "Design eco-friendly packaging",
                "thinking_method": "creative_constraint",
                "constraint": "must be made from recycled materials"
            }
        },
        {
            "description": "Shift perspective to challenge assumptions",
            "parameters": {
                "thought": "Improve online education",
                "thinking_method": "perspective_shift",
                "perspective_type": "abstract_concept"
            }
        },
        {
            "description": "Combine two concepts into something new",
            "parameters": {
                "thought": "Ergonomic office chair design",
                "thought2": "AI voice assistant technology",
                "thinking_method": "combine_thoughts"
            }
        },
        {
            "description": "Use reverse brainstorming for breakthrough thinking",
            "parameters": {
                "thought": "Create a user-friendly mobile banking app",
                "thinking_method": "reverse_brainstorming"
            }
        }
    ]
    
    return MCPToolBuilder.create_tool(
        name="divergent_thinking",
        description=description,
        properties=properties,
        required=required,
        examples=examples
    )







# All old tool functions removed - now using unified tool interface
