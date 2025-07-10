"""
Validation utilities for the Divergent Thinking MCP Server.

This module provides comprehensive validation functions for different types
of input data used in divergent thinking operations.
"""

import re
from typing import Any, Dict, List, Optional, Set
from .exceptions import ValidationError


class ThoughtValidator:
    """
    Validator class for thought-related data structures.
    
    Provides methods to validate thought content, metadata, and parameters
    used in divergent thinking operations.
    """
    
    # Valid values for enum-like fields
    VALID_PROMPT_TYPES: Set[str] = {
        "branch_generation", 
        "creative_constraint", 
        "perspective_shift", 
        "combination"
    }
    
    VALID_PERSPECTIVE_TYPES: Set[str] = {
        "inanimate_object", 
        "abstract_concept", 
        "impossible_being"
    }
    
    # Validation constraints
    MIN_THOUGHT_LENGTH = 1
    MAX_THOUGHT_LENGTH = 5000
    MIN_CONSTRAINT_LENGTH = 1
    MAX_CONSTRAINT_LENGTH = 500
    MIN_THOUGHT_NUMBER = 1
    MAX_THOUGHT_NUMBER = 1000
    MIN_TOTAL_THOUGHTS = 1
    MAX_TOTAL_THOUGHTS = 1000
    
    @classmethod
    def validate_required_fields(cls, data: Dict[str, Any], required_fields: List[str]) -> None:
        """
        Validate that all required fields are present in the data.
        
        Args:
            data: Dictionary to validate
            required_fields: List of required field names
            
        Raises:
            ValidationError: If any required field is missing
        """
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            raise ValidationError(
                f"Missing required fields: {', '.join(missing_fields)}",
                field_name=missing_fields[0] if len(missing_fields) == 1 else None
            )
    
    @classmethod
    def validate_thought_content(cls, thought: Any, field_name: str = "thought") -> str:
        """
        Validate thought content string.
        
        Args:
            thought: The thought content to validate
            field_name: Name of the field being validated
            
        Returns:
            str: Validated and cleaned thought content
            
        Raises:
            ValidationError: If thought content is invalid
        """
        if not isinstance(thought, str):
            raise ValidationError(
                f"{field_name} must be a string",
                field_name=field_name,
                field_value=thought,
                expected_type="string"
            )
        
        # Clean and validate length
        cleaned_thought = thought.strip()
        if len(cleaned_thought) < cls.MIN_THOUGHT_LENGTH:
            raise ValidationError(
                f"{field_name} must be at least {cls.MIN_THOUGHT_LENGTH} character(s) long",
                field_name=field_name,
                field_value=thought
            )
        
        if len(cleaned_thought) > cls.MAX_THOUGHT_LENGTH:
            raise ValidationError(
                f"{field_name} must be at most {cls.MAX_THOUGHT_LENGTH} characters long",
                field_name=field_name,
                field_value=f"{thought[:50]}..."
            )
        
        # Check for potentially harmful content (basic sanitization)
        if cls._contains_harmful_content(cleaned_thought):
            raise ValidationError(
                f"{field_name} contains potentially harmful content",
                field_name=field_name
            )
        
        return cleaned_thought
    
    @classmethod
    def validate_integer_field(
        cls, 
        value: Any, 
        field_name: str, 
        min_value: int, 
        max_value: int
    ) -> int:
        """
        Validate integer field with range constraints.
        
        Args:
            value: The value to validate
            field_name: Name of the field being validated
            min_value: Minimum allowed value
            max_value: Maximum allowed value
            
        Returns:
            int: Validated integer value
            
        Raises:
            ValidationError: If value is invalid
        """
        if not isinstance(value, int):
            raise ValidationError(
                f"{field_name} must be an integer",
                field_name=field_name,
                field_value=value,
                expected_type="integer"
            )
        
        if value < min_value or value > max_value:
            raise ValidationError(
                f"{field_name} must be between {min_value} and {max_value}",
                field_name=field_name,
                field_value=value
            )
        
        return value
    
    @classmethod
    def validate_boolean_field(cls, value: Any, field_name: str) -> bool:
        """
        Validate boolean field.
        
        Args:
            value: The value to validate
            field_name: Name of the field being validated
            
        Returns:
            bool: Validated boolean value
            
        Raises:
            ValidationError: If value is invalid
        """
        if not isinstance(value, bool):
            raise ValidationError(
                f"{field_name} must be a boolean",
                field_name=field_name,
                field_value=value,
                expected_type="boolean"
            )
        
        return value
    
    @classmethod
    def validate_enum_field(
        cls, 
        value: Any, 
        field_name: str, 
        valid_values: Set[str],
        required: bool = True
    ) -> Optional[str]:
        """
        Validate enum-like field with predefined valid values.
        
        Args:
            value: The value to validate
            field_name: Name of the field being validated
            valid_values: Set of valid values
            required: Whether the field is required
            
        Returns:
            Optional[str]: Validated enum value or None if not required and not provided
            
        Raises:
            ValidationError: If value is invalid
        """
        if value is None:
            if required:
                raise ValidationError(
                    f"{field_name} is required",
                    field_name=field_name
                )
            return None
        
        if not isinstance(value, str):
            raise ValidationError(
                f"{field_name} must be a string",
                field_name=field_name,
                field_value=value,
                expected_type="string"
            )
        
        if value not in valid_values:
            raise ValidationError(
                f"{field_name} must be one of: {', '.join(sorted(valid_values))}",
                field_name=field_name,
                field_value=value
            )
        
        return value
    
    @classmethod
    def validate_constraint(cls, constraint: Any) -> str:
        """
        Validate creative constraint content.
        
        Args:
            constraint: The constraint to validate
            
        Returns:
            str: Validated constraint content
            
        Raises:
            ValidationError: If constraint is invalid
        """
        if not isinstance(constraint, str):
            raise ValidationError(
                "constraint must be a string",
                field_name="constraint",
                field_value=constraint,
                expected_type="string"
            )
        
        cleaned_constraint = constraint.strip()
        if len(cleaned_constraint) < cls.MIN_CONSTRAINT_LENGTH:
            raise ValidationError(
                f"constraint must be at least {cls.MIN_CONSTRAINT_LENGTH} character(s) long",
                field_name="constraint",
                field_value=constraint
            )
        
        if len(cleaned_constraint) > cls.MAX_CONSTRAINT_LENGTH:
            raise ValidationError(
                f"constraint must be at most {cls.MAX_CONSTRAINT_LENGTH} characters long",
                field_name="constraint",
                field_value=f"{constraint[:50]}..."
            )
        
        return cleaned_constraint
    
    @classmethod
    def validate_branch_id(cls, branch_id: Any) -> str:
        """
        Validate branch identifier.
        
        Args:
            branch_id: The branch ID to validate
            
        Returns:
            str: Validated branch ID
            
        Raises:
            ValidationError: If branch ID is invalid
        """
        if not isinstance(branch_id, str):
            raise ValidationError(
                "branchId must be a string",
                field_name="branchId",
                field_value=branch_id,
                expected_type="string"
            )
        
        cleaned_id = branch_id.strip()
        if not cleaned_id:
            raise ValidationError(
                "branchId cannot be empty",
                field_name="branchId",
                field_value=branch_id
            )
        
        # Validate format (alphanumeric with hyphens and underscores)
        if not re.match(r'^[a-zA-Z0-9_-]+$', cleaned_id):
            raise ValidationError(
                "branchId must contain only alphanumeric characters, hyphens, and underscores",
                field_name="branchId",
                field_value=branch_id
            )
        
        return cleaned_id
    
    @classmethod
    def _contains_harmful_content(cls, content: str) -> bool:
        """
        Check if content contains potentially harmful patterns.
        
        Args:
            content: Content to check
            
        Returns:
            bool: True if harmful content is detected
        """
        # Basic patterns to detect potentially harmful content
        harmful_patterns = [
            r'<script[^>]*>',  # Script tags
            r'javascript:',     # JavaScript URLs
            r'data:text/html',  # Data URLs with HTML
            r'vbscript:',      # VBScript URLs
        ]
        
        content_lower = content.lower()
        for pattern in harmful_patterns:
            if re.search(pattern, content_lower):
                return True
        
        return False
