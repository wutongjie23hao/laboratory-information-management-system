# -*- coding:utf-8 -*-
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtSql import *
import sys
import xlwt
import Ui_addErrorInfo, Ui_addMachineInfo, Ui_login, Ui_main, Ui_updateErrorInfo, Ui_updateMachineInfo

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8")) 
debugTag=False
NoErrorNo=u"1"
eTable=u"error"
eTableCopy=u"error_copy"
E0=u"故障编号"
E1= u"故障现象"
E2= u"具体的故障现象"
E3= u"故障部位及原因"
E4 =u"解决方法"
E5= u"使用情况"
mTable=u"machine"
mTableCopy=u"machine_copy"
M0= u"仪器编号"
M1= u"仪器名称"
M2= u"型号"
M3=u"出厂日期"
M4=u"技术参数"
M5=u"用途及特点"
M6=u"实验价格"
M7=u"仪器负责老师"
M8= u"故障编号"
NONE_TAG=u""

def addDataFunction(y0, y1,  y2,  y3, y4, y5,  y6, y7, y8):
    for i in xrange(1, 9):
        cmd="""
if y%d==QObject().tr(''):
    y%d=QObject().tr('%s')
        """ % (i, i, NONE_TAG)
        exec(cmd)
    q=QSqlQuery()
    q.exec_(QObject().tr("INSERT INTO %s (%s,%s,%s,%s,%s,%s,%s,%s,%s) VALUES ('%d','%s','%s','%s','%s','%s','%s','%s','%s')") % (mTable, M0, M1, M2, M3, M4, M5, M6, M7, M8, y0, y1, y2, y3, y4, y5, y6, y7, y8))
    return q
def maxData(columnName, tableName):
    q=QSqlQuery()
    q.exec_(QObject().tr("SELECT MAX(%s) FROM %s"  )% (columnName,tableName))
    if q.next():
        spinMaxValue= q.value(0)
    return spinMaxValue
def sqlColumnCount(columnName,  tableName):
    q=QSqlQuery()
    q.exec_(QObject().tr("SELECT COUNT(%s) FROM %s")%(columnName, tableName))
    if q.next():
        return q.value(0)
def sqlDeleteInfo(tableName,columnName,  id):
    q=QSqlQuery()
    q.exec_(QObject().tr("DELETE FROM %s WHERE %s = '%s'  ")%(tableName,columnName,  id))
    q.exec_(QObject().tr("update %s set %s=%s-1 where %s>%d")%( tableName,columnName, columnName, columnName, id ))
def sqlDistinctItems(columnName , tableName):
    distinctList=[]
    q=QSqlQuery()
    q.exec_(QObject().tr("SELECT DISTINCT %s FROM %s ")%(columnName, tableName ))
    while q.next():
        if type(q.value(0)) == type(1L) or type(q.value(0))==type(1):
            distinctList.append(QObject().tr(str(q.value(0))) )
        else:
            distinctList.append(q.value(0))
    return distinctList

def createConnection(): 
    db=QSqlDatabase.addDatabase("QSQLITE") 
    db.setDatabaseName("info.db") 
    if not db.open():
        QMessageBox.critical(QDialog(), 'ErrorDatabase', 'createConnection() db.open() error')
        sys.exit(0)
    q=QSqlQuery()
    if debugTag:
        q.exec_(QObject().tr("drop table %s") % eTable)
    createTableString=QObject().tr("CREATE TABLE %s(%s integer primary key autoincrement,%s varchar(255),%s varchar(255),%s varchar(255),%s varchar(255),%s varchar(255))") %(eTable, E0, E1, E2, E3, E4, E5)
    #createTableString=QObject().tr("CREATE TABLE %s(%s integer primary key autoincrement,%s varchar(255),%s varchar(255),%s varchar(255),%s varchar(255),s varchar(255))") %(eTableCopy, E0, E1, E2, E3, E4, E5)
    q.exec_(createTableString)
    if debugTag:
        q.exec_(QObject().tr("drop table %s") % mTable)
    createTableString=QObject().tr("CREATE TABLE %s(%s integer primary key autoincrement,%s varchar(255),%s varchar(255),%s varchar(255),%s varchar(255),%s varchar(255),%s varchar(255),%s varchar(255),%s interger)") %(mTable, M0, M1, M2, M3, M4, M5, M6, M7, M8)
    #createTableString=QObject().tr("CREATE TABLE %s(%s integer primary key autoincrement,%s varchar(255),%s varchar(255),%s varchar(255),%s varchar(255),%s varchar(255),%s varchar(255),%s varchar(255),%s varchar(255))") %(mTableCopy, M0, M1, M2, M3, M4, M5, M6, M7, M8)
    q.exec_(createTableString)
    if debugTag:
        insertValueString="INSERT INTO %s (%s, %s,%s,%s,%s) VALUES ('%s', '%s', '%s', '%s', '%s')" % (eTable, E1, E2, E3, E4, E5, u'仪器容易产生磨损', u'仪器容易产生磨损',u'仪器容易产生磨损',u'无', u'使用中')
        q.exec_(insertValueString)
        insertValueString="INSERT INTO %s (%s, %s,%s,%s,%s,%s,%s,%s) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (mTable, M1, M2, M3, M4, M5, M6, M7, M8, u'全自动三轴仪', u'TSZ',u'2010/08/01',u'试件尺寸：TSZ-1', u'无', u'400', u'无', u'1')
        q.exec_(insertValueString)
def madeComboBoxItemsFromDatabase(self, columnName, tableName, comboBoxName):
    cmd="""
distinctList=sqlDistinctItems(u"%s", u"%s") 
self.%s.clear()
#print distinctList
self.%s.addItems(distinctList)
    """  % (columnName, tableName, comboBoxName, comboBoxName)
    exec(cmd)

def globalSetTableViewAb(self, tableViewName):
    cmd=self.tr("""
self.%s.setSelectionBehavior(QAbstractItemView.SelectRows)
self.%s.verticalHeader().setVisible(False)
self.%s.resizeColumnsToContents()
self.%s.resizeRowsToContents()
self.%s.setAlternatingRowColors(True)
""") % (tableViewName, tableViewName, tableViewName, tableViewName, tableViewName)
    exec(cmd)
def generateTable2Search(self, tablename, copytablename, m1, name, m2, size, m7, teacher , viewName):
    q=QSqlQuery()
    q.exec_(QObject().tr("drop table %s") % copytablename)
    q.exec_(QObject().tr("CREATE TABLE %s AS SELECT * FROM %s WHERE %s='%s' and %s='%s' and %s='%s' ") %(copytablename,  tablename, m1, name, m2, size, m7, teacher))
    cmd="""
self.model=QSqlTableModel(self)
self.model.setTable('%s') 
self.model.setEditStrategy(QSqlTableModel.OnManualSubmit) 
self.model.select()
self.%s.setModel(self.model)
self.%s.show()
    """ % (copytablename,  viewName, viewName)
    exec(cmd)


innerTable=u"inner_table"
class MyMainWindow(QMainWindow, Ui_main.Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.showUpdateMachineInfo)
        self.pushButton_3.clicked.connect(self.showAddMachineInfo)
        self.pushButton_5.clicked.connect(self.showUpdateErrorInfo)
        self.pushButton_6.clicked.connect(self.showAddErrorInfo)
        self.updateComboBox()
        self.back2AllDataList()
        self.pushButton_7.clicked.connect(self.queryFunc)
        self.pushButton_8.clicked.connect(self.back2AllDataList)
        self.pushButton_4.clicked.connect(self.export2excel)
    def unionData(self):
        q=QSqlQuery()
        q.exec_(self.tr("drop table %s") % innerTable)
        q.exec_(self.tr(""" 
CREATE TABLE %s
AS SELECT %s.*,%s.%s,%s.%s,%s.%s,%s.%s,%s.%s
FROM %s
INNER JOIN %s
ON %s.%s=%s.%s
""") % ( innerTable, 
mTable,  eTable, E1, eTable, E2, eTable, E3, eTable, E4, eTable, E5, 
mTable, 
eTable,  
mTable, M8, eTable, E0 ))
    def setTableViewAb(self):
        globalSetTableViewAb(self, self.tr("tableView"))
        '''
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.resizeColumnsToContents()
        self.tableView.resizeRowsToContents()
        self.tableView.setAlternatingRowColors(True)
        '''
    def showUpdateMachineInfo(self):
        dialog=UpdateMachineDialog()
        if dialog.spinBox.value()==0:
            QMessageBox.information(self,self.tr("通知"),  self.tr("数据库为空，请先到添加信息窗口添加!"))
        else:
            dialog.exec_()
        self.updateComboBox()
        self.back2AllDataList()
    def showAddMachineInfo(self):
        dialog=AddMachineDialog()
        dialog.exec_()
        self.updateComboBox()
        self.back2AllDataList()
    def showUpdateErrorInfo(self):
        dialog=UpdateErrorDialog()
        if dialog.spinBox.value()==0:
            QMessageBox.information(self,self.tr("通知"),  self.tr("数据库为空，请先到添加信息窗口添加!"))
        else:
            dialog.exec_()
        self.updateComboBox()
        self.back2AllDataList()
    def showAddErrorInfo(self):
        dialog=AddErrorDialog()
        dialog.exec_()
        self.updateComboBox()
        self.back2AllDataList()
    def queryFunc(self):
        name=self.comboBox_3.currentText()
        size=self.comboBox_2.currentText()
        teacher=self.comboBox.currentText()
        self.model.setFilter(QObject().tr("仪器名称='%s' and 型号='%s' and 仪器负责老师='%s'") %(name, size, teacher))
        self.model.select()
    def back2AllDataList(self):
        self.unionData()
        self.model=QSqlTableModel(self)
        self.tableName=innerTable
        self.model.setTable(self.tableName)
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setTableViewAb()
    def updateComboBox(self):
        madeComboBoxItemsFromDatabase(self, M7, mTable, self.tr('comboBox'))
        madeComboBoxItemsFromDatabase(self, M1, mTable, self.tr('comboBox_3'))
        madeComboBoxItemsFromDatabase(self, M2, mTable, self.tr('comboBox_2'))
    def export2excel(self):
        style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')
        wb = xlwt.Workbook()
        ws = wb.add_sheet('A Test Sheet')
        q=QSqlQuery()
        q.exec_("select * from %s" % innerTable)
        i=0
        while q.next():
            j=0
            while q.value(j):
                ws.write(i, j, q.value(j), style0)
                print q.value(j)
                j+=1
            i+=1
        wb.save('example.xls')
        pass
class UpdateMachineDialog(QDialog, Ui_updateMachineInfo.Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.updateMachInfo(1)
        self.pushButton_4.hide()
        #self.pushButton_4.clicked.connect(self.updateMachInfo)
        self.pushButton_2.clicked.connect(self.modifyMachInfo)
        self.pushButton_3.clicked.connect(self.deleteMachInfo)
        self.pushButton.clicked.connect(self.queryFunc)
        self.pushButton_6.clicked.connect(self.searchAll)
    @Slot(int)
    def on_spinBox_valueChanged(self, p0):
        #self.updateMachInfo(p0)
        self.machineWidgetList=[]
        self.machineWidgetList.append(self.tr("spinBox"))
        self.machineWidgetList.append(self.tr("lineEdit_7"))
        self.machineWidgetList.append(self.tr("lineEdit_4"))
        self.machineWidgetList.append(self.tr("dateEdit"))
        self.machineWidgetList.append(self.tr("textEdit"))
        self.machineWidgetList.append(self.tr("textEdit_2"))
        self.machineWidgetList.append(self.tr("doubleSpinBox"))
        self.machineWidgetList.append(self.tr("lineEdit_3"))
        self.machineWidgetList.append(self.tr("comboBox_4"))
        columnname=[M0, M1, M2, M3, M4, M5, M7, M8]
        id=p0
        tablename=mTable
        self.comboBoxDict={}
        self.__updateComboBox(E0, eTable, self.tr("comboBox_4"), self.comboBoxDict)
        #print self.comboBoxDict
        self.__database2widget(mTable, M0, id, self.machineWidgetList)
    @Slot(int)
    def on_comboBox_4_activated(self, index):
        q=QSqlQuery()
        q.exec_(self.tr("select %s from %s where %s=%d") %(E1, eTable, E0, index+1))
        if q.next():
            self.label_14.setText(q.value(0))
    @Slot(QModelIndex)
    def on_tableView_clicked(self, index):
        '''
        id=self.model.record(index.row()).value(self.tr("%s") % M0)
        self.updateMachInfo(id)
        '''
        self.machineWidgetList=[]
        self.machineWidgetList.append(self.tr("spinBox"))
        self.machineWidgetList.append(self.tr("lineEdit_7"))
        self.machineWidgetList.append(self.tr("lineEdit_4"))
        self.machineWidgetList.append(self.tr("dateEdit"))
        self.machineWidgetList.append(self.tr("textEdit"))
        self.machineWidgetList.append(self.tr("textEdit_2"))
        self.machineWidgetList.append(self.tr("doubleSpinBox"))
        self.machineWidgetList.append(self.tr("lineEdit_3"))
        self.machineWidgetList.append(self.tr("comboBox_4"))
        columnname=[M0, M1, M2, M3, M4, M5, M7, M8]
        id=self.model.record(index.row()).value(self.tr("%s") % M0)
        tablename=mTable
        self.comboBoxDict={}
        self.__updateComboBox(E0, eTable, self.tr("comboBox_4"), self.comboBoxDict)
        #print self.comboBoxDict
        self.__database2widget(mTable, M0, id, self.machineWidgetList)
    def database2Interface(self, id):
        q=QSqlQuery()
        q.exec_(QObject().tr("select * from machine where 仪器编号='%d'") %id)
        if q.next():
            self.spinBox.setValue(id)
            self.lineEdit_7.setText(q.value(1))
            self.lineEdit_4.setText(q.value(2))
            if len(q.value(3).split('/'))>=3:
                yearV=int( q.value(3).split('/')[0])
                monthV= int( q.value(3).split('/')[1])
                dayV=int( q.value(3).split('/')[2])
                dateV=QDate(yearV, monthV, dayV)
                self.dateEdit.setDate(dateV)
            self.textEdit.setText(q.value(4))
            self.textEdit_2.setText(q.value(5))
            self.doubleSpinBox.setValue(float(q.value(6)))
            self.lineEdit_3.setText(q.value(7))
            #self.comboBox_4.setItemText(0, q.value(8))
        else:
            self.lineEdit_7.setText(None)
            self.lineEdit_4.setText(None)
            self.dateEdit.setDate(QDate.currentDate())
            self.textEdit.setText(None)
            self.textEdit_2.setText(None)
            self.doubleSpinBox.setValue(0.00)
            self.lineEdit_3.setText(None)
        madeComboBoxItemsFromDatabase(self, M7, mTable, self.tr('comboBox'))
        madeComboBoxItemsFromDatabase(self, M1, mTable, self.tr('comboBox_2'))
        madeComboBoxItemsFromDatabase(self, M2, mTable, self.tr('comboBox_3'))
        madeComboBoxItemsFromDatabase(self, E0, eTable, self.tr('comboBox_4'))
        spinMax=maxData(M0, mTable)
        if spinMax==self.tr(""):
            self.spinBox.setRange(0, 0)
        else:
            self.spinBox.setRange(1, spinMax)
    def madeComboBoxItemsFromDatabase(self, columnName, tableName, comboBoxName):
        cmd="""
distinctList=sqlDistinctItems(self.tr("%s"), self.tr("%s")) 
self.%s.clear()
self.%s.addItems(distinctList)
            """  % (columnName, tableName, comboBoxName, comboBoxName)
        exec(cmd)
    def updateMachInfo(self, id=None):
        if id==None:
            id=self.spinBox.value()
            '''
        self.database2Interface(id)
        self.model=QSqlTableModel(self)
        self.model.setTable("machine")
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        globalSetTableViewAb(self, self.tr("tableView"))
        #globalSetTableViewAb(self, self.tr("machine"))
        self.model.select()
        '''
        #self.updateMachInfo(p0)
        self.model=QSqlTableModel(self)
        self.machineWidgetList=[]
        self.machineWidgetList.append(self.tr("spinBox"))
        self.machineWidgetList.append(self.tr("lineEdit_7"))
        self.machineWidgetList.append(self.tr("lineEdit_4"))
        self.machineWidgetList.append(self.tr("dateEdit"))
        self.machineWidgetList.append(self.tr("textEdit"))
        self.machineWidgetList.append(self.tr("textEdit_2"))
        self.machineWidgetList.append(self.tr("doubleSpinBox"))
        self.machineWidgetList.append(self.tr("lineEdit_3"))
        self.machineWidgetList.append(self.tr("comboBox_4"))
        columnname=[M0, M1, M2, M3, M4, M5, M7, M8]
        tablename=mTable
        self.comboBoxDict={}
        self.__updateComboBox(E0, eTable, self.tr("comboBox_4"), self.comboBoxDict)
        #print self.comboBoxDict
        self.__database2widget(mTable, M0, id, self.machineWidgetList)
        self.__updateComboBox(M1, mTable, self.tr("comboBox_2"))
        self.__updateComboBox(M2, mTable, self.tr("comboBox_3"))
        self.__updateComboBox(M7, mTable, self.tr("comboBox"))
        self.__updateTable(mTable)
        self.__setSpinBoxRange()
    def modifyMachInfo(self):
        id=self.spinBox.value()
        q=QSqlQuery()
        q.exec_(QObject().tr("update machine set 仪器名称 = '%s' where 仪器编号=%d")%(self.lineEdit_7.text(), id))
        q.exec_(QObject().tr("update machine set 型号 = '%s' where 仪器编号=%d")%(self.lineEdit_4.text(), id))
        q.exec_(QObject().tr("update machine set 出厂日期 = '%s/%s/%s' where 仪器编号=%d")%(self.dateEdit.date().year(), self.dateEdit.date().month(), self.dateEdit.date().day(), id))
        q.exec_(QObject().tr("update machine set 技术参数 = '%s' where 仪器编号=%d")%(self.textEdit.toPlainText() , id))
        q.exec_(QObject().tr("update machine set 用途及特点 = '%s' where 仪器编号=%d")%(self.textEdit_2.toPlainText(), id))
        q.exec_(QObject().tr("update machine set 实验价格 = '%s' where 仪器编号=%d")%(self.doubleSpinBox.value(), id))
        q. exec_(QObject().tr("update machine set 仪器负责老师 = '%s' where 仪器编号=%d")%(self.lineEdit_3.text(), id))
        q. exec_(QObject().tr("update machine set 故障编号 = '%s' where 仪器编号=%d")%(self.comboBox_4.currentText(), id))
        self.updateMachInfo(id)
    def deleteMachInfo(self): 
        id=self.spinBox.value()
        sqlDeleteInfo(mTable, M0, id) 
        self.updateMachInfo(id)
    def queryFunc(self):
        name=self.comboBox_2.currentText()
        size=self.comboBox_3.currentText()
        teacher=self.comboBox.currentText()
        columnlist=[M1, M2, M7]
        datalist=[name, size, teacher]
        self.__changeDatabaseWhenSearch(mTable, mTableCopy, columnlist, datalist )
        self.__updateTable(mTableCopy)
        #generateTable2Search(self, mTable, mTableCopy, M1, name, M2, size, M7, teacher, self.tr("tableView"))
    def searchAll(self):
        #self.__changeDatabaseWhenBackToAll( mTable, mTableCopy)
        self.__updateTable(mTable)
    def __updateComboBox(self, columnname, tablename, widgetname, comboBoxDict={}):
        #self.__updateComboBox(E0, eTable, self.tr("comboBox_4"), self.comboBoxDict)
        comboBoxDict.clear()
        exec("self.%s.clear()"% widgetname)
        q=QSqlQuery()
        q.exec_(self.tr( "SELECT DISTINCT %s FROM %s ") %( columnname, tablename))
        i=0
        while q.next():
            comboBoxDict[q.value(0)]=i
            cmd =  "self.%s.insertItem(%d,self.tr('%s')) " % (widgetname, i , q.value(0))
            exec(cmd)
            i+=1
    def __database2widget(self, tablename, columnname, id, widgetList):
        q=QSqlQuery()
        dataList=[]
        q.exec_(QObject().tr("SELECT * FROM %s WHERE %s='%d'") %(tablename, columnname, id))
        if q.next():
            for i in xrange (len(widgetList)):
                dataList.append(q.value(i))
        for i in xrange(len(dataList)):
            if widgetList[i].startswith('spinBox'):
                cmd=self.tr("self.%s.setValue(%d) " ) % (widgetList[i], dataList[i])
                exec(cmd)
            elif widgetList[i].startswith('textEdit'):
                cmd=self.tr("self.%s.setText(self.tr('%s'))") % (widgetList[i], dataList[i])
                exec(cmd)
            elif widgetList[i].startswith('comboBox'):
                tempValue='-1'
                cmd=self.tr("tempValue=self.comboBoxDict[%s]") % (dataList[i])
                exec(cmd)
                cmd=self.tr("self.%s.setCurrentIndex(%d)") % (widgetList[i],  tempValue) # More modify needed!
                exec(cmd)
            elif widgetList[i].startswith('doubleSpinBox'):
                cmd=self.tr("self.%s.setValue(float(%s))" % (widgetList[i], dataList[i]))
                exec(cmd)
            elif widgetList[i].startswith('lineEdit'):
                cmd=self.tr("self.%s.setText(self.tr('%s'))") % (widgetList[i], dataList[i])
                exec(cmd)
            elif widgetList[i].startswith('dateEdit'):
                if len(dataList[i].split('/'))>=3:
                    yearV=int( dataList[i].split('/')[0])
                    monthV= int( dataList[i].split('/')[1])
                    dayV=int( dataList[i].split('/')[2])
                    dateV=QDate(yearV, monthV, dayV)
                    cmd=self.tr("self.%s.setDate(QDate(%s,%s,%s))") % (widgetList[i], yearV, monthV, dayV)
                    exec(cmd)
                #self.doubleSpinBox.setValue(float(q.value(6)))#########################
            else:
                pass
        pass
    def __updateTable(self, tablename):
        self.model.setTable(tablename)
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        globalSetTableViewAb(self, 'tableView')
        #self.model.select()
        pass
    def __changeDatabaseWhenSearch(self, tablename, copytablename, columnlist, datalist ):
        sqldatalist=[]
        for i in xrange(len(columnlist)):
            sqldatalist.append("%s='%s'" % (columnlist[i], datalist[i]))
        sqldatalist=" and ".join(sqldatalist)
        q=QSqlQuery()
        q.exec_(QObject().tr("drop table %s") % copytablename)
        q.exec_(QObject().tr("CREATE TABLE %s AS SELECT * FROM %s WHERE %s") %(copytablename,  tablename, sqldatalist))
        pass
    def __changeDatabaseWhenBackToAll(self, tablename, copytablename):
        q=QSqlQuery()
        q.exec_(QObject().tr("drop table %s") % copytablename)
        q.exec_(QObject().tr("CREATE TABLE %s AS SELECT * FROM %s ") %(copytablename,  tablename))
        pass
    def __updatewidget2database(self, tablename, setlist, columnname, id):
        #UPDATE Person SET FirstName = 'Fred' WHERE LastName = 'Wilson'
        '''
        self.widgetRelatedWidgetList=[]
        self.databaseRelatedColumnname=[]
        self.datalist=self.__getDatalistFromWidgetlist(self.widgetRelatedDatabaseColumnname, self.databaseRelatedWidgetList)
        setlist=[]
        for i in xrange(len(self.datalist)):
            setlist.append(self.tr(" %s=%s ") % (self.widgetRelatedDatabaseColumnname[i], self.datalist[i]))
        #print setlist
        setlist=(',').join(setlist)
        id=self.spinBox.value()
        self.updateDialogdata2Database(eTable, setlist, E0, id)
        self.updateDialog()
        pass
        self.__updatewidget2database(mTable, setlist, M0, id)
        '''
        q=QSqlQuery()
        execString = self.tr( "UPDATE %s SET %s WHERE %s=%s") %(tablename, setlist, columnname, id)
        q.exec_(execString)
    def __getDatalistFromWidgetlist(self, columnnamelist, widgetlist):
        dataList=[]
        value=self.tr('')
        for i in xrange(len(widgetlist)):
            if widgetlist[i].startswith('spinBox'):
                cmd="dataList.append(self.tr( str( self.%s.value())) )" % widgetlist[i]
                exec(cmd)
            elif widgetlist[i].startswith('textEdit'):
                cmd="value=self.%s.toPlainText()" % widgetlist[i]
                exec(cmd)
                dataList.append(self.tr(" '%s' ")% value) 
            elif widgetlist[i].startswith('comboBox'):
                cmd="value=self.%s.currentText()" % widgetlist[i]
                exec(cmd)
                dataList.append(self.tr("'%s'")% value) 
            elif widgetlist[i].startswith('lineEdit'):
                cmd="value=self.%s.text()" %widgetlist[i]
                exec(cmd)
            #elif widgetlist[i].startswith('dateEdit'):
                #cmd="value=%s/%s/%s"
            #elif widget[i].startswith('doubleSpinBox'):
            #cmd
            else:
                pass
        return dataList
        pass
    def __setSpinBoxRange(self):
        idMax=maxData(M0, mTable)
        if idMax==self.tr(""):
            idMax=0
            self.machineWidgetList=[]
            self.machineWidgetList.append(self.tr("spinBox"))
            self.machineWidgetList.append(self.tr("lineEdit_7"))
            self.machineWidgetList.append(self.tr("lineEdit_4"))
            self.machineWidgetList.append(self.tr("dateEdit"))
            self.machineWidgetList.append(self.tr("textEdit"))
            self.machineWidgetList.append(self.tr("textEdit_2"))
            self.machineWidgetList.append(self.tr("doubleSpinBox"))
            self.machineWidgetList.append(self.tr("lineEdit_3"))
            self.machineWidgetList.append(self.tr("comboBox_4"))
            self.machineWidgetList.append(self.tr("pushButton_2"))
            self.machineWidgetList.append(self.tr("pushButton_3"))
            for item in self.machineWidgetList:
                cmd="self.%s.setEnabled(False)" % item
                exec(cmd)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(idMax)
        pass
class UpdateErrorDialog(QDialog, Ui_updateErrorInfo.Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.__setSpinBoxRange()
        self.comboBox.setEditable(True)
        self.model=QSqlTableModel(self)
        self.comboBoxDict={}
        self.__setSpinBoxRange()
        self.updateDialog()
        self.pushButton.clicked.connect(self.modifyAndUpdate)
        self.pushButton_2.clicked.connect(self.deleteAndUpdate)
    def updateDialog(self):
        self.__updateTable()
        self.__updateComboBox(E5, eTable, self.tr("comboBox"), self.comboBoxDict)
        self.__database2widget(self.spinBox.value(), ["spinBox","textEdit", "textEdit_2", "textEdit_3", "textEdit_4",  "comboBox"], E0, eTable)
    def modifyAndUpdate(self):  
        self.databaseRelatedWidgetList=["textEdit", "textEdit_2", "textEdit_3", "textEdit_4",  "comboBox"]
        self.widgetRelatedDatabaseColumnname=[E1,E2, E3, E4, E5]
        self.datalist=self.__getDataListFromWidgetlist(self.widgetRelatedDatabaseColumnname, self.databaseRelatedWidgetList)
        setlist=[]
        for i in xrange(len(self.datalist)):
            setlist.append(self.tr(" %s=%s ") % (self.widgetRelatedDatabaseColumnname[i], self.datalist[i]))
        #print setlist
        setlist=(',').join(setlist)
        id=self.spinBox.value()
        self.updateDialogdata2Database(eTable, setlist, E0, id)
        self.updateDialog()
        pass
    def deleteAndUpdate(self):
        id=self.spinBox.value()
        self.__sqlDelete(eTable, E0, id, mTable, M8 )
        self.updateDialog()
    @Slot(QModelIndex)
    def on_tableView_clicked(self, index):
        id=self.model.record(index.row()).value(self.tr("%s") % E0)
        self.__updateComboBox(E5, eTable, self.tr("comboBox"), self.comboBoxDict)
        self.__database2widget(id, ["spinBox","textEdit", "textEdit_2", "textEdit_3", "textEdit_4",  "comboBox"], E0, eTable)
        pass
    @Slot(int)
    def on_spinBox_valueChanged(self, p0):
        self.databaseRelatedWidgetList=["spinBox","textEdit", "textEdit_2", "textEdit_3", "textEdit_4",  "comboBox"]
        self.comboBoxDict={}
        self.__updateComboBox(E5, eTable, self.tr("comboBox"), self.comboBoxDict)
        self.__database2widget(p0, self.databaseRelatedWidgetList, E0, eTable)
    def updateDialogdata2Database(self, tablename, setlist, columnname, id):
        #UPDATE Person SET FirstName = 'Fred' WHERE LastName = 'Wilson'
        q=QSqlQuery()
        execString = self.tr( "UPDATE %s SET %s WHERE %s=%s") %(tablename, setlist, columnname, id)
        q.exec_(execString)
    def __sqlDelete(self, tablename, columnname, id, tablename_2, columnname_2):
        #DELETE FROM 表名称 WHERE 列名称 = 值
        q=QSqlQuery()
        q.exec_("DELETE FROM %s WHERE %s = %s" %(tablename, columnname, id))
        #QObject().tr("update %s set %s=%s-1 where %s>%d")%( tableName,columnName, columnName, columnName, id )
        q.exec_("update %s set %s=%s-1 where %s>%d"%( tablename,columnname, columnname, columnname, id ))
        q.exec_("update %s set %s=%s where %s=%d"%( tablename_2,columnname_2,NoErrorNo,  columnname_2, id))
        q.exec_("update %s set %s=%s-1 where %s>%d"%( tablename_2,columnname_2, columnname_2, columnname_2, id))
        pass
    def __updateTable(self):
        self.model.setTable(eTable)
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        globalSetTableViewAb(self, 'tableView')
        self.model.select()
        pass
    def __updateComboBox(self, columnname, tablename, widgetname, comboBoxDict):
        comboBoxDict.clear()
        exec("self.%s.clear()"% widgetname)
        q=QSqlQuery()
        q.exec_(self.tr( "SELECT DISTINCT %s FROM %s ") %( columnname, tablename))
        i=0
        while q.next():
            comboBoxDict[q.value(0)]=i
            cmd =  "self.%s.insertItem(%d,self.tr('%s')) " % (widgetname, i , q.value(0))
            exec(cmd)
            i+=1
    def __setSpinBoxRange(self):
        idMax=maxData(E0, eTable)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(idMax)
        pass
    def __getDataListFromWidgetlist(self, columnnamelist, widgetlist):
        dataList=[]
        value=self.tr('')
        for i in xrange(len(widgetlist)):
            if widgetlist[i].startswith('spinBox'):
                cmd="dataList.append(self.tr( str( self.%s.value())) )" % widgetlist[i]
                exec(cmd)
            elif widgetlist[i].startswith('textEdit'):
                cmd="value=self.%s.toPlainText()" % widgetlist[i]
                exec(cmd)
                dataList.append(self.tr(" '%s' ")% value) 
            elif widgetlist[i].startswith('comboBox'):
                cmd="value=self.%s.currentText()" % widgetlist[i]
                exec(cmd)
                dataList.append(self.tr("'%s'")% value) 
            else:
                pass
        return dataList
    def __database2widget(self, id, widgetList, columnname, tablename):
        q=QSqlQuery()
        dataList=[]
        q.exec_(QObject().tr("SELECT * FROM %s WHERE %s='%d'") %(tablename, columnname, id))
        if q.next():
            for i in xrange (len(widgetList)):
                dataList.append(q.value(i))
        for i in xrange(len(dataList)):
            if widgetList[i].startswith('spinBox'):
                cmd=self.tr("self.%s.setValue(%d) " ) % (widgetList[i], dataList[i])
                exec(cmd)
            elif widgetList[i].startswith('textEdit'):
                cmd=self.tr("self.%s.setText(self.tr('%s'))") % (widgetList[i], dataList[i])
                exec(cmd)
            elif widgetList[i].startswith('comboBox'):
                cmd=self.tr("self.%s.setCurrentIndex(%d)") % (widgetList[i],  self.comboBoxDict[dataList[i]]) 
                exec(cmd)
            else:
                pass
        pass
class AddMachineDialog(QDialog, Ui_addMachineInfo.Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        madeComboBoxItemsFromDatabase(self, E0, eTable, self.tr('comboBox'))
        self.widgetList=['lineEdit', 'lineEdit_2', 'dateEdit', 
        'textEdit', 'textEdit_2', 'doubleSpinBox','lineEdit_3', 'comboBox']
        self.addMachineInfom()
        self.countMachineInfo()
        self.pushButton.clicked.connect(self.addMachineInfom)
        self.pushButton_2.clicked.connect(self.updateMachineInfo)
        self.pushButton_3.clicked.connect(self.countMachineInfo)
    def addMachineInfom(self):
        ptr= maxData(M0, mTable)
        if ptr==self.tr(""):
            ptr=0
        self.spinBox.setValue(ptr+1)
        for widgetItem in self.widgetList:
            cmd='self.%s.setEnabled(True)' % widgetItem
            exec(cmd)
            self.widgetInit(widgetItem)
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(True)
    def widgetInit(self, widgetItem):
        if widgetItem.startswith('lineEdit') or widgetItem.startswith('textEdit'):
            cmd=QObject().tr("self.%s.setText(None)") % widgetItem
            exec(cmd)
        if widgetItem.startswith('dateEdit'):
            cmd=QObject().tr("self.%s.setDate(QDate.currentDate())") % widgetItem
            exec(cmd)
        if widgetItem.startswith('doubleSpinBox'):
            cmd=QObject().tr("self.%s.setValue(0.00)") % widgetItem
            exec(cmd)
    def updateMachineInfo(self):
        ptr= maxData(M0, mTable)
        if ptr==self.tr(""):
            ptr=0
        self.spinBox.setValue(ptr+1)
        dateAdd='%s/%s/%s' % (self.dateEdit.date().year(), self.dateEdit.date().month(), self.dateEdit.date().day())
        addDataFunction(self.spinBox.value(), self.lineEdit.text(),  self.lineEdit_2.text(),  dateAdd, self.textEdit.toPlainText(), self.textEdit_2.toPlainText(),  self.doubleSpinBox.value(), self.lineEdit_3.text(), self.comboBox.currentText())
        for widgetItem in self.widgetList:
            cmd='self.%s.setEnabled(False)' % widgetItem
            exec(cmd)
        id=self.spinBox.value()
        q=QSqlQuery()
        q.exec_(QObject().tr("select * from %s where %s='%d'") %(mTable, M0, id))
        if q.next():
            self.lineEdit.setText(q.value(1))
            self.lineEdit_2.setText(q.value(2))
            if len(q.value(3).split('/'))>=3:
                yearV=int( q.value(3).split('/')[0])
                monthV= int( q.value(3).split('/')[1])
                dayV=int( q.value(3).split('/')[2])
                dateV=QDate(yearV, monthV, dayV)
                self.dateEdit.setDate(dateV)
            self.textEdit.setText(q.value(4))
            self.textEdit_2.setText(q.value(5))
            self.doubleSpinBox.setValue(float(q.value(6)))
            self.lineEdit_3.setText(q.value(7))
        self.pushButton_2.setEnabled(False)
        self.pushButton.setEnabled(True)
        QMessageBox.information(self,self.tr("通知"),  self.tr("信息添加成功，点击“继续添加”按钮继续添加，或者点击”关闭“退出本窗口!"))
    def countMachineInfo(self):
        machineCount=sqlColumnCount(M0, mTable)
        self.label_10.setText(str(machineCount))
    @Slot(int)
    def on_comboBox_activated(self, index):
        q=QSqlQuery()
        q.exec_(self.tr("select %s from %s where %s=%d") %(E1, eTable, E0, index+1))
        if q.next():
            self.label_14.setText(q.value(0))
        
class AddErrorDialog(QDialog, Ui_addErrorInfo.Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.__getWidgetList()
        self.comboBoxDict={}
        self.comboBox.setEditable(True)
        self.updateErrorDialog4Add()
        self.pushButton.clicked.connect(self.updateErrorDialog4Add)
        self.pushButton_2.clicked.connect(self.addErrorInfo2Database)
        self.pushButton_3.clicked.connect(self.countErrorInfo)
    def __getWidgetList(self):
        self.widgetList=['spinBox', 'textEdit', 'textEdit_2', 'textEdit_3', 'textEdit_4', 'comboBox']
    def __widgetInit(self, widgetItem):
        if widgetItem.startswith('lineEdit') or widgetItem.startswith('textEdit'):
            cmd=QObject().tr("self.%s.setText(None)") % widgetItem
            exec(cmd)
        if widgetItem.startswith('dateEdit'):
            cmd=QObject().tr("self.%s.setDate(QDate.currentDate())") % widgetItem
            exec(cmd)
        if widgetItem.startswith('doubleSpinBox'):
            cmd=QObject().tr("self.%s.setValue(0.00)") % widgetItem
            exec(cmd)
    def addErrorInfo2Database(self):
        ptr=maxData(E0, eTable)
        self.spinBox.setValue(ptr+1)
        self.dataList=self.__getDataList(self.widgetList)
        #print self.dataList
        self.__dialog2database(self.dataList, eTable)
        self.__updateComboBox(E5, eTable, self.tr('comboBox'), self.comboBoxDict)
        for widgetItem in self.widgetList:
            cmd='self.%s.setEnabled(False)' % widgetItem
            exec(cmd)
        self.__database2dialog(eTable, self.widgetList,E0,  ptr+1)
        self.pushButton_2.setEnabled(False)
        QMessageBox.information(self,self.tr("通知"),  self.tr("信息添加成功，点击“继续添加”按钮继续添加，或者点击”关闭“退出本窗口!"))
        self.pushButton.setEnabled(True)
        pass
    def __database2dialog(self, tablename, widgetList, columnname, id):
        q=QSqlQuery()
        dataList=[]
        q.exec_(QObject().tr("SELECT * FROM %s WHERE %s='%d'") %(tablename, columnname, id))##
        if q.next():
            for i in xrange (len(widgetList)):
                dataList.append(q.value(i))
        #print dataList
        for i in xrange(len(dataList)):
            if widgetList[i].startswith('spinBox'):
                cmd=self.tr("self.%s.setValue(%d) " ) % (widgetList[i], dataList[i])
                exec(cmd)
            elif widgetList[i].startswith('textEdit'):
                cmd=self.tr("self.%s.setText(self.tr('%s'))") % (widgetList[i], dataList[i])
                exec(cmd)
            elif widgetList[i].startswith('comboBox'):
                cmd=self.tr("self.%s.setCurrentIndex(%d)") % (widgetList[i],  self.comboBoxDict[dataList[i]])
                exec(cmd)
            else:
                pass
    def __updateComboBox(self, columnname, tablename, widgetname, comboBoxDict):
        comboBoxDict.clear()
        exec("self.%s.clear()"% widgetname)
        q=QSqlQuery()
        q.exec_(self.tr( "SELECT DISTINCT %s FROM %s ") %( columnname, tablename))
        i=0
        while q.next():
            comboBoxDict[q.value(0)]=i 
            cmd = self.tr("self.%s.insertItem(%d,self.tr('%s')) ") % (widgetname, i , q.value(0))
            exec(cmd)
            i+=1
        
    def __getDataList(self, databaseRelatedWidgetList):
        dataList=[]
        value=self.tr('')
        for widgetItem in databaseRelatedWidgetList:
            if widgetItem.startswith('spinBox'):
                cmd="dataList.append(self.tr( str( self.%s.value())) )" % widgetItem
                exec(cmd)
            elif widgetItem.startswith('textEdit'):
                cmd="value=self.%s.toPlainText()" % widgetItem
                exec(cmd)
                dataList.append(self.tr(" '%s' ")% value) 
            elif widgetItem.startswith('comboBox'):
                cmd="value=self.%s.currentText()" % widgetItem
                exec(cmd)
                dataList.append(self.tr("'%s'")% value) 
            else:
                pass
        return dataList
    def __dialog2database(self, dataList, tablename):
        q=QSqlQuery()
        # INSERT INTO 表名称 VALUES (值1, 值2,....)
        dataString=','.join(dataList)
        dataString='('+dataString+')'
        q.exec_(self.tr("INSERT INTO %s VALUES %s") % (tablename, dataString))
        pass
    def updateErrorDialog4Add(self):
        ptr=maxData(E0, eTable)
        if ptr==self.tr(""):
            ptr=1
        self.spinBox.setValue(ptr+1)
        for widgetItem in self.widgetList:
            cmd='self.%s.setEnabled(True)' % widgetItem
            exec(cmd)
            self.__widgetInit(widgetItem)
        self.spinBox.setEnabled(False)
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(True)
        self.__updateComboBox(E5, eTable, self.tr('comboBox'), self.comboBoxDict)
        self.countErrorInfo()
    def countErrorInfo(self):
        errorCount=sqlColumnCount(E0, eTable)
        self.label_9.setText(str(errorCount))
        pass
class LoginDialog(QDialog, Ui_login.Ui_Dialog):
    
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.lineEdit.setText('admin')
        self.lineEdit_2.setText("admin")
        self.acceptPushButton.clicked.connect(self.loginCall)
        
    def loginCall(self):
        if self.lineEdit.text() == 'admin' and self.lineEdit_2.text()=='admin':
            self.accept()
        else:
            QMessageBox.critical(self, 'Error', 'User name or password error')  

if __name__=="__main__":
    app=QApplication(sys.argv)
    createConnection()
    #createTableMachine()
    #createTableErr()
    dialog=LoginDialog()
    if dialog.exec_():
        win=MyMainWindow()
        win.show()
        sys.exit(app.exec_())
    
