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