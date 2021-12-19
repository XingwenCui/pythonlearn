#!/usr/bin/env python
# coding: utf-8

# ## 定义名片列表变量
# - 在card_tools文件顶部增加一个列表变量
#  - card_list = []
# - 所有名片相关操作，都需要这个列表，所有设置在顶部
# - 程序刚运行时，没有数据，所有是空列表

# In[16]:


#记录所有名片
card_list = []


# ## 显示名片

# In[4]:


def show_menu():
    
    '''显示菜单'''
    print("*"*50)
    print("欢迎使用【名片管理系统】V1.0")
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print("")
    print("0.退出系统")
    print("*"*50)
    


# ## 新增名片

# In[5]:


def new_card():
    
    '''新增名片'''
    print("-"*50)
    print("新增名片")
    
    #1.提示用户输入名片的详细信息
    name = input("name:")
    phone = input("phone number")
    qq = input("qq number")
    email = input("email number")
    
    #2.使用用户输入的信息建立一个名片字典
    card_dict = {"name":name,
                 "phone":phone,
                 "qq":qq,
                 "email":email}
    
    #3.将名片字典添加到列表
    card_list.append(card_dict)
    print(card_list)
    #4.提示用户添加成功
    print("添加%s的名片成功"%name)


# ## 显示全部

# In[14]:


def show_all():
    
    '''显示全部'''
    print("-"*50)
    print("显示全部")
    
    #判断是否存在名片记录，如果没有，提示用户并返回
    if len(card_list) == 0:
        print("当前没有任何名片记录，请使用新增功能添加名片")
        
        return
    #打印表头
    for name in ['name','phone','qq','email']:
        print(name,end="\t\t")
        
    print("")
    
    #打印分割线
    print('='*60)
    
    #遍历名片列表依次输出字典信息
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t"%(card_dict["name"],card_dict["phone"],card_dict["qq"],card_dict["email"]))


# ## 查询名片

# In[18]:


def search_card():
    
    '''查询名片'''
    print("-"*50)
    print("查询名片")
    
    #1.提示用户输入要搜索的姓名
    find_name = input("请输入要搜索的name")
    
    #2.遍历名片列表，查询要搜索的姓名，如果没找到，提示用户
    for card_dict in card_list:
        if card_dict['name'] == find_name:
            for name in ['name','phone','qq','email']:
                print(name,end="\t\t")
            print("="*90)
            print("%s\t\t%s\t\t%s\t\t%s\t\t"%(card_dict["name"],card_dict["phone"],card_dict["qq"],card_dict["email"]))
            deal_card(card_dict)
            break
    else:
        print("抱歉没有找到%s"%find_name)


# ## 处理名片

# In[20]:


def deal_card(find_dict):
    
    print(find_dict)
    
    action_str = input("请选择要执行的操作 1修改 2删除 0返回上级")
    
    if action_str == "1":
        
        find_dict['name'] = input_card(find_dict['name'],'name:')
        find_dict['phone'] = input_card(find_dict['phone'],'phone:')
        find_dict['qq'] = input_card(find_dict['qq'],'qq:')
        find_dict['email'] = input_card(find_dict['email'],'email')
        
        print("修改名片成功！")
        
    elif action_str == "2":
        
        card_list.remove(find_dict)
        print("删除名片")


# ## 自己定义输入函数

# In[19]:


def input_card(dict_value,tip_message):
    #1.提示用户输入内容
    result_str = input(tip_message)
    
    #2.针对用户输入进行判断，如果用户输入了内容，直接返回结果
    if len(result_str) > 0:
        return result_str
    #3.如果没有输入内容，返回字典中原有的值
    else:
        return dict_value

