from flask import Flask, request
# from image_api import fetch_mars_images
# from random import randint

import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


app = Flask(__name__)


@app.route('/')
def home():
    return TEST_HTML

TEST_HTML = """
<html><body>
     <h2>Test Plot</h2>
         <img src="/plot.png" alt="my plot"><br>
 </body></html>
"""

@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(100)
    ys = range(100,200) #[random.randint(1, 50) for x in xs]
    axis.plot(xs, ys)
    return fig






# <img src="/plot.png" alt="my plot">



#
#
# @app.route('/')
# def home():
#     return HOME_HTML
#
#
# HOME_HTML = """
#  <html><body>
#      <h2>Random Mars Image</h2>
#      <form action="/randomimage">
#          <img src="http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01000/opgs/edr/fcam/FLB_486265257EDR_F0481570FHAZ00323M_.JPG" alt="Mars Rover Image" width="500" height="500"><br>
#          Adjust Width (100 to 1000): <input type='number' name='width' min='100' max='1000'>
#          Adjust Height (100 to 1000) <input type='number' name='height' min='100' max='1000'>
#          <input type='submit' value='Submit'>
#      </form>
#  </body></html>"""
#
#
# @app.route('/randomimage')
# def randomimage():
#     width = request.args.get('width', '')
#     height = request.args.get('height', '')
#     json = fetch_mars_images(randint(1,20))
#     json_dict_index = randint(0,len(json)-1)
#     img = json[json_dict_index].get('img_src')
#
#     # xpoints = np.array([1, 8])
#     # ypoints = np.array([3, 10])
#     #
#     # plot_obj = plt.plot(xpoints, ypoints)
#     # graph = plt.show()
#
#     return IMG_HTML.format(img,width,height)
#
#
# IMG_HTML = """
#  <html><body>
#      <h2>Random Mars Image</h2>
#      <form action="/randomimage">
#          <img src="{0}" alt="Mars Rover Image" width="{1}" height="{2}"><br>
#          Adjust Width (100 to 1000): <input type='number' name='width' min='100' max='1000'>
#          Adjust Height (100 to 1000) <input type='number' name='height' min='100' max='1000'>
#          <input type='submit' value='Submit'>
#      </form>
#  </body></html>
#  """

if __name__ == "__main__":
    # Launch the Flask dev server
    app.run(host="localhost", port=5001, debug=True)