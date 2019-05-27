# -*- coding: utf-8 -*-
# author： 傅禹宁
import shutil
import uuid
import random
import time
import os
import xlwt
import math


class BaseUtilsLibrary(object):
    """
    robot自定义扩展功能类
    """
    @classmethod
    def get_car_id(cls):
        """
        生成随机车牌号
        :return: 随机车牌号
        """
        data = "辽A"
        for index in range(0, 5):
            num = random.randint(0, 9)
            chars = chr(random.randint(65, 91))
            if (random.randint(0, 9)) % 2 == 0:
                data = data + str(num)
            else:
                data = data + str(chars)
        return data

    @classmethod
    def make_num(cls, start='', end=11):
        """
        生成纯数字字符串,默认为生成131-189开头的手机号
        :param start: 当传入start属性时会以此属性指定的字符串作为字符串的开头
        :param end: 当传入end属性时会随机生成end属性指定长度的字符串
        :return: 纯数字字符串或start开头的纯数字字符串
        """
        if end == 11:
            num_str = start+str(random.randint(131, 189))
        else:
            num_str = start+''
        for i in range(len(num_str), end):
            num = random.randint(0, 9)
            num_str = num_str + str(num)
        return num_str

    @classmethod
    def generate_random_string(cls, length, prefix=None, suffix=None, allow_number=False, allow_caps_letter=False,
                               allow_lower_letter=False):
        """
        生成随机字符串
        :param length: 长度
        :type length: int
        :param prefix: 前缀
        :type prefix: str
        :param suffix: 后缀
        :type suffix: str
        :param allow_number:只允许数字
        :type allow_number:bool
        :param allow_caps_letter:只允许大写字母
        :type allow_caps_letter:bool
        :param allow_lower_letter:只允许小写字母
        :type allow_lower_letter:bool
        :return:随机字符串
        :rtype:str
        """
        num_chars = '0123456789'
        caps_letter_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lower_letter_chars = 'abcdefghijklmnopqrstuvwxyz'
        random_chars = ''
        if allow_number:
            random_chars += num_chars
        if allow_caps_letter:
            random_chars += caps_letter_chars
        if allow_lower_letter:
            random_chars += lower_letter_chars
        if prefix is None:
            prefix = ''
        if suffix is None:
            suffix = ''
        random_string = prefix
        for _ in range(int(length) - (len(prefix) + len(suffix))):
            random_string += random.choice(random_chars)
        random_string += suffix
        return random_string

    @classmethod
    def generate_phone_num(cls, length=11, prefix=None, suffix=None):
        """
        生成随机手机号
        :param length: 长度
        :type length: int
        :param prefix: 前缀
        :type prefix: str
        :param suffix: 后缀
        :type  suffix: str
        :return: 随机手机号
        :rtype: str
        """
        if prefix is None:
            prefix = str(random.randint(131, 189))
        if suffix is None:
            suffix = ''
        phone_num = cls.generate_random_string(length, prefix=prefix, suffix=suffix, allow_number=True)
        return phone_num

    @classmethod
    def generate_num(cls, length, prefix=None, suffix=None):
        """
        生成随机手机号
        :param length: 长度
        :type length: int
        :param prefix: 前缀
        :type prefix: str
        :param suffix: 后缀
        :type  suffix: str
        :return: 随机手机号
        :rtype: str
        """
        if prefix is None:
            prefix = ''
        if suffix is None:
            suffix = ''
        num = cls.generate_random_string(length, prefix=prefix, suffix=suffix, allow_number=True)
        return num

    @classmethod
    def generate_car_id(cls, length=7, prefix=None, suffix=None):
        """
        生成随机车牌号
        :param length: 长度
        :type length: int
        :param prefix: 前缀
        :type prefix: str
        :param suffix: 后缀
        :type  suffix: str
        :return: 随机手机号
        :rtype: str
        """
        province_list = ['辽', '豫', '鄂', '琼', '桂', '湘', '皖', '云', '陕', '蒙', '京', '冀', '黑', '新', '苏', '甘', '晋',
                         '浙', '闽', '渝', '吉', '贵', '粤', '川', '鲁', '津', '沪']
        city_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S']
        if prefix is None:
            prefix = random.choice(province_list)+random.choice(city_list)
        if suffix is None:
            suffix = ''
        car_id = cls.generate_random_string(length, prefix=prefix, suffix=suffix, allow_number=True,
                                            allow_caps_letter=True)
        return car_id

    @classmethod
    def get_uuid(cls):
        """
        生成uuid并处理为32位无"-"连接格式字符串
        :return:32位无"-"连接字符串形式UUID
        """
        ids = uuid.uuid1()
        ids = str(ids)
        ids = ids.replace("-", "")
        return ids

    #
    @classmethod
    def make_time(cls):
        """
        获取当前时间戳的字符串形式
        :return: 时间戳的字符串形式
        """
        return str(time.time())

    @classmethod
    def make_now_second(cls):
        """
        获取北京时间的从当天00:00:00到此时的秒数
        :return: 秒数
        """
        return int(str(time.time())[0:10]) % (24 * 60 * 60 * 60) + (8 * 60 * 60)

    @classmethod
    def add_number(cls, x, y):
        """
        提供了两个数字相加的方式,如果是字符串会转成数字
        :param x: 数字x
        :param y: 数字y
        :return: x+y的结果
        """
        return int(x) + int(y)

    @classmethod
    def make_time_as_string(cls):
        """
        生成字符串形式时间戳,并把"."去掉
        :return: 字符串形式时间戳
        """
        time_str = str(time.time())
        time_str = time_str.replace(".", "")
        return time_str

    @classmethod
    def auto_create_bug_level_tag(cls, resp_code, status_code):
        """
        生成状态码错误等级标签
        :param resp_code:实际返回的状态码
        :type resp_code:int
        :param status_code:预期的状态码
        :type status_code:int
        :return:标签内容
        :rtype:str
        """
        bug_level = None
        resp_code = int(resp_code)
        status_code = int(status_code)
        if status_code == 200 and resp_code in (201, 204):
            bug_level = 'Major'
        if status_code == 200 and resp_code == 202:
            bug_level = 'Critical'
        if status_code in (201, 204) and resp_code == 200:
            bug_level = 'Major'
        if status_code == 201 and resp_code in (202, 204):
            bug_level = 'Critical'
        if status_code == 204 and resp_code == 201:
            bug_level = 'Major'
        if status_code == 204 and resp_code == 202:
            bug_level = 'Critical'
        if status_code in (200, 201, 202, 204) and resp_code in (400, 401, 403, 404, 405, 410, 422):
            bug_level = 'Critical'
        if status_code in (301, 302, 304) and resp_code in (301, 302, 304) and status_code != resp_code:
            bug_level = 'Major'
        if status_code == 400 and resp_code in (200, 201, 202, 204):
            bug_level = 'Major'
        if status_code == 400 and resp_code in (301, 302, 304):
            bug_level = 'Major'
        if status_code == 400 and resp_code in (401, 403, 404, 405, 410, 422):
            bug_level = 'Minor'
        if status_code in (401, 403) and resp_code in (200, 201, 202, 204):
            bug_level = 'Critical'
        if status_code in (401, 403) and resp_code in (400, 404, 405, 410, 422):
            bug_level = 'Minor'
        if status_code in (404, 410) and resp_code in (200, 201, 202, 204):
            bug_level = 'Major'
        if status_code in (404, 410) and resp_code in (400, 401, 405, 403, 422):
            bug_level = 'Major'
        if status_code == 405 and resp_code in (200, 201, 202, 204):
            bug_level = 'Major'
        if status_code == 405 and resp_code in (400, 401, 403, 404, 410, 422):
            bug_level = 'Minor'
        if status_code == 422 and resp_code in (200, 201, 202, 204):
            bug_level = 'Critical'
        if status_code == 422 and resp_code in (400, 401, 403, 404, 405, 410):
            bug_level = 'Major'
        if resp_code == 500:
            bug_level = 'Blocker'
        if resp_code == 502:
            bug_level = 'Minor'
        if resp_code == 504:
            bug_level = 'Minor'
        if status_code == 405 and resp_code in (301, 302, 304):
            bug_level = 'Major'
        if bug_level is not None:
            bug_level = 'BugLevel:' + bug_level
        return bug_level

    @classmethod
    def auto_create_status_tag(cls, resp_code, status_code):
        """
        生成状态码动态标签
        :param resp_code:实际返回的状态码
        :type resp_code:int
        :param status_code:预期的状态码
        :type status_code:int
        :return:标签内容
        :rtype:str
        """
        status_tag = None
        if str(resp_code) != str(status_code):
            status_tag = 'ShouldBe:'+str(status_code)+'But:'+str(resp_code)
        return status_tag

    @classmethod
    def write_xls(cls, rows, cols_name, cols_value, sheet_name, file_name):
        """
        生成xls文件
        :param rows:行数
        :type rows: int
        :param cols_name:每行的表头(逗号分割)
        :type cols_name: str
        :param cols_value:每行的值(逗号分割)
        :type cols_value: str
        :param sheet_name:表名
        :type sheet_name: str
        :param file_name:文件名
        :type sheet_name: str
        """
        rows = int(rows)
        cols_name = cols_name.split(",")
        cols_value = cols_value.split(",")
        times = int(math.ceil(rows/65535))
        this_rows = 0
        work_book = xlwt.Workbook(encoding='utf-8')
        for _ in range(0, times):
            sheet = work_book.add_sheet(str(sheet_name)+str(_))
            if rows <= 65534:
                this_rows = rows + 1
            elif rows > 65534:
                this_rows = 65535
                rows -= 65534
            for i in range(0, this_rows):
                for j in range(0, len(cols_name)):
                    if i == 0:
                        sheet.write(i, j, str(cols_name[j]))
                    else:
                        if j in (0, 1):
                            cols_value[j] = int(cols_value[j])+1
                        sheet.write(i, j, str(cols_value[j]))
        work_book.save(str(file_name))

    @classmethod
    def auto_params(cls, essential_params, unessential_params, success=True):
        """
        将必传参数与每个非必传参数依次组合并返回结果集
        :param essential_params:必传参数
        :type essential_params:dict
        :param unessential_params:非必传参数
        :type unessential_params:dict
        :param success:是否多种情况
        :type success:bool
        :return:参数组合的结果集
        :rtype:list
        """
        results = []
        params = {}
        if len(essential_params) != 0:
            params = essential_params.copy()
        if success is True:
            if len(unessential_params) != 0:
                for k, v in unessential_params.items():
                    params[k] = v
                    results.append(params)
            else:
                results.append(params)
        else:
            if len(unessential_params) != 0:
                for k, v in unessential_params.items():
                    params[k] = v
                results.append(params)
            else:
                results.append(params)
        return results

    @staticmethod
    def move_file(old_file_path, new_dir_path):
        """
        检查并转移文件到指定文件夹
        :param old_file_path:文件在系统中的路径(例：/home/xxx/下载/filename)
        :type old_file_path:str
        :param new_dir_path: 要放到的项目中的路径(例：tests/server_project)
        :type new_dir_path:str
        """
        if os.path.isfile(old_file_path):
            file_name = old_file_path.split('/')[-1]
            shutil.move(old_file_path, '%s/%s/%s' % (os.getcwd(), new_dir_path, file_name))
        else:
            print('文件%s不存在' % old_file_path)

    # # 自动生成所有组合方式的参数列表
    # @staticmethod
    # def auto_params(essential_params, unessential_params, success=True):
    #     data = []
    #     results = []
    #     params = ''
    #     start_num = 0
    #     index = 0
    #     if success is False:
    #         start_num = 1
    #     for i in essential_params:
    #         index += 1
    #         params = params + str(i)
    #         if index != len(essential_params):
    #             params = params + '!^￥^@'
    #     for i in range(start_num, len(unessential_params)+1):
    #         for j in list(combinations(unessential_params, i)):
    #             data.append(j)
    #     print(data)
    #     for i in data:
    #         result = params
    #         for j in i:
    #             result = result + '!^￥^@'
    #             result = result + str(j)
    #         data1 = result.split('!^￥^@')
    #         result = {}
    #         for k in data1:
    #             data2 = k.split('=')
    #             result[data2[0]] = data2[1]
    #         results.append(result)
    #         print(result)
    #     return results


if __name__ == '__main__':
    pass
