from django.db import models


# 每个表都要录入一条空语句，表示空的字

class SM(models.Model):
    # 声母表
    sm = models.CharField(max_length=10, null=False, primary_key=True)

    def __str__(self):
        return self.sm


class YM(models.Model):
    # 韵母表
    ym = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.ym


class Character(models.Model):
    # 汉字表
    # 不把字做主键，因为有多音字
    character = models.CharField(max_length=10, null=False)
    csm = models.ForeignKey(SM, on_delete=models.CASCADE)
    cym = models.ForeignKey(YM, on_delete=models.CASCADE)
    # 0-4 五种声调
    tone = models.CharField(max_length=5, null=False)
    # 对应押韵类型
    rhyme = models.CharField(max_length=5, null=False)

    def __str__(self):
        return self.character + ':' + str(self.csm) + str(self.cym) + self.tone


class Phrase(models.Model):
    # 词语表
    phrase = models.CharField(max_length=30, null=False)
    # 倒序排列每个字
    c1 = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='c1')
    c2 = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='c2')
    c3 = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='c3')
    c4 = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='c4')
    c5 = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='c5')
    c6 = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='c6')
    c7 = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='c7')

    class Meta:
        index_together = ['c1', 'c2', 'c3', 'c4']

    def __str__(self):
        return self.phrase
