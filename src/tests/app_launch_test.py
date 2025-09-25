# -*- coding: utf-8 -*-
"""五子棋应用启动测试脚本
此脚本用于自动连接设备、启动五子棋应用、等待特定界面出现并执行点击操作。
"""

import uiautomator2 as u2
import time
import pytest
import allure
# 导入截图工具函数
from ..utils.screenshot_utils import attach_screenshot_to_allure, get_current_time_str

# 导入坐标参数
from ..config.coordinates import click_position_PVE

class TestWZQApp:
    """五子棋应用测试类"""
    
    @pytest.fixture(scope="class")
    def driver(self):
        """连接到Android设备并返回驱动实例的fixture"""
        driver = u2.connect()  # 连接手机，若电脑只连接了一部手机，则不需要设备信息
        print("设备连接成功!")
        print("设备信息:")
        print(driver.info)  # 打印设备信息
        yield driver

        # 测试结束后清理资源——暂时先不关闭
        # driver.app_stop("com.duole.wuziqihd")
        # print("测试结束，已关闭应用")
        
    @allure.feature("应用启动")
    @allure.story("启动五子棋应用")
    def test_launch_app(self, driver):
        """测试启动五子棋应用"""
        with allure.step(f"[{get_current_time_str()}] 清理后台应用并启动指定包名的应用"):
            try:
                # 启动应用前先清理后台，确保应用是最新状态
                driver.app_stop("com.duole.wuziqihd")
                # 启动指定包名的应用
                driver.app_start("com.duole.wuziqihd")
                allure.attach(f"[{get_current_time_str()}] 已启动应用com.duole.wuziqihd", "操作结果")
            except Exception as e:
                print(f"启动应用时发生错误: {e}")
                allure.attach(f"[{get_current_time_str()}] {str(e)}", "错误信息", allure.attachment_type.TEXT)
                # 截图保存错误状态
                attach_screenshot_to_allure(driver, "app_launch_error", f"[{get_current_time_str()}] 启动应用错误时的界面")
                raise
            
        with allure.step("验证应用启动成功"):
            # 等待应用启动并获取当前包名
            time.sleep(3)  # 给应用启动时间
            current_package = driver.app_current()['package']
            assert current_package == "com.duole.wuziqihd", f"应用启动失败，当前包名为: {current_package}"
            allure.attach("应用启动成功", "验证结果")
    
    @allure.feature("界面验证")
    @allure.story("等待棋力评测界面")
    def test_wait_for_ui_element(self, driver):
        """测试等待棋力评测界面出现"""
        with allure.step(f"[{get_current_time_str()}] 等待'棋力评测'界面出现..."):
            try:
                result = self.wait_for_ui_element(driver, "棋力评测")
                assert result is True, "未能找到'棋力评测'界面"
                # 截图保存棋力评测元素出现的界面
                attach_screenshot_to_allure(driver, "chess_rating_element_displayed", f"[{get_current_time_str()}] 棋力评测元素显示")
                allure.attach(f"[{get_current_time_str()}] 找到棋力评测界面", "验证结果")
            except Exception as e:
                allure.attach(f"[{get_current_time_str()}] {str(e)}", "错误信息", allure.attachment_type.TEXT)
                # 截图保存错误状态
                attach_screenshot_to_allure(driver, "chess_rating_element_error", f"[{get_current_time_str()}] 等待棋力评测元素错误")
                raise
    
    @allure.feature("用户操作")
    @allure.story("点击指定坐标")
    def test_perform_click(self, driver):
        """测试在指定坐标位置执行点击操作"""
        with allure.step(f"[{get_current_time_str()}] 点击坐标: {click_position_PVE}"):
            try:
                # 确保棋力评测界面已出现
                self.wait_for_ui_element(driver, "棋力评测")
                # 执行点击
                driver.click(click_position_PVE[0], click_position_PVE[1])
                # 截图保存点击后的界面
                attach_screenshot_to_allure(driver, "chess_rating_element_clicked", f"[{get_current_time_str()}] 点击棋力评测元素后的界面")
                allure.attach(f"[{get_current_time_str()}] 已点击坐标: {click_position_PVE}", "操作结果")
            except Exception as e:
                allure.attach(f"[{get_current_time_str()}] {str(e)}", "错误信息", allure.attachment_type.TEXT)
                # 截图保存错误状态
                attach_screenshot_to_allure(driver, "click_operation_error", f"[{get_current_time_str()}] 点击操作错误")
                raise
    
    def wait_for_ui_element(self, driver, text="棋力评测", timeout=10.0):
        """等待特定文本元素在界面上出现
        
        Args:
            driver: uiautomator2驱动实例
            text: 要查找的文本内容
            timeout: 最长等待时间（秒）
        
        Returns:
            bool: 元素是否成功找到
        """
        try:
            print(f"等待'{text}'界面出现...")
            driver(text=text).wait(timeout=timeout)
            return True
        except Exception as e:
            print(f"未能找到'{text}'界面: {e}")
            return False

