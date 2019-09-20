# flask学习笔记

![](https://ws1.sinaimg.cn/large/005Pf0eLgy1g72cvpgxv7j31a40vr42l.jpg)

### 初始化创建app

```py
// fisher.py
from app import create_app

app = create_app()
app.run(debug=app.config['DEBUG'])
```

### flask细节点

1. 判断条件中越可能为false放前面，比较耗时的操作放后面，比如操作数据库

2. 常用返回response的方式：return 301， xxx， headers

3. @staticmethod，静态方法，与对象self无关函数

   @classmethod，类方法，与类变量cls有关

4. request.args是一个不可变的字典，request.args.to_dict()转化成可变的字典，要在上下文使用

5. 蓝图用来分离模块