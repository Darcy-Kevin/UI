# -*- coding: utf-8 -*-
"""截图工具函数
提供带时间戳的截图功能，统一管理测试过程中的截图保存
"""

import os
import time
from datetime import datetime
import allure


def take_screenshot(driver, screenshot_name, folder_path=None):
    """生成带时间戳的截图并保存到指定目录
    
    Args:
        driver: uiautomator2驱动实例
        screenshot_name: 截图名称（不含扩展名）
        folder_path: 截图保存目录，默认保存到src/resources/screenshots
        
    Returns:
        str: 保存的截图完整路径
    """
    # 设置默认保存目录
    if folder_path is None:
        # 获取当前文件所在目录的父目录的父目录
        current_dir = os.path.dirname(os.path.abspath(__file__))
        folder_path = os.path.join(current_dir, '..', 'resources', 'screenshots')
        
    # 确保目录存在
    os.makedirs(folder_path, exist_ok=True)
    
    # 生成带时间戳的文件名
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    screenshot_filename = f"{screenshot_name}_{timestamp}.png"
    screenshot_path = os.path.join(folder_path, screenshot_filename)
    
    # 截取并保存截图
    try:
        screenshot = driver.screenshot()
        screenshot.save(screenshot_path)
        print(f"已保存截图: {screenshot_path}")
        return screenshot_path
    except Exception as e:
        print(f"保存截图失败: {e}")
        return None


def attach_screenshot_to_allure(driver, screenshot_name, description, folder_path=None):
    """截取带时间戳的截图并附加到Allure报告
    
    Args:
        driver: uiautomator2驱动实例
        screenshot_name: 截图名称（不含扩展名）
        description: Allure报告中的描述
        folder_path: 截图保存目录，默认保存到src/resources/screenshots
        
    Returns:
        str: 保存的截图完整路径，如果失败则返回None
    """
    screenshot_path = take_screenshot(driver, screenshot_name, folder_path)
    
    if screenshot_path and os.path.exists(screenshot_path):
        try:
            with open(screenshot_path, 'rb') as f:
                screenshot_bytes = f.read()
            allure.attach(screenshot_bytes, description, allure.attachment_type.PNG)
            return screenshot_path
        except Exception as e:
            print(f"附加截图到Allure报告失败: {e}")
            return None
    return None


def get_current_time_str():
    """获取当前时间的格式化字符串，用于Allure报告
    
    Returns:
        str: 格式化的当前时间字符串
    """
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]