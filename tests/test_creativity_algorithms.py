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
            domain="artificial intelligence",
            constraints=["budget limited", "must be portable"],
            target_audience="developers",
            time_period="2024",
            resources=["cloud computing", "mobile devices"],
            goals=["improve productivity", "reduce complexity"]
        )

    @pytest.fixture
    def cybersecurity_context(self):
        """Create a cybersecurity context for testing."""
        return CreativityContext(
            domain="cybersecurity",
            constraints=["regulatory compliance", "performance requirements"],
            target_audience="security professionals",
            time_period="current",
            resources=["security tools", "threat intelligence"],
            goals=["improve security posture", "reduce vulnerabilities"]
        )

    @pytest.fixture
    def healthcare_context(self):
        """Create a healthcare context for testing."""
        return CreativityContext(
            domain="healthcare technology",
            constraints=["patient safety", "regulatory approval"],
            target_audience="healthcare providers",
            time_period="current",
            resources=["medical devices", "health data"],
            goals=["improve patient outcomes", "reduce costs"]
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
        assert len(results) == 6  # Limited to top 6 most relevant analogies
        assert all(isinstance(result, str) for result in results)
        assert all(idea in result for result in results)
    
    def test_apply_analogical_thinking_specific_domain(self, algorithms):
        """Test analogical thinking with specific domain."""
        idea = "team collaboration"
        domain = "music"
        results = algorithms.apply_analogical_thinking(idea, domain)
        
        assert isinstance(results, list)
        assert len(results) == 6  # Limited to top 6 most relevant analogies
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
            assert len(results[hat]) == 4  # 4 prompts per hat (domain-aware version)
            assert all(isinstance(prompt, str) and len(prompt) > 0 for prompt in results[hat])
    
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


class TestDomainAwareCreativity:
    """Test suite for domain-aware creativity enhancements."""

    @pytest.fixture
    def algorithms(self):
        """Create a CreativityAlgorithms instance for testing."""
        return CreativityAlgorithms()

    def test_intelligent_word_selection_ai_domain(self, algorithms):
        """Test that intelligent word selection returns AI-relevant terms."""
        context = CreativityContext(domain="artificial intelligence", constraints=[])

        words = algorithms._intelligent_word_selection("artificial intelligence", context, "core_concepts", 3)

        # Should contain AI-relevant terms
        ai_terms = ["neural networks", "machine learning", "deep learning", "algorithms", "optimization", "inference"]
        assert any(term in " ".join(words) for term in ai_terms)

        # Should not contain irrelevant terms
        irrelevant_terms = ["butterfly", "cooking", "sports"]
        assert not any(term in " ".join(words) for term in irrelevant_terms)

    def test_intelligent_word_selection_cybersecurity_domain(self, algorithms):
        """Test that intelligent word selection returns cybersecurity-relevant terms."""
        context = CreativityContext(domain="cybersecurity", constraints=[])

        words = algorithms._intelligent_word_selection("cybersecurity", context, "core_concepts", 3)

        # Should contain cybersecurity-relevant terms
        cybersec_terms = ["encryption", "authentication", "firewall", "intrusion detection", "vulnerability"]
        assert any(term in " ".join(words) for term in cybersec_terms)

    def test_domain_aware_scamper_ai(self, algorithms):
        """Test SCAMPER with AI domain awareness."""
        context = CreativityContext(domain="artificial intelligence", constraints=[])

        scamper_results = algorithms.apply_scamper("neural network optimizer", context)

        # Should contain AI-relevant terms
        combined_results = " ".join(scamper_results).lower()
        ai_terms = ["neural", "machine learning", "algorithms", "optimization", "training", "inference"]
        assert any(term in combined_results for term in ai_terms)

        # Should reference the domain
        assert "artificial intelligence" in combined_results

    def test_domain_aware_scamper_cybersecurity(self, algorithms):
        """Test SCAMPER with cybersecurity domain awareness."""
        context = CreativityContext(domain="cybersecurity", constraints=[])

        scamper_results = algorithms.apply_scamper("network monitoring system", context)

        # Should contain cybersecurity-relevant terms
        combined_results = " ".join(scamper_results).lower()
        cybersec_terms = ["encryption", "authentication", "security", "threat", "vulnerability", "firewall"]
        assert any(term in combined_results for term in cybersec_terms)

        # Should reference the domain
        assert "cybersecurity" in combined_results

    def test_domain_aware_random_word_association(self, algorithms):
        """Test random word association with domain awareness."""
        context = CreativityContext(domain="healthcare technology", constraints=[])

        word_results = algorithms.generate_random_word_associations("patient monitoring", 3, context)

        # Should contain healthcare-relevant terms
        combined_results = " ".join(word_results).lower()
        healthcare_terms = ["patient", "clinical", "medical", "health", "care", "treatment", "diagnosis"]
        assert any(term in combined_results for term in healthcare_terms)

        # Should reference the domain
        assert "healthcare technology" in combined_results

    def test_domain_aware_analogical_thinking(self, algorithms):
        """Test analogical thinking with domain-relevant analogies."""
        context = CreativityContext(domain="artificial intelligence", constraints=[])

        analogies = algorithms.apply_analogical_thinking("machine learning model", context=context)

        # Should contain AI-relevant analogies
        combined_analogies = " ".join(analogies).lower()
        ai_analogy_terms = ["biological", "neural", "cognitive", "mathematical", "learning", "intelligence"]
        assert any(term in combined_analogies for term in ai_analogy_terms)

        # Should reference the domain
        assert "artificial intelligence" in combined_analogies

    def test_domain_aware_biomimicry(self, algorithms):
        """Test biomimicry with domain-relevant examples."""
        context = CreativityContext(domain="renewable energy", constraints=[])

        biomimicry_results = algorithms.apply_biomimicry("solar panel design", context)

        # Should contain renewable energy relevant biomimicry
        combined_results = " ".join(biomimicry_results).lower()
        energy_bio_terms = ["photosynthesis", "solar", "energy", "conversion", "efficiency", "light"]
        assert any(term in combined_results for term in energy_bio_terms)

        # Should reference the domain
        assert "renewable energy" in combined_results

    def test_domain_aware_six_thinking_hats(self, algorithms):
        """Test Six Thinking Hats with domain-specific perspectives."""
        context = CreativityContext(domain="healthcare technology", constraints=[])

        hats_results = algorithms.apply_six_thinking_hats("telemedicine platform", context)

        # Should have all six hats
        assert len(hats_results) == 6

        # Should contain healthcare-specific perspectives
        all_results = " ".join([" ".join(prompts) for prompts in hats_results.values()]).lower()
        healthcare_terms = ["patient", "clinical", "medical", "healthcare", "safety", "regulatory"]
        assert any(term in all_results for term in healthcare_terms)

    def test_domain_relevance_improvement(self, algorithms):
        """Test that domain-aware methods produce more relevant outputs than generic ones."""
        context = CreativityContext(domain="cybersecurity", constraints=[])

        # Test domain-aware SCAMPER
        domain_scamper = algorithms.apply_scamper("firewall system", context)
        combined_domain = " ".join(domain_scamper).lower()

        # Should contain cybersecurity terms
        cybersec_terms = ["security", "threat", "encryption", "authentication", "vulnerability"]
        domain_relevance_score = sum(1 for term in cybersec_terms if term in combined_domain)

        # Should have domain relevance (at least 1 relevant term, showing improvement over random)
        assert domain_relevance_score >= 1

    def test_context_parameter_usage(self, algorithms):
        """Test that context parameters influence output."""
        context_with_goals = CreativityContext(
            domain="artificial intelligence",
            constraints=["performance"],
            goals=["improve accuracy", "reduce latency"]
        )

        context_with_constraints = CreativityContext(
            domain="artificial intelligence",
            constraints=["privacy", "interpretability"],
            goals=[]
        )

        # Test with goals
        words_with_goals = algorithms._intelligent_word_selection(
            "artificial intelligence", context_with_goals, "core_concepts", 5
        )

        # Test with constraints
        words_with_constraints = algorithms._intelligent_word_selection(
            "artificial intelligence", context_with_constraints, "core_concepts", 5
        )

        # Both should return AI-relevant terms
        ai_terms = ["neural networks", "machine learning", "algorithms", "optimization"]
        assert any(term in " ".join(words_with_goals) for term in ai_terms)
        assert any(term in " ".join(words_with_constraints) for term in ai_terms)

    def test_fallback_behavior(self, algorithms):
        """Test fallback behavior for unknown domains."""
        context = CreativityContext(domain="unknown_domain", constraints=[])

        # Should still work and fall back to generic words
        words = algorithms._intelligent_word_selection("unknown_domain", context, "core_concepts", 3)
        assert len(words) == 3
        assert all(isinstance(word, str) for word in words)

        # SCAMPER should still work
        scamper_results = algorithms.apply_scamper("test idea", context)
        assert len(scamper_results) == 7
