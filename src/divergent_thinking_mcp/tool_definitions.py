"""
Tool definitions for the Divergent Thinking MCP Server.

This module contains comprehensive tool definitions with proper schemas,
validation, and documentation for all divergent thinking tools.
"""

from typing import List
from mcp.types import Tool

from .mcp_utils import MCPToolBuilder
from .constants import VALID_DOMAINS


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
            description="The divergent thinking method to apply. Choose 'structured_process' for comprehensive multi-turn exploration, or single-shot methods for quick creative input.",
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
        # Interactive Context Parameters (NEW)
        "domain": MCPToolBuilder.create_string_property(
            description="REQUIRED: Specific domain/field for targeted creativity context. Must be explicitly specified by agent for precise, relevant creative outputs.",
            enum=list(VALID_DOMAINS)
        ),
        "target_audience": MCPToolBuilder.create_string_property(
            description="Optional: Target audience for user-centered creative solutions. Specify who will use/benefit from the solution (e.g., 'remote students', 'elderly users', 'small business owners', 'healthcare professionals')",
            max_length=100
        ),
        "time_period": MCPToolBuilder.create_string_property(
            description="Optional: Time context for temporally-aware creativity. Specify when the solution will be implemented or relevant (e.g., 'current', '2030s', 'next decade', 'post-pandemic era')",
            max_length=50
        ),
        "resources": MCPToolBuilder.create_string_property(
            description="Optional: Available resources and constraints for realistic innovation. Comma-separated list of what you have to work with (e.g., 'limited budget, cloud infrastructure, mobile devices, government grants')",
            max_length=500
        ),
        "goals": MCPToolBuilder.create_string_property(
            description="Optional: Specific objectives and success criteria for goal-oriented creativity. Comma-separated list of what you want to achieve (e.g., 'reduce costs, improve user experience, increase accessibility, enhance security')",
            max_length=500
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

    required = ["thought", "thinking_method", "domain"]
    
    description = """A comprehensive tool for generating creative thoughts and breakthrough ideas through structured divergent thinking processes with interactive context specification.

## 1) CONCISE DESCRIPTION
This unified tool provides access to 6 powerful creativity methods through a single interface. It offers both comprehensive multi-turn exploration (structured_process) and quick single-shot creative techniques, with agent-driven context specification for more targeted and relevant creative outputs.

## 2) WHEN TO USE THIS TOOL
- **Primary use:** Complex creative challenges requiring systematic exploration (use structured_process)
- **Quick tasks:** Need rapid creative input or specific creative techniques (use single-shot methods)
- **Problem solving:** Breaking through mental blocks and conventional thinking patterns
- **Innovation:** Developing breakthrough solutions and novel concepts
- **Ideation:** Generating multiple creative directions and alternatives
- **Context-specific creativity:** When you need creativity tailored to specific domains, audiences, or constraints

## 3) KEY FEATURES
- **Required domain specification:** Ensures targeted, relevant creativity by requiring explicit domain selection from 78+ multi-word options
- **Multi-turn structured exploration:** Complete guided creative journey with thought tracking and branching (structured_process - 多轮且结构完整的思考模式)
- **Single-shot quick methods:** Rapid creative techniques for specific needs (单次响应方法)
- **Interactive context specification:** Agent-driven domain, audience, time period, resources, and goals specification for precise targeting
- **Advanced creativity algorithms:** SCAMPER, Six Thinking Hats, morphological analysis, reverse brainstorming with context awareness
- **Intelligent parameter routing:** Single tool interface with method-specific parameter handling and comprehensive validation
- **Comprehensive coverage:** 6 proven creativity methodologies in one unified interface
- **Adaptive depth:** Adjusts exploration complexity based on problem requirements and context richness

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
- `domain`: **REQUIRED** - Specific field/domain for targeted creativity (must be explicitly specified)
  - Examples: "product design", "mobile app development", "healthcare technology", "sustainable agriculture", "e-commerce", "artificial intelligence", etc.
  - Choose from 78+ available multi-word domain options for precise context

**Interactive Context (Optional):**
- `target_audience`: Who the solution is for (e.g., 'students', 'professionals', 'elderly')
- `time_period`: Time context (e.g., 'current', 'future', '2030s', 'historical')
- `resources`: Available resources/constraints (comma-separated)
- `goals`: Specific objectives (comma-separated)

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
1. **Always specify a domain** - This is now required for targeted, relevant creativity output
   - Choose the most specific domain that matches your challenge (e.g., "mobile app development" not "software development")
   - Use multi-word domains for precision (e.g., "healthcare technology", "sustainable agriculture")
2. **Start with structured_process** for most creative challenges - it provides the complete multi-turn thinking experience
3. **Use single-shot methods** only when you need quick, specific creative input rather than comprehensive exploration
4. **Provide clear, specific thoughts** as input - the more detailed your thought, the better the creative output
5. **Enhance with context parameters** for even more targeted creativity:
   - Define `target_audience` for user-centered creative solutions
   - Specify `time_period` for temporally-aware creativity
   - List `resources` and `goals` for constraint-aware innovation
5. **Choose appropriate thinking_method** based on your specific creative need:
   - Complex problems → structured_process
   - Quick brainstorming → generate_branches
   - Stuck in conventional thinking → perspective_shift
   - Need breakthrough innovation → creative_constraint
   - Have multiple ideas to merge → combine_thoughts
   - Standard methods not working → reverse_brainstorming
6. **Enable use_advanced_techniques** for more sophisticated creativity algorithms when dealing with complex challenges
7. **Use seed parameter** when you need consistent, reproducible creative outputs across multiple runs
8. **Iterate thoughtfully** - let each creative output inform your next exploration direction
9. **Be specific with context** - the more precise your domain and context parameters, the more targeted and useful the creative output"""
    
    examples = [
        {
            "description": "Complete structured creative exploration (RECOMMENDED DEFAULT)",
            "parameters": {
                "thought": "Develop sustainable transportation solution",
                "thinking_method": "structured_process",
                "domain": "urban transportation",
                "use_advanced_techniques": True
            }
        },
        {
            "description": "Agent-driven context specification for targeted creativity",
            "parameters": {
                "thought": "Create an innovative learning platform",
                "thinking_method": "structured_process",
                "domain": "educational technology",
                "target_audience": "remote students",
                "time_period": "2025-2030",
                "resources": "cloud computing, mobile devices, limited budget",
                "goals": "improve engagement, reduce costs, increase accessibility"
            }
        },
        {
            "description": "Domain-specific creative branching",
            "parameters": {
                "thought": "Design a smart home security system",
                "thinking_method": "generate_branches",
                "domain": "cybersecurity",
                "target_audience": "elderly users",
                "goals": "ease of use, reliability, affordability"
            }
        },
        {
            "description": "Context-aware creative constraints",
            "parameters": {
                "thought": "Develop a food delivery service",
                "thinking_method": "creative_constraint",
                "domain": "e-commerce",
                "constraint": "must work without smartphones",
                "target_audience": "rural communities",
                "resources": "limited internet, local partnerships"
            }
        },
        {
            "description": "Time-specific perspective shifting",
            "parameters": {
                "thought": "Reimagine public transportation",
                "thinking_method": "perspective_shift",
                "domain": "urban transportation",
                "time_period": "2050",
                "perspective_type": "impossible_being",
                "goals": "zero emissions, universal accessibility"
            }
        },
        {
            "description": "Minimal required parameters",
            "parameters": {
                "thought": "Create a new type of office chair",
                "thinking_method": "generate_branches",
                "domain": "product design"
            }
        },
        {
            "description": "Domain-focused constraint creativity with minimal context",
            "parameters": {
                "thought": "Design eco-friendly packaging",
                "thinking_method": "creative_constraint",
                "domain": "sustainable agriculture",
                "constraint": "must be made from recycled materials"
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
