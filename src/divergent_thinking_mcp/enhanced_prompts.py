"""
Enhanced prompt templates for the Divergent Thinking MCP Server.

This module provides sophisticated prompt templates that incorporate
advanced creativity techniques and structured thinking approaches.
"""

import random
from typing import Dict, List, Any, Optional
from .creativity_algorithms import (
    CreativityAlgorithms,
    CreativityTechnique,
    CreativityContext,
)


class EnhancedPromptGenerator:
    """
    Advanced prompt generator with sophisticated creativity techniques.

    This class generates prompts that go beyond simple templates to incorporate
    proven creativity methodologies and structured thinking approaches.

    Uses class-level caching to optimize template loading performance.
    """

    # Class-level template cache to avoid reloading for each instance
    _template_cache: Dict[str, Any] = {}
    _cache_initialized: bool = False

    def __init__(self):
        self.creativity_algorithms = CreativityAlgorithms()

        # Initialize templates using class-level cache
        if not self._cache_initialized:
            self._initialize_template_cache()

        # Use cached templates
        self.perspective_templates = self._template_cache["perspective"]
        self.constraint_templates = self._template_cache["constraint"]
        self.combination_templates = self._template_cache["combination"]

    def _safe_random_sample(self, items: List[Any], size: int) -> List[Any]:
        """
        Safely sample items, handling cases where list is smaller than requested size.

        Args:
            items: List of items to sample from
            size: Desired sample size

        Returns:
            List[Any]: Sampled items (may be smaller than requested size if input is small)
        """
        if not items:
            return []
        actual_size = min(size, len(items))
        return random.sample(items, actual_size)

    @classmethod
    def _initialize_template_cache(cls) -> None:
        """Initialize the class-level template cache."""
        if not cls._cache_initialized:
            cls._template_cache.update(
                {
                    "perspective": cls._load_perspective_templates_static(),
                    "constraint": cls._load_constraint_templates_static(),
                    "combination": cls._load_combination_templates_static(),
                }
            )
            cls._cache_initialized = True

    def generate_enhanced_branch_prompt(
        self,
        thought: str,
        context: Optional[CreativityContext] = None,
        technique: Optional[CreativityTechnique] = None,
        seed: Optional[int] = None,
    ) -> str:
        """
        Generate an enhanced branch generation prompt using advanced techniques.

        Args:
            thought: The original thought to branch from
            context: Optional creativity context
            technique: Optional specific technique to use
            seed: Optional random seed for deterministic results

        Returns:
            str: Enhanced branch generation prompt
        """
        # Set random seed if provided for deterministic results
        if seed is not None:
            random.seed(seed)

        if technique is None:
            technique = random.choice(list(CreativityTechnique))

        base_prompt = f"Starting with the thought: '{thought}'\n\n"

        if technique == CreativityTechnique.SCAMPER:
            scamper_variations = self.creativity_algorithms.apply_scamper(
                thought, context
            )
            selected_variations = self._safe_random_sample(scamper_variations, 3)
            base_prompt += "Using SCAMPER technique, explore these directions:\n"
            for i, variation in enumerate(selected_variations, 1):
                base_prompt += f"{i}. {variation}\n"

        elif technique == CreativityTechnique.RANDOM_WORD:
            associations = self.creativity_algorithms.generate_random_word_associations(
                thought, 2
            )
            selected_associations = self._safe_random_sample(associations, 3)
            base_prompt += "Using random word association, explore:\n"
            for i, association in enumerate(selected_associations, 1):
                base_prompt += f"{i}. {association}\n"

        elif technique == CreativityTechnique.ANALOGICAL_THINKING:
            analogies = self.creativity_algorithms.apply_analogical_thinking(thought)
            selected_analogies = self._safe_random_sample(analogies, 3)
            base_prompt += "Using analogical thinking, consider:\n"
            for i, analogy in enumerate(selected_analogies, 1):
                base_prompt += f"{i}. {analogy}\n"

        elif technique == CreativityTechnique.BIOMIMICRY:
            biomimicry_prompts = self.creativity_algorithms.apply_biomimicry(thought)
            selected_prompts = self._safe_random_sample(biomimicry_prompts, 3)
            base_prompt += "Using biomimicry inspiration, explore:\n"
            for i, prompt in enumerate(selected_prompts, 1):
                base_prompt += f"{i}. {prompt}\n"

        else:
            # Fallback to traditional branching
            base_prompt += "Generate 3 distinct creative branches, each exploring a completely different direction:\n"
            base_prompt += "1. A practical/functional approach\n"
            base_prompt += "2. An artistic/aesthetic approach\n"
            base_prompt += "3. A radical/disruptive approach\n"

        base_prompt += "\nFor each direction, provide a detailed exploration that builds meaningfully on the original thought."
        return base_prompt

    def generate_enhanced_perspective_prompt(
        self,
        thought: str,
        perspective_type: str,
        use_six_hats: bool = False,
        seed: Optional[int] = None,
    ) -> str:
        """
        Generate an enhanced perspective shift prompt.

        Args:
            thought: The original thought
            perspective_type: Type of perspective to adopt
            use_six_hats: Whether to incorporate Six Thinking Hats
            seed: Optional random seed for deterministic results

        Returns:
            str: Enhanced perspective shift prompt
        """
        # Set random seed if provided for deterministic results
        if seed is not None:
            random.seed(seed)
        if use_six_hats:
            hats_analysis = self.creativity_algorithms.apply_six_thinking_hats(thought)
            base_prompt = f"Analyzing the thought: '{thought}'\n\n"
            base_prompt += "Using the Six Thinking Hats framework:\n\n"

            for hat_color, prompts in hats_analysis.items():
                base_prompt += f"**{hat_color}:**\n"
                for prompt in prompts:
                    base_prompt += f"- {prompt}\n"
                base_prompt += "\n"

            base_prompt += f"Now, synthesize insights from all perspectives while viewing through the lens of a {perspective_type}."
            return base_prompt

        else:
            perspective_templates = self.perspective_templates.get(perspective_type, [])
            if perspective_templates:
                template = random.choice(perspective_templates)
                return template.replace('{thought}', thought).replace('{perspective_type}', perspective_type)
            else:
                return f"View this thought from the perspective of a {perspective_type}: {thought}\nProvide a radically different interpretation that reveals hidden aspects or possibilities."

    def generate_enhanced_constraint_prompt(
        self,
        thought: str,
        constraint: str,
        use_relaxation: bool = False,
        seed: Optional[int] = None,
    ) -> str:
        """
        Generate an enhanced creative constraint prompt.

        Args:
            thought: The original thought
            constraint: The constraint to apply
            use_relaxation: Whether to use constraint relaxation technique
            seed: Optional random seed for deterministic results

        Returns:
            str: Enhanced constraint prompt
        """
        # Set random seed if provided for deterministic results
        if seed is not None:
            random.seed(seed)
        if use_relaxation:
            relaxation_prompts = self.creativity_algorithms.apply_constraint_relaxation(
                thought, [constraint]
            )
            base_prompt = f"Working with the thought: '{thought}'\n\n"
            base_prompt += f"First, apply the constraint: '{constraint}'\n"
            base_prompt += (
                "Then explore what becomes possible by relaxing this constraint:\n\n"
            )

            for i, prompt in enumerate(relaxation_prompts[:4], 1):
                base_prompt += f"{i}. {prompt}\n"

            base_prompt += "\nFinally, find creative ways to achieve the relaxed possibilities while still honoring the original constraint."
            return base_prompt

        else:
            constraint_templates = self.constraint_templates
            template = random.choice(constraint_templates)
            return template.replace('{thought}', thought).replace('{constraint}', constraint)

    def generate_enhanced_combination_prompt(
        self,
        thought1: str,
        thought2: str,
        use_morphological: bool = False,
        seed: Optional[int] = None,
    ) -> str:
        """
        Generate an enhanced thought combination prompt.

        Args:
            thought1: First thought to combine
            thought2: Second thought to combine
            use_morphological: Whether to use morphological analysis
            seed: Optional random seed for deterministic results

        Returns:
            str: Enhanced combination prompt
        """
        # Set random seed if provided for deterministic results
        if seed is not None:
            random.seed(seed)
        if use_morphological:
            base_prompt = f"Combining thoughts:\n1. '{thought1}'\n2. '{thought2}'\n\n"
            base_prompt += "Using morphological analysis, break down each thought into key dimensions:\n\n"
            base_prompt += "For Thought 1, identify:\n"
            base_prompt += "- Core function/purpose\n"
            base_prompt += "- Key components/elements\n"
            base_prompt += "- Operating principles\n"
            base_prompt += "- Target context/environment\n\n"
            base_prompt += "For Thought 2, identify:\n"
            base_prompt += "- Core function/purpose\n"
            base_prompt += "- Key components/elements\n"
            base_prompt += "- Operating principles\n"
            base_prompt += "- Target context/environment\n\n"
            base_prompt += "Now create novel combinations by mixing and matching dimensions across both thoughts. Generate at least 3 hybrid concepts that combine different dimensional aspects in unexpected ways."
            return base_prompt

        else:
            combination_templates = self.combination_templates
            template = random.choice(combination_templates)
            return template.replace('{thought1}', thought1).replace('{thought2}', thought2)

    def generate_reverse_brainstorming_prompt(
        self, thought: str, seed: Optional[int] = None
    ) -> str:
        """
        Generate a reverse brainstorming prompt.

        Args:
            thought: The original thought
            seed: Optional random seed for deterministic results

        Returns:
            str: Reverse brainstorming prompt
        """
        # Set random seed if provided for deterministic results
        if seed is not None:
            random.seed(seed)
        reverse_prompts = self.creativity_algorithms.apply_reverse_brainstorming(
            thought
        )

        base_prompt = f"Reverse brainstorming for: '{thought}'\n\n"
        base_prompt += "First, explore how to make this idea fail:\n\n"

        for i, prompt in enumerate(reverse_prompts[:-1], 1):
            base_prompt += f"{i}. {prompt}\n"

        base_prompt += f"\n{reverse_prompts[-1]}"
        return base_prompt

    @staticmethod
    def _load_perspective_templates_static() -> Dict[str, List[str]]:
        """Load perspective-specific templates (static version for caching)."""
        return {
            "inanimate_object": [
                "You are a {perspective_type} observing '{thought}'. What do you notice that humans miss? How would you interact with or modify this concept based on your unique properties?",
                "As a {perspective_type}, you have no emotions or preconceptions. Analyze '{thought}' purely from your material/functional perspective. What inefficiencies or opportunities do you detect?",
                "Imagine '{thought}' from the viewpoint of a {perspective_type} that has existed for centuries. What patterns and cycles do you observe that short-lived humans cannot see?",
            ],
            "abstract_concept": [
                "You are the embodiment of {perspective_type}. How does '{thought}' align with or challenge your fundamental nature? What would you change to make it more harmonious with your essence?",
                "As {perspective_type} personified, you see '{thought}' through the lens of your abstract principles. What deeper meanings and connections do you perceive?",
                "From your perspective as {perspective_type}, '{thought}' is just one manifestation of larger patterns. What other forms could it take while maintaining its essential relationship to you?",
            ],
            "impossible_being": [
                "You are a {perspective_type} with abilities that defy physical laws. How would you approach '{thought}' using your impossible capabilities? What solutions become available to you?",
                "As a {perspective_type}, you exist outside normal constraints of time, space, and logic. Reimagine '{thought}' from your transcendent perspective.",
                "You are a {perspective_type} who experiences reality in ways humans cannot comprehend. How would you transform '{thought}' based on your alien understanding?",
            ],
        }

    @staticmethod
    def _load_constraint_templates_static() -> List[str]:
        """Load constraint application templates (static version for caching)."""
        return [
            "Transform '{thought}' by applying the constraint: '{constraint}'. Don't just add the constraint—let it fundamentally reshape the concept's DNA.",
            "The constraint '{constraint}' isn't a limitation—it's a creative catalyst for '{thought}'. How does this constraint unlock new possibilities?",
            "Imagine '{thought}' was born in a world where '{constraint}' is the natural law. How would it evolve differently?",
            "Use '{constraint}' as a lens to reveal hidden aspects of '{thought}' that are normally invisible.",
            "The constraint '{constraint}' forces '{thought}' to find creative workarounds. What elegant solutions emerge?",
        ]

    @staticmethod
    def _load_combination_templates_static() -> List[str]:
        """Load thought combination templates (static version for caching)."""
        return [
            "'{thought1}' and '{thought2}' are two ingredients in a recipe for innovation. What unexpected dish do they create when combined with the right catalyst?",
            "Imagine '{thought1}' and '{thought2}' are two different species that must evolve together. What hybrid offspring would emerge from their symbiosis?",
            "'{thought1}' and '{thought2}' are two musical themes. Compose a symphony that weaves them together into something greater than the sum of their parts.",
            "If '{thought1}' and '{thought2}' were two puzzle pieces from different puzzles, what new picture would emerge when they're forced to fit together?",
            "'{thought1}' and '{thought2}' are two different languages. Create a new form of communication that incorporates the unique strengths of both.",
        ]
