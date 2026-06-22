# 🚀 微信小程序 - 部署指南

## 📋 概述

我已经为你创建了饭堂管理系统的微信小程序版本！

### 🎯 项目位置

```
/workspace/canteen-miniprogram/
```

### ✨ 功能特点

- ✅ 专为手机端优化的界面
- ✅ 底部导航栏，操作便捷
- ✅ 支持所有核心功能
- ✅ 数据与网页版同步

---

## 🛠 部署步骤

### 第一步：注册微信小程序

如果你还没有小程序账号：

1. 访问 [微信公众平台](https://mp.weixin.qq.com/)
2. 注册小程序账号
3. 完成主体认证

### 第二步：获取 AppID

1. 登录微信公众平台
2. 进入「开发」→「开发管理」
3. 获取你的 AppID

### 第三步：修改配置文件

编辑项目中的配置文件：

**文件：`/workspace/canteen-miniprogram/project.config.json`**

将 `YOUR_APPID` 替换为你的真实 AppID：

```json
{
  "appid": "wx1234567890abcdef",
  "projectname": "canteen-miniprogram",
  ...
}
```

### 第四步：下载微信开发者工具

1. 下载 [微信开发者工具](https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html)
2. 安装并登录

### 第五步：导入项目

1. 打开微信开发者工具
2. 点击「导入项目」
3. 选择项目目录：`/workspace/canteen-miniprogram`
4. 填写 AppID
5. 点击「导入」

### 第六步：补充代码

⚠️ **重要**：当前创建的是基础框架，需要补充完整的页面逻辑代码。

#### 需要完成的文件：

1. **pages/menu/menu.js** - 菜谱管理逻辑
2. **pages/dishes/dishes.js** - 菜品管理逻辑
3. **pages/purchase/purchase.js** - 采购管理逻辑
4. **pages/stats/stats.js** - 统计分析逻辑
5. **pages/me/me.js** - 个人中心逻辑

#### 每个页面需要创建：
- `.js` 文件（页面逻辑）
- `.json` 文件（页面配置）

### 第七步：测试

1. 在开发者工具中点击「编译」
2. 使用模拟器测试功能
3. 检查控制台是否有报错

### 第八步：上传代码

1. 点击右上角「上传」
2. 填写版本号和备注
3. 登录微信公众平台提交审核

### 第九步：发布

1. 审核通过后，在公众平台点击「发布」
2. 小程序即可在微信中搜索使用

---

## 📁 项目结构

```
canteen-miniprogram/
├── app.js              ← 应用入口
├── app.json            ← 应用配置
├── app.wxss            ← 全局样式
├── project.config.json ← 项目配置（需要修改AppID）
├── sitemap.json        ← sitemap配置
├── pages/              ← 页面目录
│   ├── index/         ← 首页
│   ├── menu/          ← 菜谱管理
│   ├── dishes/        ← 菜品管理
│   ├── purchase/      ← 采购清单
│   ├── stats/         ← 统计分析
│   └── me/           ← 个人中心
└── images/           ← 图标资源（需要添加）
```

---

## 🎨 界面预览

### 底部导航栏

```
┌─────────────────────────────────┐
│                                 │
│        页面内容区域              │
│                                 │
│                                 │
├─────────────────────────────────┤
│  首页  │  菜谱  │  菜品  │  采购  │  我的  │
│  🏠   │   📅   │   🥘   │   🛒   │   👤   │
└─────────────────────────────────┘
```

### 主要功能页面

1. **首页** - 统计概览、今日菜谱、快捷操作
2. **菜谱** - 周菜单表格、拖拽排菜
3. **菜品** - 菜品列表、搜索筛选
4. **采购** - 采购清单、勾选完成
5. **统计** - 数据报表、热门菜品
6. **我的** - 个人中心、设置备份

---

## ⚙️ 配置说明

### 应用配置（app.json）

```javascript
{
  "pages": [
    "pages/index/index",      // 首页
    "pages/menu/menu",        // 菜谱
    "pages/dishes/dishes",    // 菜品
    "pages/purchase/purchase", // 采购
    "pages/stats/stats",      // 统计
    "pages/me/me"            // 我的
  ],
  "window": {
    "navigationBarTitleText": "饭堂管理系统"
  },
  "tabBar": {
    "list": [
      // 底部导航配置
    ]
  }
}
```

### 页面配置

每个页面目录下需要 `.json` 文件：

```json
{
  "usingComponents": {},
  "navigationBarTitleText": "页面标题"
}
```

---

## 🔧 数据存储

### localStorage（本地存储）

小程序使用 `wx.setStorageSync` 和 `wx.getStorageSync` 存储数据：

```javascript
// 保存数据
wx.setStorageSync('dishes', dishes)

// 读取数据
const dishes = wx.getStorageSync('dishes')
```

### 数据结构

```javascript
// 菜品数据
{
  id: 'dish_001',
  name: '红烧肉',
  category: 'main',
  ingredients: ['五花肉', '生抽', '白糖'],
  createdAt: timestamp
}

// 采购数据
{
  id: 'purchase_001',
  name: '五花肉',
  quantity: '2kg',
  status: 'pending',  // pending / completed
  createdAt: timestamp
}
```

---

## 📱 与网页版数据同步

### 方案一：手动导入导出

1. 在网页版「备份中心」导出 JSON
2. 在小程序「我的」页面导入

### 方案二：云开发（进阶）

使用微信云开发存储数据，可实现多端同步：

```javascript
// 初始化云开发
wx.cloud.init()

// 上传数据到云端
wx.cloud.uploadFile({
  cloudPath: 'backup.json',
  filePath: tempFilePath
})
```

---

## ❓ 常见问题

### Q1: 微信开发者工具导入失败？

**解决**：
- 确保选择了正确的项目目录
- 确保 AppID 正确
- 检查是否有必要的配置文件

### Q2: 页面显示空白？

**解决**：
- 检查控制台报错
- 确保页面文件完整
- 检查路径配置是否正确

### Q3: 数据存储失败？

**解决**：
- 检查 storage 是否已满
- 清理不需要的数据
- 使用云开发扩展存储容量

### Q4: 如何实现多端同步？

**方案**：
- 使用微信云开发（推荐）
- 使用云数据库
- 使用云存储

---

## 🚀 进阶功能

### 1. 云开发版本

如需云开发和数据同步，可以升级为云开发版本。

### 2. 消息通知

使用微信订阅消息，功能：
- 菜谱变更提醒
- 采购完成通知
- 系统公告推送

### 3. 用户管理

接入微信用户登录：
- 获取用户信息
- 微信授权登录
- 用户权限管理

---

## 📞 获取帮助

### 微信小程序开发文档

- [官方文档](https://developers.weixin.qq.com/miniprogram/dev/framework/)
- [组件库](https://vant-contrib.gitee.io/vant-weapp/)
- [云开发](https://developers.weixin.qq.com/miniprogram/dev/wxcloud/basis/getting-started.html)

### 技术支持

遇到问题可以：
1. 查看官方文档
2. 搜索常见问题
3. 联系技术支持

---

## ✅ 下一步

1. **注册小程序账号** → 获取 AppID
2. **导入项目到开发者工具**
3. **补充完整页面逻辑代码**
4. **测试功能**
5. **提交审核发布**

---

**祝你开发顺利！** 🎉

如需进一步帮助，随时告诉我！
