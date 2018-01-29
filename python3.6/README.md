# 安装virtualenv
# sudo easy_install virtualenv
# sudo pip install virtualenv
# sudo apt-get install python-virtualenv

# 使用virtualenv 自己的机器必须安装python3.6 可根据自己安装目录和版本进行更换
# virtualenv -p /usr/bin/python3.6 venv
# . venv/bin/activate
# pip install Flask
# pip install Jinja2

# mkdir static
# mkdir templates

# touch schema.sql 
```
drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title string not null,
  text string not null
);
```

#touch flaskr.py