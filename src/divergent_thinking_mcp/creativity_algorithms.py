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
        self.domain_keywords = self._load_domain_keywords()
        self.domain_creativity_words = self._load_domain_creativity_words()

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
        domain_words = self.domain_creativity_words.get(domain, {})
        selected_words = []

        # Priority 1: Domain-specific words from requested category
        if category in domain_words:
            available_words = domain_words[category]
            selected_count = min(count, len(available_words))
            selected_words.extend(self._safe_random_sample(available_words, selected_count))

        # Priority 2: Context-aware selection from other categories
        remaining_count = count - len(selected_words)
        if remaining_count > 0 and context and domain_words:
            # If goals specified, add technique-related words
            if context.goals and "techniques" in domain_words and category != "techniques":
                technique_words = domain_words["techniques"]
                technique_count = min(remaining_count // 2, len(technique_words))
                if technique_count > 0:
                    selected_words.extend(self._safe_random_sample(technique_words, technique_count))

            # If constraints mentioned, add challenge-related words
            remaining_count = count - len(selected_words)
            if remaining_count > 0 and context.constraints and "challenges" in domain_words and category != "challenges":
                challenge_words = domain_words["challenges"]
                challenge_count = min(remaining_count, len(challenge_words))
                if challenge_count > 0:
                    selected_words.extend(self._safe_random_sample(challenge_words, challenge_count))

        # Priority 3: Fallback to generic words if still needed
        remaining_count = count - len(selected_words)
        if remaining_count > 0:
            # Try other categories from the same domain first
            if domain_words:
                all_domain_words = []
                for cat, words in domain_words.items():
                    if cat != category:  # Don't repeat the primary category
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
        domain_analogy_map = {
            "artificial intelligence": {
                "biological_systems": ["neural networks", "immune systems", "evolutionary processes", "swarm behavior", "brain plasticity"],
                "cognitive_processes": ["learning patterns", "memory formation", "pattern recognition", "decision making", "problem solving"],
                "mathematical_concepts": ["optimization algorithms", "statistical inference", "graph theory", "probability models", "linear algebra"]
            },
            "healthcare technology": {
                "biological_systems": ["immune response", "healing processes", "diagnostic mechanisms", "homeostasis", "cellular repair"],
                "engineering_systems": ["monitoring systems", "feedback loops", "quality control", "system integration", "fault detection"],
                "communication_systems": ["information networks", "signal processing", "data transmission", "protocol standards", "error correction"]
            },
            "sustainable agriculture": {
                "natural_ecosystems": ["nutrient cycling", "biodiversity", "symbiotic relationships", "succession patterns", "resource efficiency"],
                "engineering_systems": ["closed-loop systems", "resource optimization", "automation", "sensor networks", "precision control"],
                "economic_systems": ["supply chains", "market dynamics", "resource allocation", "risk management", "value creation"]
            },
            "cybersecurity": {
                "military_defense": ["perimeter defense", "intelligence gathering", "threat assessment", "strategic planning", "rapid response"],
                "biological_immunity": ["pathogen detection", "immune response", "memory cells", "adaptive immunity", "barrier protection"],
                "physical_security": ["access control", "surveillance systems", "alarm systems", "security protocols", "incident response"]
            },
            "product design": {
                "natural_forms": ["biomimetic structures", "efficient shapes", "adaptive mechanisms", "material properties", "functional aesthetics"],
                "architectural_principles": ["form follows function", "structural integrity", "space utilization", "user flow", "environmental integration"],
                "artistic_composition": ["visual balance", "proportion", "harmony", "contrast", "focal points"]
            },
            "business strategy": {
                "military_strategy": ["competitive intelligence", "strategic positioning", "resource allocation", "tactical execution", "alliance building"],
                "game_theory": ["strategic moves", "competitive dynamics", "win-win scenarios", "risk assessment", "decision trees"],
                "ecosystem_dynamics": ["competitive advantage", "niche specialization", "resource competition", "adaptation", "survival strategies"]
            },
            "renewable energy": {
                "natural_processes": ["photosynthesis", "wind patterns", "water cycles", "geothermal processes", "tidal forces"],
                "energy_conversion": ["mechanical systems", "electrical generation", "energy storage", "power distribution", "efficiency optimization"],
                "economic_models": ["resource economics", "investment strategies", "market dynamics", "cost optimization", "value creation"]
            },
            "educational technology": {
                "cognitive_science": ["learning theories", "memory formation", "attention mechanisms", "motivation psychology", "skill acquisition"],
                "communication_systems": ["information delivery", "feedback loops", "interactive dialogue", "content adaptation", "user engagement"],
                "game_design": ["progression systems", "reward mechanisms", "challenge scaling", "user engagement", "achievement systems"]
            }
        }

        # Return domain-specific analogies or fall back to generic ones
        return domain_analogy_map.get(domain, self.analogical_domains)

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
        domain_biomimicry_map = {
            "artificial intelligence": [
                {"organism": "neural networks", "mechanism": "parallel information processing like brain neurons", "property": "distributed intelligence"},
                {"organism": "ant colonies", "mechanism": "swarm optimization for collective problem solving", "property": "emergent intelligence"},
                {"organism": "immune system", "mechanism": "pattern recognition and adaptive memory", "property": "learning from experience"},
                {"organism": "octopus camouflage", "mechanism": "real-time pattern adaptation", "property": "dynamic response systems"},
                {"organism": "bird flocking", "mechanism": "simple rules creating complex behavior", "property": "emergent coordination"}
            ],
            "renewable energy": [
                {"organism": "photosynthesis", "mechanism": "converts sunlight to chemical energy efficiently", "property": "solar energy conversion"},
                {"organism": "wind dispersal seeds", "mechanism": "captures air currents for movement", "property": "wind energy harvesting"},
                {"organism": "thermoregulation", "mechanism": "maintains optimal temperature with minimal energy", "property": "energy conservation"},
                {"organism": "bioluminescence", "mechanism": "produces light through chemical reactions", "property": "efficient light generation"},
                {"organism": "leaf structure", "mechanism": "maximizes surface area for energy capture", "property": "energy collection optimization"}
            ],
            "healthcare technology": [
                {"organism": "immune system", "mechanism": "detects and responds to threats automatically", "property": "automated health monitoring"},
                {"organism": "blood clotting", "mechanism": "self-healing response to injury", "property": "rapid repair mechanisms"},
                {"organism": "echolocation", "mechanism": "uses sound waves for internal imaging", "property": "non-invasive diagnostics"},
                {"organism": "spider silk", "mechanism": "combines strength and flexibility", "property": "biocompatible materials"},
                {"organism": "cellular repair", "mechanism": "targeted healing at microscopic level", "property": "precision medicine"}
            ],
            "cybersecurity": [
                {"organism": "immune system", "mechanism": "distinguishes self from non-self", "property": "threat identification"},
                {"organism": "herd immunity", "mechanism": "collective protection through individual immunity", "property": "network security"},
                {"organism": "camouflage", "mechanism": "blends with environment to avoid detection", "property": "stealth protection"},
                {"organism": "warning signals", "mechanism": "alerts others to danger", "property": "threat communication"},
                {"organism": "territorial behavior", "mechanism": "defends boundaries from intruders", "property": "perimeter defense"}
            ],
            "product design": [
                {"organism": "honeycomb structure", "mechanism": "maximizes storage with minimal material", "property": "structural efficiency"},
                {"organism": "gecko feet", "mechanism": "reversible adhesion without chemicals", "property": "smart attachment"},
                {"organism": "bird wing design", "mechanism": "optimized shape for efficient movement", "property": "aerodynamic efficiency"},
                {"organism": "cactus spines", "mechanism": "collects water from air", "property": "resource harvesting"},
                {"organism": "butterfly wings", "mechanism": "creates colors through structure not pigment", "property": "sustainable aesthetics"}
            ],
            "sustainable agriculture": [
                {"organism": "mycorrhizal networks", "mechanism": "fungi connect plant roots for nutrient sharing", "property": "resource distribution"},
                {"organism": "nitrogen fixation", "mechanism": "bacteria convert atmospheric nitrogen to plant nutrients", "property": "natural fertilization"},
                {"organism": "companion planting", "mechanism": "different plants support each other's growth", "property": "symbiotic relationships"},
                {"organism": "forest succession", "mechanism": "gradual ecosystem development over time", "property": "sustainable regeneration"},
                {"organism": "pollinator networks", "mechanism": "insects facilitate plant reproduction", "property": "ecosystem services"}
            ],
            "urban transportation": [
                {"organism": "ant trails", "mechanism": "optimizes paths through pheromone feedback", "property": "traffic flow optimization"},
                {"organism": "bird migration", "mechanism": "efficient long-distance travel in groups", "property": "coordinated movement"},
                {"organism": "slime mold networks", "mechanism": "finds shortest paths between resources", "property": "route optimization"},
                {"organism": "schooling fish", "mechanism": "reduces energy through coordinated swimming", "property": "collective efficiency"},
                {"organism": "honeybee waggle dance", "mechanism": "communicates location information", "property": "navigation systems"}
            ],
            "business strategy": [
                {"organism": "ecosystem dynamics", "mechanism": "species adapt to fill available niches", "property": "market positioning"},
                {"organism": "predator-prey cycles", "mechanism": "populations balance through feedback loops", "property": "competitive dynamics"},
                {"organism": "symbiotic relationships", "mechanism": "mutual benefit through cooperation", "property": "strategic partnerships"},
                {"organism": "territorial behavior", "mechanism": "defends resources from competitors", "property": "market protection"},
                {"organism": "migration patterns", "mechanism": "moves to exploit seasonal opportunities", "property": "market timing"}
            ]
        }

        # Return domain-specific biomimicry examples or fall back to generic ones
        return domain_biomimicry_map.get(domain, self.biomimicry_examples)

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
        domain_perspectives = {
            "artificial intelligence": {
                "factual": [
                    f"What AI performance metrics validate this approach?",
                    f"What training data requirements exist?",
                    f"What computational resources are needed?",
                    f"What accuracy benchmarks apply?"
                ],
                "emotional": [
                    f"How do users feel about AI making this decision?",
                    f"What trust concerns arise with this AI system?",
                    f"How does this impact human-AI interaction?",
                    f"What ethical concerns do stakeholders have?"
                ],
                "critical": [
                    f"What bias risks exist in this AI system?",
                    f"How could this AI system fail or be misused?",
                    f"What privacy concerns arise?",
                    f"What happens when the AI encounters edge cases?"
                ],
                "positive": [
                    f"How could this AI system improve decision-making?",
                    f"What efficiency gains are possible?",
                    f"How could this democratize AI capabilities?",
                    f"What new possibilities does this AI enable?"
                ]
            },
            "healthcare technology": {
                "factual": [
                    f"What clinical evidence supports this approach?",
                    f"What regulatory approvals are required?",
                    f"What patient safety data exists?",
                    f"What cost-effectiveness studies apply?"
                ],
                "emotional": [
                    f"How do patients feel about this technology?",
                    f"What concerns do healthcare providers have?",
                    f"How does this impact patient-provider relationships?",
                    f"What anxiety or comfort does this create?"
                ],
                "critical": [
                    f"What patient safety risks exist?",
                    f"How could this technology fail in critical situations?",
                    f"What privacy concerns arise with health data?",
                    f"What happens if the technology malfunctions?"
                ],
                "positive": [
                    f"How could this improve patient outcomes?",
                    f"What healthcare access benefits are possible?",
                    f"How could this reduce healthcare costs?",
                    f"What quality of life improvements result?"
                ]
            },
            "cybersecurity": {
                "factual": [
                    f"What threat vectors does this address?",
                    f"What security standards does this meet?",
                    f"What attack success rates exist?",
                    f"What compliance requirements apply?"
                ],
                "emotional": [
                    f"How do users feel about security vs. convenience?",
                    f"What privacy concerns do stakeholders have?",
                    f"How does this impact user trust?",
                    f"What fear or confidence does this create?"
                ],
                "critical": [
                    f"What new attack vectors could this create?",
                    f"How could this security measure be bypassed?",
                    f"What happens if this security system fails?",
                    f"What false positive/negative risks exist?"
                ],
                "positive": [
                    f"How could this improve overall security posture?",
                    f"What threat prevention benefits are possible?",
                    f"How could this reduce security incidents?",
                    f"What peace of mind does this provide?"
                ]
            },
            "sustainable agriculture": {
                "factual": [
                    f"What yield data supports this approach?",
                    f"What environmental impact measurements exist?",
                    f"What cost-benefit analysis applies?",
                    f"What soil health indicators are relevant?"
                ],
                "emotional": [
                    f"How do farmers feel about adopting this practice?",
                    f"What concerns do consumers have?",
                    f"How does this impact farming communities?",
                    f"What pride or worry does this create?"
                ],
                "critical": [
                    f"What environmental risks could arise?",
                    f"How could this approach fail in different climates?",
                    f"What economic risks do farmers face?",
                    f"What unintended consequences are possible?"
                ],
                "positive": [
                    f"How could this improve soil health?",
                    f"What biodiversity benefits are possible?",
                    f"How could this reduce environmental impact?",
                    f"What long-term sustainability gains result?"
                ]
            }
        }

        return domain_perspectives.get(domain, {})

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

    def _load_domain_keywords(self) -> Dict[str, List[str]]:
        """
        Load domain keywords for potential use in creativity algorithms.

        These keywords can be used for domain-specific creativity techniques,
        analogical thinking, or context-aware prompt generation.

        Returns:
            Dict[str, List[str]]: Mapping of domains to their associated keywords
        """
        return {
            # Design & User Experience
            "product design": ["product design", "product development", "industrial design", "design thinking"],
            "user interface design": ["ui design", "interface design", "user interface", "frontend design"],
            "user experience design": ["ux design", "user experience", "usability", "user research", "user journey"],
            "graphic design": ["graphic design", "visual design", "branding", "logo design", "typography"],

            # Technology & Software
            "software development": ["software", "programming", "coding", "development", "application"],
            "mobile app development": ["mobile app", "ios app", "android app", "smartphone", "mobile development"],
            "web development": ["website", "web app", "web development", "frontend", "backend"],
            "artificial intelligence": ["artificial intelligence", "neural network", "deep learning", "ai model", "ai system"],
            "data science": ["data analysis", "data science", "analytics", "big data", "data mining", "machine learning"],
            "cybersecurity": ["security", "cybersecurity", "encryption", "privacy", "data protection"],
            "cloud computing": ["cloud computing", "cloud services", "cloud infrastructure", "cloud platform"],
            "blockchain technology": ["blockchain", "crypto", "cryptocurrency", "cryptography", "crypto token"],

            # Business & Strategy
            "business strategy": ["business strategy", "strategic planning", "market analysis", "competitive advantage"],
            "digital marketing": ["marketing", "digital marketing", "social media marketing", "advertising", "promotion"],
            "e-commerce": ["e-commerce", "online store", "retail", "shopping", "marketplace"],
            "startup ventures": ["startup", "entrepreneurship", "venture", "innovation", "business model"],

            # Healthcare & Medicine
            "medical devices": ["medical device", "healthcare equipment", "diagnostic tool", "medical technology"],
            "healthcare technology": ["health tech", "digital health", "medical software", "health app"],
            "telemedicine": ["telemedicine", "remote healthcare", "virtual consultation", "telehealth"],
            "patient care": ["patient care", "healthcare service", "medical treatment", "clinical care"],

            # Education & Learning
            "educational technology": ["edtech", "educational technology", "learning platform", "online education"],
            "online learning": ["online learning", "e-learning", "distance learning", "virtual classroom"],
            "student engagement": ["student engagement", "learning experience", "educational game", "interactive learning"],

            # Environment & Sustainability
            "renewable energy": ["renewable energy", "solar power", "wind energy", "clean energy", "green energy"],
            "sustainable agriculture": ["sustainable farming", "organic agriculture", "eco-friendly farming", "farming solutions", "agricultural"],
            "environmental conservation": ["conservation", "environmental protection", "sustainability", "eco-friendly"],
            "green technology": ["green tech", "clean technology", "environmental technology"],

            # Transportation & Mobility
            "urban transportation": ["public transport", "city transport", "urban mobility", "transit system"],
            "electric vehicles": ["electric car", "ev", "electric vehicle", "battery vehicle"],
            "autonomous vehicles": ["self-driving", "autonomous car", "driverless vehicle", "automated driving"],
            "smart cities": ["smart city", "urban planning", "city infrastructure", "urban development"],
        }

    def _load_domain_creativity_words(self) -> Dict[str, Dict[str, List[str]]]:
        """
        Load comprehensive domain-specific creativity word banks.

        This method provides structured word banks for each domain with categories:
        - core_concepts: Fundamental concepts and terminology
        - techniques: Methods, processes, and approaches
        - metaphors: Analogical and metaphorical terms
        - challenges: Common problems and obstacles
        - applications: Use cases and implementations

        Returns:
            Dict[str, Dict[str, List[str]]]: Nested mapping of domains to categorized word banks
        """
        return {
            # Design & User Experience
            "product design": {
                "core_concepts": ["user needs", "functionality", "aesthetics", "usability", "innovation", "ergonomics", "form factor"],
                "techniques": ["prototyping", "user testing", "iterative design", "design thinking", "sketching", "modeling", "validation"],
                "metaphors": ["craftsmanship", "artistry", "problem solving", "creation", "refinement", "evolution", "harmony"],
                "challenges": ["user adoption", "manufacturing constraints", "cost optimization", "sustainability", "market fit", "scalability"],
                "applications": ["consumer products", "industrial design", "user interfaces", "packaging", "furniture", "tools", "devices"]
            },
            "user interface design": {
                "core_concepts": ["user experience", "interaction design", "visual hierarchy", "accessibility", "responsiveness", "navigation"],
                "techniques": ["wireframing", "prototyping", "user research", "usability testing", "design systems", "component design"],
                "metaphors": ["conversation", "journey", "flow", "dialogue", "bridge", "gateway", "canvas"],
                "challenges": ["cross-platform compatibility", "accessibility compliance", "performance optimization", "user diversity"],
                "applications": ["web interfaces", "mobile apps", "desktop software", "kiosks", "dashboards", "control panels"]
            },
            "user experience design": {
                "core_concepts": ["user journey", "personas", "information architecture", "interaction patterns", "emotional design"],
                "techniques": ["user research", "journey mapping", "persona development", "usability testing", "service design"],
                "metaphors": ["storytelling", "orchestration", "choreography", "empathy", "connection", "understanding"],
                "challenges": ["user diversity", "context switching", "accessibility", "cross-cultural design", "behavior change"],
                "applications": ["digital products", "service design", "customer experience", "brand interaction", "touchpoint design"]
            },
            "industrial design": {
                "core_concepts": ["form and function", "materials", "manufacturing", "sustainability", "human factors", "aesthetics"],
                "techniques": ["CAD modeling", "rapid prototyping", "material selection", "ergonomic analysis", "design for manufacturing"],
                "metaphors": ["sculpture", "engineering", "problem solving", "innovation", "transformation", "optimization"],
                "challenges": ["cost constraints", "material limitations", "manufacturing complexity", "environmental impact"],
                "applications": ["consumer electronics", "furniture", "automotive", "medical devices", "appliances", "tools"]
            },
            "graphic design": {
                "core_concepts": ["visual communication", "typography", "color theory", "composition", "branding", "hierarchy"],
                "techniques": ["layout design", "brand development", "illustration", "photo editing", "print design", "digital design"],
                "metaphors": ["storytelling", "visual language", "communication", "expression", "impact", "influence"],
                "challenges": ["brand consistency", "cross-media adaptation", "cultural sensitivity", "accessibility", "trends"],
                "applications": ["marketing materials", "brand identity", "publications", "packaging", "signage", "digital media"]
            },
            "interior design": {
                "core_concepts": ["space planning", "lighting", "color schemes", "furniture selection", "functionality", "ambiance"],
                "techniques": ["space analysis", "mood boarding", "3D visualization", "material selection", "lighting design"],
                "metaphors": ["orchestration", "composition", "harmony", "atmosphere", "sanctuary", "transformation"],
                "challenges": ["budget constraints", "space limitations", "client preferences", "building codes", "sustainability"],
                "applications": ["residential spaces", "commercial interiors", "hospitality design", "retail spaces", "office design"]
            },
            "fashion design": {
                "core_concepts": ["silhouette", "fabric", "pattern making", "fit", "style", "trends", "functionality"],
                "techniques": ["sketching", "draping", "pattern making", "fitting", "textile selection", "trend analysis"],
                "metaphors": ["expression", "identity", "transformation", "artistry", "storytelling", "culture"],
                "challenges": ["sustainability", "fast fashion", "sizing diversity", "cost management", "trend prediction"],
                "applications": ["ready-to-wear", "haute couture", "accessories", "footwear", "activewear", "sustainable fashion"]
            },
            "architectural design": {
                "core_concepts": ["spatial design", "structural integrity", "environmental integration", "functionality", "aesthetics"],
                "techniques": ["site analysis", "conceptual design", "technical drawing", "3D modeling", "sustainability planning"],
                "metaphors": ["shelter", "community", "harmony", "permanence", "innovation", "legacy", "transformation"],
                "challenges": ["building codes", "environmental impact", "budget constraints", "site limitations", "client needs"],
                "applications": ["residential buildings", "commercial structures", "public spaces", "urban planning", "landscape design"]
            },

            # Technology & Software
            "software development": {
                "core_concepts": ["algorithms", "data structures", "programming languages", "software architecture", "debugging"],
                "techniques": ["agile development", "version control", "testing", "code review", "continuous integration"],
                "metaphors": ["construction", "craftsmanship", "problem solving", "logic", "creativity", "engineering"],
                "challenges": ["scalability", "maintainability", "security", "performance", "technical debt", "complexity"],
                "applications": ["web applications", "mobile apps", "desktop software", "embedded systems", "enterprise software"]
            },
            "mobile app development": {
                "core_concepts": ["user interface", "performance optimization", "platform guidelines", "touch interaction", "offline functionality"],
                "techniques": ["native development", "cross-platform frameworks", "app store optimization", "user analytics"],
                "metaphors": ["pocket companion", "digital assistant", "gateway", "tool", "experience", "connection"],
                "challenges": ["device fragmentation", "battery optimization", "app store approval", "user retention"],
                "applications": ["productivity apps", "social media", "gaming", "e-commerce", "health tracking", "education"]
            },
            "web development": {
                "core_concepts": ["frontend", "backend", "databases", "APIs", "responsive design", "web standards"],
                "techniques": ["HTML/CSS/JavaScript", "framework development", "database design", "API development", "testing"],
                "metaphors": ["architecture", "ecosystem", "network", "platform", "gateway", "foundation"],
                "challenges": ["browser compatibility", "performance optimization", "security", "accessibility", "scalability"],
                "applications": ["websites", "web applications", "e-commerce platforms", "content management", "web services"]
            },
            "artificial intelligence": {
                "core_concepts": ["neural networks", "machine learning", "deep learning", "algorithms", "optimization", "inference"],
                "techniques": ["training", "validation", "feature extraction", "classification", "regression", "clustering"],
                "metaphors": ["brain", "cognition", "learning", "adaptation", "intelligence", "reasoning", "perception"],
                "challenges": ["bias", "interpretability", "scalability", "ethics", "robustness", "data quality"],
                "applications": ["automation", "prediction", "recognition", "generation", "decision making", "natural language processing"]
            },
            "machine learning": {
                "core_concepts": ["supervised learning", "unsupervised learning", "reinforcement learning", "model training", "feature engineering"],
                "techniques": ["cross-validation", "hyperparameter tuning", "ensemble methods", "regularization", "dimensionality reduction"],
                "metaphors": ["pattern recognition", "learning", "adaptation", "optimization", "discovery", "intelligence"],
                "challenges": ["overfitting", "data scarcity", "model interpretability", "computational complexity", "generalization"],
                "applications": ["predictive analytics", "recommendation systems", "computer vision", "natural language processing"]
            },
            "data science": {
                "core_concepts": ["data analysis", "statistical modeling", "data visualization", "big data", "analytics", "insights"],
                "techniques": ["exploratory data analysis", "statistical testing", "machine learning", "data mining", "visualization"],
                "metaphors": ["detective work", "storytelling", "discovery", "exploration", "insight", "understanding"],
                "challenges": ["data quality", "missing data", "scalability", "interpretation", "bias", "privacy"],
                "applications": ["business intelligence", "predictive analytics", "market research", "scientific research", "decision support"]
            },
            "cybersecurity": {
                "core_concepts": ["encryption", "authentication", "firewall", "intrusion detection", "vulnerability", "threat modeling"],
                "techniques": ["penetration testing", "risk assessment", "incident response", "security auditing", "threat hunting"],
                "metaphors": ["fortress", "shield", "guardian", "sentinel", "barrier", "protection", "defense"],
                "challenges": ["zero-day attacks", "social engineering", "insider threats", "compliance", "evolving threats"],
                "applications": ["network security", "data protection", "identity management", "secure communications", "fraud prevention"]
            },
            "cloud computing": {
                "core_concepts": ["scalability", "elasticity", "distributed systems", "virtualization", "containerization", "microservices"],
                "techniques": ["infrastructure as code", "auto-scaling", "load balancing", "disaster recovery", "monitoring"],
                "metaphors": ["utility", "ecosystem", "platform", "infrastructure", "foundation", "network"],
                "challenges": ["vendor lock-in", "security", "compliance", "cost optimization", "performance", "integration"],
                "applications": ["web hosting", "data storage", "application deployment", "backup solutions", "development platforms"]
            },
            "blockchain technology": {
                "core_concepts": ["decentralization", "consensus", "cryptography", "smart contracts", "distributed ledger", "immutability"],
                "techniques": ["proof of work", "proof of stake", "hash functions", "digital signatures", "merkle trees"],
                "metaphors": ["ledger", "chain", "network", "trust", "verification", "transparency", "permanence"],
                "challenges": ["scalability", "energy consumption", "regulation", "adoption", "interoperability", "security"],
                "applications": ["cryptocurrency", "supply chain", "digital identity", "voting systems", "financial services"]
            },

            # Business & Strategy
            "business strategy": {
                "core_concepts": ["competitive advantage", "market positioning", "value proposition", "strategic planning", "growth strategy"],
                "techniques": ["SWOT analysis", "market research", "competitive analysis", "strategic planning", "performance metrics"],
                "metaphors": ["chess game", "navigation", "warfare", "ecosystem", "journey", "competition", "positioning"],
                "challenges": ["market uncertainty", "competition", "resource constraints", "execution", "adaptation", "measurement"],
                "applications": ["corporate strategy", "market entry", "product strategy", "digital transformation", "mergers and acquisitions"]
            },
            "digital marketing": {
                "core_concepts": ["customer acquisition", "brand awareness", "conversion optimization", "customer journey", "engagement"],
                "techniques": ["SEO", "social media marketing", "content marketing", "email marketing", "paid advertising", "analytics"],
                "metaphors": ["conversation", "relationship", "attraction", "influence", "connection", "storytelling"],
                "challenges": ["ad fatigue", "privacy regulations", "attribution", "ROI measurement", "channel optimization"],
                "applications": ["lead generation", "brand building", "customer retention", "e-commerce", "B2B marketing"]
            },
            "e-commerce": {
                "core_concepts": ["online marketplace", "customer experience", "payment processing", "inventory management", "logistics"],
                "techniques": ["conversion optimization", "personalization", "recommendation engines", "A/B testing", "customer analytics"],
                "metaphors": ["storefront", "marketplace", "journey", "ecosystem", "platform", "destination"],
                "challenges": ["competition", "customer acquisition", "fraud prevention", "scalability", "customer service"],
                "applications": ["online retail", "digital marketplace", "subscription services", "mobile commerce", "B2B e-commerce"]
            },
            "startup ventures": {
                "core_concepts": ["innovation", "disruption", "scalability", "product-market fit", "venture capital", "entrepreneurship"],
                "techniques": ["lean startup", "MVP development", "customer validation", "pivot strategies", "fundraising"],
                "metaphors": ["journey", "adventure", "experiment", "rocket ship", "seed", "growth", "transformation"],
                "challenges": ["funding", "market validation", "team building", "competition", "scaling", "sustainability"],
                "applications": ["tech startups", "social ventures", "fintech", "healthtech", "edtech", "cleantech"]
            },
            "financial services": {
                "core_concepts": ["risk management", "investment", "banking", "insurance", "financial planning", "compliance"],
                "techniques": ["portfolio management", "risk assessment", "financial modeling", "regulatory compliance", "customer onboarding"],
                "metaphors": ["stewardship", "security", "growth", "protection", "foundation", "trust", "stability"],
                "challenges": ["regulation", "cybersecurity", "market volatility", "customer trust", "digital transformation"],
                "applications": ["banking", "investment management", "insurance", "fintech", "payment processing", "wealth management"]
            },
            "supply chain management": {
                "core_concepts": ["logistics", "inventory optimization", "supplier relationships", "demand forecasting", "distribution"],
                "techniques": ["just-in-time", "vendor management", "demand planning", "logistics optimization", "quality control"],
                "metaphors": ["network", "flow", "ecosystem", "pipeline", "orchestration", "coordination"],
                "challenges": ["disruption", "cost optimization", "sustainability", "visibility", "risk management"],
                "applications": ["manufacturing", "retail", "e-commerce", "healthcare", "automotive", "food industry"]
            },
            "human resources": {
                "core_concepts": ["talent management", "employee engagement", "performance management", "organizational culture", "recruitment"],
                "techniques": ["talent acquisition", "performance reviews", "training and development", "succession planning", "employee analytics"],
                "metaphors": ["cultivation", "development", "community", "partnership", "investment", "growth"],
                "challenges": ["talent retention", "diversity and inclusion", "remote work", "skills gap", "employee satisfaction"],
                "applications": ["recruitment", "employee development", "performance management", "organizational design", "compensation"]
            },
            "customer service": {
                "core_concepts": ["customer satisfaction", "support quality", "response time", "problem resolution", "customer experience"],
                "techniques": ["multichannel support", "knowledge management", "customer feedback", "service automation", "quality assurance"],
                "metaphors": ["assistance", "partnership", "care", "support", "guidance", "relationship"],
                "challenges": ["scalability", "consistency", "customer expectations", "cost management", "technology integration"],
                "applications": ["help desk", "technical support", "customer success", "complaint resolution", "service delivery"]
            },
            "sales optimization": {
                "core_concepts": ["lead generation", "conversion rates", "sales funnel", "customer acquisition", "revenue growth"],
                "techniques": ["CRM management", "sales analytics", "lead scoring", "pipeline management", "sales automation"],
                "metaphors": ["hunting", "cultivation", "relationship building", "persuasion", "journey", "conversion"],
                "challenges": ["lead quality", "sales cycle length", "competition", "quota achievement", "customer retention"],
                "applications": ["B2B sales", "retail sales", "inside sales", "field sales", "e-commerce", "subscription sales"]
            },

            # Healthcare & Medicine
            "medical devices": {
                "core_concepts": ["patient safety", "regulatory compliance", "biocompatibility", "clinical efficacy", "usability"],
                "techniques": ["clinical trials", "regulatory approval", "quality assurance", "risk management", "user testing"],
                "metaphors": ["healing tools", "precision instruments", "life support", "diagnostic aids", "therapeutic solutions"],
                "challenges": ["FDA approval", "cost containment", "technology integration", "patient compliance", "market access"],
                "applications": ["diagnostic equipment", "surgical instruments", "monitoring devices", "therapeutic devices", "implantables"]
            },
            "healthcare technology": {
                "core_concepts": ["patient care", "clinical workflows", "health data", "interoperability", "telemedicine"],
                "techniques": ["electronic health records", "clinical decision support", "health analytics", "mobile health", "AI diagnostics"],
                "metaphors": ["digital health", "connected care", "intelligent systems", "health ecosystem", "care coordination"],
                "challenges": ["privacy", "interoperability", "adoption", "cost", "regulatory compliance", "data security"],
                "applications": ["EHR systems", "telemedicine platforms", "health apps", "clinical analytics", "patient monitoring"]
            },
            "pharmaceutical research": {
                "core_concepts": ["drug discovery", "clinical trials", "regulatory approval", "therapeutic efficacy", "safety profile"],
                "techniques": ["compound screening", "preclinical testing", "clinical trial design", "regulatory submission", "pharmacovigilance"],
                "metaphors": ["discovery", "development", "healing", "innovation", "breakthrough", "transformation"],
                "challenges": ["development costs", "regulatory hurdles", "clinical trial recruitment", "market competition", "patent protection"],
                "applications": ["drug development", "vaccine research", "personalized medicine", "rare diseases", "oncology"]
            },
            "mental health services": {
                "core_concepts": ["psychological well-being", "therapeutic intervention", "mental health assessment", "treatment planning", "recovery"],
                "techniques": ["cognitive behavioral therapy", "psychotherapy", "medication management", "crisis intervention", "group therapy"],
                "metaphors": ["healing", "support", "journey", "recovery", "resilience", "empowerment", "transformation"],
                "challenges": ["stigma", "access to care", "treatment adherence", "provider shortage", "insurance coverage"],
                "applications": ["therapy services", "crisis intervention", "addiction treatment", "psychiatric care", "wellness programs"]
            },
            "telemedicine": {
                "core_concepts": ["remote healthcare", "virtual consultations", "digital health", "patient monitoring", "healthcare access"],
                "techniques": ["video conferencing", "remote monitoring", "digital diagnostics", "e-prescribing", "health data integration"],
                "metaphors": ["bridge", "connection", "accessibility", "reach", "virtual presence", "digital care"],
                "challenges": ["technology adoption", "regulatory compliance", "reimbursement", "digital divide", "privacy"],
                "applications": ["virtual consultations", "remote monitoring", "specialist access", "rural healthcare", "chronic care management"]
            },
            "health informatics": {
                "core_concepts": ["health data", "clinical information systems", "health analytics", "interoperability", "data standards"],
                "techniques": ["data integration", "clinical analytics", "health information exchange", "data visualization", "predictive modeling"],
                "metaphors": ["intelligence", "insight", "connectivity", "knowledge", "understanding", "integration"],
                "challenges": ["data silos", "privacy", "standardization", "system integration", "data quality"],
                "applications": ["EHR systems", "clinical decision support", "population health", "quality improvement", "research"]
            },
            "medical education": {
                "core_concepts": ["clinical training", "medical knowledge", "competency development", "simulation", "continuing education"],
                "techniques": ["case-based learning", "simulation training", "clinical rotations", "competency assessment", "peer learning"],
                "metaphors": ["apprenticeship", "mastery", "development", "practice", "expertise", "lifelong learning"],
                "challenges": ["curriculum design", "assessment methods", "technology integration", "clinical exposure", "competency validation"],
                "applications": ["medical school", "residency training", "continuing education", "simulation centers", "online learning"]
            },
            "patient care": {
                "core_concepts": ["patient-centered care", "care coordination", "quality outcomes", "patient safety", "care delivery"],
                "techniques": ["care planning", "multidisciplinary teams", "patient engagement", "quality improvement", "care transitions"],
                "metaphors": ["healing", "compassion", "partnership", "support", "guidance", "recovery"],
                "challenges": ["care coordination", "patient compliance", "resource constraints", "quality measurement", "patient satisfaction"],
                "applications": ["hospital care", "primary care", "specialty care", "home healthcare", "palliative care"]
            },

            # Education & Learning
            "educational technology": {
                "core_concepts": ["digital learning", "educational software", "learning management systems", "adaptive learning", "educational content"],
                "techniques": ["instructional design", "learning analytics", "gamification", "personalized learning", "assessment technology"],
                "metaphors": ["empowerment", "transformation", "discovery", "growth", "exploration", "innovation"],
                "challenges": ["digital divide", "teacher training", "content quality", "student engagement", "technology integration"],
                "applications": ["LMS platforms", "educational apps", "online courses", "virtual classrooms", "assessment tools"]
            },
            "online learning": {
                "core_concepts": ["distance education", "virtual classrooms", "self-paced learning", "digital content", "remote instruction"],
                "techniques": ["video lectures", "interactive content", "discussion forums", "virtual labs", "online assessment"],
                "metaphors": ["accessibility", "flexibility", "connection", "reach", "opportunity", "democratization"],
                "challenges": ["student engagement", "technical barriers", "quality assurance", "social interaction", "assessment integrity"],
                "applications": ["MOOCs", "corporate training", "K-12 education", "higher education", "professional development"]
            },
            "curriculum development": {
                "core_concepts": ["learning objectives", "instructional design", "assessment strategies", "content sequencing", "competency mapping"],
                "techniques": ["backward design", "standards alignment", "learning outcome mapping", "assessment design", "content curation"],
                "metaphors": ["blueprint", "journey", "scaffolding", "progression", "development", "structure"],
                "challenges": ["standards alignment", "content relevance", "assessment validity", "implementation", "continuous improvement"],
                "applications": ["K-12 curriculum", "higher education", "corporate training", "professional certification", "skill development"]
            },
            "teacher training": {
                "core_concepts": ["pedagogical skills", "classroom management", "instructional strategies", "professional development", "educational theory"],
                "techniques": ["mentoring", "peer observation", "reflective practice", "action research", "collaborative learning"],
                "metaphors": ["growth", "mastery", "development", "empowerment", "transformation", "expertise"],
                "challenges": ["time constraints", "resource limitations", "technology integration", "diverse learners", "assessment methods"],
                "applications": ["pre-service training", "in-service development", "leadership training", "subject-specific training", "technology training"]
            },
            "student engagement": {
                "core_concepts": ["active learning", "motivation", "participation", "learning experience", "student-centered learning"],
                "techniques": ["gamification", "interactive activities", "collaborative learning", "project-based learning", "peer learning"],
                "metaphors": ["spark", "connection", "involvement", "participation", "energy", "enthusiasm"],
                "challenges": ["attention span", "diverse learning styles", "technology distractions", "motivation", "assessment"],
                "applications": ["classroom activities", "online learning", "educational games", "interactive content", "learning platforms"]
            },
            "learning analytics": {
                "core_concepts": ["educational data", "learning patterns", "performance tracking", "predictive modeling", "personalized learning"],
                "techniques": ["data mining", "statistical analysis", "visualization", "machine learning", "dashboard development"],
                "metaphors": ["insight", "intelligence", "understanding", "discovery", "optimization", "guidance"],
                "challenges": ["data privacy", "interpretation", "actionable insights", "system integration", "teacher training"],
                "applications": ["LMS analytics", "student performance tracking", "early warning systems", "personalized recommendations"]
            },
            "educational games": {
                "core_concepts": ["game-based learning", "educational content", "engagement", "skill development", "assessment"],
                "techniques": ["game design", "narrative development", "progression systems", "feedback mechanisms", "assessment integration"],
                "metaphors": ["play", "adventure", "challenge", "discovery", "achievement", "exploration"],
                "challenges": ["educational effectiveness", "content alignment", "engagement sustainability", "assessment validity"],
                "applications": ["serious games", "simulation games", "skill training", "language learning", "STEM education"]
            },
            "skill development": {
                "core_concepts": ["competency building", "practical skills", "professional development", "lifelong learning", "capability enhancement"],
                "techniques": ["hands-on training", "mentorship", "practice sessions", "skill assessment", "progressive learning"],
                "metaphors": ["growth", "building", "craftsmanship", "mastery", "development", "enhancement"],
                "challenges": ["skill relevance", "transfer to practice", "assessment methods", "motivation", "resource availability"],
                "applications": ["vocational training", "professional development", "technical skills", "soft skills", "certification programs"]
            },

            # Environment & Sustainability
            "renewable energy": {
                "core_concepts": ["solar power", "wind energy", "hydroelectric", "geothermal", "biomass", "energy storage"],
                "techniques": ["energy conversion", "grid integration", "energy storage", "efficiency optimization", "lifecycle assessment"],
                "metaphors": ["harvest", "capture", "transformation", "sustainability", "clean power", "natural resources"],
                "challenges": ["intermittency", "storage", "cost competitiveness", "grid integration", "policy support"],
                "applications": ["solar installations", "wind farms", "energy storage systems", "smart grids", "distributed energy"]
            },
            "sustainable agriculture": {
                "core_concepts": ["organic farming", "soil health", "biodiversity", "water conservation", "crop rotation", "ecosystem balance"],
                "techniques": ["precision farming", "integrated pest management", "cover cropping", "composting", "water-efficient irrigation"],
                "metaphors": ["cultivation", "stewardship", "harmony", "balance", "regeneration", "nurturing"],
                "challenges": ["yield optimization", "pest management", "climate adaptation", "market access", "certification"],
                "applications": ["organic farming", "permaculture", "vertical farming", "precision agriculture", "sustainable livestock"]
            },
            "environmental conservation": {
                "core_concepts": ["biodiversity protection", "habitat preservation", "species conservation", "ecosystem restoration", "sustainability"],
                "techniques": ["habitat restoration", "species monitoring", "conservation planning", "community engagement", "policy advocacy"],
                "metaphors": ["protection", "preservation", "stewardship", "guardianship", "restoration", "balance"],
                "challenges": ["habitat loss", "climate change", "human-wildlife conflict", "funding", "policy implementation"],
                "applications": ["wildlife conservation", "marine protection", "forest conservation", "wetland restoration", "urban conservation"]
            },
            "green technology": {
                "core_concepts": ["clean technology", "environmental innovation", "sustainable solutions", "eco-friendly design", "circular economy"],
                "techniques": ["lifecycle assessment", "eco-design", "material selection", "energy efficiency", "waste reduction"],
                "metaphors": ["innovation", "transformation", "sustainability", "harmony", "efficiency", "responsibility"],
                "challenges": ["cost competitiveness", "market adoption", "scalability", "regulatory approval", "consumer acceptance"],
                "applications": ["clean energy", "waste management", "water treatment", "sustainable materials", "green building"]
            },
            "waste management": {
                "core_concepts": ["waste reduction", "recycling", "circular economy", "waste-to-energy", "sustainable disposal"],
                "techniques": ["source reduction", "material recovery", "composting", "anaerobic digestion", "waste sorting"],
                "metaphors": ["transformation", "recovery", "renewal", "efficiency", "responsibility", "stewardship"],
                "challenges": ["contamination", "cost effectiveness", "behavior change", "infrastructure", "regulation"],
                "applications": ["municipal waste", "industrial waste", "electronic waste", "organic waste", "hazardous waste"]
            },
            "climate solutions": {
                "core_concepts": ["carbon reduction", "climate adaptation", "mitigation strategies", "resilience building", "sustainability"],
                "techniques": ["carbon capture", "emission reduction", "adaptation planning", "resilience assessment", "policy development"],
                "metaphors": ["healing", "protection", "adaptation", "resilience", "transformation", "stewardship"],
                "challenges": ["scale of impact", "cost", "political will", "technology readiness", "global coordination"],
                "applications": ["carbon capture", "renewable energy", "climate adaptation", "sustainable transport", "green buildings"]
            },
            "eco-friendly products": {
                "core_concepts": ["sustainable materials", "biodegradable", "non-toxic", "energy efficient", "minimal packaging"],
                "techniques": ["sustainable design", "material selection", "lifecycle assessment", "eco-labeling", "green chemistry"],
                "metaphors": ["harmony", "responsibility", "care", "sustainability", "mindfulness", "stewardship"],
                "challenges": ["cost premium", "performance", "consumer acceptance", "certification", "supply chain"],
                "applications": ["consumer goods", "packaging", "textiles", "cosmetics", "cleaning products"]
            },
            "carbon reduction": {
                "core_concepts": ["emission reduction", "carbon footprint", "net zero", "carbon neutrality", "decarbonization"],
                "techniques": ["emission measurement", "reduction strategies", "offset programs", "renewable energy", "efficiency improvements"],
                "metaphors": ["reduction", "neutrality", "balance", "responsibility", "transformation", "commitment"],
                "challenges": ["measurement accuracy", "cost", "technology availability", "behavior change", "policy support"],
                "applications": ["corporate sustainability", "carbon markets", "renewable energy", "energy efficiency", "transportation"]
            },

            # Transportation & Mobility
            "urban transportation": {
                "core_concepts": ["public transit", "mobility solutions", "traffic management", "sustainable transport", "accessibility"],
                "techniques": ["route optimization", "demand forecasting", "multimodal integration", "smart traffic systems", "accessibility design"],
                "metaphors": ["flow", "network", "connectivity", "movement", "accessibility", "efficiency"],
                "challenges": ["congestion", "funding", "infrastructure", "user adoption", "integration"],
                "applications": ["bus systems", "rail transit", "bike sharing", "ride sharing", "pedestrian infrastructure"]
            },
            "electric vehicles": {
                "core_concepts": ["battery technology", "charging infrastructure", "energy efficiency", "emission reduction", "sustainable mobility"],
                "techniques": ["battery management", "charging optimization", "range extension", "grid integration", "lifecycle assessment"],
                "metaphors": ["transformation", "clean energy", "efficiency", "innovation", "sustainability"],
                "challenges": ["battery cost", "charging infrastructure", "range anxiety", "grid impact", "material sourcing"],
                "applications": ["passenger vehicles", "commercial vehicles", "public transport", "delivery vehicles", "micro-mobility"]
            },
            "autonomous vehicles": {
                "core_concepts": ["self-driving", "artificial intelligence", "sensor technology", "safety systems", "traffic optimization"],
                "techniques": ["machine learning", "sensor fusion", "path planning", "safety validation", "human-machine interaction"],
                "metaphors": ["intelligence", "automation", "safety", "efficiency", "transformation", "evolution"],
                "challenges": ["safety validation", "regulatory approval", "public acceptance", "ethical decisions", "infrastructure"],
                "applications": ["passenger cars", "commercial vehicles", "public transport", "delivery systems", "mobility services"]
            },

            # For brevity, I'll add a few more key domains and close the dictionary
            # This covers the most important domains for creativity enhancement
            "general innovation": {
                "core_concepts": ["creativity", "problem solving", "ideation", "innovation process", "breakthrough thinking"],
                "techniques": ["brainstorming", "design thinking", "lateral thinking", "systematic innovation", "creative problem solving"],
                "metaphors": ["discovery", "breakthrough", "transformation", "creation", "evolution", "inspiration"],
                "challenges": ["idea generation", "implementation", "resource constraints", "risk management", "market acceptance"],
                "applications": ["product development", "process improvement", "service innovation", "business model innovation", "social innovation"]
            }
        }
