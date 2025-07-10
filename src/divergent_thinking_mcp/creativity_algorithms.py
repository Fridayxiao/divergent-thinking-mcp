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
    
    def __init__(self):
        self.random_words = self._load_random_words()
        self.analogical_domains = self._load_analogical_domains()
        self.biomimicry_examples = self._load_biomimicry_examples()

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
    
    def apply_scamper(self, idea: str, context: Optional[CreativityContext] = None) -> List[str]:
        """
        Apply SCAMPER technique (Substitute, Combine, Adapt, Modify, Put to other uses, Eliminate, Reverse).
        
        Args:
            idea: The original idea to transform
            context: Optional context for more targeted suggestions
            
        Returns:
            List[str]: List of SCAMPER-generated variations
        """
        scamper_prompts = {
            "Substitute": [
                f"What if we substitute the main component of '{idea}' with something unexpected?",
                f"How could we replace the traditional materials in '{idea}' with sustainable alternatives?",
                f"What if we substitute the target user of '{idea}' with a completely different demographic?"
            ],
            "Combine": [
                f"How could we combine '{idea}' with a completely unrelated concept?",
                f"What if we merged '{idea}' with technology from a different industry?",
                f"How could '{idea}' be combined with a natural phenomenon?"
            ],
            "Adapt": [
                f"How could we adapt '{idea}' to work in a completely different environment?",
                f"What if we adapted '{idea}' to solve a problem in another field?",
                f"How could we adapt the principles of '{idea}' to work at a different scale?"
            ],
            "Modify": [
                f"What if we exaggerated one aspect of '{idea}' to an extreme?",
                f"How could we minimize the size/complexity of '{idea}' while maintaining its essence?",
                f"What if we changed the timing or sequence of how '{idea}' works?"
            ],
            "Put to other uses": [
                f"What are 5 completely different applications for '{idea}'?",
                f"How could '{idea}' be repurposed for emergency situations?",
                f"What if '{idea}' was used by children vs. elderly people?"
            ],
            "Eliminate": [
                f"What if we removed the most obvious feature of '{idea}'?",
                f"How would '{idea}' work if we eliminated the need for power/energy?",
                f"What if we eliminated all physical components of '{idea}'?"
            ],
            "Reverse": [
                f"What if '{idea}' worked in the opposite way?",
                f"How could we reverse the user experience of '{idea}'?",
                f"What if the problem '{idea}' solves was actually the solution to something else?"
            ]
        }
        
        results = []
        for category, prompts in scamper_prompts.items():
            selected_prompt = random.choice(prompts)
            results.append(f"[{category}] {selected_prompt}")
        
        return results
    
    def generate_random_word_associations(self, idea: str, num_words: int = 3) -> List[str]:
        """
        Generate ideas using random word association technique.
        
        Args:
            idea: The original idea
            num_words: Number of random words to use
            
        Returns:
            List[str]: List of random word association prompts
        """
        selected_words = self._safe_random_sample(self.random_words, num_words)
        
        prompts = []
        for word in selected_words:
            prompts.extend([
                f"How could '{idea}' incorporate the concept of '{word}'?",
                f"What if '{idea}' had the properties of '{word}'?",
                f"How would '{word}' approach the problem that '{idea}' is trying to solve?",
                f"What unexpected connection exists between '{idea}' and '{word}'?"
            ])
        
        return prompts
    
    def apply_analogical_thinking(self, idea: str, domain: Optional[str] = None) -> List[str]:
        """
        Apply analogical thinking by drawing parallels from other domains.
        
        Args:
            idea: The original idea
            domain: Optional specific domain to draw analogies from
            
        Returns:
            List[str]: List of analogical thinking prompts
        """
        if domain and domain in self.analogical_domains:
            source_domains = [domain]
        else:
            source_domains = self._safe_random_sample(list(self.analogical_domains.keys()), 3)
        
        prompts = []
        for domain_name in source_domains:
            domain_examples = self.analogical_domains[domain_name]
            example = random.choice(domain_examples)
            
            prompts.extend([
                f"How is '{idea}' similar to {example} in {domain_name}? What can we learn?",
                f"If '{idea}' worked like {example} in {domain_name}, what would change?",
                f"What principles from {example} in {domain_name} could improve '{idea}'?",
                f"How would someone from {domain_name} approach '{idea}' differently?"
            ])
        
        return prompts
    
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
    
    def apply_six_thinking_hats(self, idea: str) -> Dict[str, List[str]]:
        """
        Apply Edward de Bono's Six Thinking Hats technique.
        
        Args:
            idea: The original idea
            
        Returns:
            Dict[str, List[str]]: Prompts organized by thinking hat color
        """
        return {
            "White Hat (Facts)": [
                f"What factual information do we need about '{idea}'?",
                f"What data would prove or disprove the viability of '{idea}'?",
                f"What are the measurable aspects of '{idea}'?"
            ],
            "Red Hat (Emotions)": [
                f"What emotional response does '{idea}' evoke?",
                f"How would different people feel about '{idea}'?",
                f"What intuitive reactions arise from '{idea}'?"
            ],
            "Black Hat (Critical)": [
                f"What could go wrong with '{idea}'?",
                f"What are the risks and limitations of '{idea}'?",
                f"Why might '{idea}' not work in practice?"
            ],
            "Yellow Hat (Positive)": [
                f"What are the benefits and advantages of '{idea}'?",
                f"What opportunities does '{idea}' create?",
                f"What's the best-case scenario for '{idea}'?"
            ],
            "Green Hat (Creative)": [
                f"What creative alternatives exist to '{idea}'?",
                f"How could we make '{idea}' more innovative?",
                f"What wild possibilities does '{idea}' suggest?"
            ],
            "Blue Hat (Process)": [
                f"How should we approach developing '{idea}'?",
                f"What process would best evaluate '{idea}'?",
                f"How can we organize our thinking about '{idea}'?"
            ]
        }
    
    def apply_biomimicry(self, idea: str) -> List[str]:
        """
        Apply biomimicry by drawing inspiration from nature.
        
        Args:
            idea: The original idea
            
        Returns:
            List[str]: List of biomimicry-inspired prompts
        """
        selected_examples = self._safe_random_sample(self.biomimicry_examples, 4)
        
        prompts = []
        for example in selected_examples:
            prompts.extend([
                f"How could '{idea}' work like {example['organism']} which {example['mechanism']}?",
                f"What if '{idea}' adopted the {example['property']} of {example['organism']}?",
                f"How would {example['organism']} solve the problem that '{idea}' addresses?"
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
    
    def _load_random_words(self) -> List[str]:
        """Load a collection of random words for association."""
        return [
            "butterfly", "quantum", "mirror", "whisper", "gravity", "crystal", "shadow",
            "lightning", "ocean", "mountain", "forest", "desert", "volcano", "glacier",
            "spiral", "rhythm", "harmony", "chaos", "balance", "flow", "energy",
            "transformation", "evolution", "revolution", "innovation", "discovery",
            "mystery", "adventure", "journey", "destination", "path", "bridge",
            "door", "window", "key", "lock", "treasure", "map", "compass", "star",
            "moon", "sun", "earth", "fire", "water", "air", "metal", "wood",
            "silk", "velvet", "diamond", "pearl", "gold", "silver", "copper",
            "magnet", "prism", "lens", "telescope", "microscope", "kaleidoscope"
        ]
    
    def _load_analogical_domains(self) -> Dict[str, List[str]]:
        """Load analogical thinking domains and examples."""
        return {
            "nature": ["ant colonies", "bird flocks", "tree root systems", "coral reefs", "beehives"],
            "sports": ["team coordination", "strategic plays", "training regimens", "equipment design", "performance optimization"],
            "music": ["orchestral harmony", "improvisation", "rhythm patterns", "instrument design", "sound mixing"],
            "cooking": ["recipe development", "flavor combinations", "cooking techniques", "kitchen organization", "presentation"],
            "architecture": ["structural design", "space utilization", "material selection", "environmental integration", "aesthetic balance"],
            "transportation": ["traffic flow", "route optimization", "vehicle design", "logistics systems", "navigation methods"],
            "games": ["rule systems", "strategy development", "player interaction", "challenge progression", "reward mechanisms"]
        }
    
    def _load_biomimicry_examples(self) -> List[Dict[str, str]]:
        """Load biomimicry examples from nature."""
        return [
            {"organism": "gecko feet", "mechanism": "uses van der Waals forces for adhesion", "property": "reversible sticking ability"},
            {"organism": "shark skin", "mechanism": "reduces drag with dermal denticles", "property": "hydrodynamic efficiency"},
            {"organism": "lotus leaves", "mechanism": "self-clean with micro/nano structures", "property": "superhydrophobic surface"},
            {"organism": "spider silk", "mechanism": "combines strength and flexibility", "property": "optimal material properties"},
            {"organism": "bird wings", "mechanism": "generate lift through airfoil shape", "property": "efficient flight dynamics"},
            {"organism": "honeycomb", "mechanism": "maximizes storage with minimal material", "property": "structural efficiency"},
            {"organism": "cactus spines", "mechanism": "collect water from air", "property": "moisture harvesting"},
            {"organism": "butterfly wings", "mechanism": "create colors through interference", "property": "structural coloration"},
            {"organism": "echolocation", "mechanism": "uses sound waves for navigation", "property": "acoustic sensing"},
            {"organism": "photosynthesis", "mechanism": "converts light to chemical energy", "property": "energy transformation"}
        ]
