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

## 获取七牛token

method: GET

url: /getqiniutoken

arguments: token

return: 七牛token
