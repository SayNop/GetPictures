# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


from scrapy.pipelines.images import ImagesPipeline
from GetPictures.settings import IMAGES_STORE
from scrapy.http import Request
import os

class ImgPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        img_url = item['img_url']
        yield Request(img_url, meta={'mid_data': item['title']})


    def file_path(self, request, response=None, info=None):

        title = request.meta['mid_data']
        # print(request.meta['mid_data'])
        img_path = os.path.join(IMAGES_STORE, title)
        # if not os.path.exists(img_path):
        #     os.mkdir(img_path)
        name = request.url.split('/')[-1]
        img_path = os.path.join(img_path, name)
        print(img_path)
        return img_path
