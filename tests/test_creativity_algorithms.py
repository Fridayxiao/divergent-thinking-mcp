"""
Tests for creativity algorithms module.

This module tests the various creativity techniques and algorithms
implemented in the divergent thinking MCP server.
"""

import pytest
from divergent_thinking_mcp.creativity_algorithms import (
    CreativityAlgorithms, 
    CreativityTechnique, 
    CreativityContext
)


class TestCreativityAlgorithms:
    """Test suite for CreativityAlgorithms class."""
    
    @pytest.fixture
    def algorithms(self):
        """Create a CreativityAlgorithms instance for testing."""
        return CreativityAlgorithms()
    
    @pytest.fixture
    def sample_context(self):
        """Create a sample creativity context for testing."""
        return CreativityContext(
            domain="technology",
            constraints=["budget limited", "must be portable"],
            target_audience="developers",
            time_period="2024",
            resources=["cloud computing", "mobile devices"],
            goals=["improve productivity", "reduce complexity"]
        )
    
    def test_apply_scamper(self, algorithms):
        """Test SCAMPER technique application."""
        idea = "design a smart water bottle"
        results = algorithms.apply_scamper(idea)
        
        assert isinstance(results, list)
        assert len(results) == 7  # One for each SCAMPER letter
        assert all(isinstance(result, str) for result in results)
        assert all(idea in result for result in results)
        
        # Check that each SCAMPER category is represented
        scamper_categories = ["Substitute", "Combine", "Adapt", "Modify", "Put to other uses", "Eliminate", "Reverse"]
        for category in scamper_categories:
            assert any(category in result for result in results)
    
    def test_generate_random_word_associations(self, algorithms):
        """Test random word association technique."""
        idea = "office chair"
        num_words = 3
        results = algorithms.generate_random_word_associations(idea, num_words)
        
        assert isinstance(results, list)
        assert len(results) == num_words * 4  # 4 prompts per word
        assert all(isinstance(result, str) for result in results)
        assert all(idea in result for result in results)
    
    def test_apply_analogical_thinking(self, algorithms):
        """Test analogical thinking technique."""
        idea = "mobile app design"
        results = algorithms.apply_analogical_thinking(idea)
        
        assert isinstance(results, list)
        assert len(results) == 12  # 3 domains × 4 prompts each
        assert all(isinstance(result, str) for result in results)
        assert all(idea in result for result in results)
    
    def test_apply_analogical_thinking_specific_domain(self, algorithms):
        """Test analogical thinking with specific domain."""
        idea = "team collaboration"
        domain = "music"
        results = algorithms.apply_analogical_thinking(idea, domain)
        
        assert isinstance(results, list)
        assert len(results) == 4  # 1 domain × 4 prompts
        assert all(isinstance(result, str) for result in results)
        assert all("music" in result.lower() for result in results)
    
    def test_apply_reverse_brainstorming(self, algorithms):
        """Test reverse brainstorming technique."""
        idea = "create a user-friendly app"
        results = algorithms.apply_reverse_brainstorming(idea)
        
        assert isinstance(results, list)
        assert len(results) == 7  # 6 failure prompts + 1 reversal instruction
        assert all(isinstance(result, str) for result in results)
        assert all(idea in result for result in results[:-1])  # All except last should contain idea
        assert "reverse" in results[-1].lower()  # Last should be about reversing
    
    def test_apply_six_thinking_hats(self, algorithms):
        """Test Six Thinking Hats technique."""
        idea = "implement remote work policy"
        results = algorithms.apply_six_thinking_hats(idea)
        
        assert isinstance(results, dict)
        assert len(results) == 6  # Six different hats
        
        expected_hats = [
            "White Hat (Facts)",
            "Red Hat (Emotions)", 
            "Black Hat (Critical)",
            "Yellow Hat (Positive)",
            "Green Hat (Creative)",
            "Blue Hat (Process)"
        ]
        
        for hat in expected_hats:
            assert hat in results
            assert isinstance(results[hat], list)
            assert len(results[hat]) == 3  # 3 prompts per hat
            assert all(idea in prompt for prompt in results[hat])
    
    def test_apply_biomimicry(self, algorithms):
        """Test biomimicry technique."""
        idea = "efficient transportation"
        results = algorithms.apply_biomimicry(idea)
        
        assert isinstance(results, list)
        assert len(results) == 12  # 4 examples × 3 prompts each
        assert all(isinstance(result, str) for result in results)
        assert all(idea in result for result in results)
    
    def test_apply_constraint_relaxation(self, algorithms):
        """Test constraint relaxation technique."""
        idea = "design a mobile app"
        constraints = ["limited battery", "small screen", "slow internet"]
        results = algorithms.apply_constraint_relaxation(idea, constraints)
        
        assert isinstance(results, list)
        assert len(results) == 12  # 3 constraints × 4 prompts each
        assert all(isinstance(result, str) for result in results)
        assert all(idea in result for result in results)
    
    def test_apply_constraint_relaxation_default_constraints(self, algorithms):
        """Test constraint relaxation with default constraints."""
        idea = "create a learning platform"
        results = algorithms.apply_constraint_relaxation(idea, [])
        
        assert isinstance(results, list)
        assert len(results) == 20  # 5 default constraints × 4 prompts each
        assert all(isinstance(result, str) for result in results)
        assert all(idea in result for result in results)


class TestCreativityContext:
    """Test suite for CreativityContext dataclass."""
    
    def test_creativity_context_creation(self):
        """Test creating a creativity context."""
        context = CreativityContext(
            domain="design",
            constraints=["eco-friendly", "affordable"],
            target_audience="students",
            time_period="future",
            resources=["3D printing", "recycled materials"],
            goals=["sustainability", "accessibility"]
        )
        
        assert context.domain == "design"
        assert context.constraints == ["eco-friendly", "affordable"]
        assert context.target_audience == "students"
        assert context.time_period == "future"
        assert context.resources == ["3D printing", "recycled materials"]
        assert context.goals == ["sustainability", "accessibility"]
    
    def test_creativity_context_minimal(self):
        """Test creating a minimal creativity context."""
        context = CreativityContext(
            domain="technology",
            constraints=[]
        )
        
        assert context.domain == "technology"
        assert context.constraints == []
        assert context.target_audience is None
        assert context.time_period is None
        assert context.resources is None
        assert context.goals is None


class TestCreativityTechnique:
    """Test suite for CreativityTechnique enum."""
    
    def test_creativity_technique_values(self):
        """Test that all expected creativity techniques are available."""
        expected_techniques = [
            "scamper",
            "random_word",
            "morphological_analysis",
            "analogical_thinking",
            "reverse_brainstorming",
            "six_thinking_hats",
            "biomimicry",
            "constraint_relaxation"
        ]
        
        actual_techniques = [technique.value for technique in CreativityTechnique]
        
        for expected in expected_techniques:
            assert expected in actual_techniques
        
        assert len(actual_techniques) == len(expected_techniques)


class TestIntegration:
    """Integration tests for creativity algorithms."""
    
    def test_algorithms_with_context(self):
        """Test algorithms work with creativity context."""
        algorithms = CreativityAlgorithms()
        context = CreativityContext(
            domain="business",
            constraints=["remote work", "global team"],
            target_audience="managers"
        )
        
        # Test SCAMPER with context
        idea = "team communication tool"
        results = algorithms.apply_scamper(idea, context)
        
        assert isinstance(results, list)
        assert len(results) == 7
        assert all(isinstance(result, str) for result in results)
    
    def test_all_techniques_produce_output(self):
        """Test that all techniques produce non-empty output."""
        algorithms = CreativityAlgorithms()
        idea = "sustainable packaging"
        
        # Test each technique
        scamper_results = algorithms.apply_scamper(idea)
        assert len(scamper_results) > 0
        
        word_results = algorithms.generate_random_word_associations(idea, 1)
        assert len(word_results) > 0
        
        analogical_results = algorithms.apply_analogical_thinking(idea)
        assert len(analogical_results) > 0
        
        reverse_results = algorithms.apply_reverse_brainstorming(idea)
        assert len(reverse_results) > 0
        
        hats_results = algorithms.apply_six_thinking_hats(idea)
        assert len(hats_results) > 0
        
        biomimicry_results = algorithms.apply_biomimicry(idea)
        assert len(biomimicry_results) > 0
        
        constraint_results = algorithms.apply_constraint_relaxation(idea, ["cost"])
        assert len(constraint_results) > 0
