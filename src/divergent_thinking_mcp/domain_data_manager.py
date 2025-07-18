"""
Domain Data Manager for unified access to domain-specific information.

This module provides a centralized interface for accessing domain-specific data
including creativity words, analogies, biomimicry examples, and perspectives.
It consolidates the previously scattered domain mappings to reduce redundancy
while maintaining backward compatibility.
"""

from typing import Dict, List
from functools import lru_cache

from .constants import DOMAIN_CREATIVITY_WORDS, ANALOGICAL_DOMAINS, BIOMIMICRY_EXAMPLES


class DomainDataManager:
    """
    Centralized manager for domain-specific data with caching and fallback logic.
    
    This class provides unified access to all domain-specific information while
    maintaining backward compatibility with existing code patterns.
    """
    
    def __init__(self) -> None:
        """Initialize the domain data manager."""
        self._creativity_words = DOMAIN_CREATIVITY_WORDS
        self._generic_analogies = ANALOGICAL_DOMAINS
        self._generic_biomimicry = BIOMIMICRY_EXAMPLES
        
        # Initialize specialized domain data (consolidated from creativity_algorithms.py)
        self._domain_analogies = self._initialize_domain_analogies()
        self._domain_biomimicry = self._initialize_domain_biomimicry()
        self._domain_perspectives = self._initialize_domain_perspectives()
    
    @lru_cache(maxsize=128)
    def get_creativity_words(self, domain: str, category: str) -> List[str]:
        """
        Get creativity words for a specific domain and category.
        
        Args:
            domain: Target domain
            category: Word category (core_concepts, techniques, metaphors, challenges, applications)
            
        Returns:
            List of words for the domain/category combination
        """
        if domain in self._creativity_words:
            domain_data = self._creativity_words[domain]
            if category in domain_data:
                return domain_data[category]
        return []
    
    @lru_cache(maxsize=64)
    def get_domain_analogies(self, domain: str) -> Dict[str, List[str]]:
        """
        Get analogies for a specific domain with fallback to generic analogies.
        
        Args:
            domain: Target domain
            
        Returns:
            Dictionary mapping analogy categories to examples
        """
        return self._domain_analogies.get(domain, self._generic_analogies)
    
    @lru_cache(maxsize=64)
    def get_domain_biomimicry(self, domain: str) -> List[Dict[str, str]]:
        """
        Get biomimicry examples for a specific domain with fallback to generic examples.
        
        Args:
            domain: Target domain
            
        Returns:
            List of biomimicry examples with organism, mechanism, and property
        """
        return self._domain_biomimicry.get(domain, self._generic_biomimicry)
    
    @lru_cache(maxsize=64)
    def get_domain_perspectives(self, domain: str) -> Dict[str, List[str]]:
        """
        Get Six Thinking Hats perspectives for a specific domain.
        
        Args:
            domain: Target domain
            
        Returns:
            Dictionary mapping perspective types to prompts
        """
        return self._domain_perspectives.get(domain, {})
    
    def _initialize_domain_analogies(self) -> Dict[str, Dict[str, List[str]]]:
        """Initialize domain-specific analogies (consolidated from creativity_algorithms.py)."""
        return {
            # AI & Machine Learning
            "artificial intelligence systems": {
                "biological_systems": ["neural networks", "immune systems", "evolutionary processes", "swarm behavior", "brain plasticity"],
                "cognitive_processes": ["learning patterns", "memory formation", "pattern recognition", "decision making", "problem solving"],
                "mathematical_concepts": ["optimization algorithms", "statistical inference", "graph theory", "probability models", "linear algebra"]
            },
            "machine learning algorithms": {
                "mathematical_systems": ["optimization functions", "statistical models", "probability distributions", "algorithmic processes", "computational methods"],
                "learning_processes": ["pattern recognition", "adaptive behavior", "experience accumulation", "skill development", "knowledge acquisition"],
                "biological_learning": ["neural adaptation", "memory formation", "skill acquisition", "pattern recognition", "behavioral conditioning"]
            },
            "deep learning architectures": {
                "architectural_systems": ["layered structures", "hierarchical design", "modular construction", "interconnected networks", "scalable frameworks"],
                "information_processing": ["hierarchical processing", "feature extraction", "pattern recognition", "information flow", "data transformation"],
                "biological_networks": ["neural hierarchies", "brain architecture", "synaptic connections", "neural pathways", "cortical layers"]
            },
            
            # Internet & Web Technologies  
            "web application development": {
                "architectural_systems": ["building construction", "infrastructure design", "modular assembly", "foundation systems", "structural engineering"],
                "communication_networks": ["postal systems", "telephone networks", "transportation hubs", "information exchange", "message routing"],
                "user_interfaces": ["storefront design", "navigation systems", "interactive displays", "user experience", "accessibility design"]
            },
            "microservices architecture": {
                "organizational_systems": ["team coordination", "departmental structure", "distributed organizations", "autonomous units", "collaborative networks"],
                "biological_systems": ["cellular organization", "organ systems", "ecosystem interactions", "symbiotic relationships", "distributed intelligence"],
                "urban_planning": ["city districts", "infrastructure networks", "service distribution", "resource allocation", "interconnected systems"]
            },
            
            # Computer Science & Systems
            "distributed systems design": {
                "organizational_networks": ["corporate structures", "government systems", "collaborative networks", "distributed teams", "federated organizations"],
                "biological_ecosystems": ["forest networks", "mycelial connections", "ant colonies", "bird flocks", "ecosystem interactions"],
                "infrastructure_systems": ["power grids", "transportation networks", "communication systems", "supply chains", "utility distribution"]
            },
            "cybersecurity architecture": {
                "defense_systems": ["military fortifications", "castle defenses", "security protocols", "surveillance networks", "protective barriers"],
                "biological_immunity": ["immune responses", "pathogen detection", "cellular defense", "adaptive immunity", "threat recognition"],
                "physical_security": ["access control", "perimeter defense", "monitoring systems", "threat detection", "security layers"]
            },
            
            # Product Development & Management
            "digital product strategy": {
                "business_ecosystems": ["market positioning", "competitive landscapes", "value networks", "customer ecosystems", "strategic alliances"],
                "evolutionary_processes": ["adaptation strategies", "survival mechanisms", "environmental fitness", "competitive advantage", "evolutionary pressure"],
                "game_theory": ["strategic moves", "competitive dynamics", "player interactions", "winning strategies", "market games"]
            },
            "agile product development": {
                "adaptive_systems": ["evolutionary processes", "responsive organisms", "adaptive behavior", "iterative improvement", "environmental adaptation"],
                "collaborative_networks": ["team sports", "orchestra performance", "collaborative creation", "group dynamics", "collective intelligence"],
                "iterative_processes": ["scientific method", "artistic creation", "skill development", "continuous improvement", "learning cycles"]
            },
            
            # Engineering & Infrastructure
            "devops automation systems": {
                "manufacturing_systems": ["assembly lines", "quality control", "automated production", "process optimization", "continuous flow"],
                "biological_processes": ["metabolic pathways", "cellular automation", "homeostatic regulation", "automated responses", "system maintenance"],
                "orchestration_systems": ["conductor coordination", "traffic management", "workflow automation", "process synchronization", "system coordination"]
            },
            "scalable system architecture": {
                "growth_systems": ["organic growth", "fractal patterns", "scalable structures", "modular expansion", "adaptive scaling"],
                "infrastructure_scaling": ["city planning", "transportation scaling", "utility expansion", "network growth", "capacity planning"],
                "biological_scaling": ["organism growth", "population dynamics", "ecosystem scaling", "adaptive capacity", "resource scaling"]
            },
            "site reliability engineering": {
                "medical_systems": ["health monitoring", "preventive care", "emergency response", "system diagnostics", "recovery procedures"],
                "infrastructure_maintenance": ["preventive maintenance", "system monitoring", "failure prevention", "reliability assurance", "operational excellence"],
                "ecosystem_resilience": ["system stability", "adaptive capacity", "disturbance recovery", "resilience mechanisms", "sustainable operation"]
            }
        }
    
    def _initialize_domain_biomimicry(self) -> Dict[str, List[Dict[str, str]]]:
        """Initialize domain-specific biomimicry examples (consolidated from creativity_algorithms.py)."""
        return {
            # AI & Machine Learning
            "artificial intelligence systems": [
                {"organism": "neural networks", "mechanism": "parallel information processing like brain neurons", "property": "distributed intelligence"},
                {"organism": "ant colonies", "mechanism": "swarm optimization for collective problem solving", "property": "emergent intelligence"},
                {"organism": "immune system", "mechanism": "pattern recognition and adaptive memory", "property": "learning from experience"},
                {"organism": "octopus camouflage", "mechanism": "real-time pattern adaptation", "property": "dynamic response systems"},
                {"organism": "bird flocking", "mechanism": "simple rules creating complex behavior", "property": "emergent coordination"}
            ],
            "machine learning algorithms": [
                {"organism": "evolutionary processes", "mechanism": "iterative improvement through selection", "property": "optimization algorithms"},
                {"organism": "neural plasticity", "mechanism": "adapts connections based on experience", "property": "adaptive learning"},
                {"organism": "genetic algorithms", "mechanism": "combines successful traits for improvement", "property": "feature selection"},
                {"organism": "foraging behavior", "mechanism": "explores environment to find optimal resources", "property": "search optimization"},
                {"organism": "memory consolidation", "mechanism": "strengthens important connections over time", "property": "learning retention"}
            ],
            "deep learning architectures": [
                {"organism": "cortical layers", "mechanism": "hierarchical processing from simple to complex", "property": "layered architecture"},
                {"organism": "visual cortex", "mechanism": "processes visual information in specialized layers", "property": "convolutional processing"},
                {"organism": "attention mechanisms", "mechanism": "focuses on relevant information while filtering noise", "property": "attention networks"},
                {"organism": "memory networks", "mechanism": "stores and retrieves information contextually", "property": "memory architectures"},
                {"organism": "neural pathways", "mechanism": "creates efficient information routing", "property": "network connectivity"}
            ],
            
            # Internet & Web Technologies
            "web application development": [
                {"organism": "spider webs", "mechanism": "creates interconnected structures for resource capture", "property": "network architecture"},
                {"organism": "mycelial networks", "mechanism": "distributes resources through underground connections", "property": "distributed systems"},
                {"organism": "coral reefs", "mechanism": "builds complex structures through collaborative growth", "property": "modular development"},
                {"organism": "ecosystem interactions", "mechanism": "multiple species interact through defined interfaces", "property": "api design"},
                {"organism": "river networks", "mechanism": "efficiently routes water through branching systems", "property": "routing systems"}
            ],
            "microservices architecture": [
                {"organism": "cellular organization", "mechanism": "specialized cells perform specific functions", "property": "service specialization"},
                {"organism": "organ systems", "mechanism": "independent organs coordinate through interfaces", "property": "loose coupling"},
                {"organism": "ecosystem niches", "mechanism": "species specialize in specific environmental roles", "property": "domain separation"},
                {"organism": "swarm intelligence", "mechanism": "simple agents create complex collective behavior", "property": "emergent functionality"},
                {"organism": "modular organisms", "mechanism": "independent modules can function separately", "property": "service independence"}
            ],
            
            # Computer Science & Systems
            "distributed systems design": [
                {"organism": "ant colonies", "mechanism": "decentralized coordination without central control", "property": "distributed coordination"},
                {"organism": "neural networks", "mechanism": "parallel processing across multiple nodes", "property": "parallel computation"},
                {"organism": "immune system", "mechanism": "distributed defense with local and global responses", "property": "fault tolerance"},
                {"organism": "forest ecosystems", "mechanism": "resource sharing through underground networks", "property": "resource distribution"},
                {"organism": "bird flocks", "mechanism": "emergent behavior from simple local rules", "property": "emergent coordination"}
            ],
            "cybersecurity architecture": [
                {"organism": "immune system", "mechanism": "distinguishes self from non-self", "property": "threat identification"},
                {"organism": "herd immunity", "mechanism": "collective protection through individual immunity", "property": "network security"},
                {"organism": "camouflage", "mechanism": "blends with environment to avoid detection", "property": "stealth protection"},
                {"organism": "warning signals", "mechanism": "alerts others to danger", "property": "threat communication"},
                {"organism": "territorial behavior", "mechanism": "defends boundaries from intruders", "property": "perimeter defense"}
            ]
        }
    
    def _initialize_domain_perspectives(self) -> Dict[str, Dict[str, List[str]]]:
        """Initialize domain-specific Six Thinking Hats perspectives (consolidated from creativity_algorithms.py)."""
        return {
            # AI & Machine Learning
            "artificial intelligence systems": {
                "factual": [
                    "What AI performance metrics validate this approach?",
                    "What training data requirements exist?",
                    "What computational resources are needed?",
                    "What accuracy benchmarks apply?"
                ],
                "emotional": [
                    "How do users feel about AI making this decision?",
                    "What trust concerns arise with this AI system?",
                    "How does this impact human-AI interaction?",
                    "What ethical concerns do stakeholders have?"
                ],
                "critical": [
                    "What bias risks exist in this AI system?",
                    "How could this AI system fail or be misused?",
                    "What privacy concerns arise?",
                    "What happens when the AI encounters edge cases?"
                ],
                "positive": [
                    "How could this AI system improve decision-making?",
                    "What efficiency gains are possible?",
                    "How could this democratize AI capabilities?",
                    "What new possibilities does this AI enable?"
                ]
            },
            "machine learning algorithms": {
                "factual": [
                    "What training data quality metrics support this?",
                    "What model performance benchmarks exist?",
                    "What computational complexity analysis applies?",
                    "What validation methodology is used?"
                ],
                "emotional": [
                    "How do data scientists feel about this algorithm's interpretability?",
                    "What concerns do stakeholders have about black-box decisions?",
                    "How does this impact user confidence in predictions?",
                    "What excitement or anxiety does this algorithm create?"
                ],
                "critical": [
                    "What overfitting risks exist with this algorithm?",
                    "How could this algorithm fail on edge cases?",
                    "What bias could be introduced through training data?",
                    "What happens when the algorithm encounters novel scenarios?"
                ],
                "positive": [
                    "How could this algorithm improve prediction accuracy?",
                    "What automation benefits are possible?",
                    "How could this reduce manual analysis time?",
                    "What new insights could this algorithm reveal?"
                ]
            }
        }


# Global instance for easy access
domain_data_manager = DomainDataManager()
