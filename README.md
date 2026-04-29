# 高州食堂菜谱管理系统

> 🍚 基于浏览器本地存储的食堂菜谱管理 Web 应用

## 功能特点

- 📅 **本周菜谱**：拖拽排菜、随机生成、确认流程
- 📦 **菜品管理**：193道高州特色菜品，支持自定义添加
- 🛒 **采购清单**：按天/按周汇总，自动计算食材
- 📊 **统计分析**：上菜次数、分类占比、重复检测
- ⭐ **高州推荐**：68道高州特色菜式一键导入

## 快速开始

### 方法一：直接打开
下载 `canteen-menu.html` 直接在浏览器打开即可使用。

### 方法二：GitHub Pages
```bash
# 克隆项目
git clone https://github.com/[你的用户名]/canteen-menu.git
cd canteen-menu
# 用浏览器打开 index.html
```

### 方法三：本地服务
```bash
# 用 Python 启动本地服务器
python3 -m http.server 8080
# 访问 http://localhost:8080
```

## 数据存储

- 主要数据：浏览器 localStorage
- 备份导出：JSON 文件（点击顶栏「💾 保存」）

## 技术栈

- 纯 HTML + CSS + JavaScript（无框架依赖）
- 响应式布局，支持移动端

## 部署到 GitHub Pages

1. 创建新仓库：`canteen-menu`
2. 推送代码：`git push origin main`
3. 设置 Pages：Settings → Pages → main branch
4. 访问：`https://[你的用户名].github.io/canteen-menu`

## 目录结构

```
canteen-menu/
├── README.md              # 本说明文件
├── .gitignore           # Git 忽略配置
├── index.html           # 入口文件（复制自 canteen-menu.html）
├── canteen-menu.html    # 主应用文件
└── 广东茂名高州家常菜式大全.md  # 菜谱数据
```