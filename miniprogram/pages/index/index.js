// pages/index/index.js
const app = getApp()

Page({
  data: {
    currentDate: '',
    todayMenu: [],
    stats: {
      dishCount: 0,
      weekCount: 0,
      purchaseCount: 0,
      completionRate: 0
    },
    recentActivities: []
  },

  onLoad() {
    this.loadData()
  },

  onShow() {
    this.loadData()
  },

  // 加载数据
  loadData() {
    // 设置当前日期
    const now = new Date()
    const dateStr = `${now.getFullYear()}年${now.getMonth() + 1}月${now.getDate()}日`
    this.setData({ currentDate: dateStr })

    // 从本地存储加载数据
    const allDishes = wx.getStorageSync('dishes') || []
    const weekMenus = wx.getStorageSync('weekMenus') || {}
    const purchaseList = wx.getStorageSync('purchaseList') || []

    // 计算统计数据
    const dishCount = allDishes.length
    const weekCount = Object.keys(weekMenus).length
    const purchaseCount = purchaseList.length

    // 计算完成率（假设已完成100个采购项）
    const completedCount = purchaseList.filter(item => item.status === 'completed').length
    const completionRate = purchaseCount > 0 ? Math.round((completedCount / purchaseCount) * 100) : 0

    this.setData({
      stats: {
        dishCount,
        weekCount,
        purchaseCount,
        completionRate
      }
    })

    // 加载今日菜谱
    this.loadTodayMenu()
    
    // 加载最近活动
    this.loadRecentActivities()
  },

  // 加载今日菜谱
  loadTodayMenu() {
    const weekMenus = wx.getStorageSync('weekMenus') || {}
    const days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    const today = days[new Date().getDay()]
    
    // 获取本周的菜谱
    const weekKey = this.getWeekKey()
    const currentWeekMenu = weekMenus[weekKey] || {}
    const todayMenu = currentWeekMenu[today] || []

    if (todayMenu.length > 0) {
      const menuData = []
      
      // 早餐
      const breakfast = todayMenu.filter(d => d.meal === 'breakfast')
      if (breakfast.length > 0) {
        menuData.push({
          meal: '☀️ 早餐',
          dishes: breakfast.map(d => d.name).join('、')
        })
      }

      // 午餐
      const lunch = todayMenu.filter(d => d.meal === 'lunch')
      if (lunch.length > 0) {
        menuData.push({
          meal: '🍱 午餐',
          dishes: lunch.map(d => d.name).join('、')
        })
      }

      // 晚餐
      const dinner = todayMenu.filter(d => d.meal === 'dinner')
      if (dinner.length > 0) {
        menuData.push({
          meal: '🌙 晚餐',
          dishes: dinner.map(d => d.name).join('、')
        })
      }

      this.setData({ todayMenu: menuData })
    } else {
      this.setData({ todayMenu: [] })
    }
  },

  // 获取本周的key
  getWeekKey() {
    const now = new Date()
    const year = now.getFullYear()
    const week = this.getWeekNumber(now)
    return `${year}-W${week.toString().padStart(2, '0')}`
  },

  // 获取第几周
  getWeekNumber(date) {
    const firstDayOfYear = new Date(date.getFullYear(), 0, 1)
    const pastDaysOfYear = (date - firstDayOfYear) / 86400000
    return Math.ceil((pastDaysOfYear + firstDayOfYear.getDay() + 1) / 7)
  },

  // 加载最近活动
  loadRecentActivities() {
    const activities = wx.getStorageSync('activities') || []
    this.setData({
      recentActivities: activities.slice(0, 5)
    })
  },

  // 页面跳转
  goToPage(e) {
    const page = e.currentTarget.dataset.page
    const pageMap = {
      'menu': '/pages/menu/menu',
      'dishes': '/pages/dishes/dishes',
      'purchase': '/pages/purchase/purchase',
      'stats': '/pages/stats/stats',
      'me': '/pages/me/me'
    }
    
    if (pageMap[page]) {
      wx.switchTab({
        url: pageMap[page]
      })
    }
  }
})
