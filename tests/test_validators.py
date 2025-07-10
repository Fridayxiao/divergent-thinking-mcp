"""
Tests for validators module.

This module tests the validation functionality for thought data
and other input validation requirements.
"""

import pytest
from divergent_thinking_mcp.validators import ThoughtValidator
from divergent_thinking_mcp.exceptions import ValidationError


class TestThoughtValidator:
    """Test suite for ThoughtValidator class."""
    
    def test_validate_required_fields_success(self):
        """Test successful validation of required fields."""
        data = {
            "thought": "Test thought",
            "thoughtNumber": 1,
            "totalThoughts": 3,
            "nextThoughtNeeded": True
        }
        required_fields = ["thought", "thoughtNumber", "totalThoughts", "nextThoughtNeeded"]
        
        # Should not raise any exception
        ThoughtValidator.validate_required_fields(data, required_fields)
    
    def test_validate_required_fields_missing(self):
        """Test validation failure when required fields are missing."""
        data = {
            "thought": "Test thought",
            "thoughtNumber": 1
            # Missing totalThoughts and nextThoughtNeeded
        }
        required_fields = ["thought", "thoughtNumber", "totalThoughts", "nextThoughtNeeded"]
        
        with pytest.raises(ValidationError) as exc_info:
            ThoughtValidator.validate_required_fields(data, required_fields)
        
        assert "Missing required fields" in str(exc_info.value)
        assert "totalThoughts" in str(exc_info.value)
    
    def test_validate_thought_content_success(self):
        """Test successful thought content validation."""
        valid_thoughts = [
            "This is a valid thought",
            "Design an innovative product",
            "A" * 100,  # Long but valid
            "思考一个创新的解决方案"  # Unicode content
        ]
        
        for thought in valid_thoughts:
            result = ThoughtValidator.validate_thought_content(thought)
            assert result == thought.strip()
    
    def test_validate_thought_content_invalid_type(self):
        """Test thought content validation with invalid types."""
        invalid_thoughts = [123, None, [], {}]
        
        for thought in invalid_thoughts:
            with pytest.raises(ValidationError) as exc_info:
                ThoughtValidator.validate_thought_content(thought)
            assert "must be a string" in str(exc_info.value)
    
    def test_validate_thought_content_empty(self):
        """Test thought content validation with empty content."""
        empty_thoughts = ["", "   ", "\t\n"]
        
        for thought in empty_thoughts:
            with pytest.raises(ValidationError) as exc_info:
                ThoughtValidator.validate_thought_content(thought)
            assert "must be at least" in str(exc_info.value)
    
    def test_validate_thought_content_too_long(self):
        """Test thought content validation with content that's too long."""
        long_thought = "A" * (ThoughtValidator.MAX_THOUGHT_LENGTH + 1)
        
        with pytest.raises(ValidationError) as exc_info:
            ThoughtValidator.validate_thought_content(long_thought)
        assert "must be at most" in str(exc_info.value)
    
    def test_validate_thought_content_harmful(self):
        """Test thought content validation with potentially harmful content."""
        harmful_thoughts = [
            "<script>alert('xss')</script>",
            "javascript:void(0)",
            "data:text/html,<h1>test</h1>"
        ]
        
        for thought in harmful_thoughts:
            with pytest.raises(ValidationError) as exc_info:
                ThoughtValidator.validate_thought_content(thought)
            assert "harmful content" in str(exc_info.value)
    
    def test_validate_integer_field_success(self):
        """Test successful integer field validation."""
        valid_values = [1, 5, 100, 999]
        
        for value in valid_values:
            result = ThoughtValidator.validate_integer_field(
                value, "testField", 1, 1000
            )
            assert result == value
    
    def test_validate_integer_field_invalid_type(self):
        """Test integer field validation with invalid types."""
        invalid_values = ["1", 1.5, None, []]
        
        for value in invalid_values:
            with pytest.raises(ValidationError) as exc_info:
                ThoughtValidator.validate_integer_field(
                    value, "testField", 1, 1000
                )
            assert "must be an integer" in str(exc_info.value)
    
    def test_validate_integer_field_out_of_range(self):
        """Test integer field validation with out-of-range values."""
        with pytest.raises(ValidationError) as exc_info:
            ThoughtValidator.validate_integer_field(0, "testField", 1, 10)
        assert "must be between" in str(exc_info.value)
        
        with pytest.raises(ValidationError) as exc_info:
            ThoughtValidator.validate_integer_field(11, "testField", 1, 10)
        assert "must be between" in str(exc_info.value)
    
    def test_validate_boolean_field_success(self):
        """Test successful boolean field validation."""
        valid_values = [True, False]
        
        for value in valid_values:
            result = ThoughtValidator.validate_boolean_field(value, "testField")
            assert result == value
    
    def test_validate_boolean_field_invalid_type(self):
        """Test boolean field validation with invalid types."""
        invalid_values = [1, 0, "true", "false", None, []]
        
        for value in invalid_values:
            with pytest.raises(ValidationError) as exc_info:
                ThoughtValidator.validate_boolean_field(value, "testField")
            assert "must be a boolean" in str(exc_info.value)
    
    def test_validate_enum_field_success(self):
        """Test successful enum field validation."""
        valid_values = {"option1", "option2", "option3"}
        
        for value in valid_values:
            result = ThoughtValidator.validate_enum_field(
                value, "testField", valid_values
            )
            assert result == value
    
    def test_validate_enum_field_invalid_value(self):
        """Test enum field validation with invalid values."""
        valid_values = {"option1", "option2", "option3"}
        
        with pytest.raises(ValidationError) as exc_info:
            ThoughtValidator.validate_enum_field(
                "invalid_option", "testField", valid_values
            )
        assert "must be one of" in str(exc_info.value)
    
    def test_validate_enum_field_optional(self):
        """Test enum field validation with optional field."""
        valid_values = {"option1", "option2"}
        
        # Should return None for optional field
        result = ThoughtValidator.validate_enum_field(
            None, "testField", valid_values, required=False
        )
        assert result is None
        
        # Should raise error for required field
        with pytest.raises(ValidationError):
            ThoughtValidator.validate_enum_field(
                None, "testField", valid_values, required=True
            )
    
    def test_validate_constraint_success(self):
        """Test successful constraint validation."""
        valid_constraints = [
            "must be eco-friendly",
            "introduce impossible elements",
            "A" * 100  # Long but valid
        ]
        
        for constraint in valid_constraints:
            result = ThoughtValidator.validate_constraint(constraint)
            assert result == constraint.strip()
    
    def test_validate_constraint_invalid(self):
        """Test constraint validation with invalid input."""
        # Invalid type
        with pytest.raises(ValidationError) as exc_info:
            ThoughtValidator.validate_constraint(123)
        assert "must be a string" in str(exc_info.value)
        
        # Too short
        with pytest.raises(ValidationError) as exc_info:
            ThoughtValidator.validate_constraint("")
        assert "must be at least" in str(exc_info.value)
        
        # Too long
        long_constraint = "A" * (ThoughtValidator.MAX_CONSTRAINT_LENGTH + 1)
        with pytest.raises(ValidationError) as exc_info:
            ThoughtValidator.validate_constraint(long_constraint)
        assert "must be at most" in str(exc_info.value)
    
    def test_validate_branch_id_success(self):
        """Test successful branch ID validation."""
        valid_ids = [
            "branch1",
            "main-branch",
            "test_branch_123",
            "A1B2C3",
            "creative-idea-1"
        ]
        
        for branch_id in valid_ids:
            result = ThoughtValidator.validate_branch_id(branch_id)
            assert result == branch_id.strip()
    
    def test_validate_branch_id_invalid(self):
        """Test branch ID validation with invalid input."""
        # Invalid type
        with pytest.raises(ValidationError) as exc_info:
            ThoughtValidator.validate_branch_id(123)
        assert "must be a string" in str(exc_info.value)
        
        # Empty
        with pytest.raises(ValidationError) as exc_info:
            ThoughtValidator.validate_branch_id("")
        assert "cannot be empty" in str(exc_info.value)
        
        # Invalid characters
        invalid_ids = ["branch with spaces", "branch@special", "branch/slash"]
        for branch_id in invalid_ids:
            with pytest.raises(ValidationError) as exc_info:
                ThoughtValidator.validate_branch_id(branch_id)
            assert "alphanumeric characters" in str(exc_info.value)
    
    def test_class_constants(self):
        """Test that class constants are properly defined."""
        assert ThoughtValidator.MIN_THOUGHT_LENGTH == 1
        assert ThoughtValidator.MAX_THOUGHT_LENGTH == 5000
        assert ThoughtValidator.MIN_CONSTRAINT_LENGTH == 1
        assert ThoughtValidator.MAX_CONSTRAINT_LENGTH == 500
        assert ThoughtValidator.MIN_THOUGHT_NUMBER == 1
        assert ThoughtValidator.MAX_THOUGHT_NUMBER == 1000
        assert ThoughtValidator.MIN_TOTAL_THOUGHTS == 1
        assert ThoughtValidator.MAX_TOTAL_THOUGHTS == 1000
    
    def test_valid_enum_sets(self):
        """Test that valid enum sets are properly defined."""
        assert "branch_generation" in ThoughtValidator.VALID_PROMPT_TYPES
        assert "creative_constraint" in ThoughtValidator.VALID_PROMPT_TYPES
        assert "perspective_shift" in ThoughtValidator.VALID_PROMPT_TYPES
        assert "combination" in ThoughtValidator.VALID_PROMPT_TYPES
        
        assert "inanimate_object" in ThoughtValidator.VALID_PERSPECTIVE_TYPES
        assert "abstract_concept" in ThoughtValidator.VALID_PERSPECTIVE_TYPES
        assert "impossible_being" in ThoughtValidator.VALID_PERSPECTIVE_TYPES


class TestValidationErrorHandling:
    """Test suite for validation error handling."""
    
    def test_validation_error_with_context(self):
        """Test that validation errors include proper context."""
        try:
            ThoughtValidator.validate_integer_field(
                "not_an_int", "thoughtNumber", 1, 10
            )
        except ValidationError as e:
            assert e.field_name == "thoughtNumber"
            assert e.field_value == "not_an_int"
            assert e.expected_type == "integer"
            assert e.error_code == "VALIDATION_ERROR"
    
    def test_validation_error_serialization(self):
        """Test that validation errors can be serialized."""
        try:
            ThoughtValidator.validate_thought_content(123)
        except ValidationError as e:
            error_dict = e.to_dict()
            assert error_dict["error_type"] == "ValidationError"
            assert error_dict["message"] is not None
            assert error_dict["error_code"] == "VALIDATION_ERROR"
            assert "context" in error_dict
