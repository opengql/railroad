import re
import argparse

def modify_html_content(text):
    comment_pattern = r'<!--.*?-->'
    text_without_comments = re.sub(comment_pattern, '', text, flags=re.DOTALL)

    css_pattern = r'<style\b[^<]*(?:(?!<\/style>)<[^<]*)*<\/style>'
    text_without_css = re.sub(css_pattern, '', text_without_comments, flags=re.DOTALL)

    remove_scripts = r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>'
    text_without_scripts = re.sub(remove_scripts, '', text_without_css, flags=re.DOTALL)
    
    remove_links = r'<link\b[^<>]*>'
    text_without_links = re.sub(remove_links, '', text_without_scripts, flags=re.DOTALL)

    title_pattern = r'(?<=<title>).+?(?=</title>)'
    text_with_new_title = re.sub(title_pattern, 'GQL Railroad Diagrams', text_without_links)

    h1_change = r'<h1>GQL\.g4</h1>'
    text_with_updated_h1 = re.sub(h1_change, '<h1>GQL Railroad Diagrams</h1>', text_with_new_title)

    css_to_add = """
<style>
body {
  padding: 20px 0;
  margin: 0;
}
h1 {
  padding-bottom: 10px;
  padding-left: 10px;
  font-family: sans-serif;
}
.border-notop td {
   border-top: none;
}
.table {
  width: 100%;
  border-collapse: collapse;
  table-layout: fixed;
  font-family: sans-serif;
}
.table tr:hover td {
  background-color: rgba(214, 214, 214, 0.8);
}
.table tr:nth-child(odd){
 background-color: rgba(244, 244, 244, 1);
}

.table td, .table th {
  word-wrap: break-word;
  padding: 5px 10px;
}
.table td:nth-child(1) {
  width: 20%;
  min-width: 375px;
}
.table td:nth-child(2) {
  min-width: 80%;
}
.table tr:hover {
  background-color: hsl(30, 20%, 95%);
}
svg.railroad-diagram path { 
  stroke-width: 2px; 
  stroke: black; 
  fill-opacity: 0; 
}
svg.railroad-diagram text { 
  font: bold 13px monospace; 
  text-anchor: middle; 
  /*! font-weight: 600; */
}
svg.railroad-diagram text.label { 
  text-anchor: start; 
}
svg.railroad-diagram text.comment { 
  font: italic 12px monospace; 
}
svg.railroad-diagram rect { 
  stroke-width: 2px; 
  stroke: black; 
  fill: #9db0e5; 
}
svg.railroad-diagram rect[rx~="10"] { 
  fill: #c7a6d8; 
}
svg.railroad-diagram a:hover {
  text-decoration: underline;
}
</style>
"""
    text_with_css = re.sub(r'(?<=<head>)', f'{css_to_add}', text_with_updated_h1, flags=re.DOTALL)

    final_text = re.sub(r'\n+', '\n', text_with_css)

    return final_text

def main():
    parser = argparse.ArgumentParser(description="Modify HTML content")
    parser.add_argument("html_file", type=argparse.FileType('r'), help="HTML file to be processed")
    
    args = parser.parse_args()
    
    html_content = args.html_file.read()
    args.html_file.close()
    
    modified_html = modify_html_content(html_content)
    
    print(modified_html)

if __name__ == "__main__":
    main()
