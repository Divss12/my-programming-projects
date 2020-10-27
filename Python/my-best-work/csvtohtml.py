#converts a given CSV file to an html table

def csvtohtml(cpath,hpath):
    with open(cpath,"r") as csv, open(hpath,"w") as html:
        html.write("<table>\n")
        for l in csv:
            html.write("  <tr>\n")
            for i in l.split(","):
                html.write(f"   <td>{i.strip()}</td>\n")
            html.write("  </tr>\n")
        html.write("</table>")

csvtohtml("../python-batch2/CSVFileDemo.csv","./Data1/CSVhtml.html")