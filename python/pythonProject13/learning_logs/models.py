from django.db import models

# Create your models here.
class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text


class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    # 在Entry重嵌套了Meta类，Meta存储用于管理模型的额外信息
    class Meta:
        # 让我们能够设置一个特殊属性，让Django在需要时使用Entries来表示多个条目
        # 如果没有这个类，Django将使用Entrys来表示多个条目
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text[:50] + "..."