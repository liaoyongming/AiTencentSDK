# AiTencentSDK
腾讯AI SDK

## 使用
参照 demo.py
1. 在腾讯ai开放平台管理后台获取你应用的appid，appkey实例化一个AiTencentBase对象；
2. 调用`_doHttpPost`函数，传入请求参数和对应接口的api地址，如demo.py中是智能闲聊接口的请求范例；
3. `app_id`,`time_stamp`,`nonce_str`,`sign`这些参数均由sdk统一处理，参数中只需传入接口对应的关键参数。

## todo
基于`AiTencentBase`类将各类人工智能接口再一次封装
