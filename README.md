# API

## login

method: POST

url: /login

arguments(form data): phone, password

return: user dict with name, id, content and so on.


## logout

method: PUT

url: /logout

arguments: None

return: 'Logout Success!' 200


## signup

method POST

url: /signup

arguments(form data): phone(required), password(required), name

return: user dict... 


## 个人餐厅列表

method: GET

url: /myrestaurants

arguments: token(user id)

return: 餐厅JSON列表

## 新建餐厅信息

method: POST

url: /newrestaurant

arguments: token and form data

return: 餐厅JSON数据

## 更新餐厅信息

method: POST

url: /updaterestaurant

arguments: 和新建餐厅一样，form data 里面要包含需要更新的餐厅ID ‘rid’

return: 是否成功string


## 餐厅广场

method: GET

url: /restaurantplaza

arguments: token

return: 餐厅JSON列表

## 获取七牛上传token（24hours 更新一次）

method : GET

url: /getqiniutoken

arguments: token

return: qiniu token

## 搜索餐厅

method: GET

url: /search

arguments: token, keyword(GET 参数)

return: 搜索结果列表


## 微信登陆

method: POST

url: /wechatlogin

arguments: form data(openid, avatar)

return: 用户JSON信息


## 更新个人信息

method: POST

url: /updateme

arguments: 个人信息字段

return: 用户JSON信息

## 绑定手机号

method: POST

url: /phonebind

arguments: form data (phone)

return 0000 code

## 绑定微信

method: POST

url: /wechatbind

arguments: form data(openid)

return 0000 code


## 读书评分

1. method: POST

	url: /score

	arguments :form data(name:要评分的人名， score:评分)

	return: string 成功信息

2. method: GET

	url: /score
	
	arguments: get型参数--name 
	
	return: 所要获取人的评分信息
	

