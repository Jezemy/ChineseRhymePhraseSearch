from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import traceback
import time
from django.core.paginator import *


def rhyme(request):
    return render(request, 'rhyme.html')


def get_rhyme(request, pnum=1):
    page_data_num = 100

    phrase = request.POST['phrase']
    option = int(request.POST['rhymeOption'])
    toneNum = int(request.POST['toneOption'])
    # phrase长度和option取一个最小值,避免少字要多押
    option = min(len(phrase), option)
    toneNum = min(len(phrase), toneNum)
    # print(toneNum)

    rev_phrase = phrase[::-1]

    # 储存指定数量的韵母对应押韵表的数字
    rhyme_num = []
    tone_num = []

    st = time.clock()

    try:
        for i in range(option):
            num = Character.objects.filter(character=rev_phrase[i]).only('rhyme')[0].rhyme
            rhyme_num.append(num)
            if i < toneNum:
                tone = Character.objects.filter(character=rev_phrase[i]).only('tone')[0].tone
                tone_num.append(tone)
            else:
                tone_num.append('')

    except Exception as e:
        traceback.print_exc()
        return JsonResponse({"code": "404"}, safe=False)

    # print(tone_num)

    # 获取相同押韵的字
    rhyme_words = []
    try:
        for i in range(option):
            words = Character.objects.filter(rhyme=rhyme_num[i]).filter(tone__contains=tone_num[i]).only('id')
            rhyme_words.append(words)
    except Exception as e:
        traceback.print_exc()
        return JsonResponse({"code": "404"}, safe=False)

    # 查询相同韵脚的字
    if option == 1:
        rhyme_phrases = Phrase.objects.filter(c1_id__in=rhyme_words[0]).only('phrase')
    elif option == 2:
        rhyme_phrases = Phrase.objects.filter(c1_id__in=rhyme_words[0]).filter(c2_id__in=rhyme_words[1]).only('phrase')
    elif option == 3:
        rhyme_phrases = Phrase.objects.filter(c1_id__in=rhyme_words[0]).filter(c2_id__in=rhyme_words[1]).filter(
            c3_id__in=rhyme_words[2]).only('phrase')
    else:
        rhyme_phrases = Phrase.objects.filter(c1_id__in=rhyme_words[0]).filter(c2_id__in=rhyme_words[1]).filter(
            c3_id__in=rhyme_words[2]).filter(c4_id__in=rhyme_words[3]).only('phrase')

    # 序列化
    result = []
    for phrase in rhyme_phrases[(pnum - 1) * page_data_num:(pnum * page_data_num)]:
        result.append(phrase.phrase)

    et = time.clock()
    print(f"查询花费总时间{et - st:.10f} s")

    dataNum = len(rhyme_phrases)
    pagesNum = int((dataNum / page_data_num)) + 1 if dataNum % page_data_num > 0 else dataNum / page_data_num

    return JsonResponse({"code": "200", "result": result, "totals": dataNum, "pagesNum": pagesNum, "curpage": pnum},
                        safe=False)
