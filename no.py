# coding:utf-8

def createTableErr(): 
    q=QSqlQuery() 
    q.exec_(QObject().tr("drop table error"))
    q.exec_(QObject().tr("create table if not exists error('故障编号' integer primary key autoincrement)"))
    q.exec_(QObject().tr("alter table error add '故障现象' varchar(128)"))
    q.exec_(QObject().tr("alter table error add '具体的故障现象' varchar(128)"))
    q.exec_(QObject().tr("alter table error add '故障部位及原因' varchar(128)"))
    q.exec_(QObject().tr("alter table error add '解决方法' varchar(128)"))
    q.exec_(QObject().tr("alter table error add '使用情况' varchar(128)"))
    #q.exec_(QObject().tr("insert into error ('故障编号','故障现象') values ('1','仪器容易产生磨损，漏油的现场，也会产生卡顿的现象')"))
    q.exec_(QObject().tr("insert into error ('故障现象') values ('仪器容易产生磨损，漏油的现场，也会产生卡顿的现象')"))
    q.exec_(QObject().tr("update error set 具体的故障现象= '仪器容易产生磨损，漏油的现场，也会产生卡顿的现象' where 故障编号=1 "))
    q.exec_(QObject().tr("update error set 故障部位及原因= '仪器容易产生磨损，漏油的现场，也会产生卡顿的现象' where 故障编号=1 "))
    q.exec_(QObject().tr("update error set 解决方法= '无' where 故障编号=1 "))
    q.exec_(QObject().tr("update error set 使用情况= '使用中' where 故障编号=1 "))
    q.exec_(QObject().tr("commit"))
    
def createTableMachine():
    q=QSqlQuery()
    q.exec_(QObject().tr("drop table machine"))
    q.exec_(QObject().tr("create table if not exists machine('仪器编号' integer primary key autoincrement)"))
    q.exec_(QObject().tr("alter table machine add '仪器名称' varchar(128)"))
    q.exec_(QObject().tr("alter table machine add '型号' varchar(128)"))
    q.exec_(QObject().tr("alter table machine add '出厂日期' varchar(128)"))
    q.exec_(QObject().tr("alter table machine add '技术参数' varchar(128)"))
    q.exec_(QObject().tr("alter table machine add '用途及特点' varchar(128)"))
    q.exec_(QObject().tr("alter table machine add '实验价格' varchar(128)"))
    q.exec_(QObject().tr("alter table machine add '仪器负责老师' varchar(128)"))
    q.exec_(QObject().tr("alter table machine add '故障' varchar(128)"))
    #q.exec_(QObject().tr("insert into machine ('仪器编号','仪器名称') values ('1','全自动三轴仪')"))
    q.exec_(QObject().tr("insert into machine ('仪器名称') values ('全自动三轴仪')"))
    q.exec_(QObject().tr("update machine set 型号= 'TSZ' where 仪器编号=1 "))
    q.exec_(QObject().tr("update machine set 出厂日期= '2010/08/01' where 仪器编号=1 "))
    q.exec_(QObject().tr("update machine set 技术参数= '试件尺寸：TSZ-1、TSZ-1A Φ39.1mm x 80mm' where 仪器编号=1 "))
    q.exec_(QObject().tr("update machine set 用途及特点= '常规应力应变式无侧限试验' where 仪器编号=1 "))
    q.exec_(QObject().tr("update machine set 实验价格= '400' where 仪器编号=1 "))
    q.exec_(QObject().tr("update machine set 仪器负责老师= '李老师' where 仪器编号=1 "))
    q.exec_(QObject().tr("update machine set 故障= '1' where 仪器编号=1 "))
    q.exec_(QObject().tr("commit"))

class Model(QSqlTableModel): 
    def __init__(self,parent): 
        QSqlTableModel.__init__(self,parent) 
        self.setTable(QObject().tr("machine") )
        self.select()
        self.removeColumn(0) 
        self.setEditStrategy(QSqlTableModel.OnManualSubmit) 

class TestWidget(QWidget): 
    def __init__(self): 
        QWidget.__init__(self) 
        vbox=QVBoxLayout(self) 
        self.view=QTableView() 
        self.model=Model(self.view) 
        self.view.setModel(self.model) 
        vbox.addWidget(self.view)
        
#temp=q.value(3).split('/')
            '''
            if len(temp)<3:#type(q.value(3)) is type(QDate()):
                tempDate=q.value(3).split('(')[1]
                tempDateE=tempDate.split(')')[0]
                yearV=int(tempDateE.split(',')[0])
                monthV=int(tempDateE.split(',')[1])
                dayV=int(tempDateE.split(',')[2])
            else:
            '''
            
def createConnection(): 
    db=QSqlDatabase.addDatabase("QSQLITE") 
    db.setDatabaseName("info.db") 
    if not db.open():
        QMessageBox.critical(QDialog(), 'ErrorDatabase', 'createConnection() db.open() error')
        sys.exit(0)
    q=QSqlQuery()
    if debugTag:
        q.exec_(QObject().tr("drop table error"))
    q.exec_(QObject().tr("create table if not exists error('故障编号' integer primary key autoincrement)"))
    q.exec_(QObject().tr("alter table error add '故障现象' varchar(128)"))
    q.exec_(QObject().tr("alter table error add '具体的故障现象' varchar(128)"))
    q.exec_(QObject().tr("alter table error add '故障部位及原因' varchar(128)"))
    q.exec_(QObject().tr("alter table error add '解决方法' varchar(128)"))
    q.exec_(QObject().tr("alter table error add '使用情况' varchar(128)"))
    if debugTag:
        q.exec_(QObject().tr("drop table machine"))
    q.exec_(QObject().tr("create table if not exists machine('仪器编号' integer primary key autoincrement)"))
    q.exec_(QObject().tr("alter table machine add '仪器名称' varchar(128)"))
    q.exec_(QObject().tr("alter table machine add '型号' varchar(128)"))
    q.exec_(QObject().tr("alter table machine add '出厂日期' varchar(128)"))
    q.exec_(QObject().tr("alter table machine add '技术参数' varchar(128)"))
    q.exec_(QObject().tr("alter table machine add '用途及特点' varchar(128)"))
    q.exec_(QObject().tr("alter table machine add '实验价格' varchar(128)"))
    q.exec_(QObject().tr("alter table machine add '仪器负责老师' varchar(128)"))
    q.exec_(QObject().tr("alter table machine add '故障' varchar(128)"))
    if debugTag:
        q.exec_(QObject().tr("insert into error ('故障现象') values ('仪器容易产生磨损，漏油的现场，也会产生卡顿的现象')"))
        q.exec_(QObject().tr("update error set 具体的故障现象= '仪器容易产生磨损，漏油的现场，也会产生卡顿的现象' where 故障编号=1 "))
        q.exec_(QObject().tr("update error set 故障部位及原因= '仪器容易产生磨损，漏油的现场，也会产生卡顿的现象' where 故障编号=1 "))
        q.exec_(QObject().tr("update error set 解决方法= '无' where 故障编号=1 "))
        q.exec_(QObject().tr("update error set 使用情况= '使用中' where 故障编号=1 "))
        q.exec_(QObject().tr("commit"))
        q.exec_(QObject().tr("insert into machine ('仪器名称') values ('全自动三轴仪')"))
        q.exec_(QObject().tr("update machine set 型号= 'TSZ' where 仪器编号=1 "))
        q.exec_(QObject().tr("update machine set 出厂日期= '2010/08/01' where 仪器编号=1 "))
        q.exec_(QObject().tr("update machine set 技术参数= '试件尺寸：TSZ-1、TSZ-1A Φ39.1mm x 80mm' where 仪器编号=1 "))
        q.exec_(QObject().tr("update machine set 用途及特点= '常规应力应变式无侧限试验' where 仪器编号=1 "))
        q.exec_(QObject().tr("update machine set 实验价格= '400' where 仪器编号=1 "))
        q.exec_(QObject().tr("update machine set 仪器负责老师= '李老师' where 仪器编号=1 "))
        q.exec_(QObject().tr("update machine set 故障= '1' where 仪器编号=1 "))
        q.exec_(QObject().tr("commit"))
        
def zzzPmadeComboBoxItemsFromDatabase(self, columnName, tableName, comboBoxName):
        cmd="""
distinctList=sqlDistinctItems(self.tr("%s"), self.tr("%s")) 
self.%s.clear()
self.%s.addItems(distinctList)
            """  % (columnName, tableName, comboBoxName, comboBoxName)
        exec(cmd)

  '''
        if q.next():
            for i in xrange(len(widgetList)):
                dataList.append(self.tr("%s")) % q.value(i)
        print dataList
        for i in xrange(len(dataList)):
            if widgetList[i].startswith('spinBox'):
                cmd=self.tr("self.%s.setValue(%d) " ) % widgetList[i], dataList[i]
                exec(cmd)
        '''
