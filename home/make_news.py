import feedparser


def make_news(key):
    choice_dic = {"education": 'https://www.google.com/alerts/feeds/14555555114046780351/13329697584533306830', "science": "https://www.google.com/alerts/feeds/14555555114046780351/2259895332053150712", "youth": "https://www.google.com/alerts/feeds/14555555114046780351/16372027772606344783", 'personal': "https://www.google.com/alerts/feeds/14555555114046780351/16372027772606344783", 'personal2': 'https://www.google.com/alerts/feeds/14555555114046780351/16372027772606344783', 'personal3': 'https://www.google.com/alerts/feeds/14555555114046780351/16372027772606344783'}
    
    def do_it(key):
        feed = None
        try:
            for choice in choice_dic:
                feed = feedparser.parse(choice_dic[key])
                for ent in feed.entries[:]:
                    if len(ent['title']) < 20  or len(ent['summary']) < 20  or len(ent['link']) < 5 or len(ent['published']) <10:
                        feed.entries.remove(ent)
                        continue
                    #ent['link']=ent['link'].replace("https://www.google.com/url?rct=j&sa=t&url=",'')
                    ent['title'] = ent['title'].encode('utf-8')
                    ent['summary'] = ent['summary'].encode('utf-8')
            feed = feed.entries
            return feed
        except: pass
    feed = do_it(key)
    if key == 'personal':
        if not feed: feed = []
        import random
        feed.extend(do_it('personal2'))
        feed.extend(do_it('personal3'))
        random.shuffle(feed)
    return feed
    
def make_human(bound_field):
    import datetime, re, math
    bound_field = bound_field.replace(re.findall("^.+(\:\d{2}Z)$",bound_field)[0],"")
    re_pattern = re.findall( '^(\d{4}\-\d{2}\-\d{2}).*$',bound_field)[0]
    word = bound_field.replace(re_pattern+"T", "")
    date_article = [int(_) for _ in re_pattern.split('-')]
    date_current = (lambda _: [_.year, _.month, _.day])(datetime.datetime.now().date())
    if date_article == date_current:
        return "Сьогодні "+ word
    elif date_article[0] == date_current[0] and date_article[1] == date_current[1] and math.fabs((date_current[2] - date_article[2])) == 1:
        return "Вчора " + word
    elif date_article[0] == date_current[0] and date_article[1] == date_current[1] and math.fabs(date_current[2] - date_article[2]) == 2:
        return "Позавчора " + word
    else:
        return re_pattern+" "+word

def one_news(key):
    param = ""
    if key in ['education', 'youth', 'science', 'personal']:
        feed = make_news(key)
        param = '<ul class="list-group">'
        if key == "personal": param += "<small><i>Новини по Персоналіям і назвам (зараз тількі молодь)</i></small>"
        if not feed:
            param += "Нема новин на сьогодні"
        else:
            for news in feed:
                param += """<br><br>
                 <li class="list-group-item list-group-item-secondary"><h2 class="text-center">{}</h2></li>
                <a href="{}" class="list-group-item list-group-item-light">
                <i align="left" class="badge badge-info">{}</i> 
                <p>{}</p>
                 </a>""".format(news.title.decode('utf-8'), news.link, make_human(news.published) , news.summary.decode('utf-8'))
        param += """</ul>"""
    return param

