def gantt(tasks):
    calculate_percentage = lambda t: ((t.promizhny_date - t.start).days * 100)//((t.finish - t.start).days)
    adding_row = """

  <script type="text/javascript">
    google.charts.load('current', {'packages':['timeline'], language: 'uk'});
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {


    var chart = new google.visualization.Timeline(document.getElementById('chart_div'));
    var data = new google.visualization.DataTable();

    data.addColumn({ type: 'string', id: 'Term' });
    data.addColumn({ type: 'string', id: 'Name' });
    data.addColumn({ type: 'date', id: 'Start' });
    data.addColumn({ type: 'date', id: 'End' });      
      
    data.addRows(["""
    
    for _ in range(len(tasks)):
        adding_row += """['{}', '{}',  new Date({}, {}, {}), new Date({}, {}, {})],""".format(_+1, tasks[_].name_task, tasks[_].start.year, tasks[_].start.month, tasks[_].start.day, tasks[_].finish.year, tasks[_].finish.month, tasks[_].finish.day)
        #adding_row += """['{}','{}',new Date({}, {}, {}), new Date({}, {}, {})],""".format(_, tasks[_].name_task, tasks[_].start.year, tasks[_].start.month, tasks[_].start.day, tasks[_].finish.year, tasks[_].finish.month, tasks[_].finish.day)
        
    adding_row = adding_row.strip()[:-1] + """]);


var viewportwidth;
 var viewportheight;
  
 // the more standards compliant browsers (mozilla/netscape/opera/IE7) use window.innerWidth and window.innerHeight
  
 if (typeof window.innerWidth != 'undefined')
 {
      viewportwidth = window.innerWidth,
      viewportheight = window.innerHeight
 }
  
// IE6 in standards compliant mode (i.e. with a valid doctype as the first line in the document)
 
 else if (typeof document.documentElement != 'undefined'
     && typeof document.documentElement.clientWidth !=
     'undefined' && document.documentElement.clientWidth != 0)
 {
       viewportwidth = document.documentElement.clientWidth,
       viewportheight = document.documentElement.clientHeight
 }
  
 // older versions of IE
  
 else
 {
       viewportwidth = document.getElementsByTagName('body')[0].clientWidth,
       viewportheight = document.getElementsByTagName('body')[0].clientHeight
 }

      var options = {
               //width: document.documentElement.clientWidth*0.87,
               //height: document.documentElement.clientHeight*0.75};
               width: viewportwidth*0.87,
               height: viewportheight*0.75,
               //height: 400,
               timeline: { showRowLabels: false, colorByRowLabel: true, 
               rowLabelStyle: {fontName: 'Helvetica', fontSize: 14,  color: '#603913' },
               barLabelStyle: { fontName: 'Garamond', fontSize: 14,  }},
               backgroundColor: '#faf9ec',
               'tooltip': {
                'isHtml': true,
                'trigger': 'none'
                },
               colors: ['#fce94f', '#3fd1f0', '#51f140', '#cc6bef' ]
               
               

      };


      
      chart.draw(data, options);
    }
  </script>
        """
    return adding_row

