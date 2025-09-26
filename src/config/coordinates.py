#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
坐标参数配置文件
用于集中管理所有UI自动化测试中使用的坐标参数
"""

# 五子棋应用相关坐标
# 棋力评测按钮坐标
click_position_PVE = (0.536, 0.342)

# 可以在这里添加更多坐标参数
# 例如：
# 开始游戏按钮坐标
# click_position_start_game = (0.5, 0.6)

# 返回按钮坐标
# click_position_back = (0.1, 0.1)

# 确认按钮坐标
# click_position_confirm = (0.75, 0.7)

# 取消按钮坐标
# click_position_cancel = (0.25, 0.7)

# 启动隐私弹窗resourceId合集
sdk_privacy_title = "com.duole.wuziqihd:id/dl_sdk_privacy_title" # 启动隐私弹窗标题resourceId
sdk_privacy_disagree = "com.duole.wuziqihd:id/dl_sdk_privacy_disagree" # 启动隐私弹窗拒绝按钮resourceId
sdk_privacy_agree = "com.duole.wuziqihd:id/dl_sdk_privacy_agree" # 启动隐私弹窗同意按钮resourceId
# 登录大厅按钮resourceId合集
common_login_button = "com.duole.wuziqihd:id/dl_sdk_acc_common_login" # 登录大厅按钮resourceId
wechat_login_button = "com.duole.wuziqihd:id/dl_sdk_acc_wechat_login" # 微信登录按钮resourceId
login_service_button = "com.duole.wuziqihd:id/dl_sdk_acc_login_service" # 人工客服按钮resourceId
login_upload_button = "com.duole.wuziqihd:id/dl_sdk_acc_login_upload_log" # 上传日志按钮resourceId
login_age_button = "com.duole.wuziqihd:id/dl_sdk_acc_login_suitable_age" # 适龄提醒按钮resourceId