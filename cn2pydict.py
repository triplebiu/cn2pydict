from pypinyin import lazy_pinyin, Style
import argparse
import os

def name2username(cname):
    usernames = set()
    pylist = lazy_pinyin(cname, style=Style.NORMAL)

    # 全拼，小写
    usernames.add("".join(pylist))

    # 全拼，首字母大写
    # usernames.add("".join(list(map( lambda x: x[0].upper()+x[1:], pylist ))))

    # 全拼，姓氏首字母大写
    # usernames.add(pylist[0][0].upper()+pylist[0][1:]+"".join(pylist[1:]))

    # 姓全拼，名首字母
    # usernames.add(pylist[0][0].upper()+pylist[0][1:]+"".join(list(map(lambda x: x[0],pylist[1:]))))
    # usernames.add(pylist[0][0]+pylist[0][1:]+"".join(list(map(lambda x: x[0],pylist[1:]))))

    # 姓氏，小写
    # usernames.add(pylist[0])

    # 姓氏，首字母大写
    # usernames.add(pylist[0][0].upper()+pylist[0][1:])

    # 全首字母
    usernames.add("".join(list(map(lambda x: x[0],pylist))))

    # 全首字母，第一个大写
    # usernames.add(pylist[0][0].upper()+"".join(list(map(lambda x: x[0],pylist[1:]))))

    # 名
    # usernames.add("".join(pylist[1:]))

    # 名，首字母
    # usernames.add("".join(list(map(lambda x: x[0],pylist[1:]))))

    return usernames


def build_list(listFile):
    with open(listFile, "r") as fd:
        return list(map(lambda x:x.strip(), fd.readlines()))

def main():
    usernames = set()
    # Creating a parser
    parser=argparse.ArgumentParser(description="中文名转用户名字典")

    groupUser = parser.add_mutually_exclusive_group(required=True)
    groupUser.add_argument('-n',dest="name",help="姓名，可以用逗号分隔。")
    groupUser.add_argument('-N',dest='nameList',help="姓名列表文件")

    parser.add_argument("-o",dest="outFile", help="输出生成的用户名字典")

    args=parser.parse_args()

    nameList = []
    if args.name is not None:
        nameList=list(args.name.split(","))
    else:
        nameList = build_list(args.nameList)
    
    for name in nameList:
        usernames.update(name2username(name))

    # for n in usernames:
        # print(n)


    if args.outFile is not None and len(usernames)>0:
        if os.path.exists(args.outFile):
            print("\t目标文件已经存在\n")
            # for n in usernames:
            #     print(n)
            return

        filePath,fileName=os.path.split(args.outFile)
        if (filePath!="") and (not os.path.exists(filePath)):
            os.mikedirs(filePath)
        with open(args.outFile, mode="w") as fout:
            for n in usernames:
                fout.write("%s\n"%n)
                
        print("Done\n\t%s\n"%os.path.abspath(args.outFile))
        return

    else:
        for n in usernames:
            print(n)

if __name__ == '__main__':
    main()