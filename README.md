# Divergent Thinking MCP Server / 发散思维MCP服务器

An MCP (Model Context Protocol) server that promotes divergent and creative thinking patterns for creation - the Supplement of sequential logical thinking.
一个MCP（模型上下文协议）服务器，促进创造性思维模式，是顺序逻辑思维的补充。

## 🎨 Philosophy / 设计理念

While other thinking follows logical progressions, this MCP server embraces divergent
传统思维遵循逻辑进展，而此MCP服务器拥抱发散思维

## 🛠️ Tools / 工具

### Unified Divergent Thinking Tool / 统一发散思维工具

This MCP server provides a **single comprehensive tool** that offers 6 powerful creativity methods through one unified interface, eliminating confusion and cognitive overload.
此MCP服务器提供**单一综合工具**，通过统一界面提供6种强大的创意方法，消除混乱和认知负担。

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

- **Multi-turn vs Single-shot**: `structured_process` provides complete multi-turn exploration; others are single-response methods
  多轮与单次：`structured_process`提供完整的多轮探索；其他为单次响应方法
- **Advanced Techniques**: Optional SCAMPER, Six Thinking Hats, morphological analysis integration
  高级技术：可选的SCAMPER、六顶思考帽、形态分析集成
- **Intelligent Routing**: Single tool interface with method-specific parameter handling
  智能路由：具有方法特定参数处理的单一工具界面
- **Deterministic Results**: Optional seed parameter for reproducible creative outputs
  确定性结果：可选种子参数用于可重现的创意输出

## 🚀 Installation & Usage / 安装与使用

### Installation

```bash
# 1. using uv
uv tool install divergent-thinking-mcp --index https://pypi.org/simple

# 2. Clone the project
# 克隆或创建项目
git clone https://github.com/Fridayxiao/divergent-thinking-mcp.git
cd divergent-thinking-mcp
# install  with uv
uv tool install .

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
    }
  }
}
```

## 🎭 Example Usage / 使用示例

### Examples / 示例

<!-- Usage examples will be added here -->
<!-- 使用示例将在此处添加 -->

**Coming Soon / 即将推出:**

- Complete usage examples for all 6 thinking methods
  所有6种思维方法的完整使用示例
- Step-by-step tutorials for complex creative challenges
  复杂创意挑战的分步教程
- Integration examples with popular MCP clients
  与流行MCP客户端的集成示例

**Placeholder for detailed examples:**

```text
[Examples will be updated to reflect the new unified tool structure]
[示例将更新以反映新的统一工具结构]
```
