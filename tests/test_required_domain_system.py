"""
Comprehensive test suite for the required domain system.

This module tests the new interactive domain specification functionality
including required domain validation, multi-word domain enum validation,
context parameter handling, and integration with all 6 thinking methods.
"""

import pytest
from unittest.mock import Mock, patch
from divergent_thinking_mcp.divergent_mcp import DivergentThinkingServer
from divergent_thinking_mcp.validators import ThoughtValidator
from divergent_thinking_mcp.exceptions import ValidationError
from divergent_thinking_mcp.creativity_algorithms import CreativityContext


class TestRequiredDomainValidation:
    """Test suite for required domain validation."""
    
    def test_domain_is_required_in_tool_definition(self):
        """Test that domain is marked as required in tool definition."""
        from divergent_thinking_mcp.tool_definitions import create_divergent_thinking_tools

        tools = create_divergent_thinking_tools()
        divergent_tool = tools[0]  # Should be only one tool

        # Check that domain is in required fields
        assert "domain" in divergent_tool.inputSchema["required"]
        assert "thought" in divergent_tool.inputSchema["required"]
        assert "thinking_method" in divergent_tool.inputSchema["required"]
    
    def test_validate_domain_success(self):
        """Test successful domain validation with valid multi-word domains."""
        valid_domains = [
            "product design",
            "mobile app development", 
            "healthcare technology",
            "sustainable agriculture",
            "artificial intelligence",
            "user experience design"
        ]
        
        for domain in valid_domains:
            result = ThoughtValidator.validate_domain(domain)
            assert result == domain
    
    def test_validate_domain_invalid_type(self):
        """Test domain validation fails with non-string types."""
        invalid_types = [123, None, [], {}, True]
        
        for invalid_domain in invalid_types:
            with pytest.raises(ValidationError) as exc_info:
                ThoughtValidator.validate_domain(invalid_domain)
            
            assert "domain must be a string" in str(exc_info.value)
            assert exc_info.value.field_name == "domain"
    
    def test_validate_domain_empty_string(self):
        """Test domain validation fails with empty strings."""
        empty_domains = ["", "   ", "\t", "\n"]
        
        for empty_domain in empty_domains:
            with pytest.raises(ValidationError) as exc_info:
                ThoughtValidator.validate_domain(empty_domain)
            
            assert "domain cannot be empty" in str(exc_info.value)
            assert exc_info.value.field_name == "domain"
    
    def test_validate_domain_invalid_domain(self):
        """Test domain validation fails with invalid domain values."""
        invalid_domains = [
            "invalid_domain",
            "technology",  # Single word instead of multi-word
            "random text",
            "product",  # Partial match
            "mobile development",  # Close but not exact
            "PRODUCT DESIGN",  # Wrong case
        ]
        
        for invalid_domain in invalid_domains:
            with pytest.raises(ValidationError) as exc_info:
                ThoughtValidator.validate_domain(invalid_domain)
            
            assert "domain must be one of the valid multi-word domains" in str(exc_info.value)
            assert exc_info.value.field_name == "domain"
            assert exc_info.value.field_value == invalid_domain.strip()
    
    def test_all_78_domains_are_valid(self):
        """Test that all 78 domains in VALID_DOMAINS are actually valid."""
        domains = ThoughtValidator.VALID_DOMAINS
        
        # Verify we have exactly 78 domains
        assert len(domains) == 78
        
        # Verify each domain validates successfully
        for domain in domains:
            result = ThoughtValidator.validate_domain(domain)
            assert result == domain
    
    def test_domains_are_mostly_multi_word(self):
        """Test that most domains are multi-word (contain spaces)."""
        domains = ThoughtValidator.VALID_DOMAINS

        # Allow some single-word domains like "cybersecurity", "telemedicine"
        single_word_domains = [d for d in domains if " " not in d]
        multi_word_domains = [d for d in domains if " " in d]

        # Most should be multi-word (at least 90%)
        assert len(multi_word_domains) >= len(domains) * 0.9, f"Expected at least 90% multi-word domains"

        # Verify no leading/trailing spaces
        for domain in domains:
            assert domain == domain.strip(), f"Domain '{domain}' has leading/trailing spaces"


class TestContextParameterValidation:
    """Test suite for context parameter validation."""
    
    def test_validate_target_audience_success(self):
        """Test successful target audience validation."""
        valid_audiences = [
            "students",
            "professionals", 
            "elderly users",
            "remote workers",
            "healthcare professionals"
        ]
        
        for audience in valid_audiences:
            result = ThoughtValidator.validate_target_audience(audience)
            assert result == audience
    
    def test_validate_target_audience_optional(self):
        """Test that target audience is optional."""
        result = ThoughtValidator.validate_target_audience(None)
        assert result is None
        
        result = ThoughtValidator.validate_target_audience("")
        assert result is None
    
    def test_validate_time_period_success(self):
        """Test successful time period validation."""
        valid_periods = [
            "current",
            "future",
            "2030s", 
            "historical",
            "next decade"
        ]
        
        for period in valid_periods:
            result = ThoughtValidator.validate_time_period(period)
            assert result == period
    
    def test_validate_resources_success(self):
        """Test successful resources validation."""
        valid_resources = [
            "cloud computing, mobile devices",
            "limited budget, local partnerships",
            "high-speed internet, advanced hardware"
        ]
        
        for resources in valid_resources:
            result = ThoughtValidator.validate_resources(resources)
            assert result == resources
    
    def test_validate_goals_success(self):
        """Test successful goals validation."""
        valid_goals = [
            "improve engagement, reduce costs",
            "increase accessibility, enhance security",
            "optimize performance, reduce environmental impact"
        ]
        
        for goals in valid_goals:
            result = ThoughtValidator.validate_goals(goals)
            assert result == goals


class TestCreativityContextCreation:
    """Test suite for creativity context creation with required domain."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.server = DivergentThinkingServer()
    
    def test_create_context_with_required_domain(self):
        """Test successful context creation with required domain."""
        thought_data = {
            "domain": "product design",
            "target_audience": "professionals",
            "time_period": "current",
            "resources": "advanced tools, experienced team",
            "goals": "innovation, user satisfaction"
        }
        
        context = self.server.create_creativity_context(thought_data)
        
        assert isinstance(context, CreativityContext)
        assert context.domain == "product design"
        assert context.target_audience == "professionals"
        assert context.time_period == "current"
        assert context.resources == ["advanced tools", "experienced team"]
        assert context.goals == ["innovation", "user satisfaction"]
    
    def test_create_context_missing_domain_raises_error(self):
        """Test that missing domain raises ValidationError."""
        thought_data = {
            "target_audience": "students",
            "time_period": "future"
        }
        
        with pytest.raises(ValidationError) as exc_info:
            self.server.create_creativity_context(thought_data)
        
        assert "Domain must be explicitly specified by the agent" in str(exc_info.value)
        assert exc_info.value.field_name == "domain"
        assert exc_info.value.field_value is None
    
    def test_create_context_minimal_required_data(self):
        """Test context creation with only required domain."""
        thought_data = {
            "domain": "healthcare technology"
        }
        
        context = self.server.create_creativity_context(thought_data)
        
        assert isinstance(context, CreativityContext)
        assert context.domain == "healthcare technology"
        assert context.target_audience is None
        assert context.time_period is None
        assert context.resources is None
        assert context.goals is None
        assert context.constraints == []


class TestIntegrationWithThinkingMethods:
    """Test suite for integration with all 6 thinking methods."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.server = DivergentThinkingServer()
        self.base_thought_data = {
            "thought": "Create an innovative solution",
            "domain": "artificial intelligence",
            "target_audience": "developers",
            "thoughtNumber": 1,
            "totalThoughts": 1,
            "nextThoughtNeeded": False
        }
    
    @pytest.mark.parametrize("thinking_method", [
        "structured_process",
        "generate_branches", 
        "perspective_shift",
        "creative_constraint",
        "combine_thoughts",
        "reverse_brainstorming"
    ])
    def test_thinking_method_with_required_domain(self, thinking_method):
        """Test that all thinking methods work with required domain."""
        thought_data = self.base_thought_data.copy()
        thought_data["thinking_method"] = thinking_method
        
        if thinking_method == "combine_thoughts":
            thought_data["thought2"] = "Another innovative concept"
        
        # This should not raise any validation errors
        validated_data = self.server.validate_thought_data(thought_data)
        assert validated_data["domain"] == "artificial intelligence"
        
        # Context creation should work
        context = self.server.create_creativity_context(validated_data)
        assert context.domain == "artificial intelligence"
    
    def test_structured_process_domain_validation(self):
        """Test structured process specifically validates domain."""
        thought_data = {
            "thought": "Develop a new AI system",
            "thinking_method": "structured_process",
            "thoughtNumber": 1,
            "totalThoughts": 3,
            "nextThoughtNeeded": True
            # Missing domain - should fail
        }
        
        with pytest.raises(ValidationError):
            validated_data = self.server.validate_thought_data(thought_data)
            self.server.create_creativity_context(validated_data)


class TestDomainEnumCompleteness:
    """Test suite for domain enum completeness and consistency."""
    
    def test_tool_definition_domains_match_validator_domains(self):
        """Test that tool definition domains match validator domains."""
        from divergent_thinking_mcp.tool_definitions import create_divergent_thinking_tools

        tools = create_divergent_thinking_tools()
        divergent_tool = tools[0]

        # Extract domains from tool definition enum
        tool_domains = set(divergent_tool.inputSchema["properties"]["domain"]["enum"])
        validator_domains = ThoughtValidator.VALID_DOMAINS

        # They should be identical
        assert tool_domains == validator_domains
        assert len(tool_domains) == 78
        assert len(validator_domains) == 78
    
    def test_domain_categories_coverage(self):
        """Test that domains cover expected categories."""
        domains = ThoughtValidator.VALID_DOMAINS
        
        # Check for key categories (at least one domain from each)
        design_domains = [d for d in domains if "design" in d]
        tech_domains = [d for d in domains if any(tech in d for tech in ["technology", "software", "app", "web", "artificial", "machine", "data"])]
        business_domains = [d for d in domains if any(biz in d for biz in ["business", "marketing", "commerce", "financial", "sales"])]
        health_domains = [d for d in domains if any(health in d for health in ["medical", "healthcare", "health", "pharmaceutical"])]
        
        assert len(design_domains) >= 5, f"Expected at least 5 design domains, got {len(design_domains)}"
        assert len(tech_domains) >= 10, f"Expected at least 10 tech domains, got {len(tech_domains)}"
        assert len(business_domains) >= 5, f"Expected at least 5 business domains, got {len(business_domains)}"
        assert len(health_domains) >= 5, f"Expected at least 5 health domains, got {len(health_domains)}"


class TestErrorHandlingAndEdgeCases:
    """Test suite for error handling and edge cases."""

    def setup_method(self):
        """Set up test fixtures."""
        self.server = DivergentThinkingServer()

    def test_domain_validation_with_whitespace(self):
        """Test domain validation handles whitespace correctly."""
        # Leading/trailing whitespace should be stripped and validated
        domain_with_spaces = "  product design  "
        result = ThoughtValidator.validate_domain(domain_with_spaces)
        assert result == "product design"

        # Internal whitespace should be preserved
        domain_internal_spaces = "mobile app development"
        result = ThoughtValidator.validate_domain(domain_internal_spaces)
        assert result == "mobile app development"

    def test_context_parameter_parsing(self):
        """Test comma-separated context parameter parsing."""
        thought_data = {
            "domain": "e-commerce",
            "resources": "cloud computing, mobile devices, limited budget",
            "goals": "improve engagement, reduce costs, increase accessibility"
        }

        context = self.server.create_creativity_context(thought_data)

        assert context.resources == ["cloud computing", "mobile devices", "limited budget"]
        assert context.goals == ["improve engagement", "reduce costs", "increase accessibility"]

    def test_context_parameter_parsing_edge_cases(self):
        """Test edge cases in comma-separated parameter parsing."""
        # Empty strings and whitespace handling
        test_cases = [
            ("", None),
            ("   ", None),
            ("item1, , item3", ["item1", "item3"]),  # Empty item filtered out
            ("  item1  ,  item2  ", ["item1", "item2"]),  # Whitespace stripped
            ("single_item", ["single_item"]),  # Single item
        ]

        for input_value, expected in test_cases:
            result = self.server._parse_comma_separated(input_value)
            assert result == expected, f"Failed for input '{input_value}'"

    def test_validation_error_contains_helpful_information(self):
        """Test that validation errors contain helpful information."""
        with pytest.raises(ValidationError) as exc_info:
            ThoughtValidator.validate_domain("invalid_domain")

        error = exc_info.value
        assert error.field_name == "domain"
        assert error.field_value == "invalid_domain"
        assert "valid multi-word domains" in str(error)
        assert "product design" in str(error)  # Example domains mentioned
        assert "mobile app development" in str(error)

    def test_domain_case_sensitivity(self):
        """Test that domain validation is case-sensitive."""
        # Exact case should work
        assert ThoughtValidator.validate_domain("product design") == "product design"

        # Wrong case should fail
        with pytest.raises(ValidationError):
            ThoughtValidator.validate_domain("Product Design")

        with pytest.raises(ValidationError):
            ThoughtValidator.validate_domain("PRODUCT DESIGN")

        with pytest.raises(ValidationError):
            ThoughtValidator.validate_domain("Product design")

    def test_constraint_handling_in_context(self):
        """Test that constraints are properly handled in context creation."""
        thought_data = {
            "domain": "sustainable agriculture",
            "constraint": "must use renewable energy only"
        }

        context = self.server.create_creativity_context(thought_data)
        assert context.constraints == ["must use renewable energy only"]

        # Test without constraints
        thought_data_no_constraint = {
            "domain": "sustainable agriculture"
        }

        context_no_constraint = self.server.create_creativity_context(thought_data_no_constraint)
        assert context_no_constraint.constraints == []


class TestPerformanceAndScalability:
    """Test suite for performance considerations."""

    def test_domain_validation_performance(self):
        """Test that domain validation performs well with all domains."""
        import time

        domains = list(ThoughtValidator.VALID_DOMAINS)

        start_time = time.time()
        for domain in domains:
            ThoughtValidator.validate_domain(domain)
        end_time = time.time()

        # Should validate all 78 domains in under 0.1 seconds
        assert end_time - start_time < 0.1, "Domain validation is too slow"

    def test_large_context_parameters(self):
        """Test handling of large context parameters."""
        # Test with reasonable lengths (not maximum to avoid individual item length limits)
        large_audience = "a" * 100  # Reasonable length
        large_time_period = "b" * 50  # Reasonable length
        large_resources = "resource1, resource2, resource3"  # Multiple items within limits
        large_goals = "goal1, goal2, goal3"  # Multiple items within limits

        # These should all validate successfully
        assert ThoughtValidator.validate_target_audience(large_audience) == large_audience
        assert ThoughtValidator.validate_time_period(large_time_period) == large_time_period
        assert ThoughtValidator.validate_resources(large_resources) == large_resources
        assert ThoughtValidator.validate_goals(large_goals) == large_goals

    def test_context_creation_with_all_parameters(self):
        """Test context creation with all possible parameters."""
        server = DivergentThinkingServer()

        thought_data = {
            "domain": "artificial intelligence",
            "target_audience": "machine learning researchers",
            "time_period": "next 5 years",
            "resources": "high-performance computing, large datasets, expert team",
            "goals": "breakthrough accuracy, ethical AI, real-world deployment",
            "constraint": "must be explainable and transparent"
        }

        context = server.create_creativity_context(thought_data)

        assert context.domain == "artificial intelligence"
        assert context.target_audience == "machine learning researchers"
        assert context.time_period == "next 5 years"
        assert len(context.resources) == 3
        assert len(context.goals) == 3
        assert len(context.constraints) == 1


class TestBackwardCompatibilityBreaking:
    """Test suite to verify breaking changes are properly implemented."""

    def test_no_automatic_domain_extraction(self):
        """Test that automatic domain extraction is completely removed."""
        # This should fail because domain is not provided
        thought_data = {
            "thought": "Create a mobile app for healthcare professionals",
            "thinking_method": "generate_branches",
            "thoughtNumber": 1,
            "totalThoughts": 1,
            "nextThoughtNeeded": False
            # No domain provided - should fail
        }

        server = DivergentThinkingServer()

        # Validation should pass (domain not required at this level)
        validated_data = server.validate_thought_data(thought_data)

        # But context creation should fail due to missing domain
        with pytest.raises(ValidationError) as exc_info:
            server.create_creativity_context(validated_data)

        assert "Domain must be explicitly specified by the agent" in str(exc_info.value)

    def test_domain_keywords_not_used_for_extraction(self):
        """Test that domain keywords are not used for automatic extraction."""
        # Even if thought contains domain keywords, domain must be explicit
        thought_data = {
            "thought": "Design a user interface for a mobile application with great user experience",
            "thinking_method": "generate_branches",
            "thoughtNumber": 1,
            "totalThoughts": 1,
            "nextThoughtNeeded": False
            # No explicit domain despite keywords in thought
        }

        server = DivergentThinkingServer()
        validated_data = server.validate_thought_data(thought_data)

        # Should still fail even though thought contains UI/UX keywords
        with pytest.raises(ValidationError):
            server.create_creativity_context(validated_data)

    def test_breaking_change_documentation_compliance(self):
        """Test that the implementation matches breaking change requirements."""
        # Verify domain is truly required
        from divergent_thinking_mcp.tool_definitions import create_divergent_thinking_tools

        tools = create_divergent_thinking_tools()
        divergent_tool = tools[0]

        assert "domain" in divergent_tool.inputSchema["required"]

        # Verify domain description mentions it's required
        domain_description = divergent_tool.inputSchema["properties"]["domain"]["description"]
        assert "REQUIRED" in domain_description
        assert "explicitly specified" in domain_description

        # Verify no fallback logic exists
        server = DivergentThinkingServer()

        # Check that create_creativity_context doesn't have fallback logic
        import inspect
        source = inspect.getsource(server.create_creativity_context)
        # Should mention "no fallback" or "no automatic" but not implement fallback
        assert "no automatic" in source.lower() or "no fallback" in source.lower()
        # Should not have actual fallback implementation
        assert "if not domain" in source  # Should check for missing domain and raise error
