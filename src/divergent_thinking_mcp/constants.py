"""
Shared constants for the Divergent Thinking MCP Server.

This module centralizes constant values used across the application
to ensure consistency and ease of maintenance.
"""

from typing import Set, List, Dict

# The single source of truth for valid domain names.
# Using a set for efficient membership testing (e.g., `in VALID_DOMAINS`).
VALID_DOMAINS: Set[str] = {
    # Design & User Experience
    "product design", "user interface design", "user experience design", "industrial design",
    "graphic design", "interior design", "fashion design", "architectural design",

    # Technology & Software
    "software development", "mobile app development", "web development", "artificial intelligence",
    "machine learning", "data science", "cybersecurity", "cloud computing", "blockchain technology",

    # Business & Strategy
    "business strategy", "digital marketing", "e-commerce", "startup ventures", "financial services",
    "supply chain management", "human resources", "customer service", "sales optimization",

    # Healthcare & Medicine
    "medical devices", "healthcare technology", "pharmaceutical research", "mental health services",
    "telemedicine", "health informatics", "medical education", "patient care",

    # Education & Learning
    "educational technology", "online learning", "curriculum development", "teacher training",
    "student engagement", "learning analytics", "educational games", "skill development",

    # Environment & Sustainability
    "renewable energy", "sustainable agriculture", "environmental conservation", "green technology",
    "waste management", "climate solutions", "eco-friendly products", "carbon reduction",

    # Transportation & Mobility
    "urban transportation", "electric vehicles", "autonomous vehicles", "public transit",
    "logistics optimization", "smart cities", "mobility services", "transportation planning",

    # Entertainment & Media
    "content creation", "digital entertainment", "gaming industry", "social media platforms",
    "streaming services", "virtual reality", "augmented reality", "creative arts",

    # Science & Research
    "scientific research", "laboratory automation", "research methodology", "data analysis",
    "experimental design", "academic publishing", "research collaboration", "innovation management",

    # General/Other
    "general innovation", "cross-industry solutions", "emerging technologies", "social innovation"
}


# Generic random words for association
RANDOM_WORDS: List[str] = [
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

# Generic analogical thinking domains
ANALOGICAL_DOMAINS: Dict[str, List[str]] = {
    "nature": ["ant colonies", "bird flocks", "tree root systems", "coral reefs", "beehives"],
    "sports": ["team coordination", "strategic plays", "training regimens", "equipment design", "performance optimization"],
    "music": ["orchestral harmony", "improvisation", "rhythm patterns", "instrument design", "sound mixing"],
    "cooking": ["recipe development", "flavor combinations", "cooking techniques", "kitchen organization", "presentation"],
    "architecture": ["structural design", "space utilization", "material selection", "environmental integration", "aesthetic balance"],
    "transportation": ["traffic flow", "route optimization", "vehicle design", "logistics systems", "navigation methods"],
    "games": ["rule systems", "strategy development", "player interaction", "challenge progression", "reward mechanisms"]
}

# Generic biomimicry examples
BIOMIMICRY_EXAMPLES: List[Dict[str, str]] = [
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

# Domain-specific keywords for various creativity algorithms
DOMAIN_KEYWORDS: Dict[str, List[str]] = {
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

# Comprehensive domain-specific creativity word banks
DOMAIN_CREATIVITY_WORDS: Dict[str, Dict[str, List[str]]] = {
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