# -*- coding: utf-8 -*-
import copy
import json

from ..items import TaobaoItem
from traceback import format_exc
import re
import scrapy

kw = ['网络服务', '装潢', '护理', '速食', '运动鞋', '运动服', '男装', '配件', '蔬果', '干货', '攻略', '地毯', '文具', '书籍', '人偶', '饰品', '报纸', '时尚饰品', '美发', '运动包', '粮油', '吃喝玩乐折扣券', '工具', '彩妆', '演出', '童装', '个性定制', '数码相机', '日化', '游戏', '尿片', '安防', '摄像机', '厨房电器', '办公设备', '网店', 'ZIPPO', '杂志', '礼品', '摄影器材', '喂哺等用品', '软件', '笔记本电脑', '明星', '登山', '居家日用', '户外', '电脑硬件', '流行首饰', '娃娃', '收纳', '影视', '音乐', '电玩', '音像', '香水', '水产', '热销女包', '大家电', '其他保健营养品', '箱包皮具', '瑞士军刀', '3C数码配件市场', '电脑周边', '男包', '玩具', 'U盘', '模型', '孕妇装', '窗帘', '眼镜', '促销店铺', '五金', '旅行', '洗护', '清洁', '移动存储', '卫浴', '野营', '颈环配件', '童鞋', '家装饰品', '显示器', '闪存卡', '传统滋补品', '耗材', '灯具']
# https://s.taobao.com/search?spm=a21bo.2017.201867-links-8.3.44fb11d9H0N2xT&q=%E7%89%9B%E5%A5%B6&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180724&ie=utf8
# https://s.taobao.com/search?spm=a21bo.2017.201867-links-8.3.44fb11d9H0N2xT&q=%E7%89%9B%E5%A5%B6&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180724&ie=utf8&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=44
class TbSpider(scrapy.Spider):
    name = 'tb'
    allowed_domains = ['taobao.com']
    start_urls = ['https://s.m.taobao.com/search?event_submit_do_new_search_auction=1&_input_charset=utf-8&topSearch=1&atype=b&searchfrom=1&action=home%3Aredirect_app_action&from=1&q={}&sst=1&n=44&buying=buyitnow&m=api4h5&abtest=25&wlsort=25&page={}'.format(i, y) for i in range(1, 101) for y in kw]

    def parse(self, response):

        item = TaobaoItem()
        ListItem = json.loads(response.text)['listItem']

        for i in ListItem:
            item['name'] = i['name']
            item['title'] = i['title']
            item['area'] = i['area']

            # 处理不同的URL
            url = []
            if 'https:' not in i['url']:
                if 'detail.m.tmall.com' in i['url']:
                    url.append('https:' + i['url'].replace('.m', ''))
                else:
                    url.append('https:' + i['url'])
            if 'https:' in i['url']:
                url.append(i['url'])
            item['url'] = url
            print(item['url'])

            # 评论网址
            comment_url = []
            ur = item['url']
            comment_url.append(ur[0] + '#J_Reviews')
            item['comment_url'] = comment_url

            item['fastPostFee'] = i['fastPostFee']
            item['sales'] = i['act']
            item['price'] = i['price']
            item['originalPrice'] = i['originalPrice']
            item['nick'] = i['nick']
            item['id'] = i['item_id']
            item['loc'] = i['sellerLoc']

            # 图片链接
            img_url = []
            img_url.append('http:' + i['img2'])
            item['img_url'] = img_url

            count_url = []
            count_url.append('https://rate.taobao.com/detailCount.do?itemId=' + i['item_id'])

            for url in count_url:
                yield scrapy.Request(
                    url,
                    callback=self.detail_parse,
                    meta={'item': copy.deepcopy(item)},  # 使用copy.deepcopy深复制，否则数据不对啊
                    dont_filter=True,
                    errback=self.error_back
                )

    def detail_parse(self, response):
        item = response.meta['item']
        pat_count = '{"count":(.*?)}'
        item['count'] = re.findall(pat_count, str(response.body))

        print(item)

    def error_back(self, e):
        _ = e
        self.logger.error(format_exc())

