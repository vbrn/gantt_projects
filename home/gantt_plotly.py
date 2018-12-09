import plotly
import plotly.plotly as py
import plotly.figure_factory as ff
#import pandas as pd
def gantt(arg, name):
    status_dict= {'n':'Не розпочата','i':'Розпочата','c':'Завершена', 'nc': 'На контролі', 'p': 'Прострочена' }
    df = [dict(Task=_.name_task, Start='{}-{}-{}'.format(_.start.year, _.start.month, _.start.day ), Finish='{}-{}-{}'.format(_.promizhny_date.year, _.promizhny_date.month, _.promizhny_date.day ), Status="{}".format(status_dict[_.status])) for _ in arg if _.overdue]
    df_overdue = [dict(Task=_.name_task, Start='{}-{}-{}'.format(_.start.year, _.start.month, _.start.day ), Finish='{}-{}-{}'.format(_.promizhny_date.year, _.promizhny_date.month, _.promizhny_date.day ), Status="{}".format(status_dict['p'])) for _ in arg if not _.overdue]
    df_promizh = [dict(Task=_.name_task, Start='{}-{}-{}'.format(_.promizhny_date.year, _.promizhny_date.month, _.promizhny_date.day ), Finish='{}-{}-{}'.format(_.finish.year, _.finish.month, _.finish.day ), Status="{}".format(status_dict['nc'])) for _ in arg]
    df.extend(df_overdue)
    df.extend(df_promizh)

    
    colors = {'На контролі': 'rgb(220, 0, 0)',
          'Розпочата': (1, 0.9, 0.16),
          'Завершена': 'rgb(29, 206, 26))',
         'Не розпочата': 'rgb(26, 188, 206))',
          'Прострочена': 'rgb(0, 0, 0)'}

    #fig = ff.create_gantt(df)
    fig = ff.create_gantt(df, colors=colors, index_col='Status', group_tasks=True, show_colorbar=True, bar_width=0.2, showgrid_x=True, showgrid_y=True, title=name)
    #fig = ff.create_gantt(df, title='Raz i Dva i', width=1000)
    fig['layout']['hovermode']='y'
    fig['layout'].update(autosize=False,margin=dict(l=205))# width=800, height=500, )
    scriptfile =plotly.offline.plot(fig, output_type="div", show_link=False, link_text=False)
    return scriptfile

"""
#first version
def gantt2():
    df = [dict(Task="Задача 0", Start='2005-01-01', Finish='2009-02-28'),
          dict(Task="Задача 2", Start='2009-03-05', Finish='2012-04-15'),
          dict(Task="Задача 3", Start='2012-02-20', Finish='2014-05-30'),
            dict(Task="Задача 4", Start='2014-02-20', Finish='2018-05-30'),
            dict(Task="Задача 5", Start='2018-02-20', Finish='2025-05-30'),
          ]

    #fig = ff.create_gantt(df)
    fig = ff.create_gantt(df, show_colorbar=True, bar_width=0.2, showgrid_x=True, showgrid_y=True)
    scriptfile =plotly.offline.plot(fig, output_type="div", show_link=False, link_text=False)
    return scriptfile


#second version
def gantt(arg, name):
    df = [dict(Task=_.name_task, Start='{}-{}-{}'.format(_.start.year, _.start.month, _.start.day ), Finish='{}-{}-{}'.format(_.finish.year, _.finish.month, _.finish.day )) for _ in arg]

    #fig = ff.create_gantt(df)
    fig = ff.create_gantt(df, show_colorbar=True, bar_width=0.2, showgrid_x=True, showgrid_y=True, title=name)
    #fig = ff.create_gantt(df, title='Raz i Dva i', width=1000)
    fig['layout'].update(autosize=False,margin=dict(l=205))# width=800, height=500, )
    scriptfile =plotly.offline.plot(fig, output_type="div", show_link=False, link_text=False)
    return scriptfile
    
"""
"""    
fig['data'].append(scatter_trace)
#use fig['layout'] for layout change




import plotly
import plotly.plotly as py
import plotly.figure_factory as ff
from plotly.offline import iplot, plot
import plotly.figure_factory as ff
from datetime import datetime

df = [dict(Task="Job A", Start='2009-01-01', Finish='2009-02-01', Resource='Apple'),
      dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15', Resource='Grape'),
      dict(Task="Job C", Start='2009-04-20', Finish='2009-09-30', Resource='Banana')]

colors = ['#7a0504', (0.2, 0.7, 0.3), 'rgb(210, 60, 180)']

fig = ff.create_gantt(df, colors=colors, index_col='Resource', reverse_colors=True, show_colorbar=True, bar_width=0.1)
fig['layout']['hovermode']='y'
fig['layout']['yaxis'].update(range=[3,-1])
scatter_trace=dict(type='scatter',
                  x=[datetime(2009, 6, 13), datetime(2009, 6, 13)],
                  y=[3,2])

fig['data'].append(scatter_trace)

scatter_trace2=dict(type='scatter',
                  x=[datetime(2009, 4, 1), datetime(2009, 4, 1)],
                  y=[2, 1])

fig['data'].append(scatter_trace2)

scatter_trace3=dict(type='scatter',
                  x=[datetime(2009, 1, 5), datetime(2009, 1, 5)],
                  y=[1, 0])

fig['data'].append(scatter_trace3)


plot(fig)






"""



