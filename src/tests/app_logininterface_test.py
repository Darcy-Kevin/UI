# -*- coding: utf-8 -*-
"""五子棋应用登录界面测试脚本
此脚本用于自动连接设备、启动五子棋应用、处理隐私弹窗并验证登录页面。
"""

import resource
import uiautomator2 as u2
import time
import pytest
import allure
# 导入工具函数
from src.utils.screenshot_utils import attach_screenshot_to_allure
from src.utils.time_utils import get_current_time_str
# 导入配置
from src.config.coordinates import LoginButtonConfig, SDKPrivacyConfig  # 导入登录按钮和SDK隐私配置

class TestWZQLoginInterfaceShow:
    """五子棋应用登录界面元素展示测试类"""
    
    @pytest.fixture(scope="class")
    def driver(self):
        """连接到Android设备并返回驱动实例的fixture"""
        driver = u2.connect()  # 连接手机，若电脑只连接了一部手机，则不需要设备信息
        print("设备连接成功!")
        print("设备信息:")
        print(driver.info)  # 打印设备信息
        yield driver

        # 测试结束后清理资源
        # driver.app_stop("com.duole.chinachess")
        # print("测试结束，已关闭应用")
        
    @allure.feature("登录界面元素展示")
    @allure.story("启动应用并验证登录页面")
    def test_launch_app_and_verify_login_page(self, driver):
        """测试启动应用、处理隐私弹窗并验证登录页面"""
        with allure.step(f"[{get_current_time_str()}] 清理后台应用并启动指定包名的应用"):
            # 启动应用前先清理后台，确保应用是最新状态
            driver.app_stop("com.duole.wuziqihd")
            # 启动指定包名的应用
            driver.app_start("com.duole.wuziqihd")
            
        with allure.step(f"[{get_current_time_str()}] 处理隐私弹窗"):
            try:
                # 尝试查找隐私弹窗（使用resourceId）
                sdk_privacy_title = SDKPrivacyConfig.get_sdk_privacy_title()
                if driver(resourceId=sdk_privacy_title).wait(timeout=10.0):
                    print("发现隐私弹窗，点击同意按钮")
                    driver(text="同意").click()
                    allure.attach(f"[{get_current_time_str()}] 已处理隐私弹窗", "操作结果")
                    # 截图保存操作结果
                    attach_screenshot_to_allure(driver, "privacy_popup_agree", f"[{get_current_time_str()}] 点击同意按钮后的界面")
                else:
                    print("没有发现隐私弹窗")
                    allure.attach(f"[{get_current_time_str()}] 未发现隐私弹窗", "操作结果")
            except Exception as e:
                print(f"处理隐私弹窗时发生错误: {e}")
                allure.attach(f"[{get_current_time_str()}] {str(e)}", "错误信息", allure.attachment_type.TEXT)
                # 截图保存错误状态
                attach_screenshot_to_allure(driver, "privacy_popup_error", f"[{get_current_time_str()}] 处理隐私弹窗错误时的界面")
            
        with allure.step(f"[{get_current_time_str()}] 验证登录页面是否包含'通行证登录'文案"):
            try:
                # 等待登录页面加载
                time.sleep(5)  # 增加等待时间确保页面完全加载
                # 截图保存登录页面状态
                attach_screenshot_to_allure(driver, "login_page", f"[{get_current_time_str()}] 登录页面加载完成")
                
                # 直接查找"通行证登录"文本，与同意按钮保持一致的查找方式
                # if driver(text="通行证登录").wait(timeout=5.0):
                common_login_button = LoginButtonConfig.get_common_login_button()
                if driver(resourceId=common_login_button).wait(timeout=5.0):
                    print("登录页面验证成功，找到了'通行证登录'按钮")
                    assert True
                    allure.attach(f"[{get_current_time_str()}] 登录页面验证成功，找到了'通行证登录'按钮", "验证结果")
                    # 截图保存成功状态
                    attach_screenshot_to_allure(driver, "login_page_verification_success", f"[{get_current_time_str()}] 登录页面验证成功")
                else:
                    print("登录页面验证失败，未找到'通行证登录'按钮")
                    # 截图保存失败证据
                    attach_screenshot_to_allure(driver, "login_page_verification_failure", f"[{get_current_time_str()}] 登录页面验证失败")
                    assert False, "登录页面未找到'通行证登录'按钮" 
            except Exception as e:
                print(f"验证登录页面时发生错误: {e}")
                # 截图保存错误证据，使用带时间戳的截图函数
                attach_screenshot_to_allure(driver, "login_page_error", f"[{get_current_time_str()}] 验证登录页面错误")
                allure.attach(f"[{get_current_time_str()}] {str(e)}", "错误信息", allure.attachment_type.TEXT)
                raise
    
    @allure.feature("登录界面元素展示")
    @allure.story("查找并截图人工客服按钮")
    def test_find_and_screenshot_customer_service_button(self, driver):
        """测试启动应用、处理隐私弹窗并查找人工客服按钮，找到后截图"""
        with allure.step(f"[{get_current_time_str()}] 清理后台应用并启动指定包名的应用"):
            # 启动应用前先清理后台，确保应用是最新状态
            driver.app_stop("com.duole.wuziqihd")
            # 启动指定包名的应用
            driver.app_start("com.duole.wuziqihd")
            
        with allure.step(f"[{get_current_time_str()}] 处理隐私弹窗"):
            try:
                # 尝试查找隐私弹窗（使用resourceId）
                sdk_privacy_title = SDKPrivacyConfig.get_sdk_privacy_title()
                if driver(resourceId=sdk_privacy_title).wait(timeout=10.0):
                    print("发现隐私弹窗，点击同意按钮")
                    sdk_privacy_agree = SDKPrivacyConfig.get_sdk_privacy_agree()
                    driver(resourceId=sdk_privacy_agree).click()
                    allure.attach(f"[{get_current_time_str()}] 已处理隐私弹窗", "操作结果")
                else:
                    print("没有发现隐私弹窗")
                    allure.attach(f"[{get_current_time_str()}] 未发现隐私弹窗", "操作结果")
            except Exception as e:
                print(f"处理隐私弹窗时发生错误: {e}")
                allure.attach(f"[{get_current_time_str()}] {str(e)}", "错误信息", allure.attachment_type.TEXT)
    
        with allure.step(f"[{get_current_time_str()}] 查找人工客服按钮并截图"):
            try:
                # 等待登录大厅页面加载
                time.sleep(5)  # 增加等待时间确保页面完全加载
                
                # 查找人工客服按钮（使用resourceId）
                login_service_button = LoginButtonConfig.get_service_button()
                if driver(resourceId=login_service_button).wait(timeout=10.0):
                    print("找到了人工客服按钮")
                    allure.attach(f"[{get_current_time_str()}] 找到了人工客服按钮", "验证结果")
                    # 给人工客服按钮区域截图
                    attach_screenshot_to_allure(driver, "customer_service_button", f"[{get_current_time_str()}] 人工客服按钮截图")
                    assert True
                else:
                    print("未找到人工客服按钮，校验失败")
                    attach_screenshot_to_allure(driver, "customer_service_button_missing", f"[{get_current_time_str()}] 未找到人工客服按钮")
                    assert False, "未找到人工客服按钮"
            except Exception as e:
                print(f"查找人工客服按钮时发生错误: {e}")
                attach_screenshot_to_allure(driver, "customer_service_error", f"[{get_current_time_str()}] 查找人工客服按钮错误")
                allure.attach(f"[{get_current_time_str()}] {str(e)}", "错误信息", allure.attachment_type.TEXT)
                raise
    
    @allure.feature("登录界面元素展示")
    @allure.story("查找并截图上传日志按钮")
    def test_find_and_screenshot_upload_log_button(self, driver):
        """测试启动应用、处理隐私弹窗并查找上传日志按钮，找到后截图"""
        with allure.step(f"[{get_current_time_str()}] 清理后台应用并启动指定包名的应用"):
            # 启动应用前先清理后台，确保应用是最新状态
            driver.app_stop("com.duole.wuziqihd")
            # 启动指定包名的应用
            driver.app_start("com.duole.wuziqihd")
            
        with allure.step(f"[{get_current_time_str()}] 处理隐私弹窗"):
            try:
                # 尝试查找隐私弹窗（使用resourceId）
                sdk_privacy_title = SDKPrivacyConfig.get_sdk_privacy_title()
                if driver(resourceId=sdk_privacy_title).wait(timeout=10.0):
                    print("发现隐私弹窗，点击同意按钮")
                    driver(text="同意").click()
                    allure.attach(f"[{get_current_time_str()}] 已处理隐私弹窗", "操作结果")
                else:
                    print("没有发现隐私弹窗")
                    allure.attach(f"[{get_current_time_str()}] 未发现隐私弹窗", "操作结果")
            except Exception as e:
                print(f"处理隐私弹窗时发生错误: {e}")
                allure.attach(f"[{get_current_time_str()}] {str(e)}", "错误信息", allure.attachment_type.TEXT)
    
        with allure.step(f"[{get_current_time_str()}] 查找上传日志按钮并截图"):
            try:
                # 等待登录大厅页面加载
                time.sleep(5)  # 增加等待时间确保页面完全加载
                
                # 查找上传日志按钮（使用resourceId）
                login_upload_button = LoginButtonConfig.get_upload_log_button()
                if driver(resourceId=login_upload_button).wait(timeout=10.0):
                    print("找到了上传日志按钮")
                    allure.attach(f"[{get_current_time_str()}] 找到了上传日志按钮", "验证结果")
                    # 给上传日志按钮区域截图
                    attach_screenshot_to_allure(driver, "upload_log_button", f"[{get_current_time_str()}] 上传日志按钮截图")
                    assert True
                else:
                    print("未找到上传日志按钮，校验失败")
                    attach_screenshot_to_allure(driver, "upload_log_button_missing", f"[{get_current_time_str()}] 未找到上传日志按钮")
                    assert False, "未找到上传日志按钮"
            except Exception as e:
                print(f"查找上传日志按钮时发生错误: {e}")
                attach_screenshot_to_allure(driver, "upload_log_error", f"[{get_current_time_str()}] 查找上传日志按钮错误")
                allure.attach(f"[{get_current_time_str()}] {str(e)}", "错误信息", allure.attachment_type.TEXT)
                raise
    
    @allure.feature("登录界面元素展示")
    @allure.story("查找并截图适龄提醒按钮")
    def test_find_and_screenshot_suitable_age_button(self, driver):
        """测试启动应用、处理隐私弹窗并查找适龄提醒按钮，找到后截图"""
        with allure.step(f"[{get_current_time_str()}] 清理后台应用并启动指定包名的应用"):
            # 启动应用前先清理后台，确保应用是最新状态
            driver.app_stop("com.duole.wuziqihd")
            # 启动指定包名的应用
            driver.app_start("com.duole.wuziqihd")
            
        with allure.step(f"[{get_current_time_str()}] 处理隐私弹窗"):
            try:
                # 尝试查找隐私弹窗（使用resourceId）
                sdk_privacy_title = SDKPrivacyConfig.get_sdk_privacy_title()
                if driver(resourceId=sdk_privacy_title).wait(timeout=10.0):
                    print("发现隐私弹窗，点击同意按钮")
                    driver(text="同意").click()
                    allure.attach(f"[{get_current_time_str()}] 已处理隐私弹窗", "操作结果")
                else:
                    print("没有发现隐私弹窗")
                    allure.attach(f"[{get_current_time_str()}] 未发现隐私弹窗", "操作结果")
            except Exception as e:
                print(f"处理隐私弹窗时发生错误: {e}")
                allure.attach(f"[{get_current_time_str()}] {str(e)}", "错误信息", allure.attachment_type.TEXT)
    
        with allure.step(f"[{get_current_time_str()}] 查找适龄提醒按钮并截图"):
            try:
                # 等待登录大厅页面加载
                time.sleep(5)  # 增加等待时间确保页面完全加载
                
                # 查找适龄提醒按钮（使用resourceId）
                suitable_age_button = LoginButtonConfig.get_suitable_age_button()
                if driver(resourceId=suitable_age_button).wait(timeout=10.0):
                    print("找到了适龄提醒按钮")
                    allure.attach(f"[{get_current_time_str()}] 找到了适龄提醒按钮", "验证结果")
                    # 给适龄提醒按钮区域截图
                    attach_screenshot_to_allure(driver, "suitable_age_button", f"[{get_current_time_str()}] 适龄提醒按钮截图")
                    assert True
                else:
                    print("未找到适龄提醒按钮，校验失败")
                    attach_screenshot_to_allure(driver, "suitable_age_button_missing", f"[{get_current_time_str()}] 未找到适龄提醒按钮")
                    assert False, "未找到适龄提醒按钮"
            except Exception as e:
                print(f"查找适龄提醒按钮时发生错误: {e}")
                attach_screenshot_to_allure(driver, "suitable_age_error", f"[{get_current_time_str()}] 查找适龄提醒按钮错误")
                allure.attach(f"[{get_current_time_str()}] {str(e)}", "错误信息", allure.attachment_type.TEXT)
                raise

class TestWZQLoginInterfaceClick:
    """五子棋应用登录界面元素点击测试类"""

    @pytest.fixture(scope="class")
    def driver(self):
        """连接到Android设备并返回驱动实例的fixture"""
        driver = u2.connect()  # 连接手机，若电脑只连接了一部手机，则不需要设备信息
        print("设备连接成功!")
        print("设备信息:")
        print(driver.info)  # 打印设备信息
        yield driver
        # 测试结束后清理资源
        # driver.app_stop("com.duole.wuziqihd")
        # print("测试结束，已关闭应用")
    
    @allure.feature("登录界面元素点击")
    @allure.story("点击人工客服按钮并验证客服页面")
    def test_click_customer_service_and_verify_page(self, driver):
        """测试启动应用、处理隐私弹窗、点击人工客服按钮并验证客服页面"""
        with allure.step(f"[{get_current_time_str()}] 清理后台应用并启动指定包名的应用"):
            # 启动应用前先清理后台，确保应用是最新状态
            driver.app_stop("com.duole.wuziqihd")
            # 启动指定包名的应用
            driver.app_start("com.duole.wuziqihd")
            
        with allure.step(f"[{get_current_time_str()}] 处理隐私弹窗"):
            try:
                # 尝试查找隐私弹窗（使用resourceId）
                sdk_privacy_title = SDKPrivacyConfig.get_sdk_privacy_title()
                if driver(resourceId=sdk_privacy_title).wait(timeout=10.0):
                    print("发现隐私弹窗，点击同意按钮")
                    driver(text="同意").click()
                    allure.attach(f"[{get_current_time_str()}] 已处理隐私弹窗", "操作结果")
                else:
                    print("没有发现隐私弹窗")
                    allure.attach(f"[{get_current_time_str()}] 未发现隐私弹窗", "操作结果")
            except Exception as e:
                print(f"处理隐私弹窗时发生错误: {e}")
                allure.attach(f"[{get_current_time_str()}] {str(e)}", "错误信息", allure.attachment_type.TEXT)
    
        with allure.step(f"[{get_current_time_str()}] 查找并点击人工客服按钮"):
            try:
                # 等待登录大厅页面加载
                time.sleep(5)  # 增加等待时间确保页面完全加载
                
                # 查找人工客服按钮（使用resourceId）
                login_service_button = LoginButtonConfig.get_service_button()
                if driver(resourceId=login_service_button).wait(timeout=10.0):
                    print("找到了人工客服按钮")
                    # 点击人工客服按钮
                    driver(resourceId=login_service_button).click()
                    allure.attach(f"[{get_current_time_str()}] 点击了人工客服按钮", "操作结果")
                    # 等待页面跳转
                    time.sleep(3)
                else:
                    print("未找到人工客服按钮，校验失败")
                    attach_screenshot_to_allure(driver, "customer_service_button_missing", f"[{get_current_time_str()}] 未找到人工客服按钮")
                    assert False, "未找到人工客服按钮"
            except Exception as e:
                print(f"点击人工客服按钮时发生错误: {e}")
                attach_screenshot_to_allure(driver, "customer_service_click_error", f"[{get_current_time_str()}] 点击人工客服按钮错误")
                allure.attach(f"[{get_current_time_str()}] {str(e)}", "错误信息", allure.attachment_type.TEXT)
                raise
    
        with allure.step(f"[{get_current_time_str()}] 验证客服页面是否包含'小乐子'文案"):
            try:
                # 等待客服页面加载
                time.sleep(5)  # 增加等待时间确保页面完全加载
                
                # 查找"小乐子"文案
                if driver(text="小乐子").wait(timeout=10.0):
                    print("客服页面验证成功，找到了'小乐子'文案")
                    assert True
                    allure.attach(f"[{get_current_time_str()}] 客服页面验证成功，找到了'小乐子'文案", "验证结果")
                    # 截图保存成功状态
                    attach_screenshot_to_allure(driver, "customer_service_page_verification_success", f"[{get_current_time_str()}] 客服页面验证成功")
                else:
                    print("客服页面验证失败，未找到'小乐子'文案")
                    # 截图保存失败证据
                    attach_screenshot_to_allure(driver, "customer_service_page_verification_failure", f"[{get_current_time_str()}] 客服页面验证失败")
                    assert False, "客服页面未找到'小乐子'文案"
            except Exception as e:
                print(f"验证客服页面时发生错误: {e}")
                # 截图保存错误证据
                attach_screenshot_to_allure(driver, "customer_service_page_error", f"[{get_current_time_str()}] 验证客服页面错误")
                allure.attach(f"[{get_current_time_str()}] {str(e)}", "错误信息", allure.attachment_type.TEXT)
                raise