// app.js
App({
  onLaunch() {
    // 初始化云开发
    if (!wx.cloud) {
      console.error('请使用 2.2.3 或以上的基础库以使用云能力')
    } else {
      wx.cloud.init({
        traceUser: true,
      })
    }
    
    // 检查登录状态
    this.checkLoginStatus()
  },
  
  globalData: {
    userInfo: null,
    isLoggedIn: false,
    userRole: null
  },
  
  // 检查登录状态
  checkLoginStatus() {
    const userInfo = wx.getStorageSync('userInfo')
    if (userInfo) {
      this.globalData.userInfo = userInfo
      this.globalData.isLoggedIn = true
      this.globalData.userRole = userInfo.role
    }
  },
  
  // 登录
  login(userInfo) {
    this.globalData.userInfo = userInfo
    this.globalData.isLoggedIn = true
    this.globalData.userRole = userInfo.role
    wx.setStorageSync('userInfo', userInfo)
  },
  
  // 登出
  logout() {
    this.globalData.userInfo = null
    this.globalData.isLoggedIn = false
    this.globalData.userRole = null
    wx.removeStorageSync('userInfo')
  },
  
  // 检查权限
  checkPermission(requiredRole) {
    const roleHierarchy = {
      'super_admin': 4,
      'admin': 3,
      'manager': 2,
      'staff': 1
    }
    
    const userLevel = roleHierarchy[this.globalData.userRole] || 0
    const requiredLevel = roleHierarchy[requiredRole] || 0
    
    return userLevel >= requiredLevel
  }
})
