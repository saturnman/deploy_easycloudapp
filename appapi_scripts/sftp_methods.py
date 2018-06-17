# -*- coding: utf-8 -*- 
import json
import sys
import os
from subprocess import call,check_output,Popen,PIPE
def _addUser(username,password):
    userList = _getUsers(False)
    if username in userList:
        print(json.dumps({'success':False,'msg':'用户已经存在'}))
        return 1
    command1 = ['useradd','-m','-s','/usr/sbin/nologin',username]
    call(command1)
    command2 = ['echo','-e',password+'\\n'+password]
    ps = Popen(command2,stdout=PIPE)
    command3 = ['passwd',username]
    try:
        res = check_output(command3,stdin=ps.stdout)
        print(json.dumps({'success':True}))
        return 0
    except:
        print(json.dumps({'success':False}))
        return 1

def _deleteUser(username):
    userList = _getUsers(False)
    if username not in userList:
        print(json.dumps({'success':False,'msg':'用户不存在'}))
        return 1
    command = ['userdel','-r',username]
    res = call(command)
    if res == 0:
        print(json.dumps({'success':True}))
        return 0
    else:
        print(json.dumps({'success':False}))
        return 1

def _changeUserPwd(username,password):
    userList = _getUsers(False)
    if username not in userList:
        print(json.dumps({'success':False,'msg':'用户不存在'}))
        return 1

    command = ['echo','-e',password+'\\n'+password]
    ps = Popen(command,stdout=PIPE)
    command2 = ['passwd',username]
    res = call(command2,stdin=ps.stdout)
    if res==0:
        print(json.dumps({'success':True}))
        return 0
    else:
        print(json.dumps({'success':False}))
        return 1
def _getUsers(isPrint=True):
    try:
        command = ['cat','/etc/passwd']
        ps = Popen(command,stdout=PIPE)
        command2 = ['grep','/home']
        res = check_output(command2,stdin=ps.stdout)
        itemList = res.strip().split('\n')
        nameList = [name[0:name.index(':')] for name in itemList]
        if isPrint:
            print(json.dumps(nameList))
        return nameList
    except:
        if isPrint:
            print(json.dumps([]))
        return []
methods = {
        'addUser':_addUser,
        'deleteUser':_deleteUser,
        'changeUserPwd':_changeUserPwd,
        'getUsers':_getUsers
        }
methodsDef = {
        'addUser':{
            'numParams':2,
            'paramHints':['用户名','密码']
            },
        'deleteUser':{
            'numParams':1,
            'paramHints':['用户名']
            },
        'changeUserPwd':{
            'numParams':2,
            'paramHints':['用户名','密码']
            },
        'getUsers':{
            'numParams':0,
            'paramHints':[]
        }
}
statesDef = {
    'users':{
        'type':'table',
        'fields':['用户名','密码'],
        'updateApi':'getUsers'
    }
}

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('run with -m or -l and parameters')
        exit(0)
    elif sys.argv[1] == '-l':
        print(json.dumps(methodsDef))
        exit(0)
    elif sys.argv[1] == '-c':
        methodName = sys.argv[2]
        methodNumParams = methodsDef[methodName]['numParams']
        if methodNumParams == 0:
            methods[methodName]()
        elif methodNumParams == 1:
            methods[methodName](sys.argv[3])
        elif methodNumParams == 2:
            methods[methodName](sys.argv[3],sys.argv[4])
