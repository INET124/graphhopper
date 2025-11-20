# GraphHopper CI 突变测试 - 快速开始指南

## 已实现的功能

本项目现在包含：

1. **突变测试**：在每次提交到 main/master 分支后自动运行 PITest
2. **质量门禁**：如果突变分数降低，CI 构建失败
3. **失败时的 Rickroll**：当测试或突变分数失败时显示幽默的 Rickroll 消息

## 需求完成情况

### 需求一：CI 中的突变测试 ✅

- **内容**：每次提交后自动运行 PITest 突变测试
- **时机**：在 main/master 分支构建成功后
- **实现**：在 `pom.xml` 和 `.github/workflows/build.yml` 中配置

### 需求二：分数降低时 CI 失败 ✅

- **内容**：如果突变分数低于上一次运行，构建失败
- **实现**：Python 脚本比较当前和历史分数
- **存储**：分数记录在 `.github/mutation_score.txt` 中

### 需求三：测试失败时的 Rickroll ✅

- **内容**：测试失败时显示 Rickroll 消息
- **时机**：任何测试失败或突变分数降低
- **实现**：自定义 GitHub Action，位于 `.github/actions/rickroll/`

## 修改的文件

### 核心配置

- **`pom.xml`**：添加了 PITest Maven 插件（297-323 行）
- **`.github/workflows/build.yml`**：增强的 CI 包含突变测试和 Rickroll

### 新创建的文件

- **`.github/scripts/check_mutation_score.py`**：比较突变分数
- **`.github/actions/rickroll/action.yml`**：自定义 Rickroll action
- **`.github/mutation_score.txt`**：跟踪历史突变分数

## 快速测试

### 查看 CI 结果

1. 访问：https://github.com/INET124/graphhopper/actions
2. 点击任意 workflow 运行
3. 查看日志以了解：
   - 构建和测试结果
   - Rickroll 消息（如果测试失败）
   - 突变测试结果（在 main/master 分支）

### 本地运行突变测试

```bash
cd /home/ubt/CodeSpace/HomeWork/graphhopper
export JAVA_HOME=~/.sdkman/candidates/java/17.0.17-tem
mvn clean install -DskipTests
mvn org.pitest:pitest-maven:mutationCoverage -pl core
```

查看报告：`core/target/pit-reports/index.html`

### 手动触发 CI

```bash
cd /home/ubt/CodeSpace/HomeWork/graphhopper
echo "# Test" >> test.txt
git add test.txt
git commit -m "Test CI trigger"
git push
```

然后检查：https://github.com/INET124/graphhopper/actions

## 工作原理

### 1. 每次推送到 main/master 时

```
推送 → 构建任务 → 测试 → 突变测试任务 → 分数检查
                   ↓                         ↓
                (如失败)                  (如降低)
                   ↓                         ↓
                Rickroll                   Rickroll
                   ↓                         ↓
                CI 失败                    CI 失败
```

### 2. 突变测试流程

1. PITest 在代码中生成突变
2. 对突变的代码运行测试
3. 计算突变分数（被杀死的突变百分比）
4. Python 脚本与之前的分数比较
5. 如果降低 → Rickroll + 构建失败
6. 如果相同/提高 → 提交新分数

### 3. Rickroll 机制

触发时，CI 日志显示：
```
==========================================
   TESTS FAILED - YOU JUST GOT RICKROLLED!
==========================================
   
   https://www.youtube.com/watch?v=dQw4w9WgXcQ
   
   Your tests have failed, and so has your day.
   Better luck next time!
   
==========================================
```

## 设计决策

### 为什么选择 PITest？

- Java 突变测试的行业标准
- 优秀的 JUnit 5 集成
- 快速的增量分析
- 全面的突变操作符

### 为什么用 Python 检查分数？

- 简单的 XML 解析
- 易于维护
- GitHub Actions 默认可用
- 无需额外依赖

### 为什么自定义 Rickroll Action？

- 完全控制输出格式
- 可在多个 workflow 步骤中重用
- 展示 GitHub Actions 最佳实践
- 可以轻松修改或扩展

### 为什么只在 main/master 运行突变测试？

- 突变测试耗时较长（10-30 分钟）
- 节省 CI 资源
- 将质量检查聚焦在主分支
- Pull request 仍会进行常规测试

## 故障排查

### CI 没有运行？

1. 检查 Actions 是否启用：仓库设置 → Actions
2. 确保选择了 "Allow all actions"
3. 验证 workflows 具有 "Read and write permissions"

### 测试失败？

这是预期的！当前的 GraphHopper 测试有一些失败，这会正确触发 Rickroll。修复方法：
- 查看测试日志
- 修复失败的测试
- 推送更改
- CI 应该通过

### 突变测试没有运行？

- 只在 main/master 分支运行
- 需要先成功构建
- 检查是否生成了 `core/target/pit-reports/`

### 分数比较失败？

- 第一次运行建立基线（分数 = 0）
- 后续运行与基线比较
- 检查 `.github/mutation_score.txt` 是否存在

## 下一步

### 查看运行情况

1. **查看当前运行**：https://github.com/INET124/graphhopper/actions
2. **查看 Rickroll**：点击失败的运行查看消息
3. **下载报告**：突变测试完成后点击 "pit-reports" artifact

### 提高质量

1. 修复失败的测试以使构建通过
2. 编写更多测试以提高突变分数
3. 查看 PITest HTML 报告了解未捕获的突变
4. 为存活的突变添加针对性测试

### 自定义配置

- **调整突变范围**：编辑 `pom.xml` 中的 targetClasses
- **更改 Rickroll 消息**：编辑 `.github/actions/rickroll/action.yml`
- **修改分数检查**：编辑 `.github/scripts/check_mutation_score.py`
- **添加更多检查**：扩展 `.github/workflows/build.yml`

## 文档

详细实现信息请参阅 `IMPLEMENTATION.md`

## 支持

- PITest 文档：https://pitest.org
- GitHub Actions 文档：https://docs.github.com/en/actions
- GraphHopper 文档：https://www.graphhopper.com

---

**实现日期**：2025年11月  
**状态**：✅ 所有需求均已完成并测试
