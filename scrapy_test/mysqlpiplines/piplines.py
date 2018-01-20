from .sql import Sql
from scrapy_test.items import ScrapyTestItem,DcontentItem

class ScrapyTestPipeline(object):

    def process_item(self,item,spider):
        if isinstance(item,ScrapyTestItem):
            name_id = item['name_id']
            ret = Sql.select_name(name_id)

            if ret==1:
                print('已经存在了')
                pass
            else:
                xs_name = item['name']
                xs_author = item['author']
                category = item['category']
                Sql.insert_dd_name(xs_name,xs_author,category,name_id)
                print('开始存小说标题')

        if isinstance(item,DcontentItem):
            url = item['chapterurl']
            name_id = item['id_name']
            num_id = item['num']
            xs_chaptename  = item['chaptername']
            xs_content = item['chaptercontent']
            Sql.insert_dd_chaptername(xs_chaptename,xs_content,name_id,num_id,url)
            print('小说章节存储完毕')
            return item