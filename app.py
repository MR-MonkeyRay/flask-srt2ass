from flask import Flask, render_template, request, jsonify
import config.myfun

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def srt2ass():
    message = '''
    ==================================================================================================
    ====  可在上方上传字幕或将字幕文本粘贴到此处，然后点击下方“转码”按钮，即可自动完成在线转码  ========
    =======================   版本：v1.4   =====================   作者：Fall-Like-Snow   ======================

    版本更新日志：

    【v1.4】    更新了单行翻译 srt 转双行 ass 脚本

    【v1.3】    点击“转码”后实现后台数据前端同步刷新
                            修复使用百度翻译api时的504错误

    【v1.2】    将谷歌翻译修改为百度翻译以提高速度
                            增加可以去掉语气词和无用音符的功能

    【v1.1】    可以使用谷歌机器翻译
                            转码后可以下载 ass 字幕

    【v1.0】    发布了转码网站，网址http://www.fall-like-snow.com/srt2ass
                            提供了可添加样式表

    '''
    return render_template("srt2ass.html", ph=message, download=0)


@app.route('/resolve', methods=['GET', 'POST'])
def resolve():
    if 'text' not in request.form or request.form['text'] == '':
        return jsonify(result={
            'percent': 0,
            'text': "[Error -1] 未发现字幕文件",
            'complete': 0
        })
    if config.myfun.mdif(request.form['text']):
        return jsonify(result={
            'percent': 0,
            'text': "[Error -2] 字幕文件匹配失败，你所上传的文件可能不是 srt 类型字幕",
            'complete': 0
        })
    import _thread
    config.myfun.__init()
    config.myfun.set_pre(1)
    prec = config.myfun.get_pre()
    _thread.start_new_thread(config.myfun.makef, (request.form,))
    return jsonify(result={
        'percent': prec[0],
        'text': prec[1],
        'complete': prec[2]
    })


@app.route('/dataget', methods=['GET', 'POST'])
def dataget():
    prec = config.myfun.get_pre()
    return jsonify(result={
        'percent': prec[0],
        'text': prec[1],
        'complete': prec[2]
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
