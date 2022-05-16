# 主程序的开始
import datetime
import CXServices.uitls.DatabaseUitls as CXDBUit

def CheckTitle(strs):
    Title = strs
    #print("\n")
    result = []
    res = CXDBUit.Check("*","title",Title)
    if res == "":
        result.append({'title':'','ans':'','id':''})
    else:
        result.append(res)
    #print(result)
    # dic = {}
    # flag = 1
    # for item in result:
    #     dic[flag] = {'title':CXUitls.DictToList(item)[0],'ans':CXUitls.DictToList(item)[1],'id':CXUitls.DictToList(item)[2]}
    #     flag = flag + 1
    return result

def CheckTitleBR(strs):
    Title = strs
    result = CXDBUit.CheckBre("*","title",Title)
    print(result)
    # dic = {}
    # flag = 1
    # for item in result:
    #     dic[flag] = {'title':CXUitls.DictToList(item)[0],'ans':CXUitls.DictToList(item)[1],'id':CXUitls.DictToList(item)[2]}
    #     flag = flag + 1
    # #print(dic)
    return result

def InsertQA(strs,ans):
    Title = strs
    ANS = ans
    CXDBUit.Insert(Title,ANS)
    # state = '100'
    dic =[{'title':'Success insert','ans':datetime.datetime.now().timestamp(),'id':'100'}]
    # dic['state']=state
    return dic

def FunctionSelect(arg,title,anser):
    if arg == '1':
        return CheckTitle(title)
    elif arg == '2':
        return CheckTitleBR(title)
    elif arg == '3':
        return InsertQA(title,anser)

def GetIn(arg,title,anser):
    # print("\n 1 : 清晰查询题目")
    # print("\n 2 : 模糊查询题目")
    # print("\n 3 : 录入题目")
    # print("\n 4 : 修改答案")
    return FunctionSelect(arg,title,anser)