"""
添加任务菜单
使用依赖注入获取 TaskSystem 实例
"""

from core.menuModule.menu import Menu
from core.taskModule.taskSystem import TaskSystem


class AddTaskMenu(Menu):
    def __init__(self, task_system: TaskSystem):
        super().__init__(
            "添加任务",
            "输入任务标题，创建新任务"
        )
        self.__task_system = task_system

    def execute(self) -> int:
        """添加任务的核心逻辑"""
        try:
            title = input("请输入任务标题: ").strip()

            if not title:
                print("[错误] 任务标题不能为空")
                return -1

            task = self.__task_system.add(title)
            print(f"[成功] 任务添加成功: {task.title}")
            return 0

        except ValueError as e:
            print(f"[错误] 添加失败: {e}")
            return -1
        except Exception as e:
            print(f"[错误] 未知错误: {e}")
            return -1
