# Divergent Thinking MCP Server / 发散思维MCP服务器

An MCP (Model Context Protocol) server that promotes divergent and creative thinking patterns for creation - the opposite of sequential logical thinking.
一个MCP（模型上下文协议）服务器，促进创造性思维模式，是顺序逻辑思维的对立面。

## 🎨 Philosophy / 设计理念

While traditional thinking follows logical progressions, this MCP server embraces divergent
传统思维遵循逻辑进展，而此MCP服务器拥抱发散思维

## 🛠️ Tools / 工具

### Core Divergent Thinking Tools / 核心发散思维工具
- **`divergent_thinking`** - A comprehensive tool for generating creative thoughts and branches through structured divergent thinking processes. Supports linear progression and branching exploration with various thinking techniques.
- **`divergent_thinking`** - 一个全面的工具，通过结构化的发散思维过程生成创造性想法和分支。支持线性进展和使用各种思维技巧的分支探索。
- **`generate_branches`** - Generate multiple distinct creative branches from a single thought, exploring completely different directions.
- **`generate_branches`** - 从单一想法生成多个不同的创意分支，探索完全不同的方向。
- **`perspective_shift`** - Shift perspective on a thought to generate new insights by viewing concepts from impossible or unusual viewpoints.
- **`perspective_shift`** - 转变对想法的视角，通过从不可能或不寻常的角度查看概念来生成新见解。
- **`creative_constraint`** - Apply creative constraints to transform thoughts by introducing limitations or impossible elements.
- **`creative_constraint`** - 应用创造性约束，通过引入限制或不可能的元素来转变想法。
- **`combine_thoughts`** - Combine two divergent thoughts into something entirely new that incorporates elements from both.
- **`combine_thoughts`** - 将两个发散的想法合并为全新的事物，融合两者的元素。

## 🚀 Installation & Usage / 安装与使用

### Using uv (Recommended) / 使用uv（推荐）

```bash
# Clone or create the project
# 克隆或创建项目
git clone <your-repo> divergent-thinking-mcp
cd divergent-thinking-mcp

# Run directly with uv
# 使用uv直接运行
uv run divergent-thinking-mcp

# Or run the script
# 或运行脚本
uv run scripts/run_server.py
```


## 📝 Configuration / 配置

Add to your MCP client configuration:
添加到您的MCP客户端配置：

```json
{
  "mcpServers": {
    "divergent-thinking": {
      "command": "uv",
      "args": ["run", "divergent-thinking-mcp"],
      "cwd": "/path/to/divergent-thinking-mcp"
    }
  }
}
```

## 🎭 Example Usage / 使用示例

### English Examples

```python
# Generate creative branches from a core idea
generate_branches(
    thought="Design an innovative electric fan"
)

# Shift perspective to gain new insights
perspective_shift(
    thought="Design an intelligent office chair",
    perspective_type="inanimate_object"
)

# Apply creative constraints
creative_constraint(
    thought="Design an eco-friendly water bottle",
    constraint="Use edible materials"
)

# Combine two divergent thoughts
combine_thoughts(
    thought1="Ergonomic lumbar support design for intelligent office chairs",
    thought2="Office chair integrated with AI voice assistant control system"
)

# Comprehensive divergent thinking process
result = divergent_thinking(
    thought="Design an environmentally friendly smart water cup",
    thoughtNumber=1,
    totalThoughts=3,
    nextThoughtNeeded=True,
    generate_branches=True,
    prompt_type="branch_generation"
)
```

### 中文示例

```python
# 从核心想法生成创意分支
generate_branches(
    thought="设计一款新颖的电风扇"
)

# 转变视角以获得新见解
perspective_shift(
    thought="设计一款智能办公椅",
    perspective_type="inanimate_object"
)

# 应用创造性约束
creative_constraint(
    thought="设计一款环保水瓶",
    constraint="使用可食用材料"
)

# 合并两个发散的想法
combine_thoughts(
    thought1="智能办公椅的人体工学腰椎支撑设计",
    thought2="办公椅集成AI语音助手控制系统"
)

# 全面的发散思维过程
result = divergent_thinking(
    thought="设计一款环保型智能水杯",
    thoughtNumber=1,
    totalThoughts=3,
    nextThoughtNeeded=True,
    generate_branches=True,
    prompt_type="branch_generation"
)
```
