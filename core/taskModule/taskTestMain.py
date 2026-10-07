"""
Task 模块测试脚本
测试任务系统的基本增删改查功能
"""

from task import Task
from taskSystem import TaskSystem


def print_all_tasks(system: TaskSystem):
    """打印所有任务"""
    count = system.get_task_count()
    if count == 0:
        print("当前没有任务")
        return

    for i in range(count):
        task = system.get_by_index(i)
        status = "已完成" if task.is_completed else "未完成"
        print(f"{i + 1}. {task.title} [{status}]")


def test_add():
    """测试：增 - 添加任务"""
    print("=== 测试1：增 - 添加任务 ===")
    system = TaskSystem()

    system.add("写高数作业")
    system.add("复习英语")
    system.add("完成Python作业")

    print(f"[OK] 添加了3个任务")
    print(f"[OK] 任务总数: {system.get_task_count()}")
    print_all_tasks(system)
    print()


def test_query():
    """测试：查 - 查看任务"""
    print("=== 测试2：查 - 查看任务 ===")
    system = TaskSystem()

    system.add("任务1")
    system.add("任务2")
    system.add("任务3")

    # 按编号查询（索引从0开始）
    task = system.get_by_index(1)
    print(f"[OK] 查询索引1: {task.title if task else '未找到'}")
    print(f"[OK] 完成状态: {task.is_completed}")

    # 查询无效编号
    invalid = system.get_by_index(10)
    print(f"[OK] 查询索引10: {invalid}")
    print()


def test_update():
    """测试：改 - 修改任务状态"""
    print("=== 测试3：改 - 修改任务状态 ===")
    system = TaskSystem()

    system.add("需要完成的任务")
    system.add("另一个任务")

    print("修改前:")
    print_all_tasks(system)

    # 标记第1个任务为已完成（注意：索引从0开始）
    result = system.update_completed(0, True)
    print(f"\n[OK] 更新结果: {result}")

    print("\n修改后:")
    print_all_tasks(system)
    print()


def test_delete():
    """测试：删 - 删除任务"""
    print("=== 测试4：删 - 删除任务 ===")
    system = TaskSystem()

    system.add("任务1")
    system.add("任务2")
    system.add("任务3")

    print("删除前:")
    print_all_tasks(system)
    print(f"任务总数: {system.get_task_count()}")

    # 删除索引1（第2个任务）
    result = system.delete(1)
    print(f"\n[OK] 删除索引1，结果: {result}")

    print("\n删除后:")
    print_all_tasks(system)
    print(f"任务总数: {system.get_task_count()}")
    print()


def test_empty_list():
    """测试：空列表"""
    print("=== 测试5：空列表 ===")
    system = TaskSystem()
    print_all_tasks(system)
    print()


def test_error_handling():
    """测试：异常处理"""
    print("=== 测试6：异常处理 ===")
    system = TaskSystem()
    system.add("任务1")

    # 删除无效编号
    result = system.delete(10)
    print(f"[OK] 删除无效索引10: {result}")

    # 标记无效编号
    result = system.update_completed(10, True)
    print(f"[OK] 标记无效索引10: {result}")

    # 创建空标题任务
    try:
        task = Task("")
        print(f"[FAIL] 空标题应该抛出异常")
    except ValueError as e:
        print(f"[OK] 空标题正确抛出异常: {e}")

    print()


def main():
    """运行所有测试"""
    print("=" * 60)
    print("Task 模块 - 增删改查测试")
    print("=" * 60)
    print()

    test_add()
    test_query()
    test_update()
    test_delete()
    test_empty_list()
    test_error_handling()

    print("=" * 60)
    print("所有测试完成")
    print("=" * 60)


if __name__ == "__main__":
    main()
