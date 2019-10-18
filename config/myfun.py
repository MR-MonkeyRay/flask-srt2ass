def __init():
    global pre
    pre = [0, '', 0]


def mdif(data):
    import re
    extract = re.compile('\\d+\\s+([0-9:,]+)\\s--?>\\s([0-9:,]+)\\s+(.*?)\\r?\\n')
    sub = extract.findall(data)
    if sub:
        return False
    else:
        return True


def makef(form):
    import re
    global pre
    print("被调用")
    data = form['text']
    extract = re.compile('\\d+\\s+([0-9:,]+)\\s--?>\\s([0-9:,]+)\\s+([\\s\\S]*?)\\r?\\n\\r?\\n')
    gettime = re.compile('(\\d+):(\\d+):(\\d+),(\\d+)')

    def trs(tim):
        i, j, k, t = [int(x) for x in gettime.match(tim).groups()]
        t = t / 10 + 1 if t % 10 >= 5 else t / 10
        if t > 99:
            k, t = k + 1, 0
        if k > 59:
            j, k = j + 1, 0
        if j > 59:
            i, j = i + 1, 0
        return i, j, k, t

    sub = extract.findall(data)
    n1, n2, n3 = sub.pop(0)
    merge = [(trs(n1), trs(n2), n3)]
    for n1, n2, n3 in sub:
        p1, p2, p3 = merge[-1]
        n1, n2 = trs(n1), trs(n2)
        if p3 == n3:
            if p2[0] == n1[0] and p2[1] == n1[1] and p2[2] == n1[2]:
                if n1[3] - p2[3] <= 5:
                    merge[-1] = (p1, n2, p3)
                    continue
        merge.append((n1, n2, n3))
    if form['style'] == "option1":
        ass = '[Script Info]\r\n' + ';\r\n' + ';\r\n' + 'Title:\r\n' + 'Original Script:\r\n' + 'Synch Point:0\r\n' + \
              'ScriptType:v4.00+\r\n' + 'ScaledBorderAndShadow: yes\r\n''WrapStyle: 0\r\n' + 'Collisions:Normal\r\n' + \
              'PlayResX:1920\r\n' + 'PlayResY:1080\r\n' + '\r\n' + '[V4+ Styles]\r\n' + \
              'Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\r\n' + \
              'Style: 康复-EN,Arial,50,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,1,2,2,10,10,10,1\r\n' + \
              'Style: 康复-CH,Microsoft YaHei,75,&H0069D7FB,&H000000FF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,1,2.5,2,8,8,10,1\r\n' + \
              '\r\n' + '[Events]\r\n' + 'Format: Layer, Start, End, Style, Actor, MarginL, MarginR, MarginV, Effect, Text\r\n' + ''
    elif form['style'] == "option2":
        ass = '[Script Info]\r\n' + ';\r\n' + ';\r\n' + 'Title:\r\n' + 'Original Script:\r\n' + 'Synch Point:0\r\n' + \
              'ScriptType:v4.00+\r\n' + 'ScaledBorderAndShadow: yes\r\n''WrapStyle: 0\r\n' + 'Collisions:Normal\r\n' + \
              'PlayResX:1920\r\n' + 'PlayResY:1080\r\n' + '\r\n' + '[V4+ Styles]\r\n' + \
              'Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\r\n' + \
              'Style: 夏令营岛-EN,Arial,38,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,1,2,2,10,10,10,1\r\n' + \
              'Style: 夏令营岛-CH,方正超粗黑_GBK,60,&H00BCE9E6,&H000000FF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,2,2,2,10,10,10,1\r\n' + \
              '\r\n' + '[Events]\r\n' + 'Format: Layer, Start, End, Style, Actor, MarginL, MarginR, MarginV, Effect, Text\r\n' + ''
    else:
        ass = ''

    tot = len(merge)
    con = 0
    for n1, n2, n3 in merge:
        n3 = re.sub('\\r', '', n3)
        n3 = re.sub('\\n', ' ', n3)
        if 'erz' in form:
            import re
            n3 = re.sub('\[.*?\]', '', n3)
            de = re.sub(' ', '', n3)
            ds = re.sub('♪', '', n3)
            ds = re.sub(' ', '', ds)
            if ds == '' or de == '':
                continue
        con += 1
        n1 = '%02d:%02d:%02d.%02d' % n1
        n2 = '%02d:%02d:%02d.%02d' % n2
        if 'trans' in form:
            e_text = n3
            text = translator(n3)
            text = re.sub('，',' ',text)
            text = re.sub('。', '', text)
        elif 'dou' in form:
            xx = n3.split("\\N")
            text = xx[0]
            e_text = xx[1]
        else:
            e_text = n3
            text = ''
        if form['style'] == "option1":
            line = 'Dialogue: 0,%s,%s,康复-EN,,0,0,0,,%s\r\n' % (n1, n2, e_text)
            ass += line
            line = 'Dialogue: 0,%s,%s,康复-CH,,0,0,0,,%s\r\n' % (n1, n2, text)
            ass = ass + line
        elif form['style'] == "option2":
            line = 'Dialogue: 0,%s,%s,夏令营岛-EN,,0,0,0,,%s\r\n' % (n1, n2, e_text)
            ass = ass + line
            line = 'Dialogue: 0,%s,%s,夏令营岛-CH,,0,0,0,,%s\r\n' % (n1, n2, text)
            ass = ass + line
        pre[0] = round(con / tot * 100, 1)
        pre[1] = ass
    pre[0] = 100
    pre[2] = 2
    return 0


def set_pre(num):
    global pre
    pre[2] = num


def get_pre():
    global pre
    return pre


def translator(word):
    import requests
    import string
    import time
    import hashlib
    import json
    from . import baiduTranslateConf as btc
    api_url = "http://api.fanyi.baidu.com/api/trans/vip/translate"
    # init salt and final_sign
    salt = str(time.time())[:10]
    final_sign = str(btc.my_appid) + word + salt + btc.cyber
    final_sign = hashlib.md5(final_sign.encode("utf-8")).hexdigest()
    paramas = {
        'q': word,
        'from': 'en',
        'to': 'zh',
        'appid': '%s' % btc.my_appid,
        'salt': '%s' % salt,
        'sign': '%s' % final_sign
    }
    response = requests.get(api_url, params=paramas).content
    content = str(response, encoding="utf-8")
    json_reads = json.loads(content)
    return json_reads['trans_result'][0]['dst']

