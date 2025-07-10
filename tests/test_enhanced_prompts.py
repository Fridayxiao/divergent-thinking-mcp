"""
Tests for enhanced prompts module.

This module tests the enhanced prompt generation capabilities
that integrate creativity algorithms with structured templates.
"""

import pytest
from divergent_thinking_mcp.enhanced_prompts import EnhancedPromptGenerator
from divergent_thinking_mcp.creativity_algorithms import CreativityTechnique, CreativityContext


class TestEnhancedPromptGenerator:
    """Test suite for EnhancedPromptGenerator class."""
    
    @pytest.fixture
    def generator(self):
        """Create an EnhancedPromptGenerator instance for testing."""
        return EnhancedPromptGenerator()
    
    @pytest.fixture
    def sample_context(self):
        """Create a sample creativity context for testing."""
        return CreativityContext(
            domain="technology",
            constraints=["eco-friendly", "affordable"],
            target_audience="students"
        )
    
    def test_generate_enhanced_branch_prompt_default(self, generator):
        """Test enhanced branch prompt generation with default settings."""
        thought = "Create an innovative learning platform"
        prompt = generator.generate_enhanced_branch_prompt(thought)
        
        assert isinstance(prompt, str)
        assert len(prompt) > 100  # Should be substantial
        assert thought in prompt
        assert "Starting with the thought:" in prompt
    
    def test_generate_enhanced_branch_prompt_scamper(self, generator, sample_context):
        """Test enhanced branch prompt with SCAMPER technique."""
        thought = "Design a sustainable packaging solution"
        prompt = generator.generate_enhanced_branch_prompt(
            thought, 
            context=sample_context,
            technique=CreativityTechnique.SCAMPER
        )
        
        assert isinstance(prompt, str)
        assert thought in prompt
        assert "SCAMPER technique" in prompt
        # Should contain at least one SCAMPER element (any of the 7 categories)
        scamper_elements = ["Substitute", "Combine", "Adapt", "Modify", "Put to other uses", "Eliminate", "Reverse"]
        assert any(element in prompt for element in scamper_elements)
    
    def test_generate_enhanced_branch_prompt_random_word(self, generator):
        """Test enhanced branch prompt with random word technique."""
        thought = "Build a social media platform"
        prompt = generator.generate_enhanced_branch_prompt(
            thought,
            technique=CreativityTechnique.RANDOM_WORD
        )
        
        assert isinstance(prompt, str)
        assert thought in prompt
        assert "random word association" in prompt
    
    def test_generate_enhanced_branch_prompt_analogical(self, generator):
        """Test enhanced branch prompt with analogical thinking."""
        thought = "Create a fitness tracking app"
        prompt = generator.generate_enhanced_branch_prompt(
            thought,
            technique=CreativityTechnique.ANALOGICAL_THINKING
        )
        
        assert isinstance(prompt, str)
        assert thought in prompt
        assert "analogical thinking" in prompt
    
    def test_generate_enhanced_branch_prompt_biomimicry(self, generator):
        """Test enhanced branch prompt with biomimicry."""
        thought = "Design efficient transportation"
        prompt = generator.generate_enhanced_branch_prompt(
            thought,
            technique=CreativityTechnique.BIOMIMICRY
        )
        
        assert isinstance(prompt, str)
        assert thought in prompt
        assert "biomimicry" in prompt
    
    def test_generate_enhanced_perspective_prompt_basic(self, generator):
        """Test enhanced perspective prompt generation."""
        thought = "Improve online education"
        perspective_type = "inanimate_object"
        prompt = generator.generate_enhanced_perspective_prompt(thought, perspective_type)
        
        assert isinstance(prompt, str)
        assert thought in prompt
        assert perspective_type in prompt
    
    def test_generate_enhanced_perspective_prompt_six_hats(self, generator):
        """Test enhanced perspective prompt with Six Thinking Hats."""
        thought = "Implement remote work policy"
        perspective_type = "abstract_concept"
        prompt = generator.generate_enhanced_perspective_prompt(
            thought, 
            perspective_type,
            use_six_hats=True
        )
        
        assert isinstance(prompt, str)
        assert thought in prompt
        assert "Six Thinking Hats" in prompt
        assert "White Hat" in prompt  # Should contain hat references
        assert perspective_type in prompt
    
    def test_generate_enhanced_constraint_prompt_basic(self, generator):
        """Test enhanced constraint prompt generation."""
        thought = "Create a mobile game"
        constraint = "must work offline"
        prompt = generator.generate_enhanced_constraint_prompt(thought, constraint)
        
        assert isinstance(prompt, str)
        assert thought in prompt
        assert constraint in prompt
    
    def test_generate_enhanced_constraint_prompt_relaxation(self, generator):
        """Test enhanced constraint prompt with relaxation technique."""
        thought = "Design a smart home system"
        constraint = "limited budget"
        prompt = generator.generate_enhanced_constraint_prompt(
            thought, 
            constraint,
            use_relaxation=True
        )
        
        assert isinstance(prompt, str)
        assert thought in prompt
        assert constraint in prompt
        assert "relaxing this constraint" in prompt
    
    def test_generate_enhanced_combination_prompt_basic(self, generator):
        """Test enhanced combination prompt generation."""
        thought1 = "Voice-controlled smart home"
        thought2 = "Sustainable energy system"
        prompt = generator.generate_enhanced_combination_prompt(thought1, thought2)
        
        assert isinstance(prompt, str)
        assert thought1 in prompt
        assert thought2 in prompt
    
    def test_generate_enhanced_combination_prompt_morphological(self, generator):
        """Test enhanced combination prompt with morphological analysis."""
        thought1 = "AI-powered chatbot"
        thought2 = "Educational game platform"
        prompt = generator.generate_enhanced_combination_prompt(
            thought1, 
            thought2,
            use_morphological=True
        )
        
        assert isinstance(prompt, str)
        assert thought1 in prompt
        assert thought2 in prompt
        assert "morphological analysis" in prompt
        assert "Core function/purpose" in prompt
    
    def test_generate_reverse_brainstorming_prompt(self, generator):
        """Test reverse brainstorming prompt generation."""
        thought = "Create a user-friendly mobile banking app"
        prompt = generator.generate_reverse_brainstorming_prompt(thought)
        
        assert isinstance(prompt, str)
        assert thought in prompt
        assert "Reverse brainstorming" in prompt
        assert "make this idea fail" in prompt
    
    def test_all_perspective_types(self, generator):
        """Test all perspective types work correctly."""
        thought = "Design a better keyboard"
        perspective_types = ["inanimate_object", "abstract_concept", "impossible_being"]
        
        for perspective_type in perspective_types:
            prompt = generator.generate_enhanced_perspective_prompt(thought, perspective_type)
            assert isinstance(prompt, str)
            assert thought in prompt
            assert len(prompt) > 50  # Should be substantial
    
    def test_prompt_quality_and_length(self, generator):
        """Test that generated prompts meet quality standards."""
        thought = "Develop a sustainable transportation solution"
        
        # Test different prompt types
        branch_prompt = generator.generate_enhanced_branch_prompt(thought)
        perspective_prompt = generator.generate_enhanced_perspective_prompt(thought, "inanimate_object")
        constraint_prompt = generator.generate_enhanced_constraint_prompt(thought, "must be invisible")
        combination_prompt = generator.generate_enhanced_combination_prompt(thought, "AI assistant")
        reverse_prompt = generator.generate_reverse_brainstorming_prompt(thought)
        
        prompts = [branch_prompt, perspective_prompt, constraint_prompt, combination_prompt, reverse_prompt]
        
        for prompt in prompts:
            assert isinstance(prompt, str)
            assert len(prompt) > 100  # Should be substantial
            assert thought in prompt
            assert prompt.strip()  # Should not be empty or just whitespace
    
    def test_template_fallback(self, generator):
        """Test that fallback templates work when specific perspective types aren't found."""
        thought = "Create an innovative solution"
        # Use a perspective type that might not have specific templates
        prompt = generator.generate_enhanced_perspective_prompt(thought, "unknown_perspective")
        
        assert isinstance(prompt, str)
        assert thought in prompt
        assert len(prompt) > 50


class TestPromptTemplateLoading:
    """Test suite for template loading functionality."""
    
    
    
    def test_perspective_templates_loaded(self):
        """Test that perspective templates are properly loaded."""
        generator = EnhancedPromptGenerator()
        
        assert hasattr(generator, 'perspective_templates')
        assert isinstance(generator.perspective_templates, dict)
        assert "inanimate_object" in generator.perspective_templates
        assert "abstract_concept" in generator.perspective_templates
        assert "impossible_being" in generator.perspective_templates
    
    def test_constraint_templates_loaded(self):
        """Test that constraint templates are properly loaded."""
        generator = EnhancedPromptGenerator()
        
        assert hasattr(generator, 'constraint_templates')
        assert isinstance(generator.constraint_templates, list)
        assert len(generator.constraint_templates) > 0
    
    def test_combination_templates_loaded(self):
        """Test that combination templates are properly loaded."""
        generator = EnhancedPromptGenerator()
        
        assert hasattr(generator, 'combination_templates')
        assert isinstance(generator.combination_templates, list)
        assert len(generator.combination_templates) > 0


class TestIntegration:
    """Integration tests for enhanced prompt generation."""

    @pytest.fixture
    def generator(self):
        """Create an EnhancedPromptGenerator instance for testing."""
        return EnhancedPromptGenerator()

    @pytest.fixture
    def sample_context(self):
        """Create a sample creativity context for testing."""
        return CreativityContext(
            domain="technology",
            constraints=["eco-friendly", "affordable"],
            target_audience="students"
        )

    def test_creativity_algorithms_integration(self):
        """Test that creativity algorithms are properly integrated."""
        generator = EnhancedPromptGenerator()

        assert hasattr(generator, 'creativity_algorithms')
        assert generator.creativity_algorithms is not None

    def test_end_to_end_workflow(self, generator, sample_context):
        """Test complete workflow from context to final prompt."""
        thought = "Create a revolutionary educational tool"
        
        # Test each major prompt type with context
        branch_prompt = generator.generate_enhanced_branch_prompt(
            thought, 
            context=sample_context,
            technique=CreativityTechnique.SCAMPER
        )
        
        perspective_prompt = generator.generate_enhanced_perspective_prompt(
            thought, 
            "abstract_concept",
            use_six_hats=True
        )
        
        constraint_prompt = generator.generate_enhanced_constraint_prompt(
            thought,
            "must be accessible to everyone",
            use_relaxation=True
        )
        
        # Verify all prompts are generated successfully
        prompts = [branch_prompt, perspective_prompt, constraint_prompt]
        for prompt in prompts:
            assert isinstance(prompt, str)
            assert len(prompt) > 200  # Should be comprehensive
            assert thought in prompt
