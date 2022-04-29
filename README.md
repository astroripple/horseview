# horseview
ORM for JRDB

## Setup
set your environmental variable below.  
e.g.  
`DB="sqlite:///tmp/jrdb.db"`  
https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/

## 使い方
horseview.horsemodelから用途に応じたクラスをインポートする。  

## ロード例
`from  horseview.horsemodel import KaisaiData`  
`kaisais = KaisaiData.query.filter_by(KaisaiData.ymd='20181118').all()`  
