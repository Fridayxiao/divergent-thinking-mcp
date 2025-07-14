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
- **🔍 Multi-word Domain Precision**: 78+ specific domains like "mobile app development", "healthcare technology", "sustainable agriculture"
  多词领域精度：78+个特定领域，如"移动应用开发"、"医疗技术"、"可持续农业"
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
- **AI Domain**: Uses terms like "neural networks", "machine learning", "optimization" instead of random words
- **Healthcare**: Focuses on "patient safety", "clinical evidence", "regulatory compliance"
- **Business**: Emphasizes "market positioning", "competitive advantage", "ROI optimization"

#### **1. Domain-Aware Educational Technology Innovation / 领域感知教育技术创新**

```json
{
  "thought": "Create an innovative learning platform",
  "thinking_method": "structured_process",
  "domain": "educational technology",
  "target_audience": "remote students",
  "time_period": "2025-2030",
  "resources": "cloud computing, mobile devices, limited budget",
  "goals": "improve engagement, reduce costs, increase accessibility"
}
```

**🎯 Domain-Aware Output Example:**
- **SCAMPER Enhancement**: "How could 'adaptive learning' substitute traditional methods in educational technology applications?"
- **Analogical Thinking**: "How is your learning platform like 'cognitive science learning theories' in educational contexts?"
- **Biomimicry**: "How could your platform mimic 'neural plasticity' for personalized learning adaptation?"

#### **2. Cybersecurity Domain Intelligence / 网络安全领域智能**

```json
{
  "thought": "Design a smart home security system",
  "thinking_method": "generate_branches",
  "domain": "cybersecurity",
  "target_audience": "elderly users",
  "goals": "ease of use, reliability, affordability"
}
```

**🔒 Cybersecurity-Aware Outputs:**
- **Domain Terms**: Uses "authentication", "encryption", "threat detection" instead of random words
- **Six Thinking Hats**: "What threat vectors does this address?" (White Hat - Facts)
- **Professional Context**: "How could this improve overall security posture for elderly users?"

#### **3. Context-Aware Constraints / 上下文感知约束**

```json
{
  "thought": "Develop a food delivery service",
  "thinking_method": "creative_constraint",
  "domain": "e-commerce",
  "constraint": "must work without smartphones",
  "target_audience": "rural communities",
  "resources": "limited internet, local partnerships"
}
```

#### **4. Time-Specific Innovation / 时间特定创新**

```json
{
  "thought": "Reimagine public transportation",
  "thinking_method": "perspective_shift",
  "domain": "urban transportation",
  "time_period": "2050",
  "perspective_type": "impossible_being",
  "goals": "zero emissions, universal accessibility"
}
```

## 🧠 Domain-Aware Intelligence Features / 领域感知智能特性

### 🎯 Professional-Grade Creative Enhancement

**Quantitative Improvements / 量化改进:**
- **Domain Relevance**: 30% → 90%+ (relevant terms in creative outputs)
- **Context Sensitivity**: Generic → Domain-specific patterns

### 🔧 Enhanced Creativity Methods / 增强的创意方法

**All creativity techniques now feature domain-aware intelligence:**

- **🎨 SCAMPER Method**: Domain-specific prompts using intelligent word selection
  - *Before*: "What if we substitute the main component with something unexpected?"
  - *After*: "What if you replaced key components with 'neural networks' for AI applications?"

- **🔗 Analogical Thinking**: Domain-relevant analogies from biological, mathematical, and engineering systems
  - *Before*: Generic nature analogies
  - *After*: "How is your AI system like 'immune system pattern recognition' in biological contexts?"

- **🌿 Biomimicry**: Nature-inspired solutions tailored to specific domains
  - *Before*: Random nature examples
  - *After*: "How could your renewable energy system mimic 'photosynthesis energy conversion'?"

- **🎭 Six Thinking Hats**: Professional domain-specific perspectives
  - *Before*: Generic emotional/logical prompts
  - *After*: "What clinical evidence supports this healthcare technology approach?" (White Hat)

- **💭 Word Association**: Domain-relevant word selection replacing random combinations
  - *Before*: "butterfly" + "cybersecurity"
  - *After*: "encryption" + "network security"

### Available Domains / 可用领域

Choose from 78+ specific multi-word domains:
从78+个特定的多词领域中选择：

- **Design & UX**: `product design`, `user interface design`, `user experience design`
- **Technology**: `software development`, `mobile app development`, `artificial intelligence`, `cybersecurity`
- **Business**: `business strategy`, `digital marketing`, `e-commerce`, `startup ventures`
- **Healthcare**: `medical devices`, `healthcare technology`, `telemedicine`, `patient care`
- **Education**: `educational technology`, `online learning`, `curriculum development`
- **Environment**: `renewable energy`, `sustainable agriculture`, `green technology`
- **Transportation**: `urban transportation`, `electric vehicles`, `autonomous vehicles`
- And many more... / 还有更多...
