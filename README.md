# Divergent Thinking MCP Server / 发散思维MCP服务器

An MCP (Model Context Protocol) server that promotes divergent and creative thinking patterns for creation - the Supplement of sequential logical thinking.
一个MCP（模型上下文协议）服务器，促进创造性思维模式，是顺序逻辑思维的补充。

## 🎨 Philosophy / 设计理念

Designed to provide creative inspiration for both humans and AI agents, complementing the structured nature of sequential thinking.
旨在为人类与AI智能体提供创意与灵感，作为对传统顺序性思维的补充。

## 🛠️ Tools / 工具

### Unified Divergent Thinking Tool / 统一发散思维工具

This MCP server provides a **single comprehensive tool** that offers 6 powerful creativity methods through one unified interface, aiming to reduce confusion and cognitive overload.
此MCP服务器提供**单一综合工具**，通过统一界面提供6种强大的创意方法，旨在减轻混乱和认知负担。

#### **`divergent_thinking`** - Comprehensive Creative Thinking Tool / 综合创意思维工具

A unified tool providing access to 6 proven creativity methodologies through parameter-driven functionality selection:
通过参数驱动功能选择提供6种经过验证的创意方法的统一工具：

**Available Thinking Methods / 可用思维方法：**

1. **`structured_process`** (Default/默认) - Multi-turn comprehensive exploration with thought tracking and branching
   多轮综合探索，具有思维跟踪和分支功能

2. **`generate_branches`** - Create 3 different creative directions from a single thought (single response)
   从单一想法创建3个不同的创意方向（单次响应）

3. **`perspective_shift`** - View thoughts through unusual viewpoints (inanimate objects, abstract concepts, impossible beings)
   通过不寻常的视角查看想法（无生命物体、抽象概念、不可能的存在）

4. **`creative_constraint`** - Apply strategic limitations to force breakthrough innovation
   应用战略限制来强制突破性创新

5. **`combine_thoughts`** - Merge two concepts into novel hybrid solutions
   将两个概念合并为新颖的混合解决方案

6. **`reverse_brainstorming`** - Explore failure modes to discover breakthrough solutions
   探索失败模式以发现突破性解决方案

**Key Features / 主要特性：**

- **🧠 Domain-Aware Intelligence**: Intelligent word selection and context-sensitive creativity replacing generic random outputs
  领域感知智能：智能词汇选择和上下文敏感创造力，取代通用随机输出
- **📊 Contextual Creativity Methods**: Enhanced SCAMPER, analogical thinking, biomimicry, and Six Thinking Hats with domain-specific intelligence
  上下文创意方法：增强的SCAMPER、类比思维、仿生学和六顶思考帽，具有领域特定智能
- **🎨 Interactive Context Specification**: Agent-driven domain, audience, time period, resources, and goals specification for targeted creativity
  交互式上下文规范：代理驱动的领域、受众、时间段、资源和目标规范，实现有针对性的创造力
- **🔍 Multi-word Domain Precision**: 78+ specialized domains like "artificial intelligence systems", "web application development", "digital product strategy"
  多词领域精度：78+个专业领域，如"人工智能系统"、"网络应用开发"、"数字产品策略"
- **🔄 Multi-turn vs Single-shot**: `structured_process` provides complete multi-turn exploration; others are single-response methods
  多轮与单次：`structured_process`提供完整的多轮探索；其他为单次响应方法
- **⚡ Intelligent Routing**: Single tool interface with method-specific parameter handling and domain-aware processing
  智能路由：具有方法特定参数处理和领域感知处理的单一工具界面
- **🎲 Deterministic Results**: Optional seed parameter for reproducible creative outputs
  确定性结果：可选种子参数用于可重现的创意输出


## 📝 Configuration / 配置

Add to your MCP client configuration:(uv needed)
添加到您的MCP客户端配置：(需要uv)

```json
{
  "mcpServers": {
    "divergent-thinking": {
      "command": "uvx",
      "args": ["divergent-thinking-mcp"],
    }
  }
}
```

## 🎭 Example Usage / 使用示例

### Domain-Aware Creative Intelligence / 领域感知创意智能

The MCP server provides intelligent, context-sensitive creativity with professional-grade outputs tailored to specific domains:
MCP服务器提供智能的、上下文敏感的创造力，具有针对特定领域定制的专业级输出：

**🎯 Transformation Examples:**
- **Before**: "How does 'butterfly' relate to secure systems?" (generic random)
- **After**: "How does 'encryption' relate to secure systems in cybersecurity applications?" (domain-aware)

**💡 Professional Relevance:**
- **AI & Machine Learning**: Uses terms like "neural networks", "deep learning architectures", "model optimization" instead of random words
- **Internet & Web Technologies**: Focuses on "api design", "microservices architecture", "web performance optimization"
- **Computer Science & Systems**: Emphasizes "distributed systems", "cybersecurity architecture", "database optimization"
- **Product Development**: Highlights "digital product strategy", "agile development", "user experience optimization"
- **Engineering & Infrastructure**: Features "devops automation", "scalable architecture", "site reliability engineering"

#### **1. Domain-Aware AI System Development / 领域感知AI系统开发**

```json
{
  "thought": "Create an intelligent code review system",
  "thinking_method": "structured_process",
  "domain": "artificial intelligence systems",
  "target_audience": "software development teams",
  "time_period": "2025-2030",
  "resources": "cloud computing, machine learning models, development APIs",
  "goals": "improve code quality, reduce review time, enhance learning"
}
```

**🎯 Domain-Aware Output Example:**

- **SCAMPER Enhancement**: "How could 'neural network analysis' substitute traditional code review methods in AI system applications?"
- **Analogical Thinking**: "How is your code review system like 'immune system pattern recognition' in biological contexts?"
- **Biomimicry**: "How could your system mimic 'neural plasticity' for adaptive learning from code patterns?"

#### **2. Web Application Architecture Intelligence / 网络应用架构智能**

```json
{
  "thought": "Design a scalable e-commerce platform",
  "thinking_method": "generate_branches",
  "domain": "web application development",
  "target_audience": "small business owners",
  "goals": "high performance, cost-effective, easy maintenance"
}
```

**🌐 Web Development-Aware Outputs:**

- **Domain Terms**: Uses "microservices", "api design", "performance optimization" instead of random words
- **Six Thinking Hats**: "What scalability bottlenecks could this create?" (Black Hat - Critical)
- **Professional Context**: "How could this improve user experience for small business customers?"

#### **3. Context-Aware Product Strategy / 上下文感知产品策略**

```json
{
  "thought": "Develop a collaborative development platform",
  "thinking_method": "creative_constraint",
  "domain": "digital product strategy",
  "constraint": "must work with legacy systems",
  "target_audience": "enterprise development teams",
  "resources": "existing infrastructure, security requirements"
}
```

#### **4. Time-Specific Infrastructure Innovation / 时间特定基础设施创新**

```json
{
  "thought": "Reimagine cloud deployment systems",
  "thinking_method": "perspective_shift",
  "domain": "devops automation systems",
  "time_period": "2030",
  "perspective_type": "impossible_being",
  "goals": "zero-downtime deployments, self-healing infrastructure"
}
```

## 🧠 Domain-Aware Intelligence Features / 领域感知智能特性

### 🎯 Professional-Grade Creative Enhancement

**Qualitative Improvements / 质量改进:**
- **Domain Relevance**: Significant improvement in relevant terms within creative outputs
- **Context Sensitivity**: Enhanced from generic to domain-specific patterns

### 🔧 Enhanced Creativity Methods / 增强的创意方法

**All creativity techniques now feature domain-aware intelligence:**

- **🎨 SCAMPER Method**: Domain-specific prompts using intelligent word selection
  - *Before*: "What if we substitute the main component with something unexpected?"
  - *After*: "What if you replaced key components with 'machine learning algorithms' for AI system applications?"

- **🔗 Analogical Thinking**: Domain-relevant analogies from biological, mathematical, and engineering systems
  - *Before*: Generic nature analogies
  - *After*: "How is your distributed system like 'neural network coordination' in biological contexts?"

- **🌿 Biomimicry**: Nature-inspired solutions tailored to specific domains
  - *Before*: Random nature examples
  - *After*: "How could your microservices architecture mimic 'cellular organization' for specialized functions?"

- **🎭 Six Thinking Hats**: Professional domain-specific perspectives
  - *Before*: Generic emotional/logical prompts
  - *After*: "What scalability bottlenecks could this web application create?" (Black Hat - Critical)

- **💭 Word Association**: Domain-relevant word selection replacing random combinations
  - *Before*: "butterfly" + "cybersecurity"
  - *After*: "api design" + "system integration"

### Available Specialized Domains / 可用专业领域

Choose from 78+ specialized domains focused on AI, Internet, Computer Science, Product, and Engineering:
从78+个专注于AI、互联网、计算机科学、产品和工程的专业领域中选择：

- **AI & Machine Learning**: `artificial intelligence systems`, `machine learning algorithms`, `deep learning architectures`, `natural language processing`, `computer vision systems`, `reinforcement learning`, `generative ai models`
- **Internet & Web Technologies**: `web application development`, `frontend frameworks`, `backend systems architecture`, `api design and development`, `microservices architecture`, `web performance optimization`, `progressive web applications`
- **Computer Science & Systems**: `distributed systems design`, `database systems optimization`, `operating systems development`, `network protocols design`, `cybersecurity architecture`, `cloud computing platforms`, `software architecture patterns`
- **Product Development & Management**: `digital product strategy`, `product lifecycle management`, `user experience optimization`, `product analytics platforms`, `agile product development`, `product market validation`, `feature prioritization systems`
- **Engineering & Infrastructure**: `devops automation systems`, `infrastructure as code`, `continuous integration pipelines`, `container orchestration`, `monitoring and observability`, `scalable system architecture`, `site reliability engineering`
- And many more specialized domains... / 还有更多专业领域...
