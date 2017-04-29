# @Author: lucky
# @Date:   2017-04-29T22:35:02+08:00
# @Last modified by:   lucky
# @Last modified time: 2017-04-29T22:41:33+08:00



from django.contrib.syndication.views import Feed
from blog.models import Article
from django.utils.feedgenerator import Rss201rev2Feed
from django.utils.feedgenerator import AtomlFeed
from markdown2 import markdown

class ExtendedRSSFeed(Rss201rev2Feed):
    mime_type = 'application/xml'

class RssSiteNewsFeed(Feed):
    feed_type = ExtendedRSSFeed
    author_name = 'Lucky'
    title = 'Softteam'
    link = ''
    description = 'Here we go'
    feed_url = ''

    def items(self):
        return Article.objects.all().order_by('-created_time')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return markdown(description)

    def item_link(self, item):
        return '/article/%s' % item.url

    def item_pubdate(self, item):
        return item.created_time

    def item_guid(self, item):
        return item

class AtomSiteNewsFeed(RssSiteNewsFeed):
    feed_type = AtomlFeed
    subtitle = RssSiteNewsFeed.description
