"""
Advanced creativity algorithms for the Divergent Thinking MCP Server.

This module implements sophisticated creativity techniques and algorithms
to enhance divergent thinking and idea generation capabilities.
"""

import random
import logging
from typing import List, Dict, Optional, Any
from enum import Enum
from dataclasses import dataclass

from .constants import (
    RANDOM_WORDS,
    ANALOGICAL_DOMAINS,
    BIOMIMICRY_EXAMPLES,
    DOMAIN_KEYWORDS,
    DOMAIN_CREATIVITY_WORDS,
)
from .domain_data_manager import domain_data_manager

logger = logging.getLogger(__name__)


class CreativityTechnique(Enum):
    """Enumeration of available creativity techniques."""
    SCAMPER = "scamper"
    RANDOM_WORD = "random_word"
    MORPHOLOGICAL_ANALYSIS = "morphological_analysis"
    ANALOGICAL_THINKING = "analogical_thinking"
    REVERSE_BRAINSTORMING = "reverse_brainstorming"
    SIX_THINKING_HATS = "six_thinking_hats"
    BIOMIMICRY = "biomimicry"
    CONSTRAINT_RELAXATION = "constraint_relaxation"


@dataclass
class CreativityContext:
    """Context information for creativity algorithms."""
    domain: str
    constraints: List[str]
    target_audience: Optional[str] = None
    time_period: Optional[str] = None
    resources: Optional[List[str]] = None
    goals: Optional[List[str]] = None


class CreativityAlgorithms:
    """
    Advanced creativity algorithms for divergent thinking.
    
    This class implements various creativity techniques and algorithms
    to generate innovative ideas and solutions.
    """
    
    def __init__(self) -> None:
        """Initialize the creativity algorithms with required data."""
        self.random_words = RANDOM_WORDS
        self.analogical_domains = ANALOGICAL_DOMAINS
        self.biomimicry_examples = BIOMIMICRY_EXAMPLES
        self.domain_keywords = DOMAIN_KEYWORDS
        self.domain_creativity_words = DOMAIN_CREATIVITY_WORDS

        # Cache for frequently accessed domain data to improve performance
        self._domain_cache = {}

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

    def _intelligent_word_selection(self, domain: str, context: Optional[CreativityContext] = None,
                                   category: str = "core_concepts", count: int = 3) -> List[str]:
        """
        Intelligently select words based on domain and context.

        This method replaces pure randomness with context-aware selection:
        1. Priority 1: Domain-specific words from requested category
        2. Priority 2: Context-aware selection from other categories
        3. Priority 3: Fallback to generic random words

        Args:
            domain: Target domain for creativity
            context: Full creativity context (optional)
            category: Word category to select from (core_concepts, techniques, metaphors, challenges, applications)
            count: Number of words to select

        Returns:
            List[str]: Contextually relevant words
        """
        selected_words = []

        # Priority 1: Domain-specific words from requested category using domain data manager
        available_words = domain_data_manager.get_creativity_words(domain, category)
        if available_words:
            selected_count = min(count, len(available_words))
            selected_words.extend(self._safe_random_sample(available_words, selected_count))

        # Priority 2: Context-aware selection from other categories
        remaining_count = count - len(selected_words)
        if remaining_count > 0 and context:
            # If goals specified, add technique-related words
            if context.goals and category != "techniques":
                technique_words = domain_data_manager.get_creativity_words(domain, "techniques")
                if technique_words:
                    technique_count = min(remaining_count // 2, len(technique_words))
                    if technique_count > 0:
                        selected_words.extend(self._safe_random_sample(technique_words, technique_count))

            # If constraints mentioned, add challenge-related words
            remaining_count = count - len(selected_words)
            if remaining_count > 0 and context.constraints and category != "challenges":
                challenge_words = domain_data_manager.get_creativity_words(domain, "challenges")
                if challenge_words:
                    challenge_count = min(remaining_count, len(challenge_words))
                    if challenge_count > 0:
                        selected_words.extend(self._safe_random_sample(challenge_words, challenge_count))

        # Priority 3: Fallback to generic words if still needed
        remaining_count = count - len(selected_words)
        if remaining_count > 0:
            # Try other categories from the same domain first
            all_domain_words = []
            for cat in ["core_concepts", "techniques", "metaphors", "challenges", "applications"]:
                if cat != category:  # Don't repeat the primary category
                    words = domain_data_manager.get_creativity_words(domain, cat)
                    all_domain_words.extend(words)

            if all_domain_words:
                fallback_count = min(remaining_count, len(all_domain_words))
                selected_words.extend(self._safe_random_sample(all_domain_words, fallback_count))

            # Final fallback to generic random words
            remaining_count = count - len(selected_words)
            if remaining_count > 0:
                selected_words.extend(self._safe_random_sample(self.random_words, remaining_count))

        return selected_words[:count]

    def _select_contextual_prompt(self, prompts: List[str], context: Optional[CreativityContext] = None) -> str:
        """
        Select the most contextually appropriate prompt from a list.

        Args:
            prompts: List of available prompts
            context: Creativity context for selection

        Returns:
            str: Selected prompt
        """
        if not prompts:
            return ""

        if not context:
            return random.choice(prompts)

        # Simple contextual selection - can be enhanced further
        # For now, just return a random choice, but this method provides
        # a hook for more sophisticated context-aware selection
        return random.choice(prompts)
    
    def apply_scamper(self, idea: str, context: Optional[CreativityContext] = None) -> List[str]:
        """
        Apply SCAMPER technique with domain-aware prompts.

        Args:
            idea: The original idea to transform
            context: Optional context for more targeted suggestions

        Returns:
            List[str]: List of SCAMPER-generated variations
        """
        domain = context.domain if context else "general innovation"

        # Get domain-relevant words for contextual prompts
        domain_words = self._intelligent_word_selection(domain, context, "core_concepts", 5)
        technique_words = self._intelligent_word_selection(domain, context, "techniques", 3)
        application_words = self._intelligent_word_selection(domain, context, "applications", 3)

        scamper_prompts = {
            "Substitute": [
                f"What if you replaced key components of '{idea}' with {domain_words[0] if domain_words else 'innovative elements'}?",
                f"How could {technique_words[0] if technique_words else 'new approaches'} substitute current methods in '{idea}'?",
                f"What {domain}-specific alternatives exist for the core elements of '{idea}'?",
                f"How could '{idea}' substitute traditional solutions in {domain}?"
            ],
            "Combine": [
                f"How could '{idea}' merge with {domain_words[1] if len(domain_words) > 1 else 'complementary concepts'} to create something new in {domain}?",
                f"What happens when you combine '{idea}' with {technique_words[1] if len(technique_words) > 1 else 'proven techniques'} from {domain}?",
                f"How could '{idea}' integrate multiple {domain} approaches simultaneously?",
                f"What if '{idea}' combined with {application_words[0] if application_words else 'existing applications'} in {domain}?"
            ],
            "Adapt": [
                f"How could '{idea}' adapt {domain_words[2] if len(domain_words) > 2 else 'best practices'} principles for better results in {domain}?",
                f"What {domain} best practices could '{idea}' adopt and customize?",
                f"How could '{idea}' evolve to better serve {domain} needs and requirements?",
                f"What successful {domain} solutions could inspire adaptations to '{idea}'?"
            ],
            "Modify": [
                f"What if '{idea}' emphasized {domain_words[3] if len(domain_words) > 3 else 'key aspects'} more strongly for {domain} applications?",
                f"How could '{idea}' be modified using {technique_words[2] if len(technique_words) > 2 else 'specialized approaches'} from {domain}?",
                f"What {domain}-specific modifications would enhance '{idea}' effectiveness?",
                f"How could '{idea}' be scaled or optimized for {domain} requirements?"
            ],
            "Put to other uses": [
                f"How could '{idea}' solve other {domain} challenges beyond its original purpose?",
                f"What unexpected {domain} applications could '{idea}' enable or support?",
                f"How could '{idea}' transform other areas within {domain} or related fields?",
                f"What if '{idea}' was applied to {application_words[1] if len(application_words) > 1 else 'different use cases'} in {domain}?"
            ],
            "Eliminate": [
                f"What {domain} constraints or limitations could '{idea}' remove or simplify?",
                f"How could '{idea}' eliminate common {domain} pain points or inefficiencies?",
                f"What unnecessary {domain} complexities could '{idea}' strip away?",
                f"How could '{idea}' reduce barriers in {domain} processes or workflows?"
            ],
            "Reverse": [
                f"What if '{idea}' approached {domain} problems from the opposite direction or perspective?",
                f"How could '{idea}' invert typical {domain} assumptions or conventions?",
                f"What would '{idea}' look like if it challenged established {domain} practices?",
                f"How could '{idea}' reverse traditional {domain} workflows or processes?"
            ]
        }

        # Select most relevant prompts based on context
        results = []
        for category, prompts in scamper_prompts.items():
            selected_prompt = self._select_contextual_prompt(prompts, context)
            results.append(f"[{category}] {selected_prompt}")

        return results
    
    def generate_random_word_associations(self, idea: str, num_words: int = 3,
                                         context: Optional[CreativityContext] = None) -> List[str]:
        """
        Generate ideas using domain-aware word association technique.

        Args:
            idea: The original idea
            num_words: Number of words to use for associations
            context: Optional context for domain-aware word selection

        Returns:
            List[str]: List of domain-aware word association prompts
        """
        domain = context.domain if context else "general innovation"

        # Get domain-relevant words instead of purely random
        domain_words = self._intelligent_word_selection(domain, context, "core_concepts", num_words // 2)
        metaphor_words = self._intelligent_word_selection(domain, context, "metaphors", num_words // 2)

        # Combine domain-specific and metaphorical words
        selected_words = domain_words + metaphor_words

        # Ensure we have enough words
        if len(selected_words) < num_words:
            remaining = num_words - len(selected_words)
            # Try to get more from other categories
            technique_words = self._intelligent_word_selection(domain, context, "techniques", remaining)
            selected_words.extend(technique_words)

        # Final fallback to generic words if still needed
        if len(selected_words) < num_words:
            remaining = num_words - len(selected_words)
            fallback_words = self._safe_random_sample(self.random_words, remaining)
            selected_words.extend(fallback_words)

        prompts = []
        for word in selected_words[:num_words]:
            prompts.extend([
                f"How does '{word}' relate to '{idea}' in the context of {domain}?",
                f"What if '{idea}' embodied the essence of '{word}' in {domain} applications?",
                f"How could '{word}' inspire a new approach to '{idea}' within {domain}?",
                f"What {domain}-specific insights emerge when connecting '{idea}' with '{word}'?"
            ])

        return prompts

    def _get_domain_analogies(self, domain: str) -> Dict[str, List[str]]:
        """
        Get relevant analogy domains for the target domain.

        Args:
            domain: Target domain for creativity

        Returns:
            Dict[str, List[str]]: Mapping of analogy categories to examples
        """
        # Use domain data manager for consolidated access
        return domain_data_manager.get_domain_analogies(domain)


    def apply_analogical_thinking(self, idea: str, domain: Optional[str] = None,
                                 context: Optional[CreativityContext] = None) -> List[str]:
        """
        Apply analogical thinking with domain-relevant analogies.

        Args:
            idea: The original idea
            domain: Target domain for the idea (uses context.domain if not provided)
            context: Optional creativity context

        Returns:
            List[str]: List of domain-aware analogical thinking prompts
        """
        # Use context domain if available, otherwise use provided domain or default
        target_domain = domain or (context.domain if context else "general innovation")

        # Get domain-specific analogy sources
        domain_analogies = self._get_domain_analogies(target_domain)

        prompts = []
        for analogy_category, examples in domain_analogies.items():
            selected_examples = self._safe_random_sample(examples, 2)
            for example in selected_examples:
                prompts.extend([
                    f"How is '{idea}' like {example} in {analogy_category}? What insights does this reveal for {target_domain}?",
                    f"If '{idea}' operated like {example} from {analogy_category}, how would it transform {target_domain} practices?",
                    f"What principles from {example} in {analogy_category} could enhance '{idea}' for {target_domain} applications?"
                ])

        # Limit to top 6 most relevant analogies to avoid overwhelming output
        return prompts[:6]

    def _get_domain_biomimicry(self, domain: str) -> List[Dict[str, str]]:
        """
        Get domain-relevant biomimicry examples.

        Args:
            domain: Target domain for creativity

        Returns:
            List[Dict[str, str]]: List of biomimicry examples with organism, mechanism, and property
        """
        # Use domain data manager for consolidated access
        return domain_data_manager.get_domain_biomimicry(domain)


    def apply_reverse_brainstorming(self, idea: str) -> List[str]:
        """
        Apply reverse brainstorming by focusing on how to make the idea fail.
        
        Args:
            idea: The original idea
            
        Returns:
            List[str]: List of reverse brainstorming prompts
        """
        return [
            f"How could we make '{idea}' completely unusable?",
            f"What would guarantee that '{idea}' fails spectacularly?",
            f"How could we make '{idea}' as inconvenient as possible?",
            f"What would make people actively avoid '{idea}'?",
            f"How could we make '{idea}' solve the wrong problem entirely?",
            f"What would make '{idea}' work only in impossible conditions?",
            "Now, how can we reverse each of these failure modes into innovative features?"
        ]

    def _get_domain_perspectives(self, domain: str) -> Dict[str, List[str]]:
        """
        Get domain-specific perspectives for Six Thinking Hats.

        Args:
            domain: Target domain for creativity

        Returns:
            Dict[str, List[str]]: Domain-specific prompts for each thinking hat
        """
        # Use domain data manager for consolidated access
        return domain_data_manager.get_domain_perspectives(domain)


    def apply_six_thinking_hats(self, idea: str, context: Optional[CreativityContext] = None) -> Dict[str, List[str]]:
        """
        Apply Edward de Bono's Six Thinking Hats technique with domain-specific perspectives.

        Args:
            idea: The original idea
            context: Optional creativity context for domain-aware perspectives

        Returns:
            Dict[str, List[str]]: Domain-aware prompts organized by thinking hat color
        """
        domain = context.domain if context else "general innovation"
        domain_perspectives = self._get_domain_perspectives(domain)

        # Create domain-aware prompts, falling back to generic ones if domain not found
        return {
            "White Hat (Facts)": domain_perspectives.get("factual", [
                f"What {domain}-specific data validates '{idea}'?",
                f"What metrics matter most in {domain} for '{idea}'?",
                f"What evidence exists in {domain} for similar approaches?",
                f"What measurable outcomes define success for '{idea}' in {domain}?"
            ]),
            "Red Hat (Emotions)": domain_perspectives.get("emotional", [
                f"How do {domain} stakeholders feel about '{idea}'?",
                f"What emotional barriers exist in {domain} for '{idea}'?",
                f"What emotional benefits does '{idea}' provide in {domain}?",
                f"What intuitive reactions arise from {domain} professionals about '{idea}'?"
            ]),
            "Black Hat (Critical)": domain_perspectives.get("critical", [
                f"What {domain}-specific risks does '{idea}' present?",
                f"How could '{idea}' fail in {domain} contexts?",
                f"What {domain} constraints limit '{idea}'?",
                f"What unintended consequences could '{idea}' have in {domain}?"
            ]),
            "Yellow Hat (Positive)": domain_perspectives.get("positive", [
                f"What {domain} benefits does '{idea}' offer?",
                f"How could '{idea}' transform {domain} practices?",
                f"What opportunities does '{idea}' create in {domain}?",
                f"What's the best-case scenario for '{idea}' in {domain}?"
            ]),
            "Green Hat (Creative)": [
                f"What {domain}-specific innovations could '{idea}' inspire?",
                f"How could '{idea}' be creatively adapted for {domain}?",
                f"What wild {domain} possibilities does '{idea}' suggest?",
                f"What creative combinations exist between '{idea}' and {domain} practices?"
            ],
            "Blue Hat (Process)": [
                f"How should we approach implementing '{idea}' in {domain}?",
                f"What {domain} processes would best evaluate '{idea}'?",
                f"How can we organize {domain} thinking about '{idea}'?",
                f"What {domain} methodology should guide '{idea}' development?"
            ]
        }
    
    def apply_biomimicry(self, idea: str, context: Optional[CreativityContext] = None) -> List[str]:
        """
        Apply biomimicry with domain-relevant natural examples.

        Args:
            idea: The original idea
            context: Optional creativity context for domain-aware selection

        Returns:
            List[str]: List of domain-aware biomimicry-inspired prompts
        """
        domain = context.domain if context else "general innovation"
        domain_biomimicry = self._get_domain_biomimicry(domain)

        selected_examples = self._safe_random_sample(domain_biomimicry, 3)

        prompts = []
        for example in selected_examples:
            organism = example["organism"]
            mechanism = example["mechanism"]
            property_desc = example["property"]

            prompts.extend([
                f"How could '{idea}' mimic {organism}'s {mechanism} to achieve {property_desc} in {domain}?",
                f"What if '{idea}' adopted the {property_desc} strategy from {organism} for {domain} applications?",
                f"How would {organism}'s approach to {mechanism} inspire new solutions for '{idea}' in {domain}?",
                f"What {domain}-specific innovations could emerge by applying {organism}'s {property_desc} to '{idea}'?"
            ])

        return prompts
    
    def apply_constraint_relaxation(self, idea: str, constraints: List[str]) -> List[str]:
        """
        Apply constraint relaxation technique.
        
        Args:
            idea: The original idea
            constraints: List of current constraints
            
        Returns:
            List[str]: List of constraint relaxation prompts
        """
        if not constraints:
            constraints = [
                "budget limitations",
                "current technology",
                "physical laws",
                "social conventions",
                "time constraints"
            ]
        
        prompts = []
        for constraint in constraints:
            prompts.extend([
                f"What if '{idea}' had unlimited {constraint}?",
                f"How would '{idea}' change if {constraint} didn't exist?",
                f"What becomes possible with '{idea}' if we ignore {constraint}?",
                f"How could we work around the {constraint} limitation for '{idea}'?"
            ])
        
        return prompts
    
    
