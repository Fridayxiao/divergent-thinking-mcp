"""
Custom exceptions for the Divergent Thinking MCP Server.

This module defines specific exception classes for different types of errors
that can occur during divergent thinking operations.
"""

from typing import Optional, Any, Dict


class DivergentThinkingError(Exception):
    """
    Base exception class for all divergent thinking related errors.
    
    Attributes:
        message: Human-readable error message
        error_code: Optional error code for programmatic handling
        context: Optional dictionary with additional error context
    """
    
    def __init__(
        self, 
        message: str, 
        error_code: Optional[str] = None,
        context: Optional[Dict[str, Any]] = None
    ) -> None:
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        self.context = context or {}
        
    def to_dict(self) -> Dict[str, Any]:
        """Convert exception to dictionary for serialization."""
        return {
            "error_type": self.__class__.__name__,
            "message": self.message,
            "error_code": self.error_code,
            "context": self.context
        }


class ValidationError(DivergentThinkingError):
    """
    Raised when input validation fails.
    
    This exception is raised when required fields are missing,
    field types are incorrect, or field values are invalid.
    """
    
    def __init__(
        self, 
        message: str, 
        field_name: Optional[str] = None,
        field_value: Optional[Any] = None,
        expected_type: Optional[str] = None
    ) -> None:
        context = {}
        if field_name:
            context["field_name"] = field_name
        if field_value is not None:
            context["field_value"] = str(field_value)
        if expected_type:
            context["expected_type"] = expected_type
            
        super().__init__(message, "VALIDATION_ERROR", context)
        self.field_name = field_name
        self.field_value = field_value
        self.expected_type = expected_type


class TemplateError(DivergentThinkingError):
    """
    Raised when template processing fails.
    
    This exception is raised when template rendering fails,
    templates are not found, or template syntax is invalid.
    """
    
    def __init__(
        self, 
        message: str, 
        template_name: Optional[str] = None,
        template_variables: Optional[Dict[str, Any]] = None
    ) -> None:
        context = {}
        if template_name:
            context["template_name"] = template_name
        if template_variables:
            context["template_variables"] = template_variables
            
        super().__init__(message, "TEMPLATE_ERROR", context)
        self.template_name = template_name
        self.template_variables = template_variables


class ThoughtProcessingError(DivergentThinkingError):
    """
    Raised when thought processing operations fail.
    
    This exception is raised when thought validation, formatting,
    or processing logic encounters errors.
    """
    
    def __init__(
        self, 
        message: str, 
        thought_data: Optional[Dict[str, Any]] = None,
        operation: Optional[str] = None
    ) -> None:
        context = {}
        if thought_data:
            # Only include safe fields in context to avoid sensitive data exposure
            safe_fields = ["thoughtNumber", "totalThoughts", "nextThoughtNeeded", "branchId"]
            context["thought_metadata"] = {
                k: v for k, v in thought_data.items() 
                if k in safe_fields
            }
        if operation:
            context["operation"] = operation
            
        super().__init__(message, "THOUGHT_PROCESSING_ERROR", context)
        self.thought_data = thought_data
        self.operation = operation


class BranchManagementError(DivergentThinkingError):
    """
    Raised when branch management operations fail.
    
    This exception is raised when branch creation, tracking,
    or retrieval operations encounter errors.
    """
    
    def __init__(
        self, 
        message: str, 
        branch_id: Optional[str] = None,
        operation: Optional[str] = None
    ) -> None:
        context = {}
        if branch_id:
            context["branch_id"] = branch_id
        if operation:
            context["operation"] = operation
            
        super().__init__(message, "BRANCH_MANAGEMENT_ERROR", context)
        self.branch_id = branch_id
        self.operation = operation


class ServerError(DivergentThinkingError):
    """
    Raised when server-level operations fail.
    
    This exception is raised when MCP server initialization,
    tool handling, or communication errors occur.
    """
    
    def __init__(
        self, 
        message: str, 
        tool_name: Optional[str] = None,
        operation: Optional[str] = None
    ) -> None:
        context = {}
        if tool_name:
            context["tool_name"] = tool_name
        if operation:
            context["operation"] = operation
            
        super().__init__(message, "SERVER_ERROR", context)
        self.tool_name = tool_name
        self.operation = operation
