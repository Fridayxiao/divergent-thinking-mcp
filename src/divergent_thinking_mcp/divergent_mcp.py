#!/usr/bin/env python3
"""
Divergent Thinking MCP Server

An MCP server that enhances divergent thinking and creativity through prompt engineering
and context design, leveraging existing Agent/LLM capabilities.

This server provides tools for:
- Interactive domain specification with 78+ multi-word domains
- Agent-driven context parameters (audience, time, resources, goals)
- Generating creative branches from thoughts
- Shifting perspectives to gain new insights
- Applying creative constraints to transform ideas
- Combining divergent thoughts into novel concepts
- Structured divergent thinking processes

Key Features:
- Required domain specification for targeted creativity
- Multi-word domain precision (e.g., "mobile app development", "healthcare technology")
- Comprehensive parameter validation and error handling
- Context-aware prompt generation across all creativity methods

Author: Fridayxiao
Version: 0.2.2
License: MIT
"""

import asyncio
import logging
from typing import List, Dict, Any, Optional, Literal
from mcp.server.models import InitializationOptions
from mcp.server import NotificationOptions, Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool
import mcp.types as types
from jinja2 import Environment, BaseLoader

from .exceptions import (
    DivergentThinkingError,
    ValidationError,
    TemplateError,
    ThoughtProcessingError,
    BranchManagementError,
    ServerError
)
from .validators import ThoughtValidator
from .mcp_utils import MCPResponseBuilder, MCPServerConfig
from .tool_definitions import create_divergent_thinking_tools
from .enhanced_prompts import EnhancedPromptGenerator
from .creativity_algorithms import CreativityContext

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Type definitions
PerspectiveType = Literal["inanimate_object", "abstract_concept", "impossible_being"]
PromptType = Literal["branch_generation", "creative_constraint", "perspective_shift", "combination"]
ThoughtData = Dict[str, Any]
ToolResponse = List[types.TextContent]

app = Server("divergent_thinking_mcp")

# Global server instance to maintain state across tool calls
_server_instance: Optional['DivergentThinkingServer'] = None
_server_config: Optional[MCPServerConfig] = None

def get_server_instance(config: Optional[MCPServerConfig] = None) -> 'DivergentThinkingServer':
    """
    Get or create the singleton DivergentThinkingServer instance.

    This ensures thought history and branch management state is preserved
    across multiple tool calls, which is essential for the divergent thinking
    workflow to function correctly.

    Args:
        config: Optional server configuration. Only used when creating the instance.

    Returns:
        DivergentThinkingServer: The singleton server instance
    """
    global _server_instance, _server_config
    if _server_instance is None:
        _server_config = config or MCPServerConfig()
        _server_instance = DivergentThinkingServer(_server_config)
        logger.info("Created new DivergentThinkingServer instance")
    return _server_instance


@app.list_tools()
async def handle_list_tools() -> List[Tool]:
    """
    List available divergent thinking tools.

    Returns:
        List[Tool]: A list of available MCP tools for divergent thinking processes.

    Tools provided:
        - divergent_thinking: Comprehensive structured divergent thinking
        - generate_branches: Create multiple creative branches from a thought
        - perspective_shift: View thoughts from unusual perspectives
        - creative_constraint: Apply constraints to transform thoughts
        - combine_thoughts: Merge two thoughts into something new
    """
    try:
        tools = create_divergent_thinking_tools()
        logger.info(f"Loaded {len(tools)} divergent thinking tools")
        return tools
    except Exception as e:
        logger.error(f"Failed to create tool definitions: {str(e)}")
        raise ServerError(
            f"Failed to initialize tools: {str(e)}",
            operation="list_tools"
        )


@app.call_tool()
async def handle_call_tool(
    name: str, arguments: Optional[Dict[str, Any]]
) -> ToolResponse:
    """
    Handle tool calls for divergent thinking functions using prompt engineering.

    Args:
        name: The name of the tool to execute
        arguments: Optional dictionary containing tool arguments

    Returns:
        List[types.TextContent]: Response containing generated prompts or results

    Raises:
        Exception: Various exceptions for invalid inputs or processing errors
    """
    server = get_server_instance()
    thought_data: ThoughtData = arguments or {}

    try:
        if name == "divergent_thinking":
            # Handle unified divergent thinking tool with method-based routing
            thinking_method = thought_data.get("thinking_method", "structured_process")

            if thinking_method == "structured_process":
                # Use the original structured process for comprehensive multi-turn exploration
                result = server.process_thought(thought_data)
                return MCPResponseBuilder.create_success_response(result)

            elif thinking_method == "generate_branches":
                # Generate enhanced branch prompt with creativity context
                context = server.create_creativity_context(thought_data) if thought_data else None
                prompt = server.generate_prompt(
                    "branch_generation",
                    thought=thought_data.get("thought", ""),
                    context=context,
                    technique=thought_data.get("creativity_technique"),
                    seed=thought_data.get("seed")
                )
                return MCPResponseBuilder.create_text_response(prompt)

            elif thinking_method == "perspective_shift":
                # Generate enhanced perspective shift prompt
                prompt = server.generate_prompt(
                    "perspective_shift",
                    thought=thought_data.get("thought", ""),
                    perspective_type=thought_data.get("perspective_type", "inanimate_object"),
                    use_six_hats=thought_data.get("use_advanced_techniques", False),
                    seed=thought_data.get("seed")
                )
                return MCPResponseBuilder.create_text_response(prompt)

            elif thinking_method == "creative_constraint":
                # Generate enhanced creative constraint prompt
                prompt = server.generate_prompt(
                    "creative_constraint",
                    thought=thought_data.get("thought", ""),
                    constraint=thought_data.get("constraint", "introduce an impossible element"),
                    use_relaxation=thought_data.get("use_advanced_techniques", False),
                    seed=thought_data.get("seed")
                )
                return MCPResponseBuilder.create_text_response(prompt)

            elif thinking_method == "combine_thoughts":
                # Generate enhanced combination prompt
                prompt = server.generate_prompt(
                    "combination",
                    thought1=thought_data.get("thought", ""),
                    thought2=thought_data.get("thought2", ""),
                    use_morphological=thought_data.get("use_advanced_techniques", False),
                    seed=thought_data.get("seed")
                )
                return MCPResponseBuilder.create_text_response(prompt)

            elif thinking_method == "reverse_brainstorming":
                # Generate reverse brainstorming prompt
                prompt = server.generate_prompt(
                    "reverse_brainstorming",
                    thought=thought_data.get("thought", ""),
                    seed=thought_data.get("seed")
                )
                return MCPResponseBuilder.create_text_response(prompt)

            else:
                available_methods = ["structured_process", "generate_branches", "perspective_shift", "creative_constraint",
                                   "combine_thoughts", "reverse_brainstorming"]
                raise ValidationError(
                    f"Unknown thinking_method: {thinking_method}. Available methods: {available_methods}",
                    field_name="thinking_method",
                    field_value=thinking_method
                )

        else:
            logger.warning(f"Unknown tool requested: {name}")
            raise ServerError(f"Unknown tool: {name}", tool_name=name, operation="tool_dispatch")

    except ValidationError as e:
        logger.error(f"Validation error for tool {name}: {e.message}")
        return MCPResponseBuilder.create_error_response(e.message, e.error_code)
    except TemplateError as e:
        logger.error(f"Template error for tool {name}: {e.message}")
        return MCPResponseBuilder.create_error_response(e.message, e.error_code)
    except ThoughtProcessingError as e:
        logger.error(f"Thought processing error for tool {name}: {e.message}")
        return MCPResponseBuilder.create_error_response(e.message, e.error_code)
    except BranchManagementError as e:
        logger.error(f"Branch management error for tool {name}: {e.message}")
        return MCPResponseBuilder.create_error_response(e.message, e.error_code)
    except ServerError as e:
        logger.error(f"Server error for tool {name}: {e.message}")
        return MCPResponseBuilder.create_error_response(e.message, e.error_code)
    except DivergentThinkingError as e:
        logger.error(f"Divergent thinking error for tool {name}: {e.message}")
        return MCPResponseBuilder.create_error_response(e.message, e.error_code)
    except Exception as e:
        logger.error(f"Unexpected error processing tool {name}: {str(e)}")
        return MCPResponseBuilder.create_error_response(f"Unexpected error: {str(e)}")


async def main() -> None:
    """
    Main entry point for the MCP server.

    Initializes and runs the divergent thinking MCP server using stdin/stdout streams.
    Uses MCPServerConfig for centralized configuration management.
    """
    try:
        # Initialize server configuration
        config = MCPServerConfig(
            server_name="divergent-thinking",
            server_version="0.2.2",
            enable_debug_logging=False
        )

        # Configure logging level based on config
        if config.enable_debug_logging:
            logging.getLogger().setLevel(logging.DEBUG)

        logger.info(f"Starting Divergent Thinking MCP Server v{config.server_version}...")
        logger.debug(f"Server configuration: {config.to_dict()}")

        # Initialize server instance with configuration
        get_server_instance(config)

        async with stdio_server() as (read_stream, write_stream):
            await app.run(
                read_stream,
                write_stream,
                InitializationOptions(
                    server_name=config.server_name,
                    server_version=config.server_version,
                    capabilities=app.get_capabilities(
                        notification_options=NotificationOptions(),
                        experimental_capabilities={},
                    ),
                ),
            )
    except Exception as e:
        logger.error(f"Failed to start server: {str(e)}")
        raise


def run() -> None:
    """
    Entry point function for the MCP server.

    This function is called when the server is started via the command line.
    """
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Server shutdown requested by user")
    except Exception as e:
        logger.error(f"Server crashed: {str(e)}")
        raise


if __name__ == "__main__":
    run()




class DivergentThinkingServer:
    """
    Core server class for handling divergent thinking operations with interactive domain specification.

    This class manages thought history, branch generation, and context-aware prompt creation
    for various divergent thinking techniques. It provides methods for validating
    input data, creating creativity contexts, and generating targeted creative prompts.

    Key Features:
        - Interactive domain specification with 78+ multi-word domains
        - Agent-driven context parameters (audience, time, resources, goals)
        - Comprehensive parameter validation and error handling
        - Context-aware prompt generation across all creativity methods

    Attributes:
        config: Server configuration settings
        thought_history: List of processed thoughts with metadata
        branches: Dictionary mapping branch IDs to their thought sequences
        prompt_env: Jinja2 environment for template rendering
        enhanced_prompt_generator: Generator for enhanced creativity prompts with context awareness
    """

    def __init__(self, config: Optional[MCPServerConfig] = None) -> None:
        """
        Initialize the divergent thinking server with empty state.

        Args:
            config: Optional server configuration. If None, uses default configuration.
        """
        self.config = config or MCPServerConfig()
        self.thought_history: List[ThoughtData] = []
        self.branches: Dict[str, List[ThoughtData]] = {}
        self.prompt_env = Environment(loader=BaseLoader())
        self.enhanced_prompt_generator = EnhancedPromptGenerator()
        logger.info("DivergentThinkingServer initialized with enhanced creativity algorithms")

    def validate_thought_data(self, input_data: ThoughtData) -> ThoughtData:
        """
        Validate thought data structure and content using comprehensive validators.

        Args:
            input_data: Dictionary containing thought data to validate

        Returns:
            ThoughtData: Validated and cleaned thought data dictionary

        Raises:
            ValidationError: If required fields are missing or invalid
            ThoughtProcessingError: If validation logic fails
        """
        try:
            # Validate required fields
            required_fields = ["thought", "thoughtNumber", "totalThoughts", "nextThoughtNeeded"]
            ThoughtValidator.validate_required_fields(input_data, required_fields)

            # Create validated data dictionary
            validated_data: ThoughtData = {}

            # Validate and clean thought content
            validated_data["thought"] = ThoughtValidator.validate_thought_content(
                input_data["thought"], "thought"
            )

            # Validate thought number
            validated_data["thoughtNumber"] = ThoughtValidator.validate_integer_field(
                input_data["thoughtNumber"],
                "thoughtNumber",
                ThoughtValidator.MIN_THOUGHT_NUMBER,
                ThoughtValidator.MAX_THOUGHT_NUMBER
            )

            # Validate total thoughts
            validated_data["totalThoughts"] = ThoughtValidator.validate_integer_field(
                input_data["totalThoughts"],
                "totalThoughts",
                ThoughtValidator.MIN_TOTAL_THOUGHTS,
                ThoughtValidator.MAX_TOTAL_THOUGHTS
            )

            # Validate thought number doesn't exceed total
            if validated_data["thoughtNumber"] > validated_data["totalThoughts"]:
                raise ValidationError(
                    "thoughtNumber cannot exceed totalThoughts",
                    field_name="thoughtNumber",
                    field_value=validated_data["thoughtNumber"]
                )

            # Validate next thought needed flag
            validated_data["nextThoughtNeeded"] = ThoughtValidator.validate_boolean_field(
                input_data["nextThoughtNeeded"], "nextThoughtNeeded"
            )

            # Validate optional fields
            if "generate_branches" in input_data:
                validated_data["generate_branches"] = ThoughtValidator.validate_boolean_field(
                    input_data["generate_branches"], "generate_branches"
                )

            if "prompt_type" in input_data:
                validated_data["prompt_type"] = ThoughtValidator.validate_enum_field(
                    input_data["prompt_type"],
                    "prompt_type",
                    ThoughtValidator.VALID_PROMPT_TYPES,
                    required=False
                )

            if "perspective_type" in input_data:
                validated_data["perspective_type"] = ThoughtValidator.validate_enum_field(
                    input_data["perspective_type"],
                    "perspective_type",
                    ThoughtValidator.VALID_PERSPECTIVE_TYPES,
                    required=False
                )

            if "constraint" in input_data:
                validated_data["constraint"] = ThoughtValidator.validate_constraint(
                    input_data["constraint"]
                )

            if "branchId" in input_data:
                validated_data["branchId"] = ThoughtValidator.validate_branch_id(
                    input_data["branchId"]
                )

            # Validate interactive context parameters
            if "domain" in input_data:
                validated_data["domain"] = ThoughtValidator.validate_domain(
                    input_data["domain"]
                )

            if "target_audience" in input_data:
                validated_data["target_audience"] = ThoughtValidator.validate_target_audience(
                    input_data["target_audience"]
                )

            if "time_period" in input_data:
                validated_data["time_period"] = ThoughtValidator.validate_time_period(
                    input_data["time_period"]
                )

            if "resources" in input_data:
                validated_data["resources"] = ThoughtValidator.validate_resources(
                    input_data["resources"]
                )

            if "goals" in input_data:
                validated_data["goals"] = ThoughtValidator.validate_goals(
                    input_data["goals"]
                )

            # Copy other safe fields
            safe_optional_fields = ["thought1", "thought2"]
            for field in safe_optional_fields:
                if field in input_data:
                    validated_data[field] = ThoughtValidator.validate_thought_content(
                        input_data[field], field
                    )

            logger.debug(f"Validated thought data: {validated_data['thought'][:50]}...")
            return validated_data

        except ValidationError:
            # Re-raise validation errors as-is
            raise
        except Exception as e:
            # Wrap other errors in ThoughtProcessingError
            raise ThoughtProcessingError(
                f"Failed to validate thought data: {str(e)}",
                thought_data=input_data,
                operation="validation"
            )

    def create_creativity_context(self, thought_data: ThoughtData) -> CreativityContext:
        """
        Create a creativity context from thought data with agent-driven parameters.

        All context parameters must be explicitly specified by the agent.
        No automatic extraction or fallback logic is used.

        Args:
            thought_data: Validated thought data

        Returns:
            CreativityContext: Context for creativity algorithms
        """
        # 1. Domain: Agent must specify domain explicitly (already validated)
        domain = thought_data.get("domain")
        if not domain:
            raise ValidationError(
                "Domain must be explicitly specified by the agent. Please provide a specific domain/field for targeted creativity.",
                field_name="domain",
                field_value=None
            )

        # 2-5. Get validated context parameters (already cleaned and validated)
        target_audience = thought_data.get("target_audience")
        time_period = thought_data.get("time_period")

        # Parse comma-separated strings into lists
        resources = self._parse_comma_separated(thought_data.get("resources"))
        goals = self._parse_comma_separated(thought_data.get("goals"))

        # 6. Constraints: Extract from thought data (existing logic)
        constraints = []
        if "constraint" in thought_data:
            constraints.append(thought_data["constraint"])

        logger.debug(f"Created creativity context - Domain: {domain}, Audience: {target_audience}, "
                    f"Time: {time_period}, Resources: {resources}, Goals: {goals}")

        return CreativityContext(
            domain=domain,
            constraints=constraints,
            target_audience=target_audience,
            time_period=time_period,
            resources=resources,
            goals=goals
        )



    def _parse_comma_separated(self, value: Optional[str]) -> List[str]:
        """
        Parse comma-separated string into a list of strings, ensuring an empty list is returned for empty input.

        Args:
            value: Comma-separated string or None

        Returns:
            List[str]: List of parsed strings (guaranteed to be a list)
        """
        if not value or not value.strip():
            return []

        # Split by comma, strip whitespace, and filter empty strings
        return [item.strip() for item in value.split(",") if item.strip()]

    def format_thought(self, thought_data: ThoughtData) -> str:
        """
        Format thought for display with appropriate icons and metadata.

        Args:
            thought_data: Dictionary containing thought information

        Returns:
            str: Formatted thought string with prefix, numbering, and content
        """
        prefix = "🌱 Branch" if thought_data.get("branchId") else "💭 Thought"
        branch_info = (
            f" (Branch {thought_data['branchId']})"
            if thought_data.get("branchId")
            else ""
        )
        thought_text = thought_data['thought'][:100] + "..." if len(thought_data['thought']) > 100 else thought_data['thought']
        return f"{prefix} {thought_data['thoughtNumber']}/{thought_data['totalThoughts']}{branch_info}: {thought_text}"

    def generate_prompt(self, template_name: str, **kwargs: Any) -> str:
        """
        Generate prompt using enhanced creativity algorithms and templates.

        Args:
            template_name: Name of the template to use
            **kwargs: Template variables to render

        Returns:
            str: Rendered prompt string

        Raises:
            TemplateError: If template processing fails
        """
        try:
            # Use enhanced prompt generation for supported templates
            if template_name == "branch_generation":
                thought = kwargs.get("thought", "")
                context = kwargs.get("context")
                technique = kwargs.get("technique")
                seed = kwargs.get("seed")
                return self.enhanced_prompt_generator.generate_enhanced_branch_prompt(
                    thought, context, technique, seed
                )

            elif template_name == "perspective_shift":
                thought = kwargs.get("thought", "")
                perspective_type = kwargs.get("perspective_type", "inanimate_object")
                use_six_hats = kwargs.get("use_six_hats", False)
                seed = kwargs.get("seed")
                context = kwargs.get("context")
                return self.enhanced_prompt_generator.generate_enhanced_perspective_prompt(
                    thought, perspective_type, use_six_hats, seed, context
                )

            elif template_name == "creative_constraint":
                thought = kwargs.get("thought", "")
                constraint = kwargs.get("constraint", "introduce an impossible element")
                use_relaxation = kwargs.get("use_relaxation", False)
                seed = kwargs.get("seed")
                context = kwargs.get("context")
                return self.enhanced_prompt_generator.generate_enhanced_constraint_prompt(
                    thought, constraint, use_relaxation, seed, context
                )

            elif template_name == "combination":
                thought1 = kwargs.get("thought1", "")
                thought2 = kwargs.get("thought2", "")
                use_morphological = kwargs.get("use_morphological", False)
                seed = kwargs.get("seed")
                context = kwargs.get("context")
                return self.enhanced_prompt_generator.generate_enhanced_combination_prompt(
                    thought1, thought2, use_morphological, seed, context
                )

            elif template_name == "reverse_brainstorming":
                thought = kwargs.get("thought", "")
                seed = kwargs.get("seed")
                context = kwargs.get("context")
                return self.enhanced_prompt_generator.generate_reverse_brainstorming_prompt(thought, seed, context)

            
            else:
                available_templates = [
                    "branch_generation", "perspective_shift", "creative_constraint",
                    "combination", "reverse_brainstorming"
                ]
                raise TemplateError(
                    f"Unknown template: {template_name}. Available templates: {available_templates}",
                    template_name=template_name
                )

        except TemplateError:
            # Re-raise template errors as-is
            raise
        except Exception as e:
            logger.error(f"Error generating enhanced prompt '{template_name}': {str(e)}")
            raise TemplateError(
                f"Failed to generate enhanced prompt '{template_name}': {str(e)}",
                template_name=template_name,
                template_variables=kwargs
            )

    def _execute_structured_thinking_step(self, validated_data: ThoughtData, creativity_context: CreativityContext, thought_count: int) -> Dict[str, Any]:
        """
        Execute one step in the structured thinking sequence.

        Sequence: generate_branches → perspective_shift → creative_constraint → combine_thoughts → reverse_brainstorming

        Args:
            validated_data: Validated thought data
            creativity_context: Creativity context for enhanced algorithms
            thought_count: Current thought count

        Returns:
            Dict containing the next prompt and action
        """
        # Define the thinking sequence
        thinking_steps = [
            "generate_branches",
            "perspective_shift",
            "creative_constraint",
            "combine_thoughts",
            "reverse_brainstorming"
        ]

        step_name = thinking_steps[self._round_step]
        logger.info(f"Executing structured thinking step: {step_name} (round {self._current_round}, step {self._round_step + 1}/5)")

        # Store current step result
        if self._round_step > 0:  # Skip storing for first step (branches)
            prev_step = thinking_steps[self._round_step - 1]
            self._round_results[f"round_{self._current_round}_{prev_step}"] = validated_data["thought"]

        try:
            if step_name == "generate_branches":
                prompt = self._generate_branches_step(validated_data, creativity_context)
            elif step_name == "perspective_shift":
                prompt = self._generate_perspective_step(validated_data, creativity_context)
            elif step_name == "creative_constraint":
                prompt = self._generate_constraint_step(validated_data, creativity_context)
            elif step_name == "combine_thoughts":
                prompt = self._generate_combine_step(validated_data, creativity_context)
            elif step_name == "reverse_brainstorming":
                prompt = self._generate_reverse_step(validated_data, creativity_context)
            else:
                raise ThoughtProcessingError(
                    f"Unknown thinking step: {step_name}",
                    thought_data=validated_data,
                    operation="structured_thinking"
                )

        except TemplateError as e:
            raise ThoughtProcessingError(
                f"Failed to generate {step_name} prompt: {e.message}",
                thought_data=validated_data,
                operation=f"structured_thinking_{step_name}"
            )

        # Advance to next step
        self._round_step += 1

        # Check if round is complete
        if self._round_step >= len(thinking_steps):
            self._round_step = 0
            self._current_round += 1
            logger.info(f"Completed round {self._current_round - 1}, starting round {self._current_round}")

        return {
            "prompt": prompt,
            "action": f"structured_thinking_{step_name}",
            "current_thought": validated_data,
            "thought_count": thought_count,
            "round": self._current_round,
            "step": step_name,
            "step_number": self._round_step if self._round_step > 0 else len(thinking_steps),
            "round_results": dict(self._round_results)  # Copy for safety
        }

    def _generate_branches_step(self, validated_data: ThoughtData, creativity_context: CreativityContext) -> str:
        """Generate branches step with enhanced context."""
        return self.generate_prompt(
            "branch_generation",
            thought=validated_data["thought"],
            context=creativity_context,
            technique=validated_data.get("creativity_technique"),
            seed=validated_data.get("seed")
        )

    def _generate_perspective_step(self, validated_data: ThoughtData, creativity_context: CreativityContext) -> str:
        """Generate perspective shift step."""
        return self.generate_prompt(
            "perspective_shift",
            thought=validated_data["thought"],
            perspective_type=validated_data.get("perspective_type", "inanimate_object"),
            use_six_hats=validated_data.get("use_advanced_techniques", False),
            seed=validated_data.get("seed"),
            context=creativity_context
        )

    def _generate_constraint_step(self, validated_data: ThoughtData, creativity_context: CreativityContext) -> str:
        """Generate creative constraint step."""
        return self.generate_prompt(
            "creative_constraint",
            thought=validated_data["thought"],
            constraint=validated_data.get("constraint", "introduce an impossible element"),
            use_relaxation=validated_data.get("use_advanced_techniques", False),
            seed=validated_data.get("seed"),
            context=creativity_context
        )

    def _generate_combine_step(self, validated_data: ThoughtData, creativity_context: CreativityContext) -> str:
        """Generate combine thoughts step using previous round results."""
        # Use base thought and current thought for combination
        thought1 = self._base_thought
        thought2 = validated_data["thought"]

        # If we have previous round results, use the most recent constraint result
        if self._round_results:
            constraint_results = [v for k, v in self._round_results.items() if "creative_constraint" in k]
            if constraint_results:
                thought2 = constraint_results[-1]  # Use most recent constraint result

        return self.generate_prompt(
            "combination",
            thought1=thought1,
            thought2=thought2,
            use_morphological=validated_data.get("use_advanced_techniques", False),
            seed=validated_data.get("seed"),
            context=creativity_context
        )

    def _generate_reverse_step(self, validated_data: ThoughtData, creativity_context: CreativityContext) -> str:
        """Generate reverse brainstorming step."""
        return self.generate_prompt(
            "reverse_brainstorming",
            thought=validated_data["thought"],
            seed=validated_data.get("seed"),
            context=creativity_context
        )

    def _complete_thinking_process(self, thought_count: int) -> Dict[str, Any]:
        """Complete the structured thinking process and return summary."""
        current_round = getattr(self, '_current_round', 1)
        logger.info(f"Structured thinking process completed with {thought_count} thoughts across {current_round} rounds")

        # Preserve round results for final summary
        final_results = dict(getattr(self, '_round_results', {}))

        # Clean up round tracking
        if hasattr(self, '_current_round'):
            delattr(self, '_current_round')
        if hasattr(self, '_round_step'):
            delattr(self, '_round_step')
        if hasattr(self, '_base_thought'):
            delattr(self, '_base_thought')
        if hasattr(self, '_round_results'):
            delattr(self, '_round_results')

        return {
            "action": "complete",
            "thought_history": self.thought_history,
            "total_thoughts": thought_count,
            "branches": len(self.branches),
            "rounds_completed": current_round,
            "round_results": final_results,
            "summary": f"Completed structured thinking with {thought_count} thoughts across {current_round} rounds"
        }

    def process_thought(self, thought_data: ThoughtData) -> Dict[str, Any]:
        """
        Enhanced multi-round structured thinking process.

        Each round includes: generate_branches → perspective_shift → creative_constraint → combine_thoughts → reverse_brainstorming

        Args:
            thought_data: Dictionary containing thought information and parameters

        Returns:
            Dict[str, Any]: Processing result with action, prompt, and metadata

        Raises:
            ValueError: If thought data validation fails
        """
        try:
            # Validate input data
            validated_data = self.validate_thought_data(thought_data)

            # Add to history and update thought count
            self.thought_history.append(validated_data)
            thought_count = len(self.thought_history)
            logger.info(f"Added thought {validated_data['thoughtNumber']} to history (total: {thought_count})")

            # Create creativity context for enhanced algorithms
            creativity_context = self.create_creativity_context(validated_data)

            # Initialize or update round tracking
            if not hasattr(self, '_current_round'):
                self._current_round = 1
                self._round_step = 0  # 0: branches, 1: perspective, 2: constraint, 3: combine, 4: reverse
                self._round_results = {}
                self._base_thought = validated_data["thought"]
                logger.info("Starting new structured thinking process")

            # Track branch if branchId provided
            if "branchId" in validated_data:
                try:
                    branch_id = validated_data["branchId"]
                    if branch_id not in self.branches:
                        self.branches[branch_id] = []
                    self.branches[branch_id].append(validated_data)
                    logger.info(f"Added thought to branch '{branch_id}'")
                except Exception as e:
                    raise BranchManagementError(
                        f"Failed to track branch: {str(e)}",
                        branch_id=branch_id,
                        operation="add_to_branch"
                    )

            # Execute structured thinking sequence
            if validated_data["nextThoughtNeeded"]:
                return self._execute_structured_thinking_step(validated_data, creativity_context, thought_count)
            else:
                # Complete the thinking process
                return self._complete_thinking_process(thought_count)

        except (ValidationError, ThoughtProcessingError, BranchManagementError):
            # Re-raise known errors as-is
            raise
        except Exception as e:
            logger.error(f"Unexpected error in process_thought: {str(e)}")
            raise ThoughtProcessingError(
                f"Failed to process thought: {str(e)}",
                thought_data=thought_data,
                operation="process_thought"
            )
