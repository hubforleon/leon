# 练习:
#   调用函数，输入一组数字，计算求和的结果。
#目的：
#   1）函数的多参数输入；
#   2）for循环计算数组中每个值的求和；
def addmore(*numbers):
    sum =0
    print("input---",numbers)
    for num in numbers:
        sum += num
    return sum

# 练习:
#   调用函数，输入一组键值对，计算键值的求和的结果。
#目的：
#   1）函数的键值对输入；
#   2）for循环计算键值对的每个值的求和；
def addmorekeys(**numbers):
    sum=0
    print('input...',numbers)
    for k,v in numbers.items():        
        sum+=v
        # print('key: {}  value: {}'.format(k,v))
        # print('numbers[k]: ',numbers[k])
        # # sum += numbers[k]
    return sum

# 调用方法示例
t=addmore(1,3,5)
print('the sum is ',t)
t=addmorekeys(red=5, blue=7,yellow=9)
print('the sum is ',t)

# JS中的类似场景：
# 1）对象的遍历循环方式：
#             var obj = [name = 'lion', age = 50, sex = 'm'];
#             console.log(obj);   //结果：0：lion, 1:50, 2:m
#             for (v in obj) {
#                 console.log('key: ' + v);
#                 console.log(obj[v]);
#             }   //结果显示: key:0, lion, key:1,50, key:2,m
# 2）函数输入的多个参数 ----- 数组的输入： （字符串的输入要用split分解后再用parseInt()转换成数字。
# #           var attr = {“red”:a, “blue”：b};
#             if ((arguments.length == 1)&&(Array.isArray(arguments[0]))) {
#                 for (i in arguments[0]) {
#                     sum += parseInt(arguments[0][i]);   
#             }
