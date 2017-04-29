# @Author: lucky
# @Date:   2017-04-29T22:46:58+08:00
# @Last modified by:   lucky
# @Last modified time: 2017-04-29T23:21:41+08:00



from django.contrib.sitemaps import Sitemap
from blog.models import Article

class BlogSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1.0
    protocol = 'https'

    def items(self):
        return Article.objects.filter(status = 0)

    def lastmod(self):
        return obj.created_time

    def location(self, item):
        return '/article/%s' % item.url
