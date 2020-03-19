from tencentAiSDK import AiTencentBase

appId = 'your appId'
appKey = 'your appKey'
aiClient = AiTencentBase(appId, appKey)
'''
智能闲聊
api地址 ：https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat
请求参数:	
session	
question
'''
#app_id	,time_stamp,nonce_str,sign参数均有sdk统一处理
params = {'session': '1111111', 'question': '你是谁'}

url = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat'

result = aiClient._doHttpPost(params, url)
print(result)
