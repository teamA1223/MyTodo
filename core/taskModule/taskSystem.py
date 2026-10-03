from copy import deepcopy

from .task import Task


class TaskSystem:
    """任务管理系统"""

    def __init__(self):
        self.__tasks = []

    def add(self, title: str) -> Task:
        task = Task(title)
        self.__tasks.append(task)
        return task

    def list_all(self):
        """列出所有任务"""
        if not self.__tasks:
            print("当前没有任务")
            return

        for i, task in enumerate(self.__tasks, start=1):
            status = "已完成" if task.is_completed else "未完成"
            print(f"{i}. {task.title} [{status}]")

    # 返回本身（引用）,内部使用，修改数据请走专用方法
    def _get_by_index(self, idx: int) -> Task:
        if 0 <= idx <= len(self.__tasks)-1:
            return self.__tasks[idx]
        return None

    # 返回副本，只给查不给改
    def get_by_index(self, idx):
        task = self._get_by_index(idx)
        if task:
            return deepcopy(task)
        return None

    def delete(self, idx: int) -> bool:
        task = self._get_by_index(idx)
        if task:
            self.__tasks.pop(idx)
            return True
        return False

    def get_task_count(self) -> int:
        """获取任务总数"""
        return len(self.__tasks)

    def update_completed(self, idx: int, status: bool) -> bool:
        """更新任务的完成状态"""
        task = self._get_by_index(idx)
        if task:
            task.is_completed = status
            return True
        return False
