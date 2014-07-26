## Usage

1. Add your post in `posts/` with the necessary metadata:

```Markdown
---
title:Initial Post for Examplry Reward
author:Quinlan Pfiffer
date: 2014-07-24
---
````

2. `./build.py`
3. `./deploy.sh`

If you want to test locally:

```bash
cd ./built
ln -s ../static static
python -m SimpleHTTPServer
````
