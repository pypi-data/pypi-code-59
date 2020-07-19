from pathlib import Path
import json


def base_html(html_list):
    pre = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <title>Video Lister | Developed by github.com/sharadcodes</title>
        <style type="text/css" media="screen">
        * {
            padding: 0;
            margin: 0;
            box-sizing: border-box;
            font-family: monospace;
            user-select: none;
            outline: none;
        }
        body {
            color: white;
        }
        main {
            display: grid;
            grid-template-columns: 1.4fr 6fr;
        }
        .left {
            background-color: #0c4b33;
            padding: 15px;
            height: 100vh;
            overflow-y: auto;
            overflow-x: hidden;
        }
        .left details {
            font-size: 1.4rem;
            overflow: hidden;
            margin: 10px 0;
        }
        details button {
            font-size: 14px;
            padding: 5px;
            background: transparent;
            background-color: #51be95;
            border: 1px solid transparent;
            width: 100%;
            text-align: left;
            margin-top: 15px;
            cursor: pointer;
            word-break: break-all;
        }
        details button:hover {
            background-color: #20aa76;
        }
        .right {
            display: flex;
            justify-content: center;
            padding: 15px;
        }
        video {
            max-width: 90%;
            max-height: 90%;
        }
        </style>
    </head>
    <body>
    <main>  
    <div class="left">
    """
    post = """
     </div>
      <div class="right">
        <video src="" id="video_target" autobuffer autoloop loop controls />
      </div>
    </main>

    <script type="text/javascript">
      function vid_play(){
          document.getElementById("video_target").src = event.target.getAttribute("vurl");
      }
    </script>
    </body>
    </html>
    """
    return str(pre+html_list+post)

def main():
    cwd = Path.cwd()

    classes = []

    for child in cwd.iterdir():
        if child.is_dir():
            videos = []
            for i in child.iterdir():
                if not i.is_dir():
                    tmp_file_name = i.name[::-1].split('.')[0] 
                    tmp_file_name = tmp_file_name[::-1]
                    if tmp_file_name in ["mp4", "webm", "ogv", "flv", "avi", "wmv", "3gp"]:
                        videos.append({
                            "name": i.name,
                            "path": str(i.relative_to(i.parent.parent))
                        })
            classes.append({"name": child.name, "videos": videos[::-1]})

    html = ""
    for folder in classes:
        html += "<details><summary>" + str(folder['name']) + "</summary>"
        for video in folder['videos']:
            html += "<button onclick='vid_play()' title='{title}' vtitle='{title}' vurl='{url}'>{title}</button>".format(title=video['name'], url=video['path'])
        html += "</details>"

    with open('vidlist.html', 'w') as f:
        f.write(base_html(html))

if __name__ == "__main__":
    try:
    	main()
    except:
        print("Oops :( something went wront, are you sure you are in the right directory ?")