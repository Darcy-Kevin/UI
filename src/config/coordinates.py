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
class SDKPrivacyConfig:
    """启动隐私弹窗配置类，集中管理所有启动隐私弹窗相关的resourceId"""
    @staticmethod
    def get_sdk_privacy_title():
        """获取启动隐私弹窗标题resourceId"""
        return "com.duole.wuziqihd:id/dl_sdk_privacy_title" # 启动隐私弹窗标题resourceId
    @staticmethod
    def get_sdk_privacy_disagree():
        """获取启动隐私弹窗拒绝按钮resourceId"""
        return "com.duole.wuziqihd:id/dl_sdk_privacy_disagree" # 启动隐私弹窗拒绝按钮resourceId
    @staticmethod
    def get_sdk_privacy_agree():
        """获取启动隐私弹窗同意按钮resourceId"""
        return "com.duole.wuziqihd:id/dl_sdk_privacy_agree" # 启动隐私弹窗同意按钮resourceId

# 登录大厅按钮resourceId合集
class LoginButtonConfig:
    """登录大厅按钮配置类，集中管理所有登录相关按钮的resourceId"""
    
    @staticmethod
    def get_common_login_button():
        """获取普通登录按钮resourceId"""
        return "com.duole.wuziqihd:id/dl_sdk_acc_common_login"
    
    @staticmethod
    def get_wechat_login_button():
        """获取微信登录按钮resourceId"""
        return "com.duole.wuziqihd:id/dl_sdk_acc_wechat_login"
    
    @staticmethod
    def get_service_button():
        """获取人工客服按钮resourceId"""
        return "com.duole.wuziqihd:id/dl_sdk_acc_login_service"
    
    @staticmethod
    def get_upload_log_button():
        """获取上传日志按钮resourceId"""
        return "com.duole.wuziqihd:id/dl_sdk_acc_login_upload_log"
    
    @staticmethod
    def get_suitable_age_button():
        """获取适龄提醒按钮resourceId"""
        return "com.duole.wuziqihd:id/dl_sdk_acc_login_suitable_age"
    
    @staticmethod
    def get_privacy_checkbox():
        """获取登录隐私弹窗勾选框resourceId"""
        return "com.duole.wuziqihd:id/dl_sdk_acc_login_privacy_checkbox"
    
    @staticmethod
    def get_all_resource_ids():
        """获取所有登录相关按钮的resourceId字典"""
        return {
            'common_login': LoginButtonConfig.get_common_login_button(),
            'wechat_login': LoginButtonConfig.get_wechat_login_button(),
            'service_button': LoginButtonConfig.get_service_button(),
            'upload_log': LoginButtonConfig.get_upload_log_button(),
            'suitable_age': LoginButtonConfig.get_suitable_age_button(),
            'privacy_checkbox': LoginButtonConfig.get_privacy_checkbox()
        }

# 为了向后兼容，保留原有的常量定义
common_login_button = LoginButtonConfig.get_common_login_button()
wechat_login_button = LoginButtonConfig.get_wechat_login_button()
login_service_button = LoginButtonConfig.get_service_button()
login_upload_button = LoginButtonConfig.get_upload_log_button()
login_age_button = LoginButtonConfig.get_suitable_age_button()
login_privacy_checkbox = LoginButtonConfig.get_privacy_checkbox()
