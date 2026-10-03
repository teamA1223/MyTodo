from core.menuModule.menu import Menu


class MenuB(Menu):
    def __init__(self):
        super().__init__(
            "MenuA",
            "这是菜单B，测试下功能\n"
            "这是第二行\n"
            "这是第三行\n",
        )

    def execute(self) -> int: # 抛出执行结果（0或错误码）
        print("通过菜单B实现了很炫酷的功能")