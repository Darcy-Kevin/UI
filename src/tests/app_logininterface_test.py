# -*- coding: utf-8 -*-
"""五子棋应用登录界面测试脚本
此脚本用于自动连接设备、启动五子棋应用、处理隐私弹窗并验证登录页面。
"""

import uiautomator2 as u2
import time
import pytest
import allure
# 导入工具函数
from ..utils.screenshot_utils import attach_screenshot_to_allure
from ..utils.time_utils import get_current_time_str

class TestWZQLoginInterface:
    """五子棋应用登录界面测试类"""
    
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
        
    @allure.feature("登录界面")
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
                # 尝试查找隐私弹窗的同意按钮
                if driver(text="同意").wait(timeout=5.0):
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
                if driver(text="通行证登录").wait(timeout=5.0):
                    print("登录页面验证成功，找到了'通行证登录'文案")
                    assert True
                    allure.attach(f"[{get_current_time_str()}] 登录页面验证成功，找到了'通行证登录'文案", "验证结果")
                    # 截图保存成功状态
                    attach_screenshot_to_allure(driver, "login_page_verification_success", f"[{get_current_time_str()}] 登录页面验证成功")
                else:
                    print("登录页面验证失败，未找到'通行证登录'文案")
                    # 截图保存失败证据
                    attach_screenshot_to_allure(driver, "login_page_verification_failure", f"[{get_current_time_str()}] 登录页面验证失败")
                    assert False, "登录页面未找到'通行证登录'文案"
            except Exception as e:
                print(f"验证登录页面时发生错误: {e}")
                # 截图保存错误证据，使用带时间戳的截图函数
                attach_screenshot_to_allure(driver, "login_page_error", f"[{get_current_time_str()}] 验证登录页面错误")
                allure.attach(f"[{get_current_time_str()}] {str(e)}", "错误信息", allure.attachment_type.TEXT)
                raise