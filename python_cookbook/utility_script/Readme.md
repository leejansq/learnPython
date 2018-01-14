#python 脚本编程 todo
http://python3-cookbook.readthedocs.io/zh_CN/latest/chapters/p13_utility_script_and_system_manage.html


为了解析命令行选项，你首先要创建一个 ArgumentParser 实例， 并使用 add_argument() 方法声明你想要支持的选项。 在每个 add_argument() 调用中，dest 参数指定解析结果被指派给属性的名字。 metavar 参数被用来生成帮助信息。action 参数指定跟属性对应的处理逻辑， 通常的值为 store ,被用来存储某个值或讲多个参数值收集到一个列表中。