"""
MCP (Model Context Protocol) utilities for the Divergent Thinking server.

This module provides utilities for MCP server operations, tool definitions,
response formatting, and protocol compliance.
"""

import logging
from typing import List, Dict, Any, Optional
from mcp.types import Tool
import mcp.types as types

from .exceptions import ServerError

logger = logging.getLogger(__name__)


class MCPResponseBuilder:
    """
    Builder class for creating properly formatted MCP responses.
    
    Provides methods to create consistent, well-formatted responses
    for different types of MCP operations.
    """
    
    @staticmethod
    def create_text_response(content: str, metadata: Optional[Dict[str, Any]] = None) -> List[types.TextContent]:
        """
        Create a text content response.
        
        Args:
            content: The text content to return
            metadata: Optional metadata to include
            
        Returns:
            List[types.TextContent]: Formatted MCP text response
        """
        if not isinstance(content, str):
            raise ServerError(
                "Response content must be a string",
                operation="create_text_response"
            )
        
        if not content.strip():
            logger.warning("Creating response with empty content")
        
        response = types.TextContent(type="text", text=content)
        
        # Add metadata if provided (MCP may support this in future versions)
        if metadata:
            logger.debug(f"Response metadata: {metadata}")
        
        return [response]
    
    @staticmethod
    def create_error_response(error_message: str, error_code: Optional[str] = None) -> List[types.TextContent]:
        """
        Create a standardized error response.
        
        Args:
            error_message: Human-readable error message
            error_code: Optional error code for programmatic handling
            
        Returns:
            List[types.TextContent]: Formatted error response
        """
        if error_code:
            formatted_message = f"[{error_code}] {error_message}"
        else:
            formatted_message = f"Error: {error_message}"
        
        logger.error(f"Creating error response: {formatted_message}")
        return MCPResponseBuilder.create_text_response(formatted_message)
    
    @staticmethod
    def create_success_response(
        result: Dict[str, Any], 
        message: Optional[str] = None
    ) -> List[types.TextContent]:
        """
        Create a success response with structured result data.
        
        Args:
            result: Dictionary containing operation results
            message: Optional success message
            
        Returns:
            List[types.TextContent]: Formatted success response
        """
        if message:
            content = f"{message}\n\nResult: {result}"
        else:
            content = str(result)
        
        return MCPResponseBuilder.create_text_response(content)


class MCPToolBuilder:
    """
    Builder class for creating MCP tool definitions.
    
    Provides methods to create properly structured tool definitions
    with comprehensive schemas and documentation.
    """
    
    @staticmethod
    def create_tool(
        name: str,
        description: str,
        properties: Dict[str, Any],
        required: List[str],
        examples: Optional[List[Dict[str, Any]]] = None
    ) -> Tool:
        """
        Create a properly formatted MCP tool definition.
        
        Args:
            name: Tool name (must be unique)
            description: Comprehensive tool description
            properties: JSON schema properties for tool parameters
            required: List of required parameter names
            examples: Optional usage examples
            
        Returns:
            Tool: Formatted MCP tool definition
            
        Raises:
            ServerError: If tool definition is invalid
        """
        if not name or not isinstance(name, str):
            raise ServerError(
                "Tool name must be a non-empty string",
                operation="create_tool"
            )
        
        if not description or not isinstance(description, str):
            raise ServerError(
                f"Tool '{name}' must have a non-empty description",
                tool_name=name,
                operation="create_tool"
            )
        
        if not isinstance(properties, dict):
            raise ServerError(
                f"Tool '{name}' properties must be a dictionary",
                tool_name=name,
                operation="create_tool"
            )
        
        if not isinstance(required, list):
            raise ServerError(
                f"Tool '{name}' required fields must be a list",
                tool_name=name,
                operation="create_tool"
            )
        
        # Validate required fields exist in properties
        missing_props = [field for field in required if field not in properties]
        if missing_props:
            raise ServerError(
                f"Tool '{name}' required fields not in properties: {missing_props}",
                tool_name=name,
                operation="create_tool"
            )
        
        # Add examples to description if provided
        enhanced_description = description
        if examples:
            enhanced_description += "\n\nExamples:\n"
            for i, example in enumerate(examples, 1):
                enhanced_description += f"{i}. {example}\n"
        
        input_schema = {
            "type": "object",
            "properties": properties,
            "required": required,
        }
        
        logger.debug(f"Created tool definition for '{name}'")
        return Tool(
            name=name,
            description=enhanced_description,
            inputSchema=input_schema
        )
    
    @staticmethod
    def create_string_property(
        description: str,
        default: Optional[str] = None,
        enum: Optional[List[str]] = None,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        pattern: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Create a string property definition for tool schemas.
        
        Args:
            description: Property description
            default: Default value
            enum: List of valid values (for enum properties)
            min_length: Minimum string length
            max_length: Maximum string length
            pattern: Regex pattern for validation
            
        Returns:
            Dict[str, Any]: String property definition
        """
        prop = {
            "type": "string",
            "description": description
        }
        
        if default is not None:
            prop["default"] = default
        if enum is not None:
            prop["enum"] = enum
        if min_length is not None:
            prop["minLength"] = min_length
        if max_length is not None:
            prop["maxLength"] = max_length
        if pattern is not None:
            prop["pattern"] = pattern
        
        return prop
    
    @staticmethod
    def create_integer_property(
        description: str,
        default: Optional[int] = None,
        minimum: Optional[int] = None,
        maximum: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Create an integer property definition for tool schemas.
        
        Args:
            description: Property description
            default: Default value
            minimum: Minimum value
            maximum: Maximum value
            
        Returns:
            Dict[str, Any]: Integer property definition
        """
        prop = {
            "type": "integer",
            "description": description
        }
        
        if default is not None:
            prop["default"] = default
        if minimum is not None:
            prop["minimum"] = minimum
        if maximum is not None:
            prop["maximum"] = maximum
        
        return prop
    
    @staticmethod
    def create_boolean_property(
        description: str,
        default: Optional[bool] = None
    ) -> Dict[str, Any]:
        """
        Create a boolean property definition for tool schemas.
        
        Args:
            description: Property description
            default: Default value
            
        Returns:
            Dict[str, Any]: Boolean property definition
        """
        prop = {
            "type": "boolean",
            "description": description
        }
        
        if default is not None:
            prop["default"] = default
        
        return prop


class MCPServerConfig:
    """
    Configuration class for MCP server settings.
    
    Centralizes server configuration and provides validation
    for server initialization parameters.
    """
    
    def __init__(
        self,
        server_name: str = "divergent-thinking",
        server_version: str = "0.1.0",
        max_thought_length: int = 5000,
        max_constraint_length: int = 500,
        max_thoughts_per_sequence: int = 1000,
        enable_debug_logging: bool = False
    ):
        self.server_name = server_name
        self.server_version = server_version
        self.max_thought_length = max_thought_length
        self.max_constraint_length = max_constraint_length
        self.max_thoughts_per_sequence = max_thoughts_per_sequence
        self.enable_debug_logging = enable_debug_logging
        
        self._validate_config()
    
    def _validate_config(self) -> None:
        """Validate configuration parameters."""
        if not self.server_name or not isinstance(self.server_name, str):
            raise ServerError("Server name must be a non-empty string")
        
        if not self.server_version or not isinstance(self.server_version, str):
            raise ServerError("Server version must be a non-empty string")
        
        if self.max_thought_length <= 0:
            raise ServerError("Max thought length must be positive")
        
        if self.max_constraint_length <= 0:
            raise ServerError("Max constraint length must be positive")
        
        if self.max_thoughts_per_sequence <= 0:
            raise ServerError("Max thoughts per sequence must be positive")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to dictionary."""
        return {
            "server_name": self.server_name,
            "server_version": self.server_version,
            "max_thought_length": self.max_thought_length,
            "max_constraint_length": self.max_constraint_length,
            "max_thoughts_per_sequence": self.max_thoughts_per_sequence,
            "enable_debug_logging": self.enable_debug_logging
        }
