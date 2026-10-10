# 视频论文工作流技能收藏（2026-10-10）

按用户提供的视频文字稿中明确点名的 12 个项目整理。各目录是固定上游提交的技能文件收藏，不代表安全审计或自动启用；上游代码、hooks、自动研究循环均未执行。

`sources.json` 提供每个项目的来源、提交、许可证和逐文件 SHA256。原有 `skills/` 下 25 个技能及安装清单未被覆盖，本收藏也不由根目录安装脚本自动安装。

## 使用与恢复

克隆本仓库后，先选择目录中的具体 `SKILL.md`，阅读它及需要的参考文件，再通过 Codex 的技能安装器选择安装。保留同级 references、assets、scripts 和共享依赖；存在同名技能时先比较，不覆盖现有文件。本次项目内另已安装 `exploratory-data-analysis` 与 `statistical-analysis` 两个副本，位于 ECHO 工作区 `research-skills/installed/`，未修改全局技能配置。

## 许可证边界

每个上游保持自己的 LICENSE/NOTICE，不对本收藏统一重许可。`academic-research-skills` 为 CC-BY-NC-4.0：需署名且限非商业用途。Anthropic 仅收藏明确采用 Apache-2.0 的 `frontend-design` 子目录，不复制其专有 Office 技能。`social-science-paper-writing` 未找到明确许可证，故只在索引保存来源，不将源码转载到本仓库；本机有用户请求下载的原始仓库。

技能文件可能需要外部服务、付费 API 或额外依赖。下载不等于已配置这些服务。任何技能的建议均不能替代研究方案、知情同意、人工盲评或隐私规则；本仓库不包含学生名单、答卷、对话、数据库、口令或研究身份映射。
