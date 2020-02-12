-- 创建数据库
CREATE SCHEMA `djangodemo` ;

-- 在pycharm根据模型创建数据库
-- python manage.py makemigrations
-- Python manage.py migrate

-- 关闭保护模式，能批量删除
SET SQL_SAFE_UPDATES = 0;
-- 开启保护模式，不能批量删除
SET SQL_SAFE_UPDATES = 1;

-- 添加岗位
SELECT REPLACE(uuid(), '-', '')
insert into djangodemo.sys_position(id,pos_no,pos_name,create_date,modify_date,status)
values('71600db34d9d11eabf8500ff6d4d1e41','P001','总经理',now(),now(),1);
insert into djangodemo.sys_position(id,pos_no,pos_name,create_date,modify_date,status)
values('71600db34d9d11eabf8500ff6d4d1e42','P002','财务总监',now(),now(),1);
insert into djangodemo.sys_position(id,pos_no,pos_name,create_date,modify_date,status)
values('71600db34d9d11eabf8500ff6d4d1e43','P003','销售总监',now(),now(),1);
insert into djangodemo.sys_position(id,pos_no,pos_name,create_date,modify_date,status)
values('71600db34d9d11eabf8500ff6d4d1e44','P004','人事总监',now(),now(),1);
update djangodemo.sys_position set status=0 where id='71600db34d9d11eabf8500ff6d4d1e44';
-- 查询
SELECT * FROM djangodemo.sys_user order by create_date desc;
SELECT * FROM djangodemo.sys_userposition order by create_date desc;
SELECT * FROM djangodemo.sys_position order by create_date desc;
-- 删除
delete from  djangodemo.sys_user;
delete from djangodemo.sys_postion;
delete from djangodemo.sys_userposition;

