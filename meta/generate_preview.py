import glob
import os

header = """<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
.collapsible {
  background-color: #777;
  color: white;
  cursor: pointer;
  padding: 18px;
  width: 100%;
  border: none;
  text-align: left;
  outline: none;
  font-size: 15px;
}

.active, .collapsible:hover {
  background-color: #555;
}

.content {
  padding: 0 18px;
  display: none;
  overflow: hidden;
  background-color: #f1f1f1;
}

div {
  white-space: pre-wrap;
}
</style>
</head>
<body>
"""

footer = """
<script>
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}
</script>

</body>
</html>"""


def build_collapsible_section(title, body):
    return f"""<button type="button" class="collapsible">{title}</button>
<div class="content">
  <p>{body}</p>
</div>"""


def build_scripts_html():
    scripts = {}
    for script in glob.glob(os.path.join(os.path.realpath(os.path.join(os.getcwd(),
                                                                       os.path.dirname(__file__))), "..", "*.nct")):
        with open(script) as s:
            body = s.read()
            title = os.path.basename(os.path.splitext(script)[0])
            scripts[title] = body
    html = []
    for script in sorted(scripts.keys()):
        html.append(build_collapsible_section(script.replace("_", " ").title(), scripts[script]))
    html.insert(0, header)
    html.append(footer)
    html = "\n".join(html)
    with open(os.path.join(os.path.realpath(os.path.join(os.getcwd(),
                                                         os.path.dirname(__file__))), "preview.html"), "w") as f:
        f.write(html)


build_scripts_html()
